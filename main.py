from pythonds.basic.queue import Queue
from doctor import *
from patient import *


def simulation(numberOfHours, workRate):
    # A function that do all the simulation of the working times and manage the queue of patients
    clinicDoctor = Doctor(workRate)
    clinicQueue = Queue()
    waitingTimes = []
    numberOfMinutes = numberOfHours * 60

    for currentMinute in range(numberOfMinutes):
        if randrange(1, 7) == 1:
            patient = Patient(currentMinute)
            clinicQueue.enqueue(patient)

        if (not clinicDoctor.busy()) and (not clinicQueue.isEmpty()):
            nextPatient = clinicQueue.dequeue()
            waitingTimes.append(nextPatient.waitTime(currentMinute))
            clinicDoctor.startNext(nextPatient)

        clinicDoctor.tick()

    # Printing results
    averageTime = sum(waitingTimes) / len(waitingTimes)
    print(f"Average waiting time: {averageTime:.2f} in minutes. Remaining patients: {clinicQueue.size()}")


print('#' * 70)
print("With (Age/5) rate case:")
for i in range(10):
    simulation(4, 5)

print('#' * 70, end="")
print("\nWith (Age/10) case:")
for i in range(10):
    simulation(4, 10)

print('#' * 70, end="")