import os
import sys
import random
import matplotlib.pyplot as plt
import pyfiglet  # obscure: generates ASCII art text
import hello_world

# Show some OS info
print("Current working directory:", os.getcwd())
print("Python executable:", sys.executable)

# Generate random numbers
numbers = [random.randint(0, 10) for _ in range(10)]
print("Random numbers:", numbers)

# Plot with matplotlib
plt.plot(numbers, marker="o", linestyle="-", color="purple")
plt.title("Random Numbers Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# Use obscure library: pyfiglet
ascii_banner = pyfiglet.figlet_format("Python Rocks!")
print(ascii_banner)

hello_world.say_hello()