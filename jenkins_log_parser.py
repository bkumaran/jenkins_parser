import re
import urllib
import sys

link = sys.argv[1]
if "consoleText" in link:
    pass
elif "console" in link:
    link += "Text"
elif "consoleText" not in link:
    link += "/consoleText"
else:
    pass
found=0
dict = {}

array =[]
final_array = []
lines = urllib.urlopen(link).readlines()
for line in lines:
    line = line.strip('\n')
    if "ERROR: " in line or "FAIL: " in line:
        array.append(line)
	found = 1
    elif "Ran 1 test in" in line and found == 1 :
	array.append(line+"\n")
	final_array.extend(array)
	array =[]
	found = 0
    elif found:
	array.append(line)
    else:
	pass

for line in final_array:
    m = re.match(r"^(.*)(Exception|Error):\s+(.*)", line)
    if m :
        if not m.group(0) in dict:
            dict[m.group(0)] = 1
        else:
            dict[m.group(0)] += 1

total = 0
del dict["TypeError: kill_memcached() takes exactly 2 arguments (1 given)"]
print '-' * 158
print "{:<150} {:<8}".format('Error','Count')
print '-' * 158
for k, v in dict.items():
    print "{:<150} {:<8}".format(k[:150],v)
    total = total + v
print '-' * 158
print "{:<150} {:<8}".format('Total Errors', total)
print '-' * 158
