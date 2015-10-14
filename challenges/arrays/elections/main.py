# http://coj.uci.cu/24h/problem.xhtml?pid=1003

from numpy import argmax

t = int(raw_input())

for i in range(t):
    n, m = map(int, raw_input().split())
    votes = [0] * n
    for j in range(m):
        region_votes = map(int, raw_input().split())
        for k in range(n):
            votes[k] += region_votes[k]
    print argmax(votes)
