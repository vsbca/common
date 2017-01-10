import os
# compares two files and check if the first file data isn't present in the second file.

file1 = os.getcwd() + "\\" + "googleext.txt";
print file1;
datafile = os.getcwd() + "\\" + "rule_ext.txt";

with open(datafile, "r") as f:
    names = set(i.strip() for i in f)
output = [];
with open(file1, "r") as f:
    for name in f:
        if name.strip() not in names:
            #print name;
			output.append(name);
print output
		
			
