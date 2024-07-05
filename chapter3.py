#4-1 Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#	Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.

#Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

#favPizzas = []
#keepAsking = True

#numOfFavs = int(input("How many types of pizzas would you say are you're favorite?"))

#while keepAsking:
#	pizza = input("What are you're favorite pizzas?")
#	favPizzas.append(pizza.title())
#	numOfPizzas = len(favPizzas)

#	if numOfPizzas == numOfFavs:
#		keepAsking = False

#print("Here is a list of your favorite pizzas:\n")

#for pizza in favPizzas:
#	print(pizza)

#print("As you can see, I really like pizza!")

#4-2 Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#	Modify your program to print a statement about each animal, such as A dog would make a great pet.
#	Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

#animals = []

#keepAsking = True

#print("Can you think of at least three differet animals that have a common characteristic?")

#while keepAsking:
#	animal = input("Name the animal:")
#	animals.append(animal)
#	numOfAnimals = len(animals)
#	if numOfAnimals == 3:
#		keepAsking = False			

#for animal in animals:
#	print("A " + animal + " would make a great pet!")		

#print("The one thing they all have in common is they are both cuddly!")

#4-3 Counting to twenty: Use a for loop to print the numbers from 1 rto 20 inclusive
#for num in range (1, 21):
#	print(num)

#4-4 One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#for num in range(1, 1,000,000):
#	print(num)

#4-5 Summing a Million: Make a list of numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers. 

#numList = []

#for num in range(1, 1000000):
#	numList.append(num)	

#print(min(numList))
#print(max(numList))
#print(sum(numList))

#4-6 Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
#for num in range(0, 21, 3):
#	print(num)

#4-7 Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
#for num in range(1, 31):
#	print(num *3)

#4-8 Cubes: A number raised to the third power is called a cube. Make a list of the first 10 cubes and use a for loop to print out the value of each cube 
#for num in range(1, 11):
#	print(num**2)

#4-9 Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
#squares = [num**2 for num in range(1, 11)]
#print(squares)

#players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print(players)

#print(players[:3])
#print(players[1:4])
#print(players[:4])
#print(players[2:])

#for name in players[:3]:
#	print(name.title())

#Copying a List

#myFoods = ['pizza', 'falafel', 'carrot cake']
#friendsFoods = myFoods[:]

#print(myFoods)
#print(friendsFoods)

#myFoods.append('sushi')
#friendsFoods.append('fish & chips')

#print(myFoods)
#print(friendsFoods)

#4-10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following.

#	Print the message The first three items in the list are. Then use a slice to print the first three items from that programs list. 

#favFoods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
#for food in favFoods[:3]:
#	print('The first three items in the list are: ', food.title())
#	Print the message Three items from the middle of the list are. Then use a slice to print three items from the middle of the list. 

#for food in favFoods[1:3]:
#	print('The first three items in the list are: ', food.title())	

#	Print the message The last three items in the list are: Then use a slice to print the last three  items in the list. 
#for food in favFoods[1:]:
#	print('The last three items in the list are: ', food.title())

#4-11. My Pizzas, Your Pizzas: Start with your programs from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following:

pizzas = ['cheese', 'pepperoni', 'meat', 'margherita', 'hawaiian']

friends_pizza = pizzas[:]

#	Add a new pizza to the original list.
pizzas.append('bbq chicken')

#	Add a different pizza to the list friend_pizzas.
friends_pizza.append('buffalo pizza')

#	Prove that yoy have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

#for pizza in pizzas:
#	print('My favorite pizzas are: ', pizza.title())

#for pizza in friends_pizza:
#	print('My friends favorite pizzas are: ', pizza.title())

#4-12. More loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py and write two for loops to print each list of foods.

#for pizza in pizzas:
#	print('My favorite pizzas are: ', pizza.title())

#4-13 Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods and store them in a tuple.

foods = ('omlette', 'scramble eggs', 'bacon', 'sausage', 'french toast')

#print(foods)
#	Use a for loop to print each food the restaurant offers.
#for food in foods:
#	print(food.title())
#	Try to modify one of the items, and make sure that Python rejects the change. 

#foods[0] = 'beans'
#print(foods)

#	The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

for food in foods:
	print(food.title())

foods = ('beans', 'pancake', 'eggs over easy', 'bacon', 'sausage', 'french toast')
for food in foods:
	print('new items on the menu:', food.title())
