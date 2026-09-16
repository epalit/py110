def staggered_case(string):
    result = ""
    previous_action = None

    for char in string:
        if not char.isalpha():
            result += char
            continue

        if previous_action == 'upper':
            result += char.lower()
            previous_action = 'lower'
        else:
            result += char.upper()
            previous_action = 'upper'

    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True