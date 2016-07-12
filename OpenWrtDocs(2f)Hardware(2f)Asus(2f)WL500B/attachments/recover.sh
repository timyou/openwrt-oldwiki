#!/bin/bash

# recovery script for wl500g
#
# Copyright (C) 2004 by Oleg I. Vdovikin <oleg@cs.msu.su>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

if [ -z "$1" ] || [ ! -f $1 ]; then
    echo Usage: $0 firmware.trx
cat << EOF
IMPORTANT:
   1) be sure POWER led is flashing (If this is not a case
      poweroff the device, push the reset button & power on
      it again, then release button)
   2) connect your pc to the LAN port
   3) be sure your link is up and has an address in the
      192.168.1.0/24 address range (and not the 192.168.1.1)
EOF
    exit 0
fi
echo Confirming IP address setting...
echo -en "get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null\nquit\n" | tftp 192.168.1.1
echo Recovering 192.168.1.1 using $1...
echo -en "binary\nput $1 ASUSSPACELINK\nquit\n" | tftp 192.168.1.1
echo Please wait until leds stops flashing.
