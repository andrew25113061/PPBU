# file = open("text.txt", "r", encoding="utf-8")
# s = file.read()
# s = file.readline()
# print(s)
# s = file.readlines()
# print(s)
# file.close()

# for i  in open('text.txt', 'r', encoding='utf-8'):
#     print (i.rstrip())

with open('text.txt', 'r', encoding='utf-8') as file:
    ls = file.read().title().split()
ls.sort()
print(ls)

