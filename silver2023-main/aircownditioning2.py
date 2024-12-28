#Air Cownditioning II (Python-3.6.9)
#Akshat Garg (aksgarg)
#Submitted: Sun, Jan 29, 2023 16:23:14 EST
#Contest: USACO 2023 January Contest, Bronze


from math import *

def isCooled(stalls):
    return all(k<=0 for k in stalls)

def dec2bin(n,m):
    num = n
    out = ''
    for j in range(m):
        out = str(num%2) + out
        num = num//2
    return str(out)

def main():
    [n,m] = [int(j) for j in input().split()]
    stalls = [0 for x in range(100)]
    for j in range(n):
        [s,t,c] = [int(k) for k in input().split()]
        for k in range(s,t+1):
            stalls[k-1] = c
    aircons = [[int(j) for j in input().split()] for k in range(m)]
    aircons.sort(key=lambda x:x[3])
    aircons.reverse()
    combs = []
    for j in range(1,2**m):
        combs.append('0'*(m-len(dec2bin(j,m)))+dec2bin(j,m))
    m = []
    for j in combs:
        stallsnew = [l for l in stalls]
        mon = 0
        for k in range(len(j)):
            if j[k] == '1':
                for a in range(len(stalls)):    # 1-100
                    if a+1 >= aircons[k][0] and a+1 <= aircons[k][1]:
                        stallsnew[a] -= aircons[k][2]
                mon += aircons[k][3]
        if isCooled(stallsnew):
            m.append(mon)
    print(min(m))

main()
