#Leaders (Python-3.6.9)
#Akshat Garg (aksgarg)
#Submitted: Sun, Jan 29, 2023 19:21:09 EST
#Contest: USACO 2023 January Contest, Bronze


def main():
    n = int(input())
    breeds = [str(j) for j in str(input())]
    e = [int(j) for j in input().split()]
    g = [j for j in range(n) if breeds[j] == 'G']
    h = [j for j in range(n) if breeds[j] == 'H']
    lists = []
    for j in range(n):
        lists.append([k for k in range(j,(e[j]))])
    leaders = 0
    ming = min(g)
    minh = min(h)
    for gcow in g:
        if ming != gcow:
            if all(cow in lists[gcow] for cow in g) or h[0] in lists[gcow]:
                if all(cow in lists[hcow] for cow in h) or h[0] in lists[h[0]]:
                    leaders+=1
        else:
            for hcow in h:    #0-5
                if all(cow in lists[gcow] for cow in g) or hcow in lists[gcow]:
                    if all(cow in lists[hcow] for cow in h) or gcow in lists[hcow]:
                        leaders+=1
    print(leaders)
main()
