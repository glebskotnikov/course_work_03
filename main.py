from src.utils import import_json_file, instance_json, sorted_data, what_is_transfer

database = import_json_file('json/operations.json')
new_database = sorted_data(database)
instance_operations = instance_json(new_database)

counter = 0
for item in reversed(instance_operations):
    amount = item.operationAmount["amount"]
    currency = item.operationAmount["currency"]["name"]
    if counter < 5 and item.state == "EXECUTED":
        counter += 1
        print(f'{item.date} {item.description}')
        trans_to = what_is_transfer(item.to_)
        if item.from_ is None:
            print(f'{trans_to}')
        else:
            trans_from = what_is_transfer(item.from_)
            print(f'{trans_from} -> {trans_to}')
        print(f'{amount} {currency}\n')
    else:
        continue
