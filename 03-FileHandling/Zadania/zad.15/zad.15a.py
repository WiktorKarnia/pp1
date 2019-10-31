import re

regex = r"\b[A-Z]{3}"

test_str = ("MAT Matematyka 45\n"
	"GEO Geografia 210\n"
	"HIS Historia 28\n"
	"INF Inforamtyka 196\n"
	"AST Astronomia 9")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))