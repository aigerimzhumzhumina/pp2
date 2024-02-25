import re

def split_at_uppercase(string):
    split_string = re.findall('[A-Z][^A-Z]*', string)
    return split_string

test_string = "SplitThisStringAtUppercaseLetters"
result = split_at_uppercase(test_string)
print("Original string:", test_string)
print("Split string at uppercase letters:", result)
