places = ['ottawa', 'toronto', 'vancouver', 'italy', 'thailand', 'canada', 'china', 'england', 'france']
foods = ('hotdog', 'cheeseburger', 'corndog', 'popcorn', 'pizza')
person = {'first_name': 'zoe', 'last_name': 'walton', 'age': 20, 'city': 'ottawa'}
thesaurus = {'cool': 'popular', 'sick': 'awesome, under the weather', 'noice': 'alright', 'bird': 'girl'}
numbers = []

print(thesaurus, '\n')

print(f"\nCool could also be written as: {thesaurus['cool']}")
print(f"Sick could also be written as: {thesaurus['sick']}")
print(f"Noice could also be written as: {thesaurus['noice']}")
print(f"Bird could also be written as: {thesaurus['bird']}\n")

del thesaurus['noice']
print(thesaurus)