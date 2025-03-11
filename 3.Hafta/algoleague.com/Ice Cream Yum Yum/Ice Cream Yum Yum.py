n = int(input())
a = [int(x) for x in input().split()]
total = 0
for i in a:
    total += i
total -= min(a)
print(total)
