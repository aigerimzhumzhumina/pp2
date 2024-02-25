import re

def insert_spaces(string):
    modified_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return modified_string

test_string = "ThisIsAStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(test_string)
print("Original string:", test_string)
print("Modified string:", result)
