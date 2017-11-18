# Cleans the data points where there's a comma in the bike name
# The extra comma in the name messes up the CSV structure
with open("msrp.csv", "r") as file:
	with open("msrp_cleaned.csv", "w") as new:
		for line in file:
			if line.count(',') > 4:
				new.write(line.replace(",", "", 1))
			else:
				new.write(line)
