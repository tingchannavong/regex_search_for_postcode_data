import re

def search_and_save_instances(file_path, pattern, group=None):
     # Set the default pattern if none is provided
    if group is None:
        group = 0

    # Initialize an empty list to store found instances
    found_instances = []

    # Open the file in read mode
    with open(file_path,'r', encoding='utf-8') as file:
        # Read the content of the file
        file_content = file.read()

        # Search for the pattern in the file content
        matches = re.finditer(pattern, file_content)

        # Iterate over the matches and save each instance in the list
        for match in matches:
            found_instances.append(match.group(group))

    return found_instances

def find_instances_in_list(string_list, pattern, group):
    # Initialize an empty list to store found instances
    found_instances = []

    # Iterate over each string in the list
    for text in string_list:
        # Search for the pattern in the current string
        match = re.search(pattern, text)

        # If a match is found, append it to the list
        if match:
            found_instances.append(match.group(group))

    return found_instances







