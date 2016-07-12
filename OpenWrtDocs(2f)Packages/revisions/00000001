Describe OpenWrtDocs/Packages here.


=== socks-Proxy ===

There is a Socks-proxy available for !OpenWrt, it is called '''srelay''' (Find via the
package tracker). However, there is no documentation for this package. So, here is a
quick guide:

Srelay comes with a configuration file: /etc/srelay.conf (surprise surprise). It has some
examples, but basically you will want to do this:

{{{
192.168.1.0/24 any -
}}}

This should give every computer in the 192.168.1.0 subnet access to srelay while keeping
everything else out.

Then start srelay: '''srelay -c /etc/srelay.conf -r -s'''. Find out more about the
available options with '''srelay -h'''.

Keep in mind that this information was found using trial-and-error-methods, so it might
still be faulty or have unwanted side effects.
