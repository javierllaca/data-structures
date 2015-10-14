def find_frauds(transactions):
    frauds = []
    for name in transactions:
        last_location, last_time = None, float('-inf')
        f1, f2 = 0, 0  # fraud types
        t1, t2 = None, None  # time types
        for amount, location, time in transactions[name]:
            if amount > 3000:
                f1 = -1
                t1 = t1 or time
            if location != last_location and time - last_time < 60:
                f2 = -1
                t1 = t1 or time
                t2 = t2 or last_time
            last_location, last_time = location, time
        if f1 or f2:
            frauds.append((f1, f2, t1 if f1 else t2, name))
    return frauds


n = int(raw_input())

transactions = {}

for i in range(n):
    name, amount, location, time = raw_input().split('|')
    transaction = int(amount), location, int(time)
    if name in transactions:
        transactions[name].append(transaction)
    else:
        transactions[name] = [transaction]

for _, _, _, name in sorted(find_frauds(transactions)):
    print name
