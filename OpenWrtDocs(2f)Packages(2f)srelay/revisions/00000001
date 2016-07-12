=== srelay - socks proxy ===
There is a socks proxy available for !OpenWrt, it is called '''srelay''' (Find via the package tracker). However, there is no documentation for this package. So, here is a quick guide:

Srelay comes with a configuration file: /etc/srelay.conf. It has some examples, but basically you will want to do this:

{{{
192.168.1.0/24 any -
}}}
This should give every computer in the 192.168.1.0 subnet access to srelay while keeping everything else out.

Another interpretation about the config file is that it configures proxy chaining. You can specify what the next proxy hop should be for a specific destination. If you want srelay to directly connect to any destination you can use a config file like this:

{{{
# destination                  port range      next-hop/port
0.0.0.0                          any
}}}
Then start srelay: '''srelay -c /etc/srelay.conf -r -s'''. Find out more about the available options with '''srelay -h'''.

Keep in mind that this information was found using trial-and-error-methods, so it might still be faulty or have unwanted side effects.

CategoryPackage
