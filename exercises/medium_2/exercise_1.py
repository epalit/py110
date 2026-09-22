"""
Write a function that returns the % of lowercase, uppercase and non-alpha
characters in a given string.

Input: string
Output: dictionary containing the percentage of each category

requirements:
- percentages should be strings to 2dp
- assume input is minimum one character
- whitespace characters count

algorithm:
1. Count the occurrences of each category
  a. Initialise three counts to 0
  b. Iterate over the string
  c. check which category the char is in and increment the count
2. Calculate the percentages of each
  a. for each category calculate count / len(str) * 100
3. Format the output
  a. build a dictionary where keys are the categories and values are the %
4. Return the dictionary
"""

def letter_percentages(string):
    lowercase = 0
    uppercase = 0
    neither = 0

    for char in string:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        else:
            neither += 1

    string_length = len(string)
    lowercase_pct = (lowercase / string_length) * 100
    uppercase_pct = (uppercase / string_length) * 100
    neither_pct = (neither / string_length) * 100

    result = {
        'lowercase': f"{lowercase_pct:.2f}",
        'uppercase': f"{uppercase_pct:.2f}",
        'neither': f"{neither_pct:.2f}",
    }

    return result

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)