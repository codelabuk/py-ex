
acronyms = {'LOL': 'Laughing out load',
            'IDK': "I dont know",
            'TBH': 'to be honest'}


try:
    definitions = acronyms['BTW']
    print('Definition of')
except:
    print('The key does not exist')
finally:
    print('The acronyms we have defined are:')
    for acronym in acronyms:
        print(acronym)
