"""
Write a function that returns whether a triangle is acute, right, obtuse or invalid.

Input: 3 ints representing the angles in whole degrees
Output: string representing the triangle classification

Rules:
- a triangle is invalid if any angles are 0 or if they do not sum to 180
- a triangle is right if one angle is 90 degrees
- a triangle is obtuse if one angle is greater than 90 degrees
- a triangle is acute if all three angles are less than 90 degrees

Algorithm:
1. Check the triangle is valid, if not return invalid
  a. check all angles are greater than 0
  b. check all angles sum to 180
2. Classify the triangle
  a. check if any angle is 90 degrees, if yes return right
  b. check if any angle is greater than 90 degrees, if yes return obtuse
  c. else return acute
"""

DEGREES_IN_TRIANGLE = 180

def triangle_is_valid(angles):
    return all(angle > 0 for angle in angles) \
        and sum(angles) == DEGREES_IN_TRIANGLE

def get_triangle_type(angles):
    if any(angle == 90 for angle in angles):
        return "right"
    if any(angle > 90 for angle in angles):
        return "obtuse"

    return "acute"

def triangle(a, b, c):
    angles = [a, b, c]
    if not triangle_is_valid(angles):
        return "invalid"

    return get_triangle_type(angles)

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True