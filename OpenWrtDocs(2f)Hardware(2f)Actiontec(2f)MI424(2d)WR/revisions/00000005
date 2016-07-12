#pragma section-numbers off
[[TableOfContents]]

= Actiontec MI424-WR Overview =
The [http://www.actiontec.com Actiontec] MI424-WR router is based on a 533MHz IXP425. It has 32MB RAM and 8MB of FLASH. It has 4 external LAN ports and 1 WAN port. It has a coax interface and IEEE 802.11g support. Some pictures of the unit and the various revisions can be found here: [http://en.wikipedia.org/wiki/MI424WR].

== Hardware ==
 * NPEB - WAN interface with separate Micrel KS8721 PHY.
 * NPEC - LAN interface connected to Micrel KSZ8995MA switch via SPI.
 * 3 PCI slots - 2 used for coax interface.
 * Wireless MiniPCI based on RA2560.
=== GPIO ===
||'''Pin''' ||'''I/O''' ||'''Description''' ||
||<)>0 ||<:>O ||Reset? ||
||<)>2 ||<:>O ||SPI CLK ||
||<)>3 ||<:>I ||SPI RxD ||
||<)>4 ||<:>O ||SPI TxD ||
||<)>6 ||<:>I ||PCI INTA (MoCA WAN) ||
||<)>7 ||<:>I ||PCI INTB (MoCA LAN) ||
||<)>8 ||<:>I ||PCI INTC (Mini-PCI) ||
||<)>9 ||<:>O ||SPI CS ||
||<)>10 ||<:>I ||Button ||
||<)>11 ||<:>O ||MoCA WAN LED ||
||<)>14 ||<:>O ||PCI CLK Pin ||
=== Latch ===
There's a latch accessible via CS1 that is 16-bits wide.
||'''Bit''' ||'''Function''' ||
||<)>0 ||Power alarm (red) ||
||<)>1 ||Power ||
||<)>2 ||Wireless ||
||<)>3 ||Internet alarm (red) ||
||<)>4 ||Internet active ||
||<)>5 ||MoCA LAN ||
||<)>7 ||PCI reset ||

----
 CategoryModel ["CategoryIXP4xxDevice"]
