"""
file: reader.py
language: python3
author: Jacob Brown
description: Detect files that have been potentially timestomped by flagging files that have a more recent
  modify timestamp than change timestamp. This is because whenever you modify the contents of a file, you increase
  it's size and therefore modify the change timestamp as well.
"""

import csv
import os
import sys
from datetime import datetime

# Check for proper arguments
if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv":
    print("Usage: python3 reader.py <.csv file>")
    exit(1)

# gather input file
file_name = os.path.abspath(sys.argv[1])

# Class which holds access, modify, and change time
class MacEntry:
    def __init__(self, access_time, modify_time, change_time):
        self.access_time = access_time
        self.modify_time = modify_time
        self.change_time = change_time

# Convert csv data into a custom dictionary mapping filenames to all of their respective timestamps
with open(file_name) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    file_name_dict = {}
    for key in csv_reader:
        date_type = key["Type"]
        access_time = None
        modify_time = None
        change_time = None
        file_name = key["File Name"]
        date = datetime.strptime(key["Date"], '%a %m %d %Y %H:%M:%S')
        if 'a' in date_type:
            access_time = datetime.strptime(key["Date"], '%a %m %d %Y %H:%M:%S')
        if 'm' in date_type:
            modify_time = datetime.strptime(key["Date"], '%a %m %d %Y %H:%M:%S')
        if 'c' in date_type:
            change_time = datetime.strptime(key["Date"], '%a %m %d %Y %H:%M:%S')

        if file_name in file_name_dict:
            if access_time != None:
                file_name_dict[file_name].access_time = access_time
            if modify_time != None:
                file_name_dict[file_name].modify_time = modify_time
            if change_time != None:
                file_name_dict[file_name].change_time = change_time
        else:
            file_name_dict[file_name] = MacEntry(access_time, modify_time, change_time)

# Loop through all entries in dictionary to flag which file timestamps seem wrong
# Timestamps that seem wrong are ones where the modify time is more recent than the change time
count = 0
for key in file_name_dict:
    if file_name_dict[key].modify_time == None or file_name_dict[key].access_time == None or file_name_dict[key].change_time == None:
        print("File exluded due to inconclusive timestamps:", key)
        break
    if file_name_dict[key].change_time < file_name_dict[key].modify_time:
        count += 1
        print("THIS FILE MAY HAVE BEEN TIMESTOMPED:", key)
        print("access_time =", file_name_dict[key].access_time)
        print("modify_time =", file_name_dict[key].modify_time)
        print("change_time =", file_name_dict[key].change_time)

print()
if count == 0:
    print("No files have been flagged for timestomping")

print("Number of timestamp files found:", count)
