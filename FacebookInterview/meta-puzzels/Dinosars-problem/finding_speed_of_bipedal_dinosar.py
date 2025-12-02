"""
You are given two data files in CSV format. 
One file contains statistics about various dinosaurs. 
The other contains additional data. 
Given the following formula,
 speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g), 
 where g = 9.8 m/s^2 (gravitational constant),
write a program to read in the data files from disk. 
It must then print the names of only the bipedal dinosaurs, from fastest to slowest
"""
import csv
import math

# File paths
dataset1 = "dataset1.csv"
dataset2 = "dataset2.csv"

# Step 1: Read leg length data
leg_length_map = {}

with open(dataset1, 'r') as file1:
    reader = csv.reader(file1)
    next(reader)  # Skip header
    for row in reader:
        if len(row) == 3:
            name, leg_length, _ = row
            leg_length_map[name.strip()] = float(leg_length.strip())  # FIXED: replaced leg_length_map() with leg_length.strip()

# Step 2: Read stride length and stance, calculate speed
dino_speed = []

with open(dataset2, 'r') as file2:
    reader = csv.reader(file2)
    next(reader)  # Skip header
    for row in reader:
        if len(row) == 3:
            name, stride_length, stance = row
            name = name.strip()
            stance = stance.strip().lower()
            if stance == 'bipedal' and name in leg_length_map:
                leg_length = leg_length_map[name]
                stride = float(stride_length.strip())
                speed = (stride / math.sqrt(leg_length)) * math.sqrt(9.8)  # FIXED: correct formula syntax
                dino_speed.append((name, speed))

# Step 3: Sort by speed descending
dino_speed.sort(key=lambda x: x[1], reverse=True)

# Step 4: Print names only
for name, _ in dino_speed:
    print(name)


