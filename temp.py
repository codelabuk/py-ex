acronym = input('What acronym do you want?\n')
definition = input('What is the definition?\n')
with open('acronym.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
