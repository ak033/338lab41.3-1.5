import timeit
x  = {}
def func(n): 
    if n == 0 or n == 1:
        return n
    if n in x:
        return x[n]

    else:
     
        x[n] =  func(n-1) + func(n-2)
        return x[n]


elapsed_time = timeit.timeit(lambda:func(200), number=1)
print(f'the elapsed time Is:{elapsed_time} seconds')

