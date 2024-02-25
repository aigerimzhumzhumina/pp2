import re

def match_pattern(string):
    pattern = r'^a.*b$'  
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ["ab", "acb", "azb", "a123b", "abab", "axby", "abc", "a", "b"]
for string in test_strings:
    if match_pattern(string):
        print(f"Match found: '{string}'")
    else:
        print(f"No match found: '{string}'")
