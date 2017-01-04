


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


