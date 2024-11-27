import math
import argparse

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--radius', help='Radius size', required=True, type=int)
args = parser.parse_args()
radius = args.radius

# Define pi
pi = 3.14

# Calculate area
area = pi * (radius**2)
print("Circle area: ", area)

# Calculate circumference
circumference = pi * 2 * radius
print("Circle circumference: ", circumference)
