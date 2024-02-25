import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'  
    sequences = re.findall(pattern, string)
    return sequences

test_string = "This is A Test String With Some Sequences Like This One And Another One Here"
result = find_sequences(test_string)
print("Sequences found:", result)
