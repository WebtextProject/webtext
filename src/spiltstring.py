#!/usr/bin/python3

string_to_spilt = input("Enter a string: ")
size_of_chunk = int(input("Enter size: "))

message_array = []

for i in range(0, len(string_to_spilt), size_of_chunk):
    temp = ''
    for j in range(0, size_of_chunk):
        if i + j < len(string_to_spilt):
            temp += string_to_spilt[i + j]
        
    message_array.append(temp)
    
print(message_array)
    
