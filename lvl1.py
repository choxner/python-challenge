
# Level 1 of pythonchallenge.com!
# Challenge: decode a message by shifting each character 2 
# letters to the right, alphabetically. Then, apply the same
# translation to the original url ("map")

from solution_framework import Solution
import string

original_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# the original text to be translated

alphabet = string.ascii_lowercase
trans_alphabet = "yz" + string.ascii_lowercase.split("y")[0]
translation = original_text.maketrans(trans_alphabet, alphabet)
# create the translation table 

new_text = original_text.translate(translation)
print(new_text)
# get the new text. print to view instructions

old_url = "map"
new_url = old_url.translate(translation)
# translate the url extension

Solution(new_url)
# solve!
