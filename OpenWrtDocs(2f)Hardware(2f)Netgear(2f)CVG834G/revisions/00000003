= Netgear CVG834G =

{{{
OS : eCos
CPU : BCM3368
Flash: 
RAM : 32M
DOCSIS/EuroDOCSIS : BCM3421
Wi-Fi: BCM4318
}}}

Sources of eCos can be found from the netgear site here : ftp://downloads.netgear.com/files/GPL/CVG834G_V3.9.21_NOOS_src_20070731.zip

Though it does not describe the firmware header (which could be found dumping the flash anyway), you will notice that the BCM3368 core is the same as the BCM63xx family (DSL SoC). In fact it is exactly the same chip, thus making the porting easier :).


== Serial pinout ==

{{{
Ethernet

[x] VCC
[x] TX
[x] RX
[x] GND

SoC
}}}

== Bootlog ==

{{{
BCM3368A1 TP1
1
Asymmetric VCDL shmoo:
DDR1 DDR2 DDR3 DDR4 VCDL
0000 0000 0424 000D 0C0C
Reduced DDR drive strength
PI sync init:1
346890
MemSize: .........................32M
Flash detected @0xbf000000

Signature: a020


AsusTek BootLoader Version: 2.1.6l_R2 Release Gnu
Build Date: Aug  5 2006
Build Time: 22:21:40

Image 1 Program Header:
   Signature: a020
     Control: 0005
   Major Rev: 0001
   Minor Rev: 0022
  Build Time: 2007/11/27 07:30:11 Z
 File Length: 2937522 bytes
Load Address: 80010000
    Filename: CVG834G_E15R3921V0122R_L70F7EE_0_NOOS_071127.bin
         HCS: 51b9
         CRC: d30374de


Image 2 Program Header:
   Signature: a020
     Control: 0005
   Major Rev: 0001
   Minor Rev: 0022
  Build Time: 2007/11/27 07:30:11 Z
 File Length: 2937522 bytes
Load Address: 80010000
    Filename: CVG834G_E15R3921V0122R_L70F7EE_0_NOOS_071127.bin
         HCS: 51b9
         CRC: d30374de



Enter '1', '2', or 'p' within 2 seconds or take default...
.

Performing CRC on Image 1...
CRC time = 142668534
Detected LZMA compressed image... decompressing...
Target Address: 0x80010000
...............................................Elapsed time 1480045506

Decompressed length: 12321799

Executing Image 1...


 eCos - hal_diag_init
Init device '/dev/BrcmTelnetIoDriver'
Init device '/dev/ttydiag'
Init tty channel: 80bce3e8
Init device '/dev/tty0'
Init tty channel: 80bce408
Init device '/dev/haldiag'
HAL/diag SERIAL init
Init device '/dev/ser0'
BCM 33XX SERIAL init - dev: 0.2
Set output buffer - buf: 80daca80 len: 2048
Set input buffer - buf: 80dad280 len: 2048
BCM 33XX SERIAL config
BcmBfcAppNonVolSettings::GetSingletonInstance:  WARNING - the singleton instance is NULL, and someone is accessing it!
0x0000000a [tStartup] BcmBfcStdEmbeddedTarget::InitStorageDrivers:  (BFC Target) Configuring/Loading Flash driver...
Detect 8M Intel Flash, boot loader sector is 32
BcmIntelFlashDevice::ConfigurationComplete: Debug, Detect Block Num 32 Locked
0x0000000a [tStartup] BcmBfcStdEmbeddedTarget::InitStorageDrivers:  (BFC Target) Loading ProgramStore driver...
0x00000014 [tStartup] BcmBfcStdEmbeddedTarget::InitStorageDrivers:  (BFC Target) Loading BootloaderStore driver...
0x00000014 [tStartup] BcmBfcStdEmbeddedTarget::InitStorageDrivers:  (BFC Target) Loading NonVol driver...
0x00000014 [tStartup] BcmBfcStdEmbeddedTarget::InitStorageDrivers:  (BFC Target) Storage drivers initialized successfully.
0x00000014 [tStartup] BcmBfcStdEmbeddedTarget::InitDeviceAbstractions:  (BFC Target) Creating singletons for ProgramStore/BootloaderStore/NonVol devices...
Detecting the next image number that we will store to by default...
0x14 Computing CRC32 over image2 to ensure that it is valid...
0x294 Done computing CRC32!
By default, we will dload to image number 1!

0x00000294 [tStartup] BcmBfcStdEmbeddedTarget::InitDeviceAbstractions:  (BFC Target) Device abstraction singletons created successfully.

BcmCapNonVolSettings::GetSingletonInstance:  WARNING - the singleton instance is NULL, and someone is accessing it!
WARNING: ResetDefaultBlindEmtaData() -Resetting EMTA non-vol data section to default values
mtaNvCalcChecksum: checksum= 1273101780
Reading Permanent settings from non-vol...
Checksum for permanent settings:  0x8c3b2608
Settings were read and verified.


Reading Dynamic settings from non-vol...
Checksum for dynamic settings:  0x40891f74
Settings were read and verified.

FreePoolManagerDriver::BcmFpmInit:  INFO - SRAM Config size=16384 bytes:BufferSize=1920:NumBuffers=512
Programming BMU for ADC use.
  picocode: BCM3367/68 ADC Picocode rev 1.0.2
  Date / Time stamp = Tue Jun 20 15:12:19 2006
  BMU picocode verified.
0x000002c6 [Telnet Thread] BcmTelnetThread::ThreadMain:  (Telnet Thread) Telnet server thread running...
0x000002c6 [SSH Thread] BcmThread::ThreadMain:  (SSH Thread) SSH server thread running...
Creating SNMP agent cablemodem agent
DON'T think we need to go here - so don't:::: init_mib !!!!
WARNING: netsnmp_brcm_create_tstring called with no address!
Creating BcmEmtaCommandTable
Creating BcmEmtaEndptCommandTable

If you pressed the 's' key before this point, we will skip driver initialization...
Creating DOCSIS Control Thread...

vvv Interface creation and driver startup beginning vvv

-> Begin DOCSIS CM WAN interface
        Creating HAL object for the DOCSIS CableModem interface
        Registering DOCSIS CableModem driver
Fxtal is 25000000
Fclk_us_vco is 1050000000
Fclk_us_pll is 525000000
Writing 0x00362267 to US_PLL
Fxtal is 25000000
Fclk_us_vco is 1050000000
Fclk_us_pll is 525000000
Writing 0x00362267 to US_PLL
FreePoolManagerDriver::BcmFpmMemoryReserve:  INFO - Reserved 4080 bytes:Available Memory=11280 bytes:AvailMemAddress=0xfffc13f0
FreePoolManagerDriver::BcmFpmMemoryReserve:  INFO - Reserved 2040 bytes:Available Memory=9240 bytes:AvailMemAddress=0xfffc1be8
FreePoolManagerDriver::BcmFpmMemoryReserve:  INFO - Reserved 1152 bytes:Available Memory=8088 bytes:AvailMemAddress=0xfffc2068
BcmMacInit: advMapRunAheadTimeMin = 5120 (0x00001400) 10.24 MHz ticks, 500 usec
0x0000085c [tStartup] BcmDocsisCmHalIf::Register:  (DOCSIS CableModem HalIf) CM HAL reports h/w support for PHS, bitmask=0x3
0x00000866 [tStartup] BcmDocsisCmHalIf::Register:  (DOCSIS CableModem HalIf) CM HAL reports h/w support for PHS, size=64 bytes.
-> End DOCSIS CM WAN interface

-> Begin Ethernet LAN interfaces
        Creating HAL object for the Ethernet interface
        Registering Ethernet driver
FreePoolManagerDriver::BcmFpmMemoryReserve:  INFO - Reserved 1024 bytes:Available Memory=7064 bytes:AvailMemAddress=0xfffc2468
FreePoolManagerDriver::BcmFpmMemoryReserve:  INFO - Reserved 1024 bytes:Available Memory=6040 bytes:AvailMemAddress=0xfffc2868
-> End Ethernet LAN interfaces

-> Begin USB LAN interface
        Creating HAL object for the USB 1.1 interface
        Registering USB driver
-> End USB LAN interface

-> Begin 802.11 WiFi LAN interface.

        Creating HAL object for 802.11 RF (WiFi) interface #100
        Registering 802.11 RF (WiFi)(0) driver
        Creating HAL object for 802.11 RF (WiFi) interface #101
        Registering 802.11 RF (WiFi)(1) driver
        Creating HAL object for 802.11 RF (WiFi) interface #102
        Registering 802.11 RF (WiFi)(2) driver
        Creating HAL object for 802.11 RF (WiFi) interface #103
        Registering 802.11 RF (WiFi)(3) driver
        Creating HAL object for 802.11 RF (WiFi) interface #104
        Registering 802.11 RF (WiFi)(4) driver
        Creating HAL object for 802.11 RF (WiFi) interface #105
        Registering 802.11 RF (WiFi)(5) driver
-> End 802.11 WDS WiFi LAN interfaces.

-> Begin IP Stack interfaces
-> Starting V2 DHCP Client subsystem...
        Creating HAL object for IP Stack1 (MAC Addr=00:1e:2a:34:d2:f8)
DHCPc:  Created default DHCP lease for IP Stack1
        using client id htype=1, value=00:1e:2a:34:d2:f8; auto-config enabled (IP, subnet, router).
        Registering IP Stack1 driver
Tcpip NI: Init - RegisteredStackCount = 1

        Creating HAL object for IP Stack2 (MAC Addr=00:09:5b:de:ad:02)
DHCPc:  Created default DHCP lease for IP Stack2
        using client id htype=1, value=00:09:5b:de:ad:02; auto-config enabled (IP, subnet, router).
        Registering IP Stack2 driver
Tcpip NI: Init - RegisteredStackCount = 2

        Creating HAL object for IP Stack3 (MAC Addr=00:1e:2a:34:d2:fa)
DHCPc:  Created default DHCP lease for IP Stack3
        using client id htype=1, value=00:1e:2a:34:d2:fa; auto-config enabled (IP, subnet, router).
        Registering IP Stack3 driver
Tcpip NI: Init - RegisteredStackCount = 3

        Creating HAL object for IP Stack4 (MAC Addr=00:1e:2a:34:d2:fb)
DHCPc:  Created default DHCP lease for IP Stack4
        using client id htype=1, value=00:1e:2a:34:d2:fb; auto-config enabled (IP, subnet, router).
        Registering IP Stack4 driver
Tcpip NI: Init - RegisteredStackCount = 4

        Creating HAL object for IP Stack5 (MAC Addr=00:1e:2a:34:d2:fc)
DHCPc:  Created default DHCP lease for IP Stack5
        using client id htype=1, value=00:1e:2a:34:d2:fc; auto-config enabled (IP, subnet, router).
        Registering IP Stack5 driver
Tcpip NI: Init - RegisteredStackCount = 5

        Creating HAL object for IP Stack6 (MAC Addr=00:1e:2a:34:d2:f9)
DHCPc:  Created default DHCP lease for IP Stack6
        using client id htype=1, value=00:1e:2a:34:d2:f9; auto-config enabled (IP, subnet, router).
        Registering IP Stack6 driver
Tcpip NI: Init - RegisteredStackCount = 6

        IP Stack7 not enabled or failed to create and start interface; no other stacks will be loaded.
-> End IP Stack interfaces

^^^ Interface creation and driver startup complete ^^^

BcmCommandTable::AddSubtable:  ERROR - Attempted to add subtable that already exists!
Creating the PacketCable Forwarder...
  Adding IP Stack6 HalIf to the PacketCable Forwarder
Calling BcmEpsCmDocsisSystem::PostDriverInitialization()...
Creating the CableHome Forwarder...
  Adding Ethernet HalIf to the CableHome Forwarder
  Adding USB HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(0) HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(1) HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(2) HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(3) HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(4) HalIf to the CableHome Forwarder
  Adding 802.11 RF (WiFi)(5) HalIf to the CableHome Forwarder
  Adding IP Stack3 HalIf to the CableHome Forwarder
  Adding IP Stack4 HalIf to the CableHome Forwarder
  Adding IP Stack5 HalIf to the CableHome Forwarder
Creating the DOCSIS Forwarder...
  Adding DOCSIS CableModem HalIf as the default interface to the DOCSIS Forwarder
  Adding IP Stack1 HalIf to the DOCSIS Forwarder
  Adding IP Stack2 HalIf to the DOCSIS Forwarder

  Adding WAN-Man Interface HalIf as the default interface to the CableHome Forwarder
  Adding CableHome Embedded Interface HalIf to the DOCSIS Forwarder
0x00000a78 [tStartup] BcmEmtaEpsCmDocsisSystem::InstallMiniUsfs:  (BFC System) Installing Mini-Usfs snoop

Linking Docsis and PacketCable packet switches...
  Adding WAN-Man Interface HalIf as the default interface to the PacketCable Forwarder
  Adding PacketCable Embedded Interface HalIf to the DOCSIS Forwarder
0x00000a96 [tStartup] BcmSled::GlobalEnable:  (Singleton Instance) WARNING - eDOCSIS SLED is being disabled.
BcmFirewallThread::GetSingletonInstance:  WARNING - the singleton instance is NULL, and someone is accessing it!
Current IP address is default 0.0.0.0.
0x00000ab4 [tStartup] BcmEcosIpHalIf::ConfigureLeaseImpl:  (IP Stack2 HalIf)
Configuring IP stack 2:
  IP Address = 192.168.100.1 (primary IP address)
   Subnet Mask = 255.255.255.0
   Router = 192.168.100.254
   IsPrimaryInterface = 0

Creating Propane Control Thread...
Propane version: 2.0.1 (28 Oct 2002)
Instantiating CmSnmpAgent object.
Starting SNMP subsystem
Registering STP Filter Snoop with all interfaces.
Registering DOCSIS MIB Filter Snoop with CPE and WAN interfaces.
0x00000d02 [tStartup] BcmDocsisCmHalIf::RegisterSnmpObjects:  (DOCSIS CableModem HalIf) Interface 10 additional registration w/ SNMP agent OK.
0x00000d20 [tStartup] BcmPacketSwitchBridgingHalIf::RegisterSnmpObjects:  (CableHome Embedded Interface HalIf) Interface 39 additional registration w/ SNMP agent OK.
0x00000d34 [tStartup] BcmPacketSwitchBridgingHalIf::RegisterSnmpObjects:  (PacketCable Embedded Interface HalIf) Interface 39 additional registration w/ SNMP agent OK.
CmSnmpAgent installing views...
Vendor CM Agent w/ BRCM Factory Support setting V1/V2 view to unrestricted
Vendor CM Agent w/ BRCM Factory Support IpStackEvent: Ip=0.0.0.0, Subnet=0.0.0.0, Gateway=0.0.0.0
  Ip addr is the same, not rebinding.
Vendor CM Agent w/ BRCM Factory Support installing engine ID...
Vendor CM Agent w/ BRCM Factory Support installing context...
Creating SNMP agent CPE diag agent
Vendor CPE Agent w/ BRCM Factory Support setting V1/V2 view to unrestricted
Vendor CPE Agent w/ BRCM Factory Support IpStackEvent: Ip=192.168.100.1, Subnet=255.255.255.0, Gateway=192.168.100.254
Vendor CPE Agent w/ BRCM Factory Support enabling management.
Vendor CPE Agent w/ BRCM Factory Support sending deferred traps...
Done w/ deferred traps.
BcmSnmpThread starting thread operation.
Vendor CPE Agent w/ BRCM Factory Support installing engine ID...
Vendor CPE Agent w/ BRCM Factory Support installing context...
Vendor CPE Agent w/ BRCM Factory Support setting V1/V2 view to docsisCpeView
SNMP startup complete.
  Added WPA-NAS snoop to 802.11 interface.
Current IP address is default 0.0.0.0.
0x00000f64 [tStartup] BcmEcosIpHalIf::ConfigureLeaseImpl:  (IP Stack5 HalIf)
Configuring IP stack 5:
  IP Address = 192.168.0.1 (primary IP address)
   Subnet Mask = 255.255.255.0
   Router = 192.168.0.254
   IsPrimaryInterface = 0

0x00000f78 [tStartup] BcmEpsCmDocsisApplication::InitializeLanInterface:  (EPS-CM DOCSIS Application) Binding 192.168.0.1 ip address to interface.
0x00000f82 [tStartup] BcmCableHomeIpStackHelper::CreateLease:  DHCP lease already exists, releasing lease clientId = htype=1, value=00:1e:2a:34:d2:fa
Creating SNMP agent CH agent
CH agent disabling management.
CH agent defering traps.
 Registering Passthrough Entry Table
 Registering Passthrough Entry Table
Current IP address is default 0.0.0.0.
0x00000faa [CableHomeCtlThread] BcmEcosIpHalIf::ConfigureLeaseImpl:  (IP Stack4 HalIf)
Configuring IP stack 4:
  IP Address = 192.168.100.5 (primary IP address)
   Subnet Mask = 255.255.255.0
   Router = 192.168.100.254
   IsPrimaryInterface = 0

rtrequest: allow interface on same subnet.
S *** FWSTATE: kFwStateFwActive ***
Firewall: WAN HalIf is CableHome Embedded Interface(70736231)
Instantiating CableHome SnmpAgent object.
ES2WindowClosed! (unexpected)
Vendor CM Event Log initializing with stored events.
Event log initialization complete.
Vendor CM Agent w/ BRCM Factory Support setting master agent to Vendor CH Agent w/ BRCM Factory Support
===> WARNING: Can't add ieee802dot11Group @ 0x81a86f4c to iso, group already exists.
===> WARNING: Can't add ieee802dot11Group @ 0x81a862ec to iso, group already exists.
===> WARNING: Can't add ieee802dot11Group @ 0x81a8568c to iso, group already exists.
===> WARNING: Can't add ieee802dot11Group @ 0x81a84a2c to iso, group already exists.
===> WARNING: Can't add ieee802dot11Group @ 0x81a83dcc to iso, group already exists.
CHSnmpAgent installing views...
Vendor CH Agent w/ BRCM Factory Support setting V1/V2 view to unrestricted
Vendor CH Agent w/ BRCM Factory Support IpStackEvent: Ip=0.0.0.0, Subnet=0.0.0.0, Gateway=0.0.0.0
  Ip addr is the same, not rebinding.
Vendor CH Agent w/ BRCM Factory Support installing engine ID...
Vendor CH Agent w/ BRCM Factory Support installing context...

Setting EngineId for CableHome
DumpBuf(27): Setting CH engine - <80 00 11 ae 04 50 53 2f 30 30 3a 31 65 3a 32 61 3a 33 34 3a 64 32 3a 66 61 01 00 >
Creating SNMP agent CH diag agent
CH diag agent setting V1/V2 view to unrestricted
CH diag agent IpStackEvent: Ip=192.168.0.1, Subnet=255.255.255.0, Gateway=192.168.0.254
CH diag agent enabling management.
CH diag agent sending deferred traps...
Done w/ deferred traps.
CH diag agent installing engine ID...
CH diag agent installing context...
Stored lease with clientId: htype=0, value=00 1e 2a 34 d2 fd Ip address: 192.168.0.10 has been added as zombie!

0x0000139c [tStartup] CableHomeDhcpServerIpServiceAppIf::HandleStoredDhcpServerLease:  (CableHomeDhcpServerIpServiceAppIf) Updating database entry method to (4) for stored lease 192.168.0.10
0x000013b0 [tStartup] CableHomeDhcpServerIpServiceAppIf::HandleStoredDhcpServerLease:  (CableHomeDhcpServerIpServiceAppIf) Updating NonVol method to (4) for stored lease 192.168.0.10
0x000013c4 [tStartup] CableHomeDhcpServerIpServiceAppIf::HandleStoredDhcpServerLease:  (CableHomeDhcpServerIpServiceAppIf) Adding NAPT entry for LAN address = 192.168.0.10
0 Registering Qos2 Policy Table
 Registering Qos2 Traffic Class Table
 Registering Lan Addr Entry Table
x Registering Wan Data Address Entry Table
 Registering Passthrough Entry Table
0x000013ec [tStartup] BcmRipClientThread::AuthEnable:  (Rip Client Thread) Broadcom V2 RIP Client MD5 Authentication status = 0
0x000013f6 [tStartup] BcmRipClientThread::Enable:  (Rip Client Thread) Broadcom RIP disabled!
Dynamic DNS client DISABLED.
Setting up the NetgearHttpCacheVariables singleton pointer.
0x00001432 [tStartup] BcmRgHttpServerThread::Enable:  (HttpServerThread) Broadcom HttpServerThread running status = 1

Residential Gateway UPnP mode enable = 0


**********************************************************
 Running as a Residental Gateway Enabled device!
**********************************************************



***********************************************
 (DHCP) WAN IP Connection Configuration
***********************************************

0x00001464 [tStartup] CableHomeDhcpServerIpServiceAppIf::EnableDhcpServerProvisioning:  (CableHomeDhcpServerIpServiceAppIf) Setting DHCP server provisioning to (1)
0BOS: Enter bosInit
BOS: Exit bosInit
Creating SNMP agent EMTA agent
EMTA agent entering RFC-2576 Coexistence security mode.
EMTA agent setting V1/V2 view to coexistenceView
EMTA agent entering Basic/Hybrid flow provisioning mode.
initBlindData: nvramSize= 716
mtaNvCalcChecksum: checksum= 1846036517EMTA battery callback = 0x806cfd08
0

bosAppRootTask() - Is it morning already? Spawning app task (epoch #0)...

TaskCreate - spawn new task aoAP
0013e2 [DNS Server Thread] BcmDnsServerThread::ThreadMain:  (DNS Server Thread) Broadcom V2 DNS Server starting...waiting for events...
VTaskCreate - spawn new task CMT_EXCEPTION_IST
TaskCreate - spawn new task Load-balance
0x    14b4 [IpsecTimer] IpsecTimer::ThreadMain:  Entering...
endor CH Event Log w/ BRCM Factory Support initializing with stored events.
Event log initialization complete.
TaskCreate - spawn new task HTSK


CC: Initialization starting...

===> WARNING: Can't add esafeMibObjectsGroup @ 0x80ba48c0 to iso, group already exists.
===> WARNING: Can't add snmpSetGroup @ 0x80b9e82c to iso, group already exists.
0x000015d6 [tStartup] BcmPacketSwitchBridgingHalIf::RegisterSnmpObjects:  (WAN-Man Interface HalIf) Interface 40 additional registration w/ SNMP agent OK.
emta factory agent IpStackEvent: Ip=0.0.0.0, Subnet=0.0.0.0, Gateway=0.0.0.0
  Ip addr is the same, not rebinding.
emta factory agent installing engine ID...
emta factory agent installing context...
emta factory agent setting V1/V2 view to
0x000016bc [tStartup] BcmSled::Register:  (Singleton Instance) WARNING - PacketCable Embedded Interface is already registered!
StartUsb()...
0x000016c6 [tStartup] CableHomeDhcpServerIpServiceAppIf::ArpServerLeasePool:  (CableHomeDhcpServerIpServiceAppIf) Arping Dhcp Server Lease pool to populate Usfs table: (192.168.0.10) --> (192.168.0)
Checking board manufacturing state...
WARNING: Board NV manufacturing incomplete.
  Check the following settings:
  IP stack 2 MAC
Installing temporary factory key.


                          *
                         * *
                         * *
                        *   *
                        *   *
                       *     *
                       *     *
                       *     *
                      *       *
                      *       *
                      *       *
                     *         *
                     *         *
                     *         *
                     *         *
                    *           *
          *         *           *         *
        *   *       *           *       *   *          ***
*     *      *     *             *     *      *     *       *******************
   *          *   *               *   *          *
                *                   *

Broadcom Corporation

 +----------------------------------------------------------------------------+
 |       _/_/     _/_/_/_/    _/_/                                            |
 |      _/  _/   _/        _/    _/   Broadband                               |
 |     _/  _/   _/        _/                                                  |
 |    _/_/     _/_/_/    _/           Foundation                              |
 |   _/  _/   _/        _/                                                    |
 |  _/   _/  _/        _/    _/       Classes                                 |
 | _/_/_/   _/          _/_/                                                  |
 |                                                                            |
 | Copyright (c) 1999 - 2005 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.9.33.1 RELEASE                                                |
 |                                                                            |
 | Features:  Console TelnetConsole SshConsole Nonvol Fat HeapManager SNMP    |
 | Features:  Networking USB1.1                                               |
 +----------------------------------------------------------------------------+
 | Standard Embedded Target Support for BFC                                   |
 |                                                                            |
 | Copyright (c) 2003-2004 Broadcom Corporation                               |
 |                                                                            |
 | Revision:  3.0.1 RELEASE                                                   |
 |                                                                            |
 | Features:  PID=0xa020 Bootloader-Rev=2.1.6l                                |
 | Features:  Bootloader-Compression-Support=0x19                             |
 | Features:  Bcm80211g Library Build Aug 28 2007 12:26:16 Ver 3.130.35.1.16  |
 +----------------------------------------------------------------------------+
 | eCos BFC Application Layer                                                 |
 |                                                                            |
 | Copyright (c) 1999 - 2004 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.0.2 RELEASE                                                   |
 |                                                                            |
 | Features:  eCos Console Cmds, (no Idle Loop Profiler)                      |
 +----------------------------------------------------------------------------+
 |         _/_/    _/     _/                                                  |
 |      _/    _/  _/_/ _/_/   DOCSIS Cable Modem                              |
 |     _/        _/  _/ _/                                                    |
 |    _/        _/     _/                                                     |
 |   _/        _/     _/                                                      |
 |  _/    _/  _/     _/                                                       |
 |   _/_/    _/     _/                                                        |
 |                                                                            |
 | Copyright (c) 1999 - 2005 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.9.33.1 RELEASE                                                |
 |                                                                            |
 | Features:  AckCel(tm) DOCSIS 1.0/1.1/2.0 Propane(tm) CM SNMP w/Factory MIB |
 | Features:  Support CM Vendor Extension eDOCSIS SLED                        |
 +----------------------------------------------------------------------------+
 | Broadcom Data-Only CM Vendor Extension                                     |
 |                                                                            |
 | Copyright (c) 1999 - 2004 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.0.0a PRE-RELEASE                                              |
 |                                                                            |
 | Features:  (none)                                                          |
 +----------------------------------------------------------------------------+
 |         _/_/    _/    _/                                                   |
 |      _/    _/  _/    _/   CableHome Cable Modem                            |
 |     _/        _/    _/                                                     |
 |    _/        _/_/_/_/                                                      |
 |   _/        _/    _/      CableLabs Certified                              |
 |  _/    _/  _/    _/                                                        |
 |   _/_/    _/    _/                                                         |
 |                                                                            |
 | Copyright (c) 1999 - 2005 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.9.33.1 RELEASE                                                |
 |                                                                            |
 | Features:  CableHome 1.0/1.1 CH SNMP CH Customer Extension                 |
 +----------------------------------------------------------------------------+
 | Broadcom CableHome Customer Extension                                      |
 |                                                                            |
 | Copyright (c) 1999 - 2004 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.1.3 PRE-RELEASE                                               |
 |                                                                            |
 | Features:  ()                                                              |
 +----------------------------------------------------------------------------+
 |       _/     _/ _/_/_/ _/                                                  |
 |      _/_/ _/_/   _/   _/_/  Embedded MTA                                   |
 |     _/  _/ _/   _/   _/ _/                                                 |
 |    _/     _/   _/   _/  _/                                                 |
 |   _/     _/   _/   _/_/__/  CableLabs Certified                            |
 |  _/     _/   _/   _/    _/  PacketCable Certified                          |
 | _/     _/   _/   _/     _/                                                 |
 |                                                                            |
 | Copyright (c) 1999 - 2005 Broadcom Corporation                             |
 |                                                                            |
 | Revision:  3.9.21.1 RELEASE                                                |
 |                                                                            |
 | Features:  CVG834G_bcm93368wvg (EuroPacketCable) eCos                      |
 | Features:  IPSEC NCS PacketCable-v1.5                                      |
 | Features:  dspApp3368 (LDX app)                                            |
 | Features:  (MTA LIB DATE: Nov 27 2007 15:07:28)                            |
 +----------------------------------------------------------------------------+
 | Build Date:  Nov 27 2007                                                   |
 | Build Time:  15:29:53                                                      |
 | Built By:    root                                                          |
 +----------------------------------------------------------------------------+


Running the system...


Beginning Parental Control operation...


Beginning Cable Modem operation...


Beginning CableHome operation...


Beginning MTA operation...

BcmEmtaDhcpStateMachineGlue: Setting up the singleton pointer.

0x00001b26 [Scan Downstream Thread] BcmNetgearCmDownstreamScanThread::ThreadMain:  (Scan Downstream Thread) Scanning for a Downstream Channel...

==============================================================
Scanning Last Known Frequency..
==============================================================

331000000 Hz...
Type 'help' or '?' for a list of commands...

CM> 0x00001b62 [CableHomePingTool Thread] CableHomePingTool::ArpIpAddressRange:  (CableHomePingTool Thread) ARP'ing of Ip Address Range (192.168.0.10) --> (192.168.0.19)

==============================================================
Finish scanning Last Known Frequency
==============================================================



==============================================================
Scanning CFL Frequency..
==============================================================

442000000 Hz...
115125000 Hz...
122000000 Hz...
122500000 Hz...
123125000 Hz...
130000000 Hz...
138000000 Hz...
0x00001fe0 [HttpServerThread] BcmRgHttpServerThread::ThreadMain:  (HttpServerThread) Recv'd event to resynchronize sockets!
139125000 Hz...
146000000 Hz...
CM> 147125000 Hz...
154000000 Hz...
155125000 Hz...
160000000 Hz...
162000000 Hz...
163125000 Hz...
171125000 Hz...
235125000 Hz...
258000000 Hz...
266000000 Hz...
274000000 Hz...
282000000 Hz...
306000000 Hz...
307750000 Hz...
313750000 Hz...
314000000 Hz...
319750000 Hz...
322000000 Hz...
325750000 Hz...
330000000 Hz...
394000000 Hz...
410000000 Hz...
426000000 Hz...
427125000 Hz...
435000000 Hz...
435125000 Hz...
435137500 Hz...
453000000 Hz...
458000000 Hz...
570000000 Hz...
570375000 Hz...
578000000 Hz...
602375000 Hz...
610375000 Hz...
626000000 Hz...
634000000 Hz...
634750000 Hz...
650000000 Hz...
650375000 Hz...
666000000 Hz...
674375000 Hz...
682000000 Hz...
698000000 Hz...
770000000 Hz...

==============================================================
Finish scanning CFL Frequency.
==============================================================


299000000 Hz...
307000000 Hz...
315000000 Hz...
323000000 Hz...
331000000 Hz...
339000000 Hz...
347000000 Hz...
355000000 Hz...
363000000 Hz...
371000000 Hz...
379000000 Hz...
387000000 Hz...
395000000 Hz...
403000000 Hz...
411000000 Hz...
419000000 Hz...
427000000 Hz...
435000000 Hz...
443000000 Hz...
451000000 Hz...
459000000 Hz...
467000000 Hz...
475000000 Hz...
483000000 Hz...
491000000 Hz...
499000000 Hz...
507000000 Hz...
515000000 Hz...
523000000 Hz...
531000000 Hz...

==============================================================
Scanning Last Known Frequency..
==============================================================

331000000 Hz...

==============================================================
Finish scanning Last Known Frequency
==============================================================


539000000 Hz...
547000000 Hz...
555000000 Hz...
563000000 Hz...
571000000 Hz...
579000000 Hz...
587000000 Hz...
595000000 Hz...
603000000 Hz...
611000000 Hz...
.
==============================================================
Scanning CFL Frequency..
==============================================================

442000000 Hz...
115125000 Hz...
122000000 Hz...
122500000 Hz...
123125000 Hz...
130000000 Hz...
138000000 Hz...
139125000 Hz...
146000000 Hz...
147125000 Hz...
154000000 Hz...
}}}
