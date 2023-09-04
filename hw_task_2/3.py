list_1 = [2,3,4,'word_1',6,'word_2']
print(list(filter(lambda x: isinstance(x,str), list_1)))
