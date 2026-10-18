#!/bin/bash

echo "Installing SW1 -> SW2 flow"

ovs-ofctl -O OpenFlow13 add-flow s1 \
"priority=100,in_port=3,actions=output:1"

echo "Installing SW2 -> SW1 flow"

ovs-ofctl -O OpenFlow13 add-flow s2 \
"priority=100,in_port=1,actions=output:3"

echo "Flow rules installed"
