import re

def replace_characters(string):
    pattern = r'[ ,.]'  
    replaced_string = re.sub(pattern, ':', string)
    return replaced_string

test_string = "This is a test, with some. spaces and commas."
result = replace_characters(test_string)
print("Original string:", test_string)
print("Modified string:", result)
