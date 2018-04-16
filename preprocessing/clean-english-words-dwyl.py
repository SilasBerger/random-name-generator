import re

# accept words with at least 2 characters, letters only, starting with upper or lower case,
# no upper case anywhere other than first character
pattern = re.compile("[a-zA-Z][a-z]+")

candidates = []
with open("english-words-dwyl.txt", "r") as infile:
	for line in infile:
		line = line.strip()
		match = re.match(pattern, line)
		if (match is not None) and (match.span()[0] == 0) and (match.span()[1] == len(line)):
			candidates.append(line)

with open("english-words-dwyl-clean.txt", "w") as outfile:
	for c in candidates:
		outfile.write(c + "\n")
