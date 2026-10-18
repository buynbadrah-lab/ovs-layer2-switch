#!/bin/bash

echo "OVS Layer 2 Connectivity Test"
echo "Testing basic connectivity..."

sudo mn \
--topo single,2 \
--switch ovsk,protocols=OpenFlow13 \
--test pingall
