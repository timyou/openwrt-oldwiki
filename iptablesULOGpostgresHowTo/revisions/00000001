{{{Quick and dirty on how to get iptables to work with ULOG, and ULOG to work with postgresql.

assuming openwrt@192.168.1.1
assuming pgsql@192.168.1.2 on Debian or similar
assuming database name ulogd, user ulogd, password ulogd, table ulog (below)

Using postgres 7.4 on Debian:

/etc/postgresql/pg_hba.conf: 
(/etc/postgresql/<version>/main/pg_hba.conf on Ubuntu)
(Allows md5 password auth for login from 192.168.1.*)

# IPv4-style local connections:
host    all         all         127.0.0.1         255.255.255.255   md5
host    all         all         192.168.1.1       255.255.255.0     md5

/etc/postgresql/postgres.conf:
(tcpip_socket disabled by default in Ubuntu; skip this step in Debian)
# - Connection Settings -
tcpip_socket = true

Set up user/database:
# su postgres
$ psql template1
Welcome to postgres, yadda yadda
> create user ulogd with encrypted password 'ulogd' createdb;
> \q
$ psql -U ulogd template1
(If this doesn't work, fiddle with pg_hba.conf above and restart the db: /etc/init.d/postgresql restart)
> create database ulogd;
> \q
$ psql -U postgres ulogd
(Create pgsql language and necessary casts as master user)
create or replace function plpgsql_call_handler() RETURNS language_handler
AS '$libdir/plpgsql', 'plpgsql_call_handler'
LANGUAGE c;
create trusted procedural language plpgsql handler plpgsql_call_handler;

CREATE FUNCTION integerip_to_str(integer) RETURNS inet AS '
DECLARE
    t inet;
BEGIN
    t = (($1>>24) & 255::int8) || ''.'' ||
        (($1>>16) & 255::int8) || ''.'' ||
        (($1>>8)  & 255::int8) || ''.'' ||
        ($1     & 255::int8);
    RETURN t;
END;
' LANGUAGE 'plpgsql';

CREATE CAST (integer AS inet)
  WITH FUNCTION integerip_to_str(integer)
  AS IMPLICIT;

CREATE OR REPLACE FUNCTION ulogtimecast(integer)
  RETURNS timestamp AS
'select "timestamp"($1::abstime);'
  LANGUAGE 'sql' VOLATILE;

CREATE CAST (integer AS timestamp)
  WITH FUNCTION ulogtimecast(integer)
  AS IMPLICIT;

$ psql -U ulogd ulogd
create sequence 'seq_ulog';
CREATE TABLE ulog
(
  id int4 NOT NULL DEFAULT nextval('seq_ulog'),
  oob_prefix varchar(32),
  oob_time_sec timestamp,
  oob_time_usec int4,
  oob_mark int8,
  oob_in varchar(32),
  oob_out varchar(32),
  raw_mac varchar(80),
  raw_pktlen int8,
  ip_ihl int2,
  ip_tos int2,
  ip_totlen int4,
  ip_id int4,
  ip_fragoff int4,
  ip_ttl int2,
  ip_protocol int2,
  ip_csum int4,
  ip_saddr inet,
  ip_daddr inet,
  tcp_sport int4,
  tcp_dport int4,
  tcp_seq int8,
  tcp_ackseq int8,
  tcp_urg bool,
  tcp_ack bool,
  tcp_psh bool,
  tcp_rst bool,
  tcp_syn bool,
  tcp_fin bool,
  tcp_window int4,
  tcp_urgp int4,
  udp_sport int4,
  udp_dport int4,
  udp_len int4,
  icmp_type int2,
  icmp_code int2,
  icmp_echoid int4,
  icmp_echoseq int4,
  icmp_gateway int8,
  icmp_fragmtu int4,
  pwsniff_user varchar(30),
  pwsniff_pass varchar(30),
  ahesp_spi int2,
  local_time int8,
  local_hostname varchar
) WITH OIDS;










Using rc4:

root@OpenWrt:~# ipkg list | grep ulog
iptables-mod-ulog - 1.3.3-1 - Iptables (IPv4) extension for user-space packet logging
kmod-ipt-ulog - 2.4.30-brcm-2 - Netfilter (IPv4) kernel module for user-space packet logging
ulogd - 1.23-2 - Netfilter userspace logging daemon
ulogd-mod-pgsql - 1.23-2 - Netfilter userspace logging daemon (PostgreSQL plugin)

Make sure you have those installed:
ipkg install iptables-mod-ulog kmod-ipt-ulog ulogd ulogd-mod-pgsql

/etc/ulogd.conf :
(Loads PGSQL plugin, sets PGSQL db settings)

# output plugins.
plugin="/usr/lib/ulogd/ulogd_LOGEMU.so"
#plugin="/usr/lib/ulogd/ulogd_OPRINT.so"
#plugin="/usr/lib/ulogd/ulogd_MYSQL.so"
plugin="/usr/lib/ulogd/ulogd_PGSQL.so"
#plugin="/usr/lib/ulogd/ulogd_SQLITE3.so"
#plugin="/usr/lib/ulogd/ulogd_PCAP.so"

[PGSQL]
table="ulog"
schema="public"
user="ulogd"
pass="ulogd"
host="192.168.1.2"
db="ulogd"

/etc/modules :
ipt_ULOG


next, reboot or modprobe ipt_ULOG

try a rule to be sure it all works.  Maybe something like:
iptables -A forwarding_rule ULOG --ulog-nlgroup 1
to log all forwarded packets.  

Much of the above cobbled from following URLS:
http://www.snort.org/docs/snortdb/snortdb_faq.html#faq_b4
http://lists.gnumonks.org/pipermail/ulogd/2004-January/000494.html

TODO: mac addr in table schema should be pgsql's native mac addr type, but ULOGD is sending it as "XX:XX:XX:XX:XX:XX:XX:XX " with a space at the end which throws everything off
}}}
----
CategoryHowTo
