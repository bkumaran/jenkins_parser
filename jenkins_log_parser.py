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
tc_count = 0
for line in lines:
    line = line.strip('\n')
    if "ERROR: The system was unable to find the specified registry key or value." in line:
	    pass
    elif 'ERROR: The process "epmd.exe*" not found.' in line:
	    pass
    elif 'ERROR: The process "erl*" not found.' in line:
	    pass
    elif 'ERROR: The process "erl_crash.dump" not found.' in line:
	    pass
    elif "ERROR: " in line or "FAIL: " in line:
	    tc_count += 1
	    found = 1
    elif "Ran 1 test in" in line and found == 1 :
    	final_array.extend(array)
    	array =[]
    	found = 0
    elif "Ran 1 test in" in line and found == 0 :
    	tc_count += 1
        string = str(tc_count)+"\t"+ "PASS"
        final_array.append(string)
    elif found == 1:
    	m = re.match(r"^(.*)(Exception|Error):\s+(.*)", line)
    	if m:
                array.append(str(tc_count)+"\t"+ m.group(0))

for line in final_array:
    print line
