import json

exit = False

while not exit:
    print('1 - Add name')
    print('2 - Print')
    print('3 - Exit')

    option = input('option: ')
    if option == '1':
        user_input = input('name: ')
        with open('user_input.txt', mode='w') as f:
            f.write(user_input)
            f.write('\n')
    elif option == '2':
        with open('user_input.txt', mode='r') as f:
            print(f.readlines())
    else:
        break