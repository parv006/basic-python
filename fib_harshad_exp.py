import matplotlib.pyplot as plt
def harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    if n % digit_sum == 0:
        return n

def is_fibonacci(y):
    a, b = 0, 1
    while b < y:
        a, b = b, a + b
    if b == y:
        return y

c = 1
fin = []

while c <= 100000:
    if harshad(c) and is_fibonacci(c):
        fin.append(c)
    c += 1

print(f"Harshad Fibonacci numbers: {fin}")
ab=[]
ac=[]
num=int(input('enter: '))
for j in range(1,num):
    
    ab.append(harshad(j))

for u in range(1,num):
    
    ac.append((harshad(u)))
plt.plot(ab,ac)
plt.show()

