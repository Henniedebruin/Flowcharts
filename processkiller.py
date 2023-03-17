import psutil

# get all running processes
processes = []
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    process = {
        'pid': proc.info['pid'],
        'name': proc.info['name'],
        'cpu_percent': proc.info['cpu_percent'],
        'memory_percent': proc.info['memory_percent']
    }
    processes.append(process)

# sort by memory usage
sorted_processes = sorted(processes, key=lambda k: k['memory_percent'], reverse=True)

# print the top 10 processes by memory usage
print('Top 10 processes by memory usage:')
for i in range(10):
    process = sorted_processes[i]
    print(f"PID: {process['pid']}, Name: {process['name']}, Memory usage: {process['memory_percent']}%")
    # ask for user confirmation to kill process
    while True:
        answer = input("Do you want to kill this process? (y/n): ")
        if answer.lower() == 'y':
            psutil.Process(process['pid']).kill()
            print(f"{process['name']} process with PID {process['pid']} has been killed.")
            break
        elif answer.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
