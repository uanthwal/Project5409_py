import time
import matplotlib.pyplot as plt


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
number_list = []
time_list = []
with open("Factorial_Output.log", "a") as log_file:
    for x in range(len(lines)):
        # program_starts = time.time_ns()
        # start = time.time()
        # start = time.process_time()
        start = time.time()
        print()

        print()
        print("Request ID: ", str(x))
        print("N: ", lines[x])

        log_file.write("\n")
        log_file.write("\n")

        log_file.write("Request ID: "+str(x))
        log_file.write("\n")
        log_file.write("N: "+lines[x])
        log_file.write("\n")

        n = int(lines[x])
        number_list.append(n)

        if n == 0 or n == 1:
            print(1)
            log_file.write("Factorial of " + str(n) + " is: " + str(1))
        else:
            fact_val = factorial(n)
            print("Factorial of " + str(n) + " is: " + str(fact_val))
            log_file.write("Factorial of " + str(n) + " is: " + str(fact_val))

        end = time.time()
        log_file.write("\n")

        print("Time Taken (s): "+ str(end - start))
        log_file.write("Time Taken (s): " + str(end - start))
        time_list.append(end - start)


plt.plot(number_list, time_list)
plt.show()
