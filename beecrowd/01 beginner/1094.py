

amount = int(input())
animals = {'C': 0, 'R': 0, 'S': 0}
for time in range(0, amount):
    quantity, animal_type = input().split(' ')
    animals[animal_type] += int(quantity)
total = sum(animals.values())
print(f'Total: {total} cobaias')
print(f"Total de coelhos: {animals.get('C')}")
print(f"Total de ratos: {animals.get('R')}")
print(f"Total de sapos: {animals.get('S')}")
print(f"Percentual de coelhos: {(animals['C']/total)*100:.2f} %")
print(f"Percentual de ratos: {(animals['R']/total)*100:.2f} %")
print(f"Percentual de sapos: {(animals['S']/total)*100:.2f} %")
