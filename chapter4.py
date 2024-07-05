#cars = ['ford', 'chevrolet', 'toyota', 'honda', 'bmw', 'mercedes benz', 'kia', 'hyundai']

#for car in cars:
#	if car == 'bmw':
#		print(car.upper())
#	else:
#		print(car.title())

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.

#car = 'ford'

#if car == 'toyota':
#	print('Is your car a ford? I predict true.')

#3-2 More Conditional Tests: You don't have to limit the number of test you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

#	Tests for equality and inequality with strings

#favCar = 'ford bronco'
#yourFav = 'mini cooper'
#yourSecFav = 'ford bronco'

#if favCar == yourFav:
#	print(favCar.title(), ' is our favorite vehicle')
#else:
#	print('We like different vehicles.')

#if favCar == yourSecFav:
#	print('Looks like we have similar taste in cars')
#else:
#	print('Our tastes in vehicles are very different.')

#	Tests using the lower() method

#name = 'ivan'
#name2 = 'Ivan'

#if name == name2:
#	print("It's a match!")
#else:
#	print("The names are not a match")

#name = name.lower()
#name2 = name2.lower()

#if name == name2:
#	print("It's a match!")
#else:
#	print("The names are not a match")

#	Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.

#num1 = 34
#num2 = 43

#if num1 < num2:
#	print('Num1 is less than Num2')
#else:
#	print('Num1 is greater than Num2')

#num3 = 32
#num4 = 32

#if num3 == num4:
#	print('Num3 and Num4 are equal value.')
#else:
#	print('Num3 and Num4 are not equal value.')

#	Tests using the and keyword AND the OR keyword

#num5 = 12
#num6 = 14

#if (num6 >= num5) and (num5 % 2 == 0):
#	print("num6 meets all requirements in the condition")
#else:
#	print("The conditions are not met.")

#num7 = 21
#num8 = 19

#if (num8 > num7) or (num7 > 18):
#	print("Congrats! one of the conditions have been met!")
#else:
#	print("Sorry neither conditions have been met.")

#	Test whether an item is in a list


# **** code snippet completed with 'flag marker' ****
#cars = ['toyota', 'bmw', 'hyundai', 'ford', 'honda', 'kia', 'chevy', 'mercedes benz', 'audi', 'volkswagen']

#myCar = 'ford'
#myCar = 'jaguar'

#version1 ****Most Efficient****

#verified = False
#for car in cars:
#	if car == myCar:
#		verified = True
#		print("We found a match!")
#print(bool(verified))
#if verified != True:
#	print("Not in our inventory.")

# ***************************************************
#version2
#match = False
#for car in cars:
#	if car == myCar:
#		match = True 
		
#if match:
#	print("We have a match!")
#else:
#	print("Not in our inventory")


#	Test whether an item is not in a list
#cars = ['toyota', 'bmw', 'hyundai', 'ford', 'honda', 'kia', 'chevy', 'mercedes benz', 'audi', 'volkswagen']

#myCar = 'ford'
#myCar = 'jaguar'
#for car in cars:
#	if car != myCar:
#		notAvailable = True

#if notAvailable:
#	print(myCar.title(), 'is not in the list')
#else:
#	print(myCar.title(), 'is on the list!')

#5-3. Alien Colors #1: Imagine an alien was just shot down in agame. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
alien_colors = ['green', 'yellow', 'red']

#alien_color = input("What color is your alien?:") 

#	Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.

#for color in alien_colors:
#	if color == alien_color:
#		print("You just earned 5 points")
#	Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

#	***Promppt player to enter color of alien_color***

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

#alien_color = 'red'

#if alien_color == 'green':
#	print("5 points")
#else:
#	print("No points won")

#	If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.

#alien_color = input("What color is the alien? Red, Green or Yellow?")

#for color in alien_color:
#	if alien_color == 'red':
#		alien_color = 'red'
#	elif alien_color == 'yellow':
#		alien_color == 'yellow'
#	else:
#		alien_color == 'green'

#if alien_color == 'green':
#	print("5 points for shooting the alien!")

#	If the alien's color isn't green, print a statement that the player just earned 10 points.

#if alien_color != 'green':
#	print("5 points for shooting the alien!")

#	Write one version of this program that runs the if block and another that runs the else block.

#if alien_color == 'green':
#	print("5 points for shooting the alien!")
#else:
#	print("5 points for shooting the other aliens!")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

#alien_colors = ['green', 'yellow', 'red']

#	If the alien is green, print a message that the player earned 5 points.
#	If the alien is yellow, print a message that the player earned 10 points.
#	If the alien is red, print a message that the player earned 15 points.
#	Write thee versions of this program, makingsure each message is printed for the appropriate color alien.

#your_alien = input("What color alien did you shoot down?\n")

#if your_alien == alien_colors[0]:
#	print("congrats your player earned 5 points for shooting the", alien_colors[0], "alien")
#elif your_alien == alien_colors[1]:
#	print("Congrats your player earned 10 points for shooting the", alien_colors[1], "alien")
#elif if your_alien == alien_colors[2]:
#	print("Congrats your player earned 15 points for shooting the", alien_colors[2], "alien")
#else:
#	print("No other colored aliens exist")

#5-6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:

#age = int(input("How old are you?"))

#	****separate age by toddler, youth, teen, adult, senior****

#	If the person is less than 2 years old, print a message that the person is a baby.

#if age < 2:
#	print("You are a baby")
#	If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#elif age > 2 and age < 4:
#	print("You are a toddler")
#	If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#elif age >= 4 and age < 13:
#	print("You are a kid")
#	If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#elif age >= 13 and age < 20:
#	print("You are a teenager")
#	If the person is at least 20 years old but less than 65, print a message that the person is an adult. 
#elif age >= 20 and age < 65:
#	print("You are an adult")
#	If the person is age 65 or older, print a message that the person is an elder.
#elif age >= 65:
#	print("You are an elder")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list. 

fav_fruits = ['dragon fruit', 'kiwi', 'watermelon']
#	Make a list of your three favorite fruits and call it favorite_fruits.
#	Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement such as You really like bananas!

#for fruit in fav_fruits:
#	if fruit == 'watermelon':
#		print("You really like watermelons!")

#	if fruit == 'pineapple':
#		pass

#	if fruit == 'kiwi':
#		print("You really like kiwis")

#	if fruit == 'dragon fruit':
#		print("You really like dragon fruit")

#pizzaToppings = []

#if pizzaToppings:
#	for topping in pizzaToppings:
#		print("Adding", topping)
#	print("Your pizza is finished.")
#else:
#	print("Are you sure you want a plain pizza?")

#pizzaToppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

#requestedToppings = ['mushrooms', 'french fries', 'extra cheese']

#for requestedToppings in requestedToppings:
#	if requestedToppings in pizzaToppings:
#		print("Adding", requestedToppings)
#	else:
#		print("Sorry, we don't have", requestedToppings)

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#	If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#	Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

#username = ['ivan', 'jess', 'louie', 'admin', 'joanne']

#for name in username:
#	if name == "admin":
#		print('Hello admin, would you like to see a status report?')
#	else:
#		print("Hello", name.title() + ',', 'thank you for logging in again.')
	
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#	If the list is empty, print the message 'We need to find some users!'
#	Remove all of the usernames from your list, and make sure the correct message is printed.

#username = []

#if username:
#	for user in username:
#		if name == 'admin':
#			print('Hello admin, would you like to see a status report?')
#		else:
#			print('Hello', name.title() + ',', 'thank you for loggin in again.')
#else:
#	print('We need to find some users!')

#5-10. Check Usrnames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#	Make a list of five or more usernames called current_users.
#	Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#	Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a usernamehas not been used, print a message saying that the username is available.
#	Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

#currentUsers = ['joseph', 'ann', 'louie', 'dale', 'brian']
#newUsers = ['ivAn', 'jess', 'louie', 'joanne', 'brian']

#for newUser in newUsers:
#	newUser = newUser.lower()
#	if  newUser in currentUsers:
#		print('Sorry the username;', newUser, 'already exists, please enter another name.')
#	else:
#		print('The username:', newUser, 'is available.')

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2 and 3. 
#	Store the numbers 1 through 9 in a list.
#	Loop through the list.
#	Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate llne.	

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#for number in numbers:
#	number = str(number)
#	if number == '1':
#		print(number + "st")
#	elif number == '2':
#		print(number + "nd")
#	elif number == '3':
#		print(number + "rd")
#	else:
#		print(number + "th")

#5-12. Styling if Statements: Review the programs you wrote in this chapter, and make sure you styled your conditional tests appropriately.

#	**** All code written is to PEP8 standard ****

#5-13. Your Ideas: At this point, you're a more capable programmer than you were when you started this book. Now that you have a better sense of how real world situations are modeled in programs, you might bethinking of some problems you could solve with your own programs. Record any new ideas you have about problems you might want to solve as your programming skills continue to improve. Consider games you might want to write, datasets you might want to explore, and web appllications you'd like to create.


