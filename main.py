#asks size of sequence
count = int(input('How many numbers in sequence?    '))

#generates fibonacci sequence
fib = [0,1]
i = 0
while (i < count):
  x = fib[i] + fib[i+1]
  fib.append(x)
  i = i + 1
print(fib)

#draws the fibonacci spiral
import turtle
import random
i = 0
t = turtle.Turtle()
while (True):
  i = i + 1
  j = 0
  while (j < count):
    j = j + 1
    rand = random.randint(1,4)
    t.fd(fib[j + 1])
    t.rt(90)
  t.rt(90 * rand)
 

  

  