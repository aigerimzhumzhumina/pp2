import os
print("Test a path exists or not:")
path = r"C:\Users\Пользователь\Documents\pp2\Lab6\dir-and-files\1.py"
print(os.path.exists(path))
path = r'C:\Users\Пользователь\Documents\pp2\Lab6\dir-and-files\p.py'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
