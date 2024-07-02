glossary = {}
numOfTerms = input("How many terms do you want to store? ")
numOfTerms = int(numOfTerms)

for i in range (numOfTerms):
	term = input("Enter term: ")
	definition = input("Enter term definition: ")
	dict = {term: definition}
	glossary.update(dict)

print(glossary)

for i in glossary:
	print(i.title() + ": " + glossary[i])
