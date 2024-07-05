#Write a separate program to accomplish each of these exercises. Save each program with a filename that follows standard Python conventions, using lowercase letters and underscores, such as simple_message.py and simple_messages.py
	#2.1 - Simple Message: Assign a message to a variable, and thenprint that message
	#2.2 Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

#2.1 
#message = "Hello World!"
#print(message)

#2.2
#messages = "Hello World! Again"
#print(messages)

#messages = "Hello Python World"
#print(messages)

#Save each of the following exercises as a separate file, with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C

#2-3
#Personal Message: Use a variable to represent a person's name and print a message to that perosn. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

#firstName = "ivan"
#lastName = "ng"
#fullName = f"{firstName} {lastName}"
#greeting = "hello"
#automatedResponse = "would you like to learn some python today?"

#print(greeting.title(), fullName.title() + ',', automatedResponse)

#2-4 Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase and title case
#firstName = 'jessica'
#lastName = 'rafuse'
#fullName = f"{firstName} {lastName}"

#print(fullName.lower())
#print(fullName.upper())
#print(fullName.title())

#2-5 Famous quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following. including the quotation marks. 

#famousQuote = "'It's not what you don't know that gets you into trouble. It's what you know to be true that just aint so.'"
#print(famousQuote)

#2-6 Famous Quote 2: Repeat Exercise 2-5, but this time represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

#famous_person = "mark twain"
#famousQuote = "'It's not what you don't know that gets you into trouble. It's what you know to be true that just aint so.'"

#print(famousQuote,'-',famous_person.title())

#2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.Make sure you use each character combination. "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#name = " ivan "
#print('|' + name + '|','\n\t','|' + name.lstrip() + '|', '\n\t', '|' + name.rstrip() + '|', '\n\t', '|' + name.strip() + '|')

#2-8 File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do. 

#filename = 'python_notes.txt'
#print(filename)
#print(filename.removesuffix('.txt'))
#print(filename.removeprefix('python'))

#2-9 Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operatrions in print() calls to see the results. Your output sholuld be four lines, with the number 8 appearing once on each line. 

#print("----------")
#print(4 + 4)
#print("----------")
#print(10 - 2)
#print("----------")
#print(2 * 4)
#print("----------")
#print(16 / 2)

#2-10 Favorite Number: Use a variable to represent your favorite number. Then using that variable, create a message that reveals your favorite number. Print that message. 

#favNum = 1980
#statement = "my favorite number is:"
#print(statement.title(), favNum)

#2-11 Adding Comments: Choose two of the programs you've written and add at least one comment to each. If you don't have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does. 

#Ivan Ng	Jan 19/2024
#Assign Hello World to a variable and print out message using variable

#message = "hello world"
#print(message.title())

import this
