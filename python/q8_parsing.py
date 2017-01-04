# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

with open("football.csv") as fb_file:
	# Reads tuples(Team and goal difference (goal_diff)) into list, sorts it according to goal_diff

	football_clubs = []
	fb_reader = csv.DictReader(fb_file)
	for row in fb_reader:
		football_clubs.append( (row["Team"], abs(int(row["Goals"]) - int(row["Goals Allowed"]))) )
	football_clubs_sorted = sorted(football_clubs, key= lambda goal_diff: goal_diff[1])[0][0]
	print(football_clubs_sorted + "is the club with the smallest absolute difference in goals.")



'''
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
'''

#incomplete