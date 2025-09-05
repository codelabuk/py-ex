
look_up = input("WHat software acronym would you like to look up ?\n")

with open('acronym.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print('The acronym does not exist')    