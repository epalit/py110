"""
Write a function that takes 3 side lengths and determines whether the triangle
made up by those sides is equilateral, isosceles, scalene or invalid.

Input: 3 numbers representing side lengths
Output: string representing type of triangle

Rules:
- if any length is 0, the triangle is invalid
- if the sum of the two shortest sides is less than the longest side, the
triangle is invalid
- if all three sides have different lengths, the triangle is scalene
- if two sides are equal, and the other is not, it is isosceles
- if all sides are equal it is equilateral

Assumptions:
- will always get three numbers >= 0 as arguments

Algorithm:
- Check lengths are valid, if not return invalid
  a. check all lengths greater than 0
  b. check sum of two shortest sides greater than longest side
- check which type of triangle
  a. If all sides are equal return equilateral
  b. If all three sides have different lengths return scalene
  c. else return isosceles
"""

def length_values_valid(lengths):
    return all(l > 0 for l in lengths)

def length_proportions_valid(lengths):
    lengths = sorted(lengths)
    return (lengths[0] + lengths[1]) > lengths[2]

def is_valid_triangle(lengths):
    return (length_values_valid(lengths) and length_proportions_valid(lengths))

def get_triangle_type(a, b, c):
    if a == b == c:
        return 'equilateral'
    elif a != b and b != c and a != c:
        return 'scalene'
    else:
        return 'isosceles'

def triangle(a, b, c):
    if not is_valid_triangle([a, b, c]):
        return "invalid"

    return get_triangle_type(a, b, c)

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True