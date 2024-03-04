color = ['Red', 'Green', 'White', 'Black', 'Pink']
with open(r'C:\Users\Пользователь\Documents\pp2\Lab6\dir-and-files\abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open(r'C:\Users\Пользователь\Documents\pp2\Lab6\dir-and-files\abc.txt')
print(content.read())
