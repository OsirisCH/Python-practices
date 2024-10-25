# Create a countdown timer. The import time module  provides various time-related functions.
import time
my_time = int(input("Enter the time in seconds: "))

# This is a simple timer: 
for X in range(0, my_time):
    print(X)
    time.sleep(1)
print("Time's up!")

# If you want a reverse countdown:

for X in range(my_time, 0, -1):
    seconds = X % 60
    minutes = int(X/60)
    hours = int(X/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")
