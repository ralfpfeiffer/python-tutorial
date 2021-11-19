gameon = True
is_started=False

while gameon:
    command = input("> ").lower()

    if command=='start':

        if not is_started:
            is_started=True
            print('Car Started!')
        else:
            print('Error: Car is Already Started...')

    elif command=='stop':
        if is_started:
            is_started=False
            print('Car Stopped!')
        else:
            print('Error: Car Already Stopped...')
    elif command == 'help':
        print('''
help: (this text)
start: starts car
stop: stops car
quit: Quit Game
        ''')
    elif command=='quit':
        break
    else:
        print('I do not understand...')

print('Game Over.')


