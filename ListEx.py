acronyms = ['LOL1', 'DEL','lol5', 'lodkf', 'fkfo']
acronyms.append('LOL')
acronyms.remove('DEL')
del acronyms[4]
word = 'BFN'
if word  in acronyms:
    print(' exist')

for acr in acronyms:
    print(acr)

exp = [10, 100, 20, 15.5]
sum = 0
for x in exp:
    sum += x

print('You specnt Rs', sum, sep='')

for i in range(1,7, 2):
    print(i)