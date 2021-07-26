# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag
import hashlib

message = \
    """AMOUNT: $  20.00
Originating Acct Holder: Bucky
Orgininating Acct #82123-09837

I authorized the above amount to be transferred to the account #38108-443280
held by a Wisc student at the National Bank of the Cayman Islands.
"""
c1 = "AMOUNT: $  10.00"
c2 = "AMOUNT: $  20.00"


def xorStr(str1, str2):
    result = bytearray()
    for b1, b2 in zip(str1, str2):
        result.append(b1 ^ b2)
    return bytes(result)


import sys

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16 + 16 + 32:
    print("Ciphertext is too short!")
    sys.exit(0)

# print(len(ciphertextWithTag))

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag) - 32]
tag = ciphertextWithTag[len(ciphertextWithTag) - 32:]

# TODO: Modify the input so the transfer amount is more lucrative to the recipient

newIV = xorStr(xorStr(c1.encode(), c2.encode()), iv)
ciphertext = newIV + ciphertext[16:] + bytes.fromhex(hashlib.sha256(message.encode()).hexdigest())

# TODO: Print the new encrypted message
# you can change the print content if necessary
# print(ciphertext.hex() + tag.hex())
print(ciphertext.hex())