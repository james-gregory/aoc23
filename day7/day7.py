import re
from functools import cmp_to_key

# ugly

valsa = {'A':14 , 'K':13 , 'Q':12 , 'J':11 , 'T':10, '9':9 , '8':8 , '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
valsb = {'A':14 , 'K':13 , 'Q':12, 'T':10, '9':9 , '8':8 , '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1}

def comparea(a, b):
    rank1 = rank_a(a[0])
    rank2 = rank_a(b[0])

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    
    for i in range(5):
        if valsa[a[0][i]] > valsa[b[0][i]]:
            return 1
        elif valsa[a[0][i]] < valsa[b[0][i]]:
            return -1

    return 0

def compareb(a, b):
    rank1 = rank_b(a[0])
    rank2 = rank_b(b[0])

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    
    for i in range(5):
        if valsb[a[0][i]] > valsb[b[0][i]]:
            return 1
        elif valsb[a[0][i]] < valsb[b[0][i]]:
            return -1
    
    return 0

def rank_a(hand):
    m = {}
    for card in hand:
        if card not in m:
            m[card] = 1
        else:
            m[card] += 1

    return rank(list(m.values()))

def rank_b(hand):
    m = {}
    for card in hand:
        if card not in m:
            m[card] = 1
        else:
            m[card] += 1

    maxkey = hand[0]
    if 'J' in hand:
        for k in m:
            if maxkey == 'J' and k != 'J':
                maxkey = k
            if m[k] > m[maxkey] and k != 'J':
                maxkey = k
        change = m['J']
        m[maxkey] += change
        m['J'] -= change
        if m['J'] == 0:
            del m['J']

    return rank(list(m.values()))

def rank(v):
    m = max(v)
    l = len(v)

    if m == 5:
        return 6
    
    if m == 4:
        return 5
    
    if m == 3 and l == 2:
        return 4
    
    if m == 3 and l == 3:
        return 3

    if m == 2 and l == 3:
        return 2
    
    if m == 2 and l == 4:
        return 1
    
    return 0

def a():
    hands = []
    with open("input.txt") as f:
        for line in f:
            s = line.split()
            hands.append([s[0], int(s[1])])

    sa = sorted(hands, key=cmp_to_key(comparea))
    sb = sorted(hands, key=cmp_to_key(compareb))
    total_a = 0
    total_b = 0
    for i in range(len(sa)):
        total_a += (i+1) * sa[i][1]
        total_b += (i+1) * sb[i][1]
    return [total_a, total_b]

print(a())