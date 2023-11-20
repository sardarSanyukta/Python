target=int(input())
alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)
