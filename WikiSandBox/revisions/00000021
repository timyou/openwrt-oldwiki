## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:WikiSandBox
#format wiki
#language en
Bitte fühle dich frei um hier zu experimentieren, after the four dashes below... and please do '''NOT''' create new pages without any meaningful content just to try it out!

'''Tip:''' Shift-click "HelpOnEditing" to open a second window with the help pages.
----

== Formatting ==

''italic'' '''bold''' {{{typewriter}}} 

`backtick typewriter` (configurable)

~+ bigger +~ ~- smaller -~

{{{
preformatted some more
and some more lines too

}}}

{{{#!python
def syntax(highlight):
    print "on"
    return None
}}}


{{{#!java
  public void main(String[] args]){
     System.out.println("Hello world!");
  } 

}}}


== Linking ==

HelpOnEditing MoinMoin:InterWiki 

http://moinmoin.wikiwikiweb.de/ [http://www.python.org/ Python]

someone@the.inter.net

["lowercase"]
["lowercase and with spaces"]

=== Image Link ===
http://c2.com/sig/wiki.gif

== Smileys ==

/!\ Alert

== Lists ==

=== Bullet ===
 * first
   1. nested and numbered
   1. numbered lists are renumbered
 * second
 * third
 blockquote
   deeper

=== Glossary ===
 Term:: Definition

=== Drawing ===
drawing:mytest

= Heading 1 =
== Heading 2 ==
=== Heading 3 ===
==== Heading 4 ====

= IRC Log test =

{{{#!irc
(23:18) <     jroes> ah
(23:19) <     jroes> hm, i like the way {{{ works, but i was hoping the lines would wrap
(23:21) -!- gpciceri [~gpciceri@host181-130.pool8248.interbusiness.it] has quit [Read error: 110 (Connection timed out)]
(23:36) < ThomasWal> you could also write a parser or processor
(23:38) <     jroes> i could?
(23:38) <     jroes> would that require modification on the moin end though?
(23:38) <     jroes> i cant change the wiki myself :x
(23:39) < ThomasWal> parsers and processors are plugable
(23:39) < ThomasWal> so you dont need to change the core code
(23:40) < ThomasWal> you need to copy it to the wiki data directory though
(23:40) <     jroes> well, what i meant to say was that i dont have access to the box running the wiki
(23:40) < ThomasWal> then this is no option awdsd asdasd sa asdasd sad asdadasds adasd asd asd asd asd asd a dadad ad adad ad asd asd adad asdasd asd adad as d
(23:40) <     jroes> yeah :/
}}}

Kia Ora this is a test about how to use this

||'''Header'''||||''Header''||
||text||text2||text3||

= Heading test 1 =
== Heading test 2 ==
=== Heading test 3 ===

Playing with different ways to link:
 * TinyproxyPackage
 * [[tinyproxy]]
 * [tinyproxy]
 * Package/tinyproxy
 * [Configuration]
 * OpenWrtDocs/Configuration
 * PackageTinyproxy
 * tinyproxy
 * ["tinyproxy"]
 * ["all lowercase and with spaces"]

= Wiki Newbie Testing =
=== Creating a code window ===
{{{
#!/usr/bin/microperl
#######################################################################
# Author:  Kenny Saltiel (NekMech)
# Date:    9 Apr 2007
# Version: 1.0
#
# Perl script to read and set the DS1307 clock chip, convert to 
# real-time or set system clock
#
# Layout of chip registers:
# ADDR| 7       6       5       4       3       2       1       0
#------------------------------------------------------------------
# 0x00| CH  |      10 seconds        |         seconds            |
# 0x01|  0  |      10 minutes        |         minutes            |
# 0x02|  0  | 12/24 |10h/AM-PM| 10h  |          hours             |
# 0x03|  0  |   0   |   0   |   0    |  0   |     day of week     |
# 0x04|  0  |   0   |    10 date     |          date              |
# 0x05|  0  |   0   |   0   |   10m  |          month             |
# 0x06|           10 year            |          year              |
# 0x07|                     control register                      |
# 0x08 - 0x3F                 data  registers                     |
#------------------------------------------------------------------
#
# Notes:
# 1) Clock is read by setting FF in last data register causing register 
#    pointer overflow and then reading 7 bytes.
#    Avoid using last data register (0x3F) since it will be overwritten.
# 2) Since year is stored as last 2 digits only, year 2000+ is assumed
# 3) Clock init will start the counter and turn on SQW at 1Hz
########################################################################

my $help = <<EOH;

gethwclock.pl <sethw|gethw|setos|inithw>

sethw - set the hardware clock from system time
gethw - display the date stored in the hardware clock
setos - set the system time from the hardware clock
inithw - initialize hardware clock control register
         and start counter. This should be done once before
         using the clock for the first time
EOH


}}}
