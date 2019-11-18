'''def addition():
    list =[]
    i=0
    sum = 0
    number = input ("Enter the number of elements you want to add\n")
    for elements in range(i, number):
        elements = input()
        list.append(elements)
        if type(elements) == float or type(elements) == int:
            elements = input()
            list.append(elements)
            for elements in range(i, number):
                 sum = float(sum) + float(list[elements])
        elif type(elements) == str:

    return sum
print(addition())

# Python code to demonstrate the working of
# sum()

numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
Sum = sum(numbers)
print(Sum)

# start = 10
Sum = sum(numbers, 10)
print(Sum)
'''
#normal approach
import memory_profiler
import time


def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)

    return even


if __name__ == '__main__':
    m1 = memory_profiler.memory_usage()
    t1 = time.clock()
    cubes = check_even(range(100000000))
    t2 = time.clock()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")

    import memory_profiler
    import time

#build in approach
    def check_even(numbers):
        for num in numbers:
            if num % 2 == 0:
                yield num * num


    if __name__ == '__main__':
        m1 = memory_profiler.memory_usage()
        t1 = time.clock()
        cubes = check_even(range(100000000))
        t2 = time.clock()
        m2 = memory_profiler.memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]
        print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")