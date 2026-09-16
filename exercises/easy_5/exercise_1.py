def invert_dict(dictionary):
    result = {}
    for k,v in dictionary.items():
        result[v] = k
    return result

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True