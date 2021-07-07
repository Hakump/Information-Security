

def xorStr(str1, str2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))


# x = "C1"
# y = "C2"
#
# print(xorStr("0", "M")+x[:1] + y[1:])
# print(1)

temp = "bucky,Newm@dis0n,8934029034".encode()
for i in range(256):
    temp = hashlib.sha256(temp).digest()
print(temp.hex())
