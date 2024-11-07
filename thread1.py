import time

def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("square is:",n*n)

def cube(numbers):
    for n in numbers:
        time.sleep(1)
        print("cube is:",n*n*n)


numbers = [2,3,4,5,6,7,8]
t = time.time()
square(numbers)
cube(numbers)

print("Done in:",time.time()-t)
