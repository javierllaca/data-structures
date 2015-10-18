from sys import stdin


a = []
for line in stdin:
    a.append(int(line))

print str(sum(a))[:10]
