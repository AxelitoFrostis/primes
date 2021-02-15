from numba import jit, cuda
from timeit import default_timer as timer
#global a
#global b

high = int(input("Input a high:   "))+1

filename = str(input ("filename (two same names will overwrite):    "))
@jit(nopython=True)
def run():
  primes = [2]
  for x in range (3,high):
    a = True
    for y in primes: 
      if x % y == 0:
        a = False
        break
    if a:
      primes.append(x)
  return primes

start = timer()
primes = run()
print("Speed:   ", timer()-start)  

for x in range(len(primes)):
  primes[x] = str(primes[x])

with open ("../results/"+filename+".txt", "w+") as file:
  seperator = ", "
  file.write(seperator.join(primes))

print("Success! found ", len(primes), " prime numbers. ")
