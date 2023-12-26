file = open('text.txt', mode='r')
data = file.readlines()
print(data)
file.close()

#with

with open('text.txt', mode='r') as file:
    data = file.readlines()
    print(data)

# write
with open('new_file.txt', 'w') as filew:
    filew.write("Hello new file\n")
    filew.writelines(["line next\n", "line ++\n"])

# append
try:
    with open('new_fildsae.txt', 'a') as filew:
        filew.write("Hello new file\n")
        filew.writelines(["line next\n", "line ++\n"])
except Exception as e:
    print(e)

# read
try:
    with open('new_fildsae.txt', 'r') as filer:
        print("READ 3")
        print(filer.read(3))
        print("READ")
        print(filer.readline())
        print("the rest")
        print(filer.readlines())
except Exception as e:
    print(e)