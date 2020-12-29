names = ['Elder', 'Zach', 'Rosalia', 'Juliana']


def print_names():
    """ Print names """
    for name in names:
        name_length = len(name)

        print(name + " length: %i" % name_length)

        if name_length > 5 and ('N' in name or 'n' in name):
            print(name + " length is bigger than 5")

    while len(names) > 0:
        names.pop()

print_names()
print(names)