import csv
import os
import sys

from datetime import datetime

class MacEntry:
    def __init__(self, date, type):
        self.date = date
        self.type = type


file_name = os.path.abspath(sys.argv[1])

with open(file_name) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # csv.reader(csv_file, delimiter=',')
    line_count = 0
    file_name_dict = {}
    for key in csv_reader:
        file_name = key["File Name"]
        date = datetime.strptime(key["Date"], '%a %m %d %Y %H:%M:%S')
        mac_object = MacEntry(date, key["Type"])
        if file_name in file_name_dict:
            file_name_dict[file_name].append(mac_object)
        else:
            file_name_dict[file_name] = [mac_object]
    
for key in file_name_dict:
    count = 0
    print("key =", key)
    print("==========================================")
    obj_list = file_name_dict[key]
    for obj in obj_list:
        count += 1
        print("Date:", obj.date)
        print("Type:", obj.type)
        if count == len(obj_list):
            pass
        else:
            print()
    print("==========================================")
    print()
  
