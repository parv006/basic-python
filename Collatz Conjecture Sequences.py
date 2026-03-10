import matplotlib.pyplot as plt

i = int(input('Enter an integer: '))

p = []

for j in range(2, i):
    h = j
    sequence = [h]
    while h != 1:
        if h > 1 and h % 2 == 0:
            h = h // 2
        elif h > 1 and h % 2 != 0:
            h = 3 * h + 1
        sequence.append(h)
    p.append(sequence)

for seq in p:
    print(seq)
    plt.plot(seq)

plt.title('Collatz Conjecture Sequences')
plt.xlabel('Step')
plt.ylabel('Value')
plt.show()
