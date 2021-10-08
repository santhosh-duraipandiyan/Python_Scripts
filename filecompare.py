
# Importing difflib
import difflib
  
with open('urls.json') as file_1:
    new = file_1.readlines()
  
with open('urlsold.json') as file_2:
    old = file_2.readlines()
  
# Find and print the diff:
for line in difflib.unified_diff(
        new, old, fromfile='urls.json', 
        tofile='urlsold.json', lineterm=''):
    print(line)