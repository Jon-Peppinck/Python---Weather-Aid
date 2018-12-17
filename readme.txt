-----
About
-----
weather.py was created to help the King of Codetopia determine which cities are in most need of aid.
Due to limited funds, the cities with the least average rainfall in the region will be supported first.

weather.py reads in data from weather.txt - if and only if the data from the file is entered correctly
The program will ask the user (the King), to type in an integer of how many cities the user can send financial aid to
If the user does not enter a valid integer, they will be prompted to try again. Assuming weather.py receives valid input,
the program will display the name of the number of cities from least to most average rain so the King can help those in most need

For more details about weather.txt having the correct file format or any other problems, please refer to
the Troubleshooting section below

-------------
Configuration
-------------
Recommended Operating System: Linux OS

Software Required: Python3 (3.6.3 + Recommended)

------------
Installation
------------
Download weather.py and weather.txt files from Github
(or alternate link)

----------------------
Operating Instructions
----------------------
1. Open weather.py (When in Linux terminal > python3 weather.py)

2. The program ensures data from weather.txt is in the correct format. If it is the program will proceed.
   If not the user will be prompted and the program will be terminated (see Troubleshooting)

3. The user will be asked the number of cities, n, they are able to help. Only positive integers not exceeding
   the number of cities from weather.txt will be a valid input. Invalid input will result in the user either being required
   to enter a valid input or the program being terminated

4. The program will output the name of n cities from those with the least average rainfall to the most. This allows the King
   to easily see which cities are in most need of financial aid

-------------
File manifest
-------------
Includes readme.txt, weather.py, and weather.txt

-----------------------------------
Copyright and Licensing information
-----------------------------------
weather.py is public domain software - free and open source

---------------
Troubleshooting
---------------
If weather.txt has any errors in its formatting, the program will not run. Please check the following:

[1]Ensure that each line in the file is in the form City,1.23 OR City, 1.23 - where 1.23 represents any floating number
[2]Check that there is no extra spaces at the end of each line, end of file, or anywhere in the file
[3]Check the City name does not contain any numbers, symbols, or spaces. Only alphabet characters will be accepted
[4]Ensure that there is only one comma "," per line
[5]Ensure the average amount of rainfall is a valid float e.g 1.23 and not "1. 23", "hello", [1.23], "" etc.
[6]Check weather.txt to make sure that a city name is not repeated

If weather.txt does not contain any errors, and the program is still not running. Please ensure that
the number of cities to help, n, is a positive integer. Positive integers include: 1, 2, 3, 4,...
Examples of invalid entries may be but not limited to: 1.23, [2], hello, "", -1
If a positive integer is not accepted, ensure that it does not exceed the number of cities from weather.txt

File Permissions - If you are denied access to reading, writing, or executing
weather.py - from the linux terminal you can type chmod a+r weather.py,
chmod a+w weather.py, or chmod a+x weather.py

Please ensure you are in the correct directory to access weather.txt
-------
Queries
-------
For any queries please contact Jon Peppinck at mrjonpeppinck@gmail.com
