import os


count = 0
lines = 0
cwd = os.getcwd()
for root, dirs, files in os.walk(cwd):
    for file_name in files:
        print(file_name)
        fd = open(os.path.join(root, file_name), 'r')
        lines = lines + len(fd.readlines())
        fd.close()
        count+=1
print("Total number of files : %d"%count)
print("Total number of lines : %d"%lines)
