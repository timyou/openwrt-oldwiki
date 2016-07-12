## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
= Traffic logging with ULOG & MySQL =

This procedure has been implemented in a RC9 openwrt but it should also work in RC6 (though you're advised to *update*). Assuming you have enough knowledge to work your way through a linux console, it should be fairly easy to make it work.

== Installing ULOG & requisites ==

''ssh into your openwrt box first''

{{{
ipkg update
ipkg install ulogd ulogd-mod-mysql kmod-ipt-ulog iptables-mod-ulog
}}}

== Setting up your MySQL database ==

''copy & paste these lines into a text file in your linux box (the one running the mysql server), name it ulog-mysql.sql''

{{{
CREATE TABLE ulog (     id              INT UNSIGNED AUTO_INCREMENT UNIQUE,

                        raw_mac         VARCHAR(80),

                        oob_time_sec    INT UNSIGNED,
                        oob_time_usec   INT UNSIGNED,
                        oob_prefix      VARCHAR(32),
                        oob_mark        INT UNSIGNED,
                        oob_in          VARCHAR(32),
                        oob_out         VARCHAR(32),

                        ip_saddr        INT UNSIGNED,
                        ip_daddr        INT UNSIGNED,
                        ip_protocol     TINYINT UNSIGNED,
                        ip_tos          TINYINT UNSIGNED,
                        ip_ttl          TINYINT UNSIGNED,
                        ip_totlen       SMALLINT UNSIGNED,
                        ip_ihl          TINYINT UNSIGNED,
                        ip_csum         SMALLINT UNSIGNED,
                        ip_id           SMALLINT UNSIGNED,
                        ip_fragoff      SMALLINT UNSIGNED,

                        tcp_sport       SMALLINT UNSIGNED,
                        tcp_dport       SMALLINT UNSIGNED,
                        tcp_seq         INT UNSIGNED,
                        tcp_ackseq      INT UNSIGNED,
                        tcp_window      SMALLINT UNSIGNED,
                        tcp_urg         TINYINT,
                        tcp_urgp        SMALLINT UNSIGNED,
                        tcp_ack         TINYINT,
                        tcp_psh         TINYINT,
                        tcp_rst         TINYINT,
                        tcp_syn         TINYINT,
                        tcp_fin         TINYINT,

                        udp_sport       SMALLINT UNSIGNED,
                        udp_dport       SMALLINT UNSIGNED,
                        udp_len         SMALLINT UNSIGNED,

                        icmp_type       TINYINT UNSIGNED,
                        icmp_code       TINYINT UNSIGNED,
                        icmp_echoid     SMALLINT UNSIGNED,
                        icmp_echoseq    SMALLINT UNSIGNED,
                        icmp_gateway    INT UNSIGNED,
                        icmp_fragmtu    SMALLINT UNSIGNED,

                        pwsniff_user    VARCHAR(30),
                        pwsniff_pass    VARCHAR(30),

                        ahesp_spi       INT UNSIGNED,

                        KEY index_id    (id)
                );
}}}

''now create the database, the table and the user
* create database named 'ulogdb' and select it
* create table ulog from description given in 'ulog-mysql.sql'
* create user 'uloguser' with permissions to log in from any host ('%') and password 'ulogpass' and grant him privileges to do almost anything to this database''

{{{
create database ulogdb;
use ulogdb;
source /path/to/textfile/ulog-mysql.sql;
grant select,insert,update,drop,delete,create temporary tables, on ulogdb.* to 'uloguser'@'%' identified by 'ulogpass';
flush privileges;
quit;
}}}


=== Display ===
xxx
