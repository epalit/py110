def swap_name(name):
    names = name.split()
    surname = names[-1]
    forenames = names[:-1]
    return f"{surname}, {' '.join(forenames)}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
