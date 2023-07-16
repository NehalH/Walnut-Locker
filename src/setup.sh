#!/bin/bash

# Install auditd
sudo apt-get install auditd

# Define the directory or wildcard pattern to monitor
directory="/"
pattern="/**/*"

# Define the Audit rule options
options="-p rwa -k file-access"

# Modify the Audit rules
echo "-w $directory $options" >> /etc/audit/audit.rules
echo "-w $pattern $options" >> /etc/audit/audit.rules

# Restart the auditd service
service auditd restart
