'''
Fizzbuzz

While counting to 15, if the current number is divisible by 3, print "FIZZ".
  If the current number is divisible by 5, print "BUZZ". If the current
  number is divisible by both 3 AND 5, print "FIZZBUZZ".
  
Example solution for The Odin Project's Python course. See more at
  https://www.theodinproject.com/
'''

i = 1

while i <= 15:
    if (i % 3 == 0) and (i % 5 == 0):
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
    i += 1
