import hashlib
import re

# testu = "user,"
# testx = ",999999"
# tests = "c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96"

prefix = "bucky,"
suffix = ",8934029034"
line = ''


def matching(stringF):
    return stringF == "1b2ebfab6e70dcb13f3ff4750d065bab8474dac4dc611df339446071ae3e7977"

def password_check(passwd):
    # SpecialSym = ['$', '@', '#', '%',]
    SpecialSym = "~`!@#$%^&*()+=_-{}[]\|:;”’?/<>,."

    num = 4

    if len(passwd) < 6:
        return False

    if len(passwd) > 20:
        return False

    if not any(char.isdigit() for char in passwd):
        num -= 1

    if not any(char.isupper() for char in passwd):
        num -= 1

    if not any(char.islower() for char in passwd):
        num -= 1

    if not any(char in SpecialSym for char in passwd):
        num -= 1
    return num > 2

# op()
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&.])[A-Za-z\d@$!#%*?&.]{6,20}$"
# reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~`!@#$%\^&*()+=_-{}[]\\|:;”’?/<>,.])[A-Za-z\d~`!@#$%\^&*()+=_-{}[]\\|:;”’?/<>,.]{6,20}$"
# reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d]{6,20}$"
pattern = re.compile(reg)

f = open('K:\\Downloads\\realhuman_phill.txt', 'r',errors='ignore')
# f = open('test.txt', 'r', errors='ignore')
line = f.readline()

cnt = 0
while line:
    if re.search(pattern, line):  # password_check(line.strip()) :
        temp = (prefix + line.strip() + suffix).encode()
        for i in range(256):
            temp = hashlib.sha256(temp).digest()
        if matching(temp.hex()):
            print(line)
    line = f.readline()



