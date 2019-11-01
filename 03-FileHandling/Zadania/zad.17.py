import re
regex = r"(a|e|i|o|u|y)"
test_str = ("To be, or not to be, that is the question")
matches = re.findall(regex, test_str, re.MULTILINE)
print("Samogłosek jest: ",len(matches))