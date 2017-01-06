
import csv

def quest_3():
	import csv, string, operator
	with open("faculty.csv", "r") as fac:
		email_adr = []
		fac_reader = csv.DictReader(fac)
		for row in fac_reader:
			for cell in row:
				if "@" in row[cell]:
					email_adr.append(row[cell])

		return email_adr


def email_csv():
	with open ("emails.csv", "w") as e_file:
		columnheads = ["email_address"]
		writer = csv.DictWriter(e_file, fieldnames = columnheads)
		email_adr = quest_3()

		writer.writeheader()
		for i in email_adr:
			writer.writerow({"email_address" : i})

email_csv()