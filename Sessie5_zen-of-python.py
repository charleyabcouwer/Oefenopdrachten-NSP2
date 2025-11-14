# Voorbereiding sessie 5
import this  # noqa
import math


# Als code langer maar duidelijker is.
print(
    """
    Manier 1 om bits en bytes te verhouden: kort, maar onduidelijk te lezen. 
    """
    "\n".join(
        "%i bytes = %i bits which has %i possible values." % (j, j * 8, 256**j)
        for j in (1 << i for i in range(4))
    )
)

for num_bytes in [1, 2, 4, 8]:
    """
    Manier 2 om bits en bytes te verhouden: langer, maar duidelijker te lezen.
    """
    num_bits = 8 * num_bytes
    num_possible_values = 2**num_bits
    print(
        f"{num_bytes} bytes = {num_bits} bits which has {num_possible_values} possible values."
    )

# Itereren op de python manier via math

voltages = [0, 50, 100, 150, 200, 250, 300]  # mV

for voltage in voltages:
    print(f"De voltage is set to {voltage} mV.")

squares = []
for n in range(1, 11):
    squares.append(math.sqrt(n))

# print the list below each other with three decimal places
print("Square of range 1 to 10 with three decimal places: ")
for square in squares:
    print(f"{square:.3f}")

# State if number 3 or 4 appears in the list of squares
for number in [3, 4]:
    print(f"does number {number} appears in the list of squares?", number in squares)

# Itereren op de python manier via NumPy array

import numpy as np  # noqa

# Make an array from 1 to 10
numbers = np.arange(1, 11, 1)

# Take the squareroot of each number
squareroot = np.sqrt(numbers)

# Print the list of squareroots below each other with three decimal places
for root in squareroot:
    print(f"{root:.3f}")

# State if number 3 or 4 appears in the list of squares
print("does number 3 appears in the list of squares?", 3 in squareroot)
print("does number 4 appears in the list of squares?", 4 in squareroot)

# Array, for-loops en comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# use a for loop to create a list with cube root of numbers
cube_root = []
for number in numbers:
    answer = number ** (1 / 3)
    cube_root.append(answer)


# use list comprehension to create a list with cube root of numbers
cube_root_comprehension = [n ** (1 / 3) for n in numbers]

# use numpy arrays to create a list with cube root of numbers
numbers = np.array(numbers)
cube_root_array = numbers ** (1 / 3)

print(cube_root)
print(cube_root_comprehension)
print(cube_root_array)
