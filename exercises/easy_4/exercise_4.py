def get_second_element(item):
    return item[1]

def order_by_value(my_dict):
    sorted_items = sorted(my_dict.items(), key=get_second_element)
    return [k for k, v in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True