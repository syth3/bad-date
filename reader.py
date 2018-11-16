import csv
import os
import sys

from datetime import datetime

class MacEntry:
    def __init__(self, access_time, modify_time, change_time):
        self.access_time = access_time
        self.modify_time = modify_time
        self.change_time = change_time

file_name = os.path.abspath(sys.argv[1])

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

    
for key in file_name_dict:
    count = 0
    print("File =", key)
    print("==========================================")
    print("access_time =", file_name_dict[key].access_time)
    print("modify_time =", file_name_dict[key].modify_time)
    print("change_time =", file_name_dict[key].change_time)
    print("==========================================")
    print()
  
