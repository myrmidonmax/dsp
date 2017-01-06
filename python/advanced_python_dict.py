

# Part III - Q6

def quest_6():
	import csv, string, operator, itertools
	with open("faculty.csv", "r") as fac:
		faculty_dict = {}
		faculty_list = []

		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			surname = row["name"].split()[-1]

			title_full = row[" title"].replace(" is", " of").strip()
			title_short, rest = title_full.split(" of")

			memberdetails = [row[" degree"], title_short, row[" email"]]
			faculty_dict.setdefault(surname, []).append(memberdetails)

		for i in faculty_dict:
			faculty_list.append((i, faculty_dict[i]))

		for i in range(3):
			print(faculty_list[i])



# Part III - Q7

def quest_7():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		professor_dict = {}

		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			surname = row["name"].split()[-1]
			given_names = row["name"][:len(row["name"])-len(surname)-1]

			title_full = row[" title"].replace(" is", " of").strip()
			title_short, rest = title_full.split(" of")

			memberdetails = [row[" degree"], title_short, row[" email"]]
			professor_dict[surname, given_names] = memberdetails

		for i in professor_dict:
			print(i, professor_dict[i])



# Part III - Q8

def quest_8():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		professor_dict = {}

		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			surname = row["name"].split()[-1]
			given_names = row["name"][:len(row["name"])-len(surname)-1]

			title_full = row[" title"].replace(" is", " of").strip()
			title_short, rest = title_full.split(" of")

			memberdetails = [row[" degree"], title_short, row[" email"]]
			professor_dict[surname, given_names] = memberdetails

		for i in sorted(professor_dict):
			print(i, professor_dict[i])

quest_6()