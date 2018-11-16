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

all_equal = 0
m_equal_a = 0
m_equal_c = 0
a_equal_c = 0

m_lessthan_a = 0
m_lessthan_c = 0

a_lessthan_m = 0
a_lessthan_c = 0

c_lessthan_a = 0
c_lessthan_m = 0

for key in file_name_dict:
    if file_name_dict[key].modify_time == None or file_name_dict[key].access_time == None or file_name_dict[key].change_time == None:
        print("File exluded:", key)
        print("access_time =", file_name_dict[key].access_time)
        print("modify_time =", file_name_dict[key].modify_time)
        print("change_time =", file_name_dict[key].change_time)
        break
    if file_name_dict[key].modify_time == file_name_dict[key].access_time == file_name_dict[key].change_time:
        all_equal += 1
    if file_name_dict[key].modify_time == file_name_dict[key].access_time:
        m_equal_a += 1
    if file_name_dict[key].modify_time == file_name_dict[key].change_time:
        m_equal_c += 1
    if file_name_dict[key].access_time == file_name_dict[key].change_time:
        a_equal_c += 1

    if file_name_dict[key].modify_time < file_name_dict[key].access_time:
        m_lessthan_a += 1
    if file_name_dict[key].modify_time < file_name_dict[key].change_time:
        m_lessthan_c += 1

    if file_name_dict[key].access_time < file_name_dict[key].modify_time:
        a_lessthan_m += 1
    if file_name_dict[key].access_time < file_name_dict[key].change_time:
        a_lessthan_c += 1
    
    if file_name_dict[key].change_time < file_name_dict[key].access_time:
        c_lessthan_a += 1
    if file_name_dict[key].change_time < file_name_dict[key].modify_time:
        print("File with Change Time < Modify Time:", key)
        print("access_time =", file_name_dict[key].access_time)
        print("modify_time =", file_name_dict[key].modify_time)
        print("change_time =", file_name_dict[key].change_time)
        c_lessthan_m += 1

print("All Timestamps Equal:\t\t\t", all_equal)
print("Modify Timestamp = Access Timestamp:\t", m_equal_a)
print("Modify Timestamp = Change Timestamp:\t", m_equal_c)
print("Access Timestamp = Change Timestamp:\t", a_equal_c)

print("Modify Timestamp < Access Timestamp:\t", m_lessthan_a)
print("Modify Timestamp < Change Timestamp:\t", m_lessthan_c)

print("Access Timestamp < Modify Timestamp:\t", a_lessthan_m)
print("Access Timestamp < Change Timestamp:\t", a_lessthan_c)

print("Change Timestamp < Access Timestamp:\t", c_lessthan_a)
print("Change Timestamp < Modify Timestamp:\t", c_lessthan_m)

# for key in file_name_dict:
#     count = 0
#     print("File =", key)
#     print("==========================================")
#     print("access_time =", file_name_dict[key].access_time)
#     print("modify_time =", file_name_dict[key].modify_time)
#     print("change_time =", file_name_dict[key].change_time)
#     print("==========================================")
#     print()
  
