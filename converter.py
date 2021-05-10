# Insert normal .txt/.csv path here
file = open(r"C:\Users\User\Desktop\Cities in the World.csv", "r")

# Splits each row
lines = file.read().splitlines()
n = 0

# Insert target output path here
file2 = open(r"C:\Users\User\Desktop\cities.yml", "w")

# Writes the headers(?), remember to change the lookup name
file2.write("version: \"2.0\"\nnlu:\n  - lookup: city  \n    examples: |\n")

# Adds indent and dash to each line
for line in lines:
    file2.write("      - " + str(line) + "\n")

# Closes the files
file.close()
file2.close()
