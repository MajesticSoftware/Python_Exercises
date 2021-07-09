def run_timing():
    runs = 0
    total_time = 0

    while True:
        runtimes = input("Enter 10 km run time: ")

        if not runtimes:
            break

        runs += 1
        total_time += float(runtimes)

    average_time = total_time / runs
    print(average_time)

    print(f"Average of {average_time}, over {runs} runs.")


run_timing()
print("Terminating Printing...")