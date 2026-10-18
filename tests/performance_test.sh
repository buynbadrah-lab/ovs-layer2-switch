#!/bin/bash

echo "Network Performance Test"

echo ""
echo "Run Mininet first."

echo ""
echo "TCP test example:"
echo "h2 iperf -s &"
echo "h1 iperf -c 10.0.0.2"

echo ""
echo "UDP test example:"
echo "h2 iperf -s -u &"
echo "h1 iperf -c 10.0.0.2 -u -b 10M"
