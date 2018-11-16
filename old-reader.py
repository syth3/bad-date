import csv
import os
import sys

class MacEntry:
    def __init__(self, date, size, type, mode, uid, gid, meta, file_name):
        self.date = date
        self.size = size
        self.type = type
        self.mode = mode
        self.uid = uid
        self.gid = gid
        self.meta = meta
        self.file_name = file_name


file_name = os.path.abspath(sys.argv[1])

with open(file_name) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # csv.reader(csv_file, delimiter=',')
    line_count = 0
    file_name_dict = {}
    for key in csv_reader:
        file_name = key["File Name"]
        mac_object = MacEntry(key["Date"], key["Size"], key["Type"], key["Mode"], key["UID"], key["GID"], key["Meta"], key["File Name"])
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
        print("Size:", obj.size)
        print("Type:", obj.type)
        print("Mode:", obj.mode)
        print("UID:", obj.uid)
        print("GID:", obj.gid)
        print("Meta:", obj.meta)
        print("File Name:", obj.file_name)
        if count == len(obj_list):
            pass
        else:
            print()
    print("==========================================")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print("Date:", row["Date"])
    #         print("Size:", row["Size"])
    #         print("Type:", row[2])
    #         print("Mode:", row[3])
    #         print("UID:", row[4])
    #         print("GID:", row[5])
    #         print("Meta:", row[6])
    #         print("File Name:", row[7])
    #         line_count += 1
    #     print()
    # print(f'Processed {line_count} lines.')