import csv
<<<<<<< HEAD
from pprint import pprint

with open('users.csv', 'r', encoding='utf-8') as file:
    csv_dict = csv.DictReader(file)
    pprint(list(csv_dict))

with open('users.csv', 'r') as file:
    csv_list = list(csv.reader(file))
    print(csv_list)
=======

# with open('users.csv', 'r', encoding='utf-8') as file:
#     # content = file.read()
#     # print(content)
#     csv_reader = csv.reader(file)
#     # print(csv_reader)
#     for row in csv_reader:
#         print(row)

with open('users.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)

    
>>>>>>> 5a74b50cce359d43c1cd71d05f353345db0f7040
