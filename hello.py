print("Hello World")

my_name = input("What's ur name?\n")
print(my_name)

computer_choie = 'scissors'
user_choice = input('Do you want rock or scissors')

if computer_choie == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choie == 'scissors':
    print('WIN')
else:
    print('Lost')
