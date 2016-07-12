= OpenSSL Benchmarks =
== Notes: ==
 *Benchmarks are based on running: 'openssl speed md5 sha1 sha256 sha512 des des-ede3 aes-128-cbc aes-192-cbc aes-256-cbc rsa2048 dsa2048'.  '''Please include the output for 1024 byte blocks only!'''
 *Hash and block ciphers use 1024 byte blocks;  "k" refers to 1000 bytes per second.
 *Certificate verification and signing are based on 2048 bit keys;  the values are the number of signings/verifications per second.
== Benchmark Table ==
These benchmarks provide a rough estimate of how OpenSSL performance varies on various hardware and software configurations.
||<style="vertical-align: top;">Router Make and Model ||<style="vertical-align: top;">bogomips ||<style="vertical-align: top;">OpenWRT Version ||<style="vertical-align: top;">CPU Model ||<style="vertical-align: top;">OpenSSL Version ||<style="vertical-align: top;">MD5 ||<style="vertical-align: top;">SHA-1 ||<style="vertical-align: top;">SHA-256 ||<style="vertical-align: top;">SHA-512 ||<style="vertical-align: top;">DES ||<style="vertical-align: top;">3DES ||<style="vertical-align: top;">AES-128 ||<style="vertical-align: top;">AES-192 ||<style="vertical-align: top;">AES-256 ||<style="vertical-align: top;">RSA Sign ||<style="vertical-align: top;">RSA Veryfy ||<style="vertical-align: top;">DSA Sign ||<style="vertical-align: top;">DSA Veryfy ||
||<style="vertical-align: top;">LaFonera FON2100A/B/G ||183.5 ||7.09 ||MIPS 4KEc V6.4 ||OpenSSL 0.9.8e 23 Feb 2007 ||8072.31k ||2888.56k ||1812.34k ||934.82k ||1539.73k ||554.05k ||2279.59k ||1941.87k ||1699.77k ||1.9 ||69.5 ||7.2 ||5.9 ||
||<style="vertical-align: top;">Linksys WRT-54G V. 3 ||215.44 ||0.9 ||BCM3302 V0.7 ||OpenSSL 0.9.8d 28 Sep 2006 ||4890.97k ||3312.30k ||2037.42k ||918.53k ||1682.09k ||423.25k ||1529.86k ||1297.75k ||1090.90k ||1.7 ||67.2 ||7.1 ||5.8 ||
||<style="vertical-align: top;">Linksys WRTSL54GS||262.14||Kamikaze r9504/2.6||Broadcom BCM3302 V0.6||OpenSSL 0.9.8e 23 Feb 2007||10388.57k||4002.31k||2042.12k||741.79k||3138.87k||2719.14k||2278.22k||2440.36k||1307.27k||2.3/s||90.6/s||9.3/s||7.8/s||
