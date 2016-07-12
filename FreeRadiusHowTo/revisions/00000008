This documents explains what a RADIUS is, and how to install FreeRADIUS on OpenWRT.

[[TableOfContents]]

= RADIUS =
 . What is radius? It stands for "Remote Authentication Dial In User Service" with the primary functions of authenticating, accounting and authorising user activity.  In a nutshell, it allows administrators to say who can use the network, and what resources on the network. There are also accounting mechanisms to log who has used what, and when.  http://en.wikipedia.org/wiki/RADIUS  In the context of OpenWRT, it is often used to authenticate and secure wireless connections (see the WPA2 Enterprise wiki http://wiki.openwrt.org/OpenWrtDocs/Wpa2Enterprise or authenticating users on a hotspot. Use your imagination.

= FreeRADIUS =
== Install ==
{{{
ipkg install freeradius
}}}
You now have a basic FreeRADIUS (1.1.6) on your WRT and need to set up authentification modules (usually not nessecary if the radius client applications are located on localhost) and user database in order for it to run. The latter is simply be the textfile /etc/freeradius/users but could be quite simply be connected to the persistency mechanism of your chooise.

== /etc/freeradius ==
FreeRADIUS refferes to this as /etc/raddb, and it contans a bunch of files:

=== radiudd.conf ===
example:

{{{
}}}
=== clients.conf ===
example:

{{{
}}}
=== users ===
{{{
# Example Configuration
DEFAULT Group == "disabled",
    Auth-Type := Reject Reply-Message = "Your account has been disabled."

# Password Style
testuser1        User-Password == "test123"

# EAP Style (Client certificate authentication)
testuser2        Auth-Type := EAP
}}}
