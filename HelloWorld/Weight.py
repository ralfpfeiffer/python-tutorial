
#Weight converter
weight = int(input('Weight? '))
unit = input('(L)bs or (K)g ? ')
if unit.upper() == 'L':
    converted_weight = weight *0.45
    print(f"You are {converted_weight} Kilograms")
else:
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} Pounds")


i = 1
while i<=5:
    print(i*'*')
    i+=1
print('Done')

#Guessing Game

secret_num = 9
i=0

while i<3:
    guess_num = int(input('Guess:'))
    i+=1
    if guess_num == secret_num:
        print('You Won!')
        break
else:
    print('You Lose!')
