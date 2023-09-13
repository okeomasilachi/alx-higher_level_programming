#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import json

filemame = "file_1"
data = []
save_to_json_file(data, filemame)

data_bis = None
with open(filemame, 'r') as file:
    data_bis = json.load(file)
print(data_bis == data)