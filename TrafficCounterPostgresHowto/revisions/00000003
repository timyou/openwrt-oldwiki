This HOWTO describes a simple way to count network traffic passing through an OpenWRT box using an external PostgreSQL database.

You might want to log traffic usage on different interfaces on a OpenWRT router, or to create IP accounting, but storing the logs directly on the flash memory is not the best idea. One way to avoid writing anything to flash during logging is to use an external database. Using this document you can implement this using PostgreSQL.

The examples here only counts forwarded traffic, but with a minor changes can be made to count all traffic.

This is for WhiteRussian 0.9.

= PostgreSQL configuration =
== Configuration ==
You need to create a database, a user that can read and write to the database and enable access for this user from the router. To achieve this, as the postgres database superuser (postgres on most systems) execute
{{{createuser -E -P traffic
createdb -O traffic traffic}}}
This will ask you for a password for the user. Use something more complex, longer than 12 characters is recommended. You won't need to enter this password after the installation is complete, so entering one as complex as possible is not a problem.

To enable connection with that user from your OpenWRT box, you need to edit your pg_hba.conf and add
{{{
host    traffic     traffic     192.168.1.1/32      md5
}}}
where you need to replace 192.168.1.1 with your OpenWRT box IP. You also need to make your PostgreSQL to listen on the network interface where your OpenWRT box is. You can enable listening on all interfaces by changing listen_addresses in postgresql.conf to '*', or adding your PostgreSQL box IP (e.g. 192.168.1.100) to it.
{{{
listen_addresses = 'localhost, 192.168.1.100'
}}}

You need to take the appropriate security preoccasions. Don't forward traffic from the Internet to the PostgreSQL port on 192.168.1.100 unless you need it, or filter it, if needed. Don't enable listening on public addresses, without appropriate filtering, and if you are paranoid, filter all connections besides those originating on your lo interface and from your OpenWRT box.


== Database and tables ==

Now you have to create the tables and functions in the database. First connect to the database as a superuser
{{psql traffic}}
You need to create the plpgsql language. You must do this as the database superuser. Everything else can be done from the traffic user as well. In your psql shell enter the command
{{{CREATE LANGUAGE "plpgsql";}}}

Now to create the tables and functions, either paste the table code below in the shell, or save it to a file named traffic_counter.sql in your current directory and enter {{{\i traffic_counter.sql}}}

The table code:

{{{
--  Database for use with traffic counters based on iptables
--  Copyright (C) 2007 Milko Krachounov <exabyte@3mhz.net>
--  This file is part of Simple Traffic Counter
--  
--  This program is free software; you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation; either version 3 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program.  If not, see <http://www.gnu.org/licenses/>.


-- A table containing the named counters

CREATE TABLE counters (
        rid serial PRIMARY KEY,
        counter_name character varying (30)
);

CREATE UNIQUE INDEX counter_name_index ON counters (counter_name);


-- A table containing the iptables rules for each counter
-- Currently the iptables rules are specified as text, can be improved

CREATE TABLE rules (
        rid int NOT NULL REFERENCES counters ON DELETE CASCADE,
        chain character varying (30),
        target character varying  (30),
        match_rule text,
        sort_order int
);

CREATE INDEX rules_chain_index ON rules (chain);
CREATE INDEX rules_sort_index ON rules (sort_order);

-- A table where data from the counters is saved

CREATE TABLE harvests (
        rid int NOT NULL REFERENCES counters ON DELETE CASCADE,
        ts timestamp with time zone,
        packets bigint NOT NULL,
        bytes bigint NOT NULL,
        PRIMARY KEY (rid, ts)
);

CREATE INDEX harvests_ts_index ON harvests (ts);

-- A table where summarized month data is saved

CREATE TABLE summarized (
        rid int NOT NULL REFERENCES counters ON DELETE CASCADE,
        month smallint NOT NULL,
        year smallint NOT NULL,
        packets bigint NOT NULL,
        bytes bigint NOT NULL,
        PRIMARY KEY (rid, year, month)
);

CREATE INDEX s_month_index ON summarized (year, month);

-- Automatically update sumamrized month data on INSERT


CREATE FUNCTION update_summarized() RETURNS trigger AS $update_summarized$
        DECLARE
                new_month smallint;
                new_year smallint;
        BEGIN
                IF NEW.ts IS NULL THEN
                        NEW.ts := now();
                        new_month := extract(month from NEW.ts);
                        new_year := extract(year from NEW.ts);
                        PERFORM * FROM summarized WHERE (rid, year, month) = (NEW.rid, new_year, new_month);
                        IF NOT FOUND THEN
                                INSERT INTO summarized (rid, month, year, packets, bytes)
                                        VALUES (NEW.rid, new_month, new_year, NEW.packets, NEW.bytes);
                        ELSE
                                UPDATE summarized SET bytes = bytes + NEW.bytes, packets = packets + NEW.packets
                                        WHERE (rid, year, month) = (NEW.rid, new_year, new_month);
                        END IF;
                        -- If the row exists, update the old one instead
                        -- The collecting router does not want to process anything, so
                        -- this is the easiest way
                        PERFORM * FROM harvests WHERE (rid, ts) = (NEW.rid, NEW.ts);
                        IF NOT FOUND THEN
                                RETURN NEW;
                        ELSE
                                UPDATE harvests SET bytes = bytes + NEW.bytes, packets = packets + NEW.packets WHERE (rid, ts) = (NEW.rid, NEW.ts);
                                RETURN NULL;
                        END IF;
                END IF;
        END;
$update_summarized$ LANGUAGE plpgsql;

CREATE TRIGGER update_summarized BEFORE INSERT ON harvests FOR EACH ROW EXECUTE PROCEDURE update_summarized();


-- Combine many records over a time period into one to drop unneeded details and save space
-- The first argument is the size of the period you want to combine in a single record,
-- the second argument is interval of time in the past to go.
-- For example, purge_details("hour", "2 days") combines the hour two days ago into one record.

CREATE FUNCTION purge_details (varchar, varchar) RETURNS void AS $purge_details$
        DECLARE
                period_size ALIAS FOR $1;
                period_distance ALIAS FOR $2;
                temp_row record;
                period_start timestamp with time zone;
                period_end timestamp with time zone;
        BEGIN
                period_start := date_trunc(period_size, now() - period_distance::interval);
                period_end := period_start + ('1 ' || period_size)::interval;
                IF period_end - period_start > period_distance::interval THEN
                        RAISE EXCEPTION 'This operation doesn''t make sense.';
                        -- Actually it does, but we attribute it to an user error.
                        -- if you want to purge the current period, remove these lines
                        EXIT;
                END IF;
                FOR temp_row IN SELECT rid, MAX(ts) as ts, SUM(bytes) as bytes, SUM(packets) as packets
                   FROM harvests WHERE ts >= period_start AND ts < period_end GROUP BY rid LOOP
                        DELETE FROM harvests WHERE rid = temp_row.rid AND ts >= period_start AND ts < period_end;
                        INSERT INTO harvests (rid, ts, bytes, packets) VALUES (temp_row.rid, temp_row.ts, temp_row.bytes, temp_row.packets);
                END LOOP;
        END;
$purge_details$ LANGUAGE plpgsql;


-- This is for keeping the currently enabled iptables rules and their order, 
-- and is used when collecting the data from the counters
CREATE TABLE active_rules (
        chain character varying (30) DEFAULT 'forwarding_traffic',
        rulenum smallint,
        rid int REFERENCES counters ON DELETE SET NULL,
        PRIMARY KEY (chain, rulenum)
);


-- This function returns the iptables commands needed to create the counting rules
-- and adds them to the active_rules table.
CREATE FUNCTION iptables_init() RETURNS SETOF varchar AS $iptables_init$
        DECLARE
                i integer;
                chain_row record;
                rule_row record;
                select_rule varchar;
                chain_name varchar;
        BEGIN
                DELETE FROM active_rules;
                RETURN NEXT 'iptables -F forwarding_traffic';
                FOR chain_row IN SELECT DISTINCT chain FROM rules LOOP
                        IF chain_row.chain IS NOT NULL THEN
                                RETURN NEXT 'iptables -N ' || chain_row.chain || ' 2>/dev/null';
                                RETURN NEXT 'iptables -F ' || chain_row.chain;
                        END IF;
                END LOOP;
                FOR chain_row IN SELECT DISTINCT chain FROM rules LOOP
                        IF chain_row.chain IS NOT NULL THEN
                                select_rule := 'chain = ''' || chain_row.chain || '''';
                                chain_name := chain_row.chain;
                        ELSE
                                select_rule := 'chain IS NULL';
                                chain_name := 'forwarding_traffic';
                        END IF;
                        i := 0;
                        FOR rule_row IN EXECUTE 'SELECT rid, target, match_rule FROM rules WHERE ' ||
                           select_rule || ' ORDER BY sort_order' LOOP
                                i := i + 1;
                                INSERT INTO active_rules (chain, rulenum, rid) VALUES (chain_name, i, rule_row.rid);
                                IF rule_row.target IS NULL THEN
                                        RETURN NEXT 'iptables -A ' || chain_name || ' ' || rule_row.match_rule;
                                ELSE
                                        RETURN NEXT 'iptables -A ' || chain_name || ' ' || rule_row.match_rule
                                                || ' -j ' || rule_row.target;
                                END IF;
                        END LOOP;
                END LOOP;
        END;
$iptables_init$ LANGUAGE plpgsql;

-- A function which reduces typing when inserting rules directly from postgres
-- You might write your own web or command line interface
-- These functions are untested

CREATE FUNCTION add_rule (varchar, varchar, varchar, text, int) RETURNS void AS $add_rule$
        DECLARE
                rule_counter ALIAS FOR $1;
                rule_chain ALIAS FOR $2;
                rule_target ALIAS FOR $3;
                rule_match ALIAS FOR $4;
                rule_order ALIAS FOR $5;
        BEGIN
                INSERT INTO rules (rid, chain, target, match_rule, sort_order) 
                   SELECT rid, rule_chain, rule_target, rule_match, rule_order FROM counters WHERE counter_name = rule_counter;
        END;
$add_rule$ LANGUAGE plpgsql;

CREATE FUNCTION del_rule (varchar, varchar, varchar, text, int) RETURNS void AS $del_rule$
        DECLARE
                rule_counter ALIAS FOR $1;
                rule_chain ALIAS FOR $2;
                rule_target ALIAS FOR $3;
                rule_match ALIAS FOR $4;
                rule_order ALIAS FOR $5;
                temp_row record;
        BEGIN
                SELECT INTO temp_row rid FROM counters WHERE counter_name = rule_counter;
                DELETE FROM rules WHERE (rid, chain, target, match_rule, sort_order) =  (temp_row.rid, rule_chain, rule_target, rule_match, rule_order);
        END;
$del_rule$ LANGUAGE plpgsql;

}}}
== Adding iptables rules ==
Now you need to add iptables rules to your database. They are not saved on your OpenWRT box. This consists of two parts — first you need to create named counters in the counters table, then to add as many as you like rules to the rules table. The rules are specified as text arguments to the iptables command, so you are free to create any rules you like. There are seperate columns to specify the chain and the target. If the chain is NULL, the rules are added to the forwarding_traffic chain.

Here is a simple example for counting the traffic on your WAN interface:

{{{
INSERT INTO counters (counter_name) VALUES ('wan_in');
INSERT INTO counters (counter_name) VALUES ('wan_out');
SELECT add_rule ('wan_in', NULL, NULL, '-i vlan1', 0);
SELECT add_rule ('wan_out', NULL, NULL, '-o vlan1', 0);
}}}
== Optional cron jobs ==
If you don't want to keep detailed traffic logs for years in the past, you can the following to your postgres superuser crontab (if he can connect to the database without password, either via .pgpass or ident sameuser in pg_hba.conf), or to another user having write permissions to the traffic database.
{{{
# Combine the rules from the hour two days ago into one
0 * * * * echo "select purge_details ('hour', '2 days');" | psql traffic > /dev/null
# Combine the rules from the day three months ago into one
0 0 * * * echo "select purge_details ('day', '3 months');" | psql traffic > /dev/null
# Combine the rules from the month two years ago into one
0 0 1 * * echo "select purge_details ('month', '2 years');" | psql traffic > /dev/null
}}}
= OpenWRT box configuration =
You need to enable cron on your OpenWRT box. Time synchronization is recommended, but it's not needed, as time keeping is done by the PostgreSQL server. You have to create 'forwarding_traffic' chain in iptables, and to add a rule that sends (all) packets passing through the FORWARD chain there. It might be before or after dropping INVALID packets, depending on your desires, my choice was before. This means correctly counting incoming forwarded packets, but not outgoing. 

You need to install PostgreSQL console client and zlib.
{{{
ipkg install pgsql-cli
ipkg install zlib
}}}

You can add the following to your /etc/firewall.user
{{{
iptables -N forwarding_traffic 2> /dev/null
iptables -F forwarding_traffic
iptables -I FORWARD -j forwarding_traffic
}}}

Now you need scripts to create the counters and collect them. Create a directory /usr/lib/traffic. Create /usr/lib/traffic/parse_tables.awk with the following contents.
{{{
BEGIN {
        j = 1
}

/^ *[0-9]+ +[0-9]+/ {
        print "INSERT INTO harvests (rid, packets, bytes) SELECT rid, "$1", "$2" FROM active_rules WHERE (chain,rulenum) = ('"chain"',"j++");";
}

}}}
(The above code fragment is in the public domain.)

Then create executable /usr/lib/collect_traffic.sh with the following contents.
{{{
#!/bin/sh
#  Copyright (C) 2007 Milko Krachounov <exabyte@3mhz.net>
#  This file is part of Simple Traffic Counter
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


DATABASE_HOST=database.host.lan
DATABASE_USER=traffic

export PGPASSWORD=MyVewyVewyObscuredPassword

# First we check if the traffic counter is initialised
if ( ! [ -f /tmp/traffic_counter ] ) || [ "$1" = reload ]
then
        echo 'SELECT * FROM iptables_init();' | (psql -A -t -h "$DATABASE_HOST" -U traffic traffic && touch /tmp/traffic_counter) | ash
        #touch /tmp/traffic_counter
        #ln -s /usr/lib/traffic/.pgpass /tmp/
else
        (
        echo 'BEGIN;'
        echo 'SELECT DISTINCT chain FROM active_rules;' | psql -A -t -h "$DATABASE_HOST" -U traffic traffic | while read chain
        do
                iptables -Z -L $chain -n -v -x  | awk -v chain=$chain -f /usr/lib/traffic/parse_tables.awk
        done
        echo 'END;'
        ) | psql -A -t -h "$DATABASE_HOST" -U traffic traffic > /dev/null
fi


}}}

Replace the DATABASE_HOST and PGPASSWORD with your PostgreSQL host and PostgreSQL password. The .pgpass file is not supported in OpenWRT, at least I couldn't get it to work, so we need to specify the password this way. Don't forget to run {{{chmod +x /usr/lib/collect_traffic.sh}}}.

Now all you need to do is to add the above to your cron, running every 5, 15 or 30 minutes.

Run {{{crontab -e}}} and add {{{*/5 * * * * /usr/lib/traffic/collect_traffic.sh}}}

Voila.

You can reload the rules with {{{/usr/lib/traffic/parse_tables.sh reload}}}

= Usage ideas =
You get two tables with detailed traffic info and with summarized month info. You can make use of  both for your needs. 
== Get the information ==
You can query the database to get the results for a period you need.
You can get all the traffic that passed through the rules with
{{{
SELECT counter_name, SUM(bytes) FROM counters LEFT JOIN harvests USING (rid) GROUP BY counter_name;
}}}
You can get the traffic info for a specific period of one day with
{{{
SELECT counter_name, SUM(bytes) FROM counters LEFT JOIN harvests USING (rid) WHERE ts >= timestamp '2007-09-07' AND ts < timestamp '2007-09-08' GROUP BY counter_name;
}}}
You can get the summarized month info by issuing
{{{
SELECT counter_name, year || '-' || month as m, bytes FROM counters LEFT JOIN summarized USING (rid) ORDER BY m;
}}}
== Automatically turn off after a threshold ==
If you have traffic limits on your ISP, you can make your router turn your internet off automatically after a certain threshold with scripts.

= License =

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.

----
CategoryHowTo
