# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle
#  gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
#  qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
#
# K -> M
# O -> Q
# E -> G

# so it seems as if 2 letters to the right to decipher this message
#
# def translate(n):
#     print str.capitalize(n)
#
# translate("yomama")
#
#
# def translate(n):
# # import string
# # x = list(string.ascii_lowercase)
# # print x[0]


import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)
