def get_input_msg(req_num):
    match req_num:
        case 1:
            position = '1st'
        case 2:
            position = '2nd'
        case 3:
            position = '3rd'
        case 4:
            position = '4th'
        case 5:
            position = '5th'
        case 6:
            position = 'last'
            
    return f"Enter the {position} number: "

def get_num(request):
    msg = get_input_msg(request)
    num = input(msg)
    return int(num)

num_list = []

for request in range(1, 6):
    num = get_num(request)
    num_list.append(num)

final_num = get_num(6)

num_str = ','.join([str(num) for num in num_list])

if final_num in num_list:
    print(f"{final_num} is in {num_str}")
else:
    print(f"{final_num} isn't in {num_str}")
