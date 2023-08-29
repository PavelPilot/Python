def make_initials(list):
    char_length = len(list)
    initial = list[0:1]
    for i in range(char_length):
        if list[i] == '':
            initial_location = list[i + 1]
            initial += '.' + initial_location
            return initial.upper()

list = input("Введите фразу: ")

initials = make_initials(list)

print(initials)