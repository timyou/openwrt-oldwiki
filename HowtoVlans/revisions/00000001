= Howto: VLANS on the WRT54G =

== Intro ==
I am presently attempting to enable tagged VLANs on a WRT54G. I will use this page to document the progress I make.

== What are you trying to do here? ==
In order for people to understand the goal I am trying to achieve, consider this illustration:

We have two LinkSys WRT54G routers. Each has 5 ethernet jacks on the back of it, one of these ports is a CrossOver port (labeled "WAN" in software, or "Internet" on the back of the device). The other 4 are regular ports. Now, don't ask me WHY anyone would want to do the following, but just rest assured that it is a valid example that will demonstrate what this howto attempts to achieve. What we are going to do is create 5 VLANs, one for each regular port on the router, plus one for the WiFi interface. We then want to used a TaggedTrunk to connect the two routers together via their "Internet" port (NOTE: these ports should be connected with a StraightThrough cable). When all is said and done, port 1 of router A should be able to see port 1 of router B, port 2 on router A should see port 2 on router B, etc.

== So, how do we do it? ==

Well, that's what I'm working on, and also asking for help here. If anyone has suggestions or information that could be helpful, please add it here or email it to me via bhook(at)coder7(dot)com or bhook(at)kssb(dot)net.

== What I do know ==

This will likely require the use of the admcfg package, which allows us to configure the switch that controls the 5 (really it's 6) ethernet ports on the WRT54G. And just for the benefit of others that may be searching, here is what I found for documentation on the admcfg utility:

USAGE:
admcfg [<port> [option]]

      port is in the form of "portX"

      option is one of:

            ENABLED, DISABLED - enable/disable port

            100Mbps, 10Mbps - port speed

            FD, HD - full duplex/half duplex

            FLOW, NOFLOW - 802.3 flow control

            TAG, UNTAG - output vlan tagging

            TOS, VLAN - priority given to TOS/VLAN

            PRIO, NOPRIO - port based priority

            PVID:X - set the primary vlan id

            vlanX - set the vlan mappings 
