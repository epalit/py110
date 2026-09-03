## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: floating point number
output: string representing angle in degrees, minutes and seconds

rules:
  explicit requirements:
    - use `"\u00B0"` to represent degrees
    - use `'` to represent minutes
    - use `"` to represent seconds
    - there are 60mins in a degree
    - there are 60secs in a min
  implicit requirements:
    - input can be an int or a float
    - whole part of the number is the degrees

questions:
  - can the angle be > 360? assume no - added to assumptions

assumptions:
  - assume 360 is the max and return an error if it is higher
  - assume input is positive
```

## E: Examples / Test cases
```python
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*

## A: Algorithm
1. check input is between 0 - 360 inclusive, otherwise return error message
2. split into degrees and fractional part of degrees
3. convert remainder into a decimal and convert to minutes and seconds
  a. multiply remainder by 60 to get minutes
  b. split into whole minutes and fractional part
  c. convert fractional part to seconds
  d. discard the fractional part of the seconds
4. format the string and return

## C: Code
```bash
python solution.py
```
