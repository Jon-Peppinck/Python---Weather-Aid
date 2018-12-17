# Weather Funds Priority - Jon Peppinck

import sys
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

#The read_weather_data function splits data from each line of weather.txt into its city name and average amount of rainfall
#If the file has any errors the program will terminate and prompt the user to check the contents of the file
#The accepted format for each line in the file is City,1.23 or City, 1.23 - where 1.23 represents any floating number
#Checkings if the average rainfall has two or more spaces allows the line in the file to have up to 1 space after the comma
#All of the city names are to be entered in as only alphabet characters
#All of the city names in weather.txt have no numbers, symbols, or spaces and this program stays consistant with that format
#Any Value Errors or Index Errors such as; town,hello, hello, or " " (blank line) will have an exception that terminates the program
#If a comma, ",", is not in a line or it is in a line more than once, the user will be prompted and the program will be terminated

def read_weather_data():
	with open("weather.txt") as file_opened:
		for line in file_opened:
			
			if "," not in line:
				sys.exit("Error reading data. \nPlease ensure each line of weather.txt \
contains a city name, followed by a comma,\nfollowed by an \
average rainfall amount(zero or one space after comma only) and that no city is repeated throughout the file")

			if line.count(",") >= 2:
				sys.exit("Error reading data. \nPlease ensure each line of weather.txt \
contains a city name, followed by a comma,\nfollowed by an \
average rainfall amount(zero or one space after comma only) and that no city is repeated throughout the file")
			
			split = line.rstrip("\n").split(",")
			yield split

			try:
				a = "  "
				if a in rain_Amount:
					sys.exit("Error reading data. \nPlease ensure each line of weather.txt \
contains a city name, followed by a comma,\nfollowed by an \
average rainfall amount(zero or one space after comma only) and that no city is repeated throughout the file")

				if not city_Name.isalpha():
        	                        sys.exit("Please ensure city name only contains letters from the alphabet. \
Numbers, symbols, spaces, and any other non-alphabetical characters terminate the program")

				else:
                        		pass

			except (ValueError, IndexError):
				sys.exit("Error reading data. \nPlease ensure each line of weather.txt \
contains a city name, followed by a comma,\nfollowed by an \
average rainfall amount(zero or one space after comma only) and that no city is repeated throughout the file")

#Takes the city and average rainfall for each line and puts each line into its own dictionary
#Each dictionary is added to an empty list to get a list of dictionaries from each line of weather.txt
#rain_Amount has strip applied to it because the space in City, 4.30 sorts before City2,1.23 when sorting


for i in read_weather_data():
	city_Name = i[0]
	rain_Amount = i[1]
	list1.append(list1)
	dict  = {"city":city_Name, "average_rainfall":rain_Amount.strip()}

	list2.append(dict)
	list3.append(city_Name)
	list4.append(rain_Amount.strip())


#The rain amount will be put into its own list, list4
#Each element in this list4 will try be converted into a float
#If it can be converted to a float it will be added to a new list, list5
#If list5 can be created, list4 rain amounts are a valid float entry
#Otherwise the program will terminate and the user will be notified 

for k in list4:
	try:
		check_if_Float = float(k)
		list5.append(check_if_Float)
		break
	except ValueError:
		sys.exit("Error reading data. \nPlease ensure each line of weather.txt \
contains a city name, followed by a comma,\nfollowed by an \
average rainfall amount(zero or one space after comma only) and that no city is repeated throughout the file")


#Checks to see if the city from each line in weather.txt only occurs once
#The user will be noted otherwise and the program will be terminated

list3.sort()
one_Town_Only = list(set(list3))
one_Town_Only.sort()
if list3 != one_Town_Only:
	sys.exit("Please ensure each city from the file is entered only once")

# the sort_weather_data function sorts the list of dictionaries by the average rainfall (least to most)

def sort_weather_data(adict): return adict["average_rainfall"]
sortedlist2 = (sorted(list2, key=lambda k: k["average_rainfall"]))

#Asks the user for the number of cities they can help with
#The user will be prompted to re-enter if the number entered is greater than the the amount of cities on the list
#If the number is entered correctly the sorted list (least to most) will be shortened to that number 
#If the user types in a non-integer such as a string, float, list, or symbol etc. they will be prompted to re-enter
#If the user enters a negative number the program will terminate

while True:
	try:
		n = input("To how many cities can you send aid?: ")
		n = int(n)

		if n < 0:
			sys.exit("Program Terminated: Invalid value. Please only enter a non-negative integer")

		if n > len(open("weather.txt").readlines()):
			print("Please enter a value that doesn't exceed the total number of cities listed in weather.txt")

		else:
			needlist = sortedlist2[0:n]

			break

	except (ValueError, TypeError, IndexError):
		print("Invalid value. Please enter a non-negative integer")

#The list of dictionaries will now only contain the number the user selects with rainfall (least to most)
#Prints the city names with the least rainfall from the list of dictionaries

for j in needlist:
	print(j["city"])
