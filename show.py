import matplotlib.pyplot as plt

text = open ("results/primesdata.txt").read()

l = list(text.split(", "))

for i in range(len(l)):
    l[i] = int(l[i])

plt.plot(l)
plt.show()