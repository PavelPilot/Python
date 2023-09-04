list_1 = [2,3,4,5,6,7]
# def function(number):
#     return list_1[0]
#print(function(list_1))
#number = 2
lst = list(filter(lambda x: x % list_1[0] == 0, list_1))
print(lst)
# function(2)
