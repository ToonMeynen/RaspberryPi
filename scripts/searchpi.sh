#!/bin/bash
#find your pi on the network
IP=`ifconfig |grep --color -e 'inet 192.*' |cut -f 2 -d ' '`
NETWORK=`echo $IP |sed 's/[1-9]*$/0/g'`
sudo nmap -sP $NETWORK/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'
