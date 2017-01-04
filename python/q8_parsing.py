# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import string

def read_football():
	# read football.csv file into list of tuples
	football_clubs = []
	football_clubs_2 = []
	
	fin = open("football.csv")
	for line in fin:
		
		football_clubs.append(line.strip())
	for club in football_clubs:
		football_clubs_2.append(club.split(","))
	football_clubs_2.pop(0)
	for club in football_clubs_2:
		club.append(abs(int(club[5])-int(club[6]))) 	
	return football_clubs_2

print (read_football())


#incomplete