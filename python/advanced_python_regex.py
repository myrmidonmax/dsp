


# Part I - Questions 1

def quest_1():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		degrees = []
		degrees_count = {}

		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			degrees.append(row[" degree"].replace(".", "").strip().split())

		for i in range(len(degrees)):
			for j in range(len(degrees[i])):
				if degrees[i][j] != "0":
					degrees_count[degrees[i][j]] = degrees_count.setdefault(degrees[i][j], 0) + 1
		print("There are %d different degrees. The frequencies are:\n" % len(degrees_count), sorted(degrees_count.items(), key = operator.itemgetter(1), reverse=True) )



# Part I - Question 2

def quest_2():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		titles = []
		titles_count = {}

		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			title_full = row[" title"].replace(" is", " of").strip()
			title_short, rest = title_full.split(" of")

			titles.append(title_short)

		for title in titles:
			titles_count[title] = titles_count.setdefault(title, 0) + 1

		print("There are %d different titles. The frequencies are:\n" % len(titles_count), sorted(titles_count.items(), key = operator.itemgetter(1), reverse=True) )

quest_2()
# Part I - Question 3

def quest_3():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		email_adr = []
		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			for cell in row:
				if "@" in row[cell]:
					email_adr.append(row[cell])

		print(email_adr)



# Part I - Question 4

def quest_4():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		email_adr = []
		domains = []
		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			for cell in row:
				if "@" in row[cell]:
					email_adr.append(row[cell])
		for adr in email_adr:
			name, domain = adr.split("@")
			if domain not in domains:
				domains.append(domain)

		print(domains)

#quest_1()
#quest_2()
#quest_3()
#quest_4()