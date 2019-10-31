import re

regex = r"\D"

test_str = ("Forests cover about 30,5% of Poland's land area based on international standards. Its overall percentage is still increasing. Forests of Poland are managed by the national program of reforestation (KPZL), aiming at an increase of forest-cover to 33% in 2050. The richness of Polish forest (per SoEF 2011 statistics) is more than twice as high as European average (with Germany and France at the top), containing 2.304 billion cubic metres of trees. The largest forest complex in Poland is Lower Silesian Wilderness.\n"
	"More than 1% of Poland's territory, 3,145 square kilometres (1,214 sq mi), is protected within 23 Polish national parks. Three more national parks are projected for Masuria, the Polish Jura, and the eastern Beskids. In addition, wetlands along lakes and rivers in central Poland are legally protected, as are coastal areas in the north. There are over 120 areas designated as landscape parks, along with numerous nature reserves and other protected areas (e.g. Natura 2000).")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))