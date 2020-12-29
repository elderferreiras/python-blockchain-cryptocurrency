name = input('Name: ')
age = input('Age: ')


def print_user():
    print(name + " " + age)


def print_data(value_1, value_2):
    print(value_1 + " " + value_2)


def get_number_of_decades(age):
    return int(age)//10


print_user()
print_data('Hey', name)
n_decades = get_number_of_decades(age)
print('You\'ve lived %s decades' % n_decades)


