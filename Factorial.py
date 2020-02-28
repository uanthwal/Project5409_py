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
            print("Factorial of " + str(n) + " is: " + str(1))
            log_file.write("Factorial of " + str(n) + " is: " + str(1))
        else:
            fact_val = factorial(n)
            print("Factorial of " + str(n) + " is: " + str(fact_val))
            log_file.write("Factorial of " + str(n) + " is: " + str(fact_val))

        end = time.time()
        log_file.write("\n")
        print("Time Taken (s): " + str(end - start))
        log_file.write("Time Taken (s): " + str(end - start))
        time_list.append(end - start)

plt.figure(2)
plt.grid(True)
plt.tight_layout()
plt.title('Resource Usage')
plt.xlabel('Number (N)', fontsize=18)
plt.ylabel('Time taken (s)', fontsize=18)
plt.plot(number_list, time_list)
plt.show()
