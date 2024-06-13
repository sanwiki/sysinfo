#!/bin/bash

# Using curl to get public IP from ifconfig.me
public_ip=$(curl -s ifconfig.me)

echo "$public_ip"