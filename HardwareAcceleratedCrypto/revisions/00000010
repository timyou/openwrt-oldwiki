== Harware accelerated crypto ==
The BCM47xx/53xx (all xx models?) used by some of the platforms (Asus WL500GD/X, Netgear WGT634U...) have hardware accelerated encryption support for IPSec, AES, DES, SHA1, ... calculations.

The specification(s?) states the hardware is able to support 75Mbps (9,4MB/s) of encrypted throughput. Without hardware acceleration with the blowfish encryption throughput is only ~0,4MB/s.

----
[http://forum.openwrt.org/viewtopic.php?id=5032 Discussion] about hardware accelerated crypto.

Various versions of [http://80.81.183.101/openwrt/bcm5820/ BCM5820 driver sources].

----
[http://www.broadcom.com/collateral/prod_brochures/AirForceBrochure.pdf AirForce] says there are WEP 128, AES OCB and AES CCM accelerated by hardware.

||Circuit/CPU ||Accelerations ||Datasheet ||
||BCM94704AGR ||WEP 128, AES OCB AES CCM, ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM?4704P ||WEP 128, AES OCB, AES CCM, VPN ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM5365 ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] ||
||BCM5365P ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] ||
