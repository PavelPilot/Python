list_1 = [2,7,9,11]
list_2 = [2,7,9,11,12,15,14,'word_1']
#res = list_1.intersection(list_2)

print(list(filter(lambda x: x in list_2, list_1)))
#print(res)
