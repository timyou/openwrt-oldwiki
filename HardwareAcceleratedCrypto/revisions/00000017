== Hardware accelerated crypto ==
Some models of the BCM47xx/53xx family support hardware accelerated encryption for IPSec, AES, DES, SHA1 calculations. Not all devices have hw crypto supporting chip. At least Asus WL500GD/X, Netgear WGT634U and Asus WL700gE do have hw crypto.

The specification states the hardware is able to support 75Mbps (9,4MB/s) of encrypted throughput. Without hardware acceleration using the blowfish encryption throughput is only ~0,4MB/s.

----

 * There's been some reports from people working on this, but so far no visible progress. Seems that both persons have disappeared since. 

 * Links to mailing-list posts with references to more recent and working version of Linux driver for Broadcom crypto chips [http://marc.theaimsgroup.com/?l=openssl-dev&m=110915540208913&w=2 here] and [http://www.mail-archive.com/openssl-dev@openssl.org/msg18804.html here].

 * Sun Crypto Accelerator 500 and 1000 (X6762A) cards are based on BCM5821. Might be worth checking Solaris references as well. [http://src.opensolaris.org/source/xref/crypto/quantis/usr/src/uts/common/crypto/io/ Here] is OpenSolaris driver for Broadcom crypto chips.

 * Asus WL-700gE sources come with patched FreeSwan to utilize ubsec.

 * Closed-source binary included in Asus Wl-700gE sources do support AES based on headers.

 * *BSD has driver called 'ubsec' that supports some Broadcom encryption chips.

 * Neither old open-source Linux driver, OpenSolaris nor BSD driver support AES.

 * OpenSSL has some ubsec support, but it's not exactly stable based on those mailing-list posts linked above.

 * [http://forum.openwrt.org/viewtopic.php?id=5032 Discussion] about hardware accelerated crypto.

 * Various versions of [http://sukkamehulinko.romikselle.com/openwrt/bcm5820/ BCM5820 driver sources].

 * BCM5801/BCM5805/BCM5820 Security Processor Software Reference Library http://www.broadcom.com/products/access_request.php?category_id=0&id=7&filename=5801-5805-5820-SRL101-R.pdf

----
[http://www.broadcom.com/collateral/prod_brochures/AirForceBrochure.pdf AirForce] says there are WEP 128, AES OCB and AES CCM accelerated by hardware.

||Circuit/CPU ||Accelerations ||Datasheet[[FootNote(These contain absolutely no programming information)]] ||
||BCM94704AGR ||WEP 128, AES OCB AES CCM, ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM?4704P ||WEP 128, AES OCB, AES CCM, VPN ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM5365 ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] ||
||BCM5365P ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] ||
