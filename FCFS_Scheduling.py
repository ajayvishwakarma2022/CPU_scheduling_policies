processes=[]
n=int(input("Enter the number of processes: "))
for i in range(1,n+1):

    processes.append(i)
print(processes)
#take burst time from user
burst_time =[]
m=int(input("Enter the number of element: "))
for i in range(0,m):
    elements=int(input())
    burst_time.append(elements)
print(burst_time)

# of FCFS scheduling

def findWaitingTime(processes, n,
                    bt, wt):
    # waiting time for
    # first process is 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


# Function to calculate turn
# around time
def findTurnAroundTime(processes, n,
                       bt, wt, tat):
    # calculating turnaround
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# Function to calculate
# average time
def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    # Function to find waiting
    # time of all processes
    findWaitingTime(processes, n, bt, wt)

    # Function to find turn around
    # time for all processes
    findTurnAroundTime(processes, n,
                       bt, wt, tat)

    # Display processes along
    # with all details
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    # Calculate total waiting time
    # and total turn around time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " +
              str(wt[i]) + "\t\t " +
              str(tat[i]))

    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))


# Driver code
if __name__ == "__main__":
    findavgTime(processes, n, burst_time)


