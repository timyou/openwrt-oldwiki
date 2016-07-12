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

my @dowarray = ("","Mon","Tue","Wed","Thu","Fri","Sat","Sun");
my @montharray = ("","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");
my $i2cbus = "0";
my $i2caddr = "104";
my $lastregister = "63";
my $lastregvalue = "255";
my $regcount = "7";

my %hwregisters = (
   'seconds' => {
                   'register' => "0",
                   'data'     => "0"
                },
   'minutes' => {
                   'register' => "1",
                   'data'     => ""
                },
   'hours'   => {
                   'register' => "2",
                   'data'     => ""
                },
   'dow'     => {
                   'register' => "3",
                   'data'     => ""
                },
   'date'    => {
                   'register' => "4",
                   'data'     => ""
                },
   'month'   => {
                   'register' => "5",
                   'data'     => ""
                },
   'year'    => {
                   'register' => "6",
                   'data'     => ""
                },
   'control' => {
                   'register' => "7",
                   'data'     => "16"
                }
);
                                                           
my ($seconds,$minutes,$hours,$dow,$date,$month,$year);

sub showhelp {
   print $help;
}

sub get_sys_date {
   my $osdate_command = 'date +%S:%M:%H:%u:%d:%m:%y';
   my $osdate = `$osdate_command`;
   if ($?) {
      print $osdate,"\n";
      return(0);
   }
   chomp($osdate);
   # Debug: 
   # print "Got OS: $osdate\n";
   return($osdate);
}

sub convert_bcd_to_decimal {
   my $bcdvalue = shift;
   return(oct("0x".$bcdvalue));
}

sub set_hw_reg_values {
   # Load hash with OS date info
   my $OSdata = shift;
   ($hwregisters{'seconds'}->{'data'},
    $hwregisters{'minutes'}->{'data'},
    $hwregisters{'hours'}->{'data'},
    $hwregisters{'dow'}->{'data'},
    $hwregisters{'date'}->{'data'},
    $hwregisters{'month'}->{'data'},
    $hwregisters{'year'}->{'data'}) = split(/:/,$OSdata);
    
   # Convert values to correct notation and send data to hw clock.
   # Seconds should be last because of the way the clock resets the
   # internal divider when seconds are written.
   
   foreach my $reg (keys %hwregisters) {
      next if ($reg =~ /(control|seconds)/);
      $hwregisters{$reg}->{'data'} = 
         convert_bcd_to_decimal($hwregisters{$reg}->{'data'});
      set_hw_reg($hwregisters{$reg}->{'register'},
                 $hwregisters{$reg}->{'data'}) or 
                    die "clock set failed on $reg\n"; 
   }
   $hwregisters{'seconds'}->{'data'} = 
      convert_bcd_to_decimal($hwregisters{'seconds'}->{'data'});
   set_hw_reg($hwregisters{'seconds'}->{'register'},
              $hwregisters{'seconds'}->{'data'}) or 
                 die "clock set failed on seconds\n"; 
}

sub set_hw_reg {
   my ($regnum, $regvalue) = @_;
   my $i2c_command = "./i2cset $i2cbus $i2caddr $regnum $regvalue";
   my $i2cset = `$i2c_command`;
   if ($?) {
      print $i2cset,"\n";
      return(0);
   }
   return(1);
}

sub set_hw_clock {
   my $OSdata = get_sys_date();
   return (0) unless ($OSdata);
   set_hw_reg_values($OSdata);
   return(1);
}

sub get_hw_regs {
   my $i2csetstate = set_hw_reg($lastregister,$lastregvalue);
   return (0) unless ($i2csetstate);
   my $readhwclock = "./i2cread $i2cbus $i2caddr $regcount";
   my $rtcregs = `$readhwclock`;
   if ($?) {
      print $rtcregs,"\n";
      return(0);
   }
   chomp($rtcregs);
   # Debug: 
   # print "Got: $rtcregs\n";
   return ($rtcregs);
}

sub get_hw_data {
   my $rtcclockbytes = get_hw_regs() or die;
   my ($null,$null,$rtcseconds,$rtcminutes,$rtchours,$rtcday,$rtcdate,$rtcmonth,$rtcyear) =
       split(/\s+/,$rtcclockbytes);
   $date = sprintf("%02s",sprintf("%x",$rtcdate));
   $month = sprintf("%02s",sprintf("%x",$rtcmonth));
   $hours = sprintf("%02s",sprintf("%x",$rtchours));
   $minutes = sprintf("%02s",sprintf("%x",$rtcminutes));
   $seconds = sprintf("%02s",sprintf("%x",$rtcseconds));
   $year = "20".sprintf("%02s",sprintf("%x",$rtcyear));
   $dow = $rtcday;
}

sub show_hw_date {
   get_hw_data();
   printf("%s %s %s %s:%s:%s %s\n",
          $dowarray[$dow],
          $montharray[$month],
          $date, 
          $hours,
          $minutes,
          $seconds,
          $year);
}

sub set_os_date {
   get_hw_data();
   my $osdate = $month.$date.$hours.$minutes.$year.".".$seconds;
   my $res = `date -s $osdate`;
   if ($?) {
      print $res,"\n";
      return(0);
   }
   retunr(1);
}

sub init_hw_clock {
   set_hw_reg($hwregisters{'control'}->{'register'},
              $hwregisters{'control'}->{'data'}) or 
                 die "clock init failed on control register\n"; 
   set_hw_reg($hwregisters{'seconds'}->{'register'},
              $hwregisters{'seconds'}->{'data'}) or 
                 die "clock set failed on seconds register\n"; 
   return(1);
}

## Main ##

if (scalar(@ARGV)) {
   $option = shift(@ARGV);
} else {
   showhelp(); 
   exit(0);
}

if ($option eq "sethw") {
   set_hw_clock() or die "failed to set hwclock\n";
} elsif ($option eq "gethw") {
   show_hw_date();
} elsif ($option eq "setos") {
   set_os_date() or die "failed to set os clock\n";
} elsif ($option eq "inithw") {
   print "hw clock init succeeded\n" if init_hw_clock();
} else {
   showhelp();
   exit(0);
}

}}}
