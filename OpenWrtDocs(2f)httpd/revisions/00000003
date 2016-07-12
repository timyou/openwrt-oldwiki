{{{httpd}}} is the binary, part of BusyBox, tool that start httpd.

The usage for httpd is :
{{{
Usage: httpd [options]
        ===== daemon options =====
        -c FILE         Specifies configuration file. (default httpd.conf)
        -p PORT Server port (default 80)
        -r REALM        Authentication Realm for Basic Authentication
        -h HOME         Specifies http HOME directory (default ./)

        ===== script options =====
        -m PASS         Crypt PASS with md5 algorithm
        -e STRING       Html encode STRING
        -d STRING       URL decode STRING
}}}

Configuration file (/etc/httpd.conf) :
{{{
httpd.conf has the following format:

A:172.20.         # Allow address from 172.20.0.0/16
A:10.0.0.0/25     # Allow any address from 10.0.0.0-10.0.0.127
A:10.0.0.0/255.255.255.128  # Allow any address that previous set
A:127.0.0.1       # Allow local loopback connections
D:*               # Deny from other IP connections
/cgi-bin:foo:bar  # Require user foo, pwd bar on urls starting with /cgi-bin/
/adm:admin:setup  # Require user admin, pwd setup on urls starting with /adm/
/adm:toor:PaSsWd  # or user toor, pwd PaSsWd on urls starting with /adm/
.au:audio/basic   # additional mime type for audio.au files

A/D may be as a/d or allow/deny - first char case insensitive
Deny IP rules take precedence over allow rules.


The Deny/Allow IP logic:

- Default is to allow all.  No addresses are denied unless
  denied with a D: rule.
- Order of Deny/Allow rules is significant
- Deny rules take precedence over allow rules.
- If a deny all rule (D:*) is used it acts as a catch-all for unmatched
  addresses.
- Specification of Allow all (A:*) is a no-op

Example:
1. Allow only specified addresses
   A:172.20          # Allow any address that begins with 172.20.
   A:10.10.          # Allow any address that begins with 10.10.
   A:127.0.0.1       # Allow local loopback connections
   D:*               # Deny from other IP connections

2. Only deny specified addresses
   D:1.2.3.        # deny from 1.2.3.0 - 1.2.3.255
   D:2.3.4.        # deny from 2.3.4.0 - 2.3.4.255
   A:*             # (optional line added for clarity)

If a sub directory contains a config file it is parsed and merged with
any existing settings as if it was appended to the original configuration.

subdir paths are relative to the containing subdir and thus cannot
affect the parent rules.

Note that since the sub dir is parsed in the forked thread servicing the
subdir http request, any merge is discarded when the process exits.  As a
result, the subdir settings only have a lifetime of a single request.

}}}


""Document is under construction, be patient""
