= WRT54G3G on 3G/UMTS, using Merlin U630 Card =
The WRT54G3G, has a PCMCIA slot on it.  Linksys created this beast for Vodafone, as a kind of take anywhere wireless access point.    The Merlin U630 card essentially presents itself as a serial modem.  By loading the appropriate modules, and setting up ppp, you can make this work under OpenWRT.

The standard White Russian binarys don't contain all of the required bits in order to get it to work. You will need to compile your own binarys, using buildroot.

 . You will need to include kmod-pcmcia-serial, and kmod-ppp.
