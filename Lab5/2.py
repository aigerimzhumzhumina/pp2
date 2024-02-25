import re

def match_pattern(string):
    pattern = r'ab{2,3}'  
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

test_strings = ["ab", "abb", "abbb", "a", "b", "ac", "abc", "abbc", "abbbc"]
for string in test_strings:
    if match_pattern(string):
        print(f"Match found: '{string}'")
    else:
        print(f"No match found: '{string}'")
