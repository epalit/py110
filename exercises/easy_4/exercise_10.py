def transactions_for(item_id, txns):
    return [txn for txn in txns if txn["id"] == item_id]

def is_item_available(item_id, transactions):
    item_transactions = transactions_for(item_id, transactions)
    items_remaining = 0

    for txn in item_transactions:
        if txn['movement'] == 'in':
            items_remaining += txn['quantity']
        else:
            items_remaining -= txn['quantity']

    return items_remaining > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True