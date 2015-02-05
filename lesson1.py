# Fibonnaci sequence!
# Python
def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

fib(10)


# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# RUBY
def multiples(x)
  array = []
  while x > 0
    x = x - 1
    if (x % 3 == 0) || (x % 5 == 0)
      array << x
    end
  end
  return array.inject{|sum,x| sum + x }
end

puts "#{multiples(1000)}"

# PYTHON
def multiples(x):
    list = []
    while x > 0:
        x = x - 1
        if (x % 3 == 0) or (x % 5 == 0):
            list.append(x)
    b = sum(list)
    print b

multiples(10)

# oh my gosh the indenting in python is ridiculous have to get used to it
# but this is the same code as above for ruby
