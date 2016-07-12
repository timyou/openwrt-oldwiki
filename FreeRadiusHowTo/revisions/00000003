= Abstract =
Explains what a RADIUS is, and how to install FreeRADIUS on OpenWRT.

= RADIUS =
What is radius? It stands for "Remote Authentication Dial In User Service" with the primary functions of authenticating, accounting and authorising user activity.  In a nutshell, it allows administrators to say who can use the network, and what resources on the network. There are also accounting mechanisms to log who has used what, and when.  [http://en.wikipedia.org/wiki/RADIUS]  In the context of OpenWRT, it is often used to authenticate and secure wireless connections (see the WPA2 Enterprise wiki [[http://wiki.openwrt.org/OpenWrtDocs/Wpa2Enterprise]] or authenticating users on a hotspot. Use your imagination.

= FreeRADIUS =
== Install ==
{{{
ipkg install freeradius
}}}
You now have a basic and non functioning FreeRADIUS on your WRT and have to set up PAP/CHAP/Whatnot if your radius clients are not located on localhost.

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
# Example Configuration
DEFAULT Group == "disabled", Auth-Type := Reject
Reply-Message = "Your account has been disabled."
# Password Style
testuser1        User-Password == "test123"
# EAP Style (Client certificate authentication)
testuser2        Auth-Type := EAP
