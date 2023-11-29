from regex_search_postcodes import search_and_save_instances
import re

# Specify the file path and regex pattern
file_path = r"C:\Users\thipphaphone.c\Desktop\postcode_data\postcode_list.txt"
regex_pattern = re.compile(r'(.*)\b(\d{5}\s*-\s*\d{5})\b(.*)')

# Call the function to search and save instances # group(0) is all the matched pattern
name_only = search_and_save_instances(file_path, regex_pattern,1) # group(1) is the name part
code_only = search_and_save_instances(file_path, regex_pattern,2) # group(2) is the code part

# Print the found instances
for i in name_only:
    print(i)

for j in code_only:
    print(j)




