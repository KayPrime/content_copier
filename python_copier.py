#! /usr/bin/python3

file_open = open("./input.txt", "r")
content = file_open.read()
file_open.close()

new_file = open("output.txt", "a+")
new_file.write(content)
new_file.close()

