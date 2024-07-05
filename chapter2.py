#3-1 Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time. 

#names = ["toni johnson", "aidan davies", "tony dai"]
#print(names[0].title())
#print(names[1].title())
#print(names[2].title())

#3-2 Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name. 

#names = ["toni johnson", "aidan davies", "tony dai"]
#print(f"This is my coach and friend {names[0].title()}")
#print(f"This is my coach and friend {names[1].title()}")
#print(f"This is my coach and friend {names[2].title()}")

#3-3 Your own list. Think of your favorite mode of transportation, such as a motorcycle or a car and make a list that shares several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle.

#transportation = ["honda cb motorcycle", "ford bronco", "1967 chevelle"]
#message = "I would like to own a"
#print(message, f"{transportation[0].title()}")
#print(message, f"{transportation[1].title()}") 
#print(message, f"{transportation[2].title()}")

#3-4 Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

#dinnerInvites = ["Tom", "Dick", "Harry"]
#greeting = "Hello"
#inviteMessage = "I'd like to invite you over for dinner."
#print(greeting.title(), f"{dinnerInvites[0].title()}" + ",", inviteMessage)
#print(greeting.title(), f"{dinnerInvites[1].title()}" + ",", inviteMessage)
#print(greeting.title(), f"{dinnerInvites[2].title()}" + ",", inviteMessage)

#3-5 Changing guest list: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitiations. You'll have to think ofsomeone else to invite. 

#	Start your program from exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it.
#	Modify your list, replacing the name of your guest who can't make it and the name of the new person you are inviting.
#	Print a second set of invitiation messages, one for each person who is still in your list. 

#dinnerInvites = ["tom", "dick", "harry"]
#notAttending = dinnerInvites.pop()
#print(notAttending)
#print(dinnerInvites)
#dinnerInvites.append("jessica")
#print(dinnerInvites)
#invite1 = dinnerInvites[0].title()
#invite2 = dinnerInvites[1].title()
#invite3 = dinnerInvites[2].title()
#dinnerInviteMessage = "you are still on the invite list."
#print(invite1, dinnerInviteMessage)
#print(invite2, dinnerInviteMessage)
#print(invite3, dinnerInviteMessage)


#3-6 More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#	Start your program from exercise 3.4 or 3.5. Add a print() call to the end of your program. informing people you found a bigger table. 
#	Use insert() to add one new guest to the beginning of your list. 
#	Use insert() to add one new guest to the middle of your list. 
#	Use append() to add one new guest to the end of your list. 
#	Print a new set of invitation messages, one for each person in your list. 

#dinnerInvites = dinnerInvites
#dinnerInvites.insert(0, "louie")
#dinnerInvites.insert(2, "cara")
#dinnerInvites.append("dale")
#print(dinnerInvites)
#newInvite4 = dinnerInvites[3].title()
#newInvite5 = dinnerInvites[4].title()
#newInvite6 = dinnerInvites[5].title()

#print(invite1, dinnerInviteMessage)
#print(invite2, dinnerInviteMessage)
#print(invite3, dinnerInviteMessage)
#print(newInvite4, dinnerInviteMessage)
#print(newInvite5, dinnerInviteMessage)
#print(newInvite6, dinnerInviteMessage)

#3-7: Shrinking guest list: You just found out that your new dinner table won't arrive on time for the dinner and you now only have space for only 2 guests. 
#	Start with your program from exercise 3-6. Add a new line that prints a message saying that you can only invite 2 people for dinner.
#	Use pop() to remobve guests from your list one at a time until only 2 names remain in your list. Each time you pop a name from your list, print a message to that person saying your are sorry you can't invite them to dinner.
#	Print a message to each of the people still on your list, letting them know they're still invitited.
#	Use del to remove the last 2 names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

#print("Sorry guys, the dinner table did not arrive in time and dinner will be downsized to just 2 guest.")
#notAttending = dinnerInvites.pop()
#del dinnerInvites[1]
#del dinnerInvites[1]
#del dinnerInvites[1]
#print(dinnerInvites)

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)

#Now using sorted()
#sorted(cars)
#print(cars)
#print(sorted(cars))
#print(sorted(cars, reverse=True))

#3.8 Seeing the World: Think of at least five places in the world you'd like to visit.
	#Store the locations in a list. Make sure the list is not in alphabetical order
	#Print your list in its original order. Don't worry about print the list neatly: just print it as a raw Pythonlist.
	#Use sorted() to print your list in alphabetical order without modifying the actual list.
	#Show that your list is still in its original order by print it. 
	#Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. 
	#Show that your list is still in its original order by printing it again.
	#Use reverse() to change the order of your list. Print the list to show that its order has changed.
	#Use reverse() to hange the order of your list again. Print the list to show it's back to its original order.
	#Use sort() to change yourlist so it's stored in alphabetial order. Print the list to show that its order has been changed.
	#Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed. 

#places = []
#ask = True
#stop = input('How many times do you want the question to be repeated?:')
#while ask:
#	newDestination = input('Where do you want to go next?')
#	places.append(newDestination)
#	lenOfList = len(places)
#	stop = int(stop)
#	if lenOfList == stop:
#		ask = False
#print(places)
#print(sorted(places))
#print(places)

#places.reverse()
#print(places)

#places.sort()
#print(places)

#places.reverse()
#print(places)

#3-9 Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41-42). use len() to print a message indicating the number of people you're inviting to dinner.

#invitees = []
#keepGoing = True

#numInvitees = input("How many people are coming to dinner?")

#while keepGoing:
#	name = input("Who are you inviting?")	
#	invitees.append(name)
#	numInvitees = int(numInvitees)
#	attendees = len(invitees)
#	if attendees == numInvitees:
#		print("You invited " + str(len(invitees)) + " guests.")
#		keepGoing = False

#3-10 Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

#myList = []

#keepGoing = True

#listLen = input("How many items do you want to add to your list?")
#listLen = int(listLen)
#while keepGoing:
#	appendListItem = input("What or whoe would you like to add to your list?")
#	myList.append(appendListItem)
#	myListLength = len(myList)
#	if myListLength == listLen:
#		myList.sort()
#		print(myList)
#		keepGoing = False

#3-11 Intentional Error: If you haven't received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

motorcycles = ['Honda CB', 'Norton Commando', 'Harley Davidson']

print(motorcycles[-1])
