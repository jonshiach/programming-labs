# For loops
subjects = ["linear algebra", "programming", "calculus"]

for subject in subjects:
    print(subject)
    
print()
for i in range(5):
    print(i)

# Dummy loop variable
base = 2;
power = 10;
base_power = 1;

for _ in range(power):
    base_power *= base
  
print(f"\n{base}^{power} = {base_power} \n")

# First 20 Fibonacci numbers
import numpy as np

a, b = 0, 1
print(a)
print(b)

for _ in range(2, 20):
    c = a + b
    print(c)
    a = b
    b = c

    
# While loops
i = 0
print()

while i < 5:
    print(i)
    i += 1
    
# Approximating the golden ratio
a, b = 1, 1
new_phi, old_phi = 1, 0
print(f"\n{new_phi:0.6f}")

while abs(new_phi - old_phi) > 1e-6:
    a, b = b, a + b
    old_phi = new_phi
    new_phi = b / a
    print(f"{new_phi:0.6f}")


# The break command
print()
for i in range(5):
    if i == 3:
        break
    
    print(i)
    
# The continue command
print()
for i in range(5):
    if i == 3:
        continue
    
    print(i)
    
# Nested loops
mult_square = np.ones((10, 10))

for i in range(10):
    for j in range(10):
        mult_square[i, j] = (i + 1) * (j + 1);
       
print()
print(mult_square)
    
    
    
    
    
    
    