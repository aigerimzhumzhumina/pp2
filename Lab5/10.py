def camel_to_snake(camel_case_string):
    snake_case_string = camel_case_string[0].lower()  
    for char in camel_case_string[1:]:
        if char.isupper():
            snake_case_string += '_' + char.lower()  
        else:
            snake_case_string += char  
    return snake_case_string

camel_case_string = "camelCaseStringExample"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case string:", camel_case_string)
print("Snake case string:", snake_case_string)
