
from time import perf_counter
import asyncio

start = perf_counter()
for i in range(25000):
    print(i)
stop = perf_counter()
time_taken = stop - start

print("Time Taken: ", time_taken)

