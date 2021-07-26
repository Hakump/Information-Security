import re

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
pattern = re.compile(reg)

fp = open('tested.txt',"w+")

f = open('test.txt', 'r+') #'realhuman_phill.txt'
line = f.readline()

while line:
    mat = re.search(pattern, line)
    if mat:
        fp.write(line)
        print(line)
    else: 
        print("NO")
    line = f.readline()

f.close()
fp.close()