list = [0,1,2,3,4,4,4,5,2,1,3]

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0

for s in list:
   if s == 0:
       zero += 1
   if s == 1:
       one += 1
   if s == 2:
       two += 1
   if s == 3:
       three += 1
   if s == 4:
       four += 1
   if s == 5:
       five += 1

print "there are {} zeroes".format(zero)
print "there are {} ones".format(one)
print "there are {} twos".format(two)
print "there are {} threes".format(three)
print "there are {} fours".format(four)
print "there are {} fives".format(five)
