import re

def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'  
    sequences = re.findall(pattern, string)
    return sequences

test_string = "This_is_a_test_string_with_some_sequences_like_this_and_this_one"
result = find_sequences(test_string)
print("Sequences found:", result)
