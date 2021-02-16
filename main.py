from numba import jit#, cuda
#from timeit import default_timer as timer


#@jit(nopython=True)
def run():

  high = int(input("The amount you want to add:   "))+1
  
  #start = timer()
  seperator = ", "
  filename = "primesdata"

  #path_parent = path.dirname(getcwd())
  #chdir(path_parent)
  f = str(open ("results/"+filename+".txt", "r").read())
  primes = list(f.split(seperator))
  startLen = len(primes)
  for x in range (int(primes[-1]), int(primes[-1])+high):
    a = True
    for y in primes: 
      if x % int(y) == 0:
        a = False
        break
    if a:
      primes.append(x)
  #return primes

  for x in range(len(primes)):
    primes[x] = str(primes[x])

  with open ("results/"+filename+".txt", "w+") as file:

    file.write(seperator.join(primes))

  print("Success! found ", len(primes)-startLen, " prime numbers. We're now up in ",len(primes))#,". Speed: ", timer()-start,"s "


run()
