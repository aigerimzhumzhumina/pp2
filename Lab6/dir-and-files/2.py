import os
path = r"C:\Users\Пользователь\Documents\pp2\Lab6\dir-and-files"
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))
