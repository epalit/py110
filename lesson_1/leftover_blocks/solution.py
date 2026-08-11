def calculate_leftover_blocks(total_blocks):
    leftover = total_blocks
    structure = []
    layer = 1

    while True:
        required_blocks = layer ** 2
        if leftover >= required_blocks:
            structure.append(required_blocks)
            leftover -= required_blocks
        else:
            return leftover

        layer += 1

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True