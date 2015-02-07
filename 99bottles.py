# 99 bottles of beer on the wall!

bottles = 99

while bottles > 1:
    print "{} bottles of beer on the wall".format(bottles)
    print "{} bottles of beer".format(bottles)
    bottles = bottles - 1
    if bottles == 1:
        print "takes one down pass it around"
        print "{} bottle of beer on the wall".format(bottles)
        print ""
        print "{} bottle of beer on the wall".format(bottles)
        print "{} bottle of beer".format(bottles)
        print "takes one down pass it around"
        bottles = bottles - 1
        print "{} bottles of beer on the wall".format(bottles)
        print "dang someone is drunk!!"
    else:
        print "takes one down pass it around"
        print "{} bottles of beer on the wall".format(bottles)
        print ""
