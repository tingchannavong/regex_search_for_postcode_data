# regex_search_for_postcode_data
This project attempts to solve the pain point of extracting branch office information from a 100+ postcode word file.

The file regex_search_postcode.py have two functions that search for regex pattern in a text format or list.

The file divide_code_name.py executes the task with regex pattern below:
(r'(.*)\b(\d{5}\s*-\s*\d{5})\b(.*)')
This regex will return any branch office written in the following way: 'Branch Office Vientiane HQ 10501 - 10512'.
