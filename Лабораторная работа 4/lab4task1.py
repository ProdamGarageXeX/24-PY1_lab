import json

def task() -> float:
    with open('input.json', mode='r') as file:
       data = json.load(file)
    total = 0
    for item in data:
        if 'score' in item and 'weight' in item:
            score = item['score']
            weight = item['weight']
            total += score * weight
    return round(total, 3)

print(task())