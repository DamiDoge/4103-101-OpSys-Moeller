import threading
import os
from os import system
import locale
import time
import threading
import random
import json
import struct


# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []
waiter = []
screenLock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.ate = 0
		
    def run(self):
        # Assign left and right fork
		leftForkIndex = self.index
		rightForkIndex = (self.index - 1) % numPhilosophers
		forkPair = ForkPair(leftForkIndex, rightForkIndex)
		startTime = time.clock()
        # Eat til pasta is gone
		while bowl.pasta>0:
			#Clock the amount of time it has been running
			runTime = time.clock() - startTime
			if runTime < 0.001:
				#Ask waiter for permission to eat
				waiter[0].acquire()
				try:
					forkPair.pickUp()
					try:
						self.ate += 1
						bowl.eat()
						print "philosopher", self.index, "eating."
						print bowl.pasta, "left"
						time.sleep(.01)
					finally:
						forkPair.putDown()
				finally:
					waiter[0].release()
			#If running for more than .001 at a time then sleep and give others chance then reset the timer
			else:
				time.sleep(.001)
				startTime = time.clock()
		print "philosopher", self.index, "ate", self.ate
			
class ForkPair:
    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]

    def pickUp(self):
        # Acquire by starting with the lower index
        self.firstFork.acquire()
        self.secondFork.acquire()

    def putDown(self):
        # The order does not matter here
        self.firstFork.release()
        self.secondFork.release()
class Bowl:
	def __init__(self, pasta):
		self.pasta = pasta
	def eat(self):
		self.pasta -= 1

if __name__ == "__main__":
    
	bowl = Bowl(100)
	waiter.append(threading.Semaphore(1))
    # Create philosophers and forks
	for i in range(0, numPhilosophers):
		philosophers.append(Philosopher(i))
		forks.append(threading.Lock())

    # All philosophers start eating
	for philosopher in philosophers:
		philosopher.start()

    # Allow CTRL + C to exit the program
	try:
		while True: time.sleep(021)
	except (KeyboardInterrupt, SystemExit):
		os._exit(0)