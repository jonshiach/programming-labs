#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 1. Python Basics
# =============================================================================

# Print the header
print("Degrees to radians conversion\n-----------------------------")

# Define the variables
pi = 3.1415927;
angle_in_degrees = 45;

# Calculate the angle in radians
angle_in_radians = angle_in_degrees * pi / 180;

# Print the angle in degrees and radians
print(f"angle in degrees = {angle_in_degrees:6.3f}")
print(f"angle in radians = {angle_in_radians:6.3f}")