
# str_1 = 'Python', 'php', 'go', 'C', 'Hello', 'world'
# print(str_1)
# print(list(filter(lambda x: x not in stop, str_1)))

str_1 = 'Python php go C Hello world'
stop = ['Python', 'php', 'go', 'C']
str_list = str_1.split(' ')

lst = list(filter(lambda x: x not in stop, str_list))
print(lst)
print(' '.join(lst))


