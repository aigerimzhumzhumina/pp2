import re

def match_pattern(string):
    pattern = r'a*b*'  
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ["", "a", "ab", "abb", "aab", "abbb", "ac", "abc", "abbcc"]
for string in test_strings:
    if match_pattern(string):
        print(f"Match found: '{string}'")
    else:
        print(f"No match found: '{string}'")
