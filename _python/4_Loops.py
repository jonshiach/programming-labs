#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 4. Loops
# =============================================================================

print("\n4. Loops\n--------")

# For loops
print("\n4.1 For loops\n-------------")
subjects = ["linear algebra", "programming", "calculus"]

for subject in subjects:
    print(subject)
    
print()

for i in range(5):
    print(i)

# 4.1.1. Dummy loop variable
base = 2;
power = 10;
base_power = 1;

for _ in range(power):
    base_power *= base
  
print("\n4.1.1. Dummy loop variable\n--------------------------")  
print(f"{base}^{power} = {base_power}")

# 4.1.2 Fibonacci sequence
import numpy as np

F0, F1 = 0, 1
F = np.array([0, 1])

for n in range(2, 20):
    F = np.append(F, F[n-1] + F[n-2])

print("\n4.1.2 Fibonacci sequence\n------------------------")
print(f"F = {F}")

    
# 4.2 While loops
print("\n4.2 While loops\n---------------")
i = 0

while i < 5:
    print(i)
    i += 1
    
# Fibonacci numbers less than 1 million
F = np.array([0, 1])

while F[-1] + F[-2] < 1e6:
    F = np.append(F, F[-1] + F[-2])
    
print("\nFibonacci numbers less than 1 million\n-------------------------------------")
print(F)

# 4.3.1 The break command
for n in range(2, len(F)):
    phiEstimate1 = F[n] / F[n-1]
    phiEstimate2 = F[n+1] / F[n]
    
    if abs(phiEstimate1 - phiEstimate2) < 1e-6:
        break
  
print("\n4.3.1 The break command\n-----------------------")  
print(f"The estimated value of phi is {phiEstimate2:0.8f}.")   
print(f"The actual value of phi is {(1 + np.sqrt(5))/2:0.8f} (correct to 8 decimal places).")


# 4.3.2 Continue command
sum_ = 0
for n in F:
    if n % 2 == 1:
        continue

    sum_ += n
        
print("\n4.3.2 The continue command\n--------------------------")
print(f"The sum of the even Fibonacci numbers less than 1 million is {sum_}.")

# 4.4 Nested loops
multiplication_square = np.ones((10, 10))

for i in range(10):
    for j in range(10):
        multiplication_square[i, j] = (i + 1) * (j + 1);
        
print("\n4.4 Nested loops\n----------------")
print(f"10x10 multiplication square: \n\n{multiplication_square}")
    
    
    
    
    
    
    
    
    
    
    