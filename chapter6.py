#alien = {'color':'green', 'points':5}

#print(alien['color'])
#print(alien['points'])

#alien['x_position'] = 0
#alien['y_position'] = 25

#print(alien)

#alien_0 = {}

#alien_0['color'] = 'green'
#alien_0['points'] = 5
#alien_0['x_coordinate'] = 0
#alien_0['y_coordinate'] = 25

#print(alien_0)
#print(f"The alien's color is {alien_0['color']}")

#alien_0['color'] = 'yellow'
#print(f"The alien's color is {alien_0['color']}")

#alien_0['speed'] = 'medium'

#if alien_0['speed'] == 'slow':
#	x_increment = 1
#elif alien_0['speed'] == 'medium':
#	x_increment = 2
#else:
#	x_increment = 3

#alien_0['x_coordinate'] = alien_0['x_coordinate'] + x_increment
#print(f"The alien's speed is {alien_0['x_coordinate']}")

#print(alien_0)
#del alien_0['color']

#del alien_0['color']
#print(alien_0['color'])

#print(alien_0.get('color', 'Alien color has not been assigned'))

#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age and city. Print each piece of information stored in your dictionary.

fiance = {
	'firstName': 'jessica', 
	'lastName': 'Rafuse', 
	'age': 36, 
	'location': 'Chester Basin'
}

for item in fiance:
	if fiance['age']:
		fiance['age'] = str(fiance['age'])
#	print(item.title() + ": " +  fiance[item])

#6-2. Favorite Numbers: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favNums = {}

favNums['jessica'] = 1
favNums['ivan'] = 2
favNums['louie'] = 3
favNums['joanne'] = 4
favNums['brian'] = 5

#print(favNums)

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
#	Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

#	*** Term/Definitions***

#variable - a store of value
#syntax - a set of rules that define what the various combinations of symbols mean
#datastructure - a specific way of organizing data
#array - a data structure consisting of a collection of elemtns (values or variables)
#control structures - enable a programmer to determine the order in which program statements are executed

glossary = {}
numOfTerms = input("How many terms do you want to store? ")
numOfTerms = int(numOfTerms)

for i in range(numOfTerms):
	term = input("What term do you want to enter? ")
	definition = input("Enter the definition for the term: ")
	dict = {term:definition}
	glossary.update(dict)

print(glossary)	

#	Print each word and its meaning as neatly formatted output. Your might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline charactre (\n) to insert a blank line between each word-meaning pair in your output.


for i in glossary:
#	print(i + ": " +  glossary[definition])
	print(i.title() + ": " + glossary[i])
