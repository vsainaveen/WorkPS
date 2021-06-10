#!/usr/bin/env python
 
# Import modules
import os
import time
import sys
 
# Define variables for AFTNAs
xdays = 30
path = r'/mnt/EDNAS/EDSC/'
now = time.time()
date = time.strftime('%Y-%m-%d', time.localtime(now))
aftList = []
count = 0
logname = "removal_log_" + date
 
# Delete Files with modification date older than 30 days and log results.
aftList.append("List of all files older than " + str(xdays) + " days in AFTNAS")
aftList.append("==========================" + "=" * len(str(xdays)) + "=====")
for root, dirs, files in os.walk(path):
  for name in files:
    filename = os.path.join(root, name)
    if os.stat(filename).st_ctime < now - (xdays * 86400):
      aftList.append(filename)
      os.remove(filename)
      count += 1

# Add Summary Line
now = time.time()
compTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
aftList.append("Cleanup finished at " + str(compTime) + " and there were " + str(count) + " files removed.")

# Write Log file
with open('/mnt/EDNAS/file_cleanup/' + logname, mode='wt') as logfile:
    logfile.write('\n'.join(aftList)) 

# Define variables for Solvas
path = r'/mnt/SOLVAS/SOLVAS/'
now = time.time()
solvasList = []
count = 0


# Delete Files with modification date older than 30 days and log results.
solvasList.append("List all files older than " + str(xdays) + " days in AFTNAS")
solvasList.append("==========================" + "=" * len(str(xdays)) + "=====")
for root, dirs, files in os.walk(path):
  for name in files:
    filename = os.path.join(root, name)
    if os.stat(filename).st_ctime < now - (xdays * 86400):
      solvasList.append(filename)
      os.remove(filename)
      count += 1

# Add Summary Line
now = time.time()
compTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
solvasList.append("Cleanup finished at " + str(compTime) + " and there were " + str(count) + " files removed.")

# Write Log file
with open('ls /mnt/SOLVAS/file_cleanup/' + logname, mode='wt') as logfile:
    logfile.write('\n'.join(solvasList)) 