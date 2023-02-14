import timeit
import matplotlib.pyplot as plt

def func(n):
    if n== 0 or n==1:
        return n
    else:
        return func(n-1)+func(n-2)

x  = {}
def func1(n): 
    if n == 0 or n == 1:
        return n
    if n in x:
        return x[n]
    else:
        x[n] =  func1(n-1) + func1(n-2)
        return x[n]

times_func = []
times_func1 = []

for i in range(36):
    t = timeit.timeit(lambda: func(i), number=1)
    times_func.append(t)
    t = timeit.timeit(lambda: func1(i), number=1)
    times_func1.append(t)

plt.plot(range(36), times_func, label="func ")
plt.plot(range(36), times_func1, label="func1")
plt.legend()
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.show()