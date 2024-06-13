#!/bin/bash

# Using curl to get public IP from ifconfig.me
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

public_ip=$(curl -s ifconfig.me)

file_path="/home/sam/githubproject/sysinfo/risi.ip"

# Write the value to the file
echo "$public_ip" > "$file_path"
echo "Current timestamp: $timestamp"

git add .
git commit -m "IPv6 Update $timestamp" 
git push main origin main
