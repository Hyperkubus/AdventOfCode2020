import difflib

def getMatch(set):
    print(set)
    base = ''
    for s in set:
        if base == '':
            base = s
        else:
            for i in base:
                if s.find(i) == -1:
                    base = base.replace(i,'')
                    if base == '':
                        return 0
    print(base)
    return len(base)

def main():
    input = "zeta.txt"
    lines = open("../../input/"+input,"r").readlines()
    u = []
    q = []
    for line in lines:
        if line.strip() == '':
            u.append(getMatch(q))
            q = []
        else:
            q.append(''.join(sorted(line.strip())))
    u.append(getMatch(q))
    print(u)
    print(sum(u))

main()