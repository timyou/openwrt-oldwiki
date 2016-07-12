== Hardware accelerated crypto ==
Some models of the BCM47xx/53xx family support hardware accelerated encryption for IPSec (AES, DES, 3DES), simple hash calculations (MD5, SHA1) and TLS/SSL+HMAC processing. Not all devices have a hw crypto supporting chip. At least Asus WL500GD/X, Netgear WGT634U and Asus WL700gE do have hw crypto.

The specification states the hardware is able to support 75Mbps (9,4MB/s) of encrypted throughput. Without hardware acceleration using the blowfish encryption throughput is only ~0,4MB/s.

Benchmark results that show the difference between software and hardware accelerated encryption/decryption can be found [http://www.danm.de/files/src/bcm5365p/bench/ here] (no AES results yet). Due to the overhead of hardware/DMA transfers and buffer copies between kernel/user space it gives only a good return for packet sizes greater than 256 bytes. This size can be reduced for IPSec, because network hardware uses DMA and there is no need to copy the (encrypted) data between kernel and user space.

The hardware specification needed for programming the crypto API of the bcm5365P (Broadcom 5365P) can be found [http://voodoowarez.com/bcm5365p.pdf here].

----

 * The crypto chip is accessible through the SSB bus (Sonics Silicon Backplane). A Linux driver for SSB is available in OpenWRT's kernel >= 2.6.23 (Kamikaze)

 * An example about how to communicate with the crypto chip can be found [http://www.danm.de/files/src/bcm5365p/ here] (file b5365ips.tar.bz2).

 * Links to mailing-list posts with references to more recent and working version of Linux driver for Broadcom crypto chips [http://marc.theaimsgroup.com/?l=openssl-dev&m=110915540208913&w=2 here] and [http://www.mail-archive.com/openssl-dev@openssl.org/msg18804.html here].

 * Sun Crypto Accelerator 500 and 1000 (X6762A) cards are based on BCM5821. Might be worth checking Solaris references as well. [http://src.opensolaris.org/source/xref/crypto/quantis/usr/src/uts/common/crypto/io/ Here] is OpenSolaris driver for Broadcom crypto chips.

 * Asus WL-700gE sources come with patched FreeSwan to utilize ubsec.

 * Closed-source binary included in Asus Wl-700gE sources do support AES based on headers.

 * *BSD has a driver called 'ubsec' that supports some Broadcom encryption chips. The structures and registers (e.g. MCR, packet descriptors and in-/output chains) used to program the chip look similar.

 * There's a [http://ocf-linux.sourceforge.net/ Linux port] of the OpenBSD Cryptographic Framework (OCF) but the ubsec driver (Broadcom 58xx PCI cards) is not ported yet. If you compile OCF with the /dev/crypto device driver, userspace applications and libraries such as OpenSSL can be accelerated. There are patches for Openswan as well.

 * [http://forum.openwrt.org/viewtopic.php?id=5032 Discussion] about hardware accelerated crypto.

 * Various versions of old [http://sukkamehulinko.romikselle.com/openwrt/bcm5820/ BCM5820 driver sources].

 * BCM5801/BCM5805/BCM5820 Security Processor Software Reference Library http://www.broadcom.com/products/access_request.php?category_id=0&id=7&filename=5801-5805-5820-SRL101-R.pdf

 * Cisco PIX VAC+ Encryption module is 64-bit PCI card based on Broadcom BCM5823. Another similar card is Checkpoint VPN-1 Accelerator Card II, III and IV from [http://www.silicom.co.il/ Silicom].

----
[http://www.broadcom.com/collateral/prod_brochures/AirForceBrochure.pdf AirForce] says there are WEP 128, AES OCB and AES CCM accelerated by hardware.

||Circuit/CPU ||Accelerations ||Datasheet[[FootNote(These contain absolutely no programming information)]] ||
||BCM94704AGR ||WEP 128, AES OCB AES CCM, ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM?4704P ||WEP 128, AES OCB, AES CCM, VPN ||[http://www.broadcom.com/collateral/pb/94704AGR-PB00-R.pdf 94704AGR-PB00-R.pdf] ||
||BCM5365 ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] ||
||BCM5365P ||AES (up to 256-bit CTR and CBC modes), DES, 3DES (CBC), HMAC-SHA1, HMAC-MD5, SHA1 and MD5. IPSec encryption and single pass authentication. ||[http://www.broadcom.com/collateral/pb/5365_5365P-PB01-R.pdf 5365_5365P-PB01-R.pdf] [http://voodoowarez.com/bcm5365p.pdf bcm5365p.pdf] ||
