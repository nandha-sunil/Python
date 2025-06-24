name=input("SREENANDHA.A.S: ")
USN=input("1AY24BT052: ")
import random
flips = [random.choice(['H', 'T']) for _ in range(100)]
print("".join(flips))
if 'HHHHHH' in "".join(flips) or 'TTTTTT' in "".join(flips):
    print("Streak of 6 found!")
else:
    print("No streak of 6.")
