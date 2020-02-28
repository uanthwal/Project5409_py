import time
import matplotlib.pyplot as plt

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
number_list = []
time_list = []
with open("Fibonacci_Output.log", "a") as log_file:
    for x in range(len(lines)):
        start = time.time()
        print()
        print()
        print("Request ID: ", str(x))
        print("N: ", lines[x])
        print("Fibonacci Series for number: ", lines[x])

        log_file.write("\n")
        log_file.write("\n")

        log_file.write("Request ID: " + str(x))
        log_file.write("\n")
        log_file.write("N: " + lines[x])
        log_file.write("\n")
        log_file.write("Fibonacci Series for number: " + lines[x])
        log_file.write("\n")
        n = int(lines[x])
        number_list.append(n)
        n1, n2 = 0, 1
        count = 0

        if n == 1:
            print(n1)
            log_file.write(str(n1))
        else:
            while count < n:
                log_file.write(str(n1) + " ")
                print(str(n1), end=' ')
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1

        end = time.time()
        print()
        print("Time Taken (s): " + str(end - start))
        log_file.write("\n")
        log_file.write("Time Taken (s): " + str(end - start))
        time_list.append(end - start)

plt.figure(1)
plt.grid(True)
plt.tight_layout()
plt.title('Resource Usage')
plt.xlabel('Number (N)', fontsize=18)
plt.ylabel('Time taken (s)', fontsize=18)
plt.plot(number_list, time_list)
plt.show()
