rules = {}

def rule2array(rule):
    parts = rule.split('bags contain ')
    key = parts[0].strip()
    bags = parts[1].split(', ')
    value = []
    for bagDef in bags:
        i = bagDef.find('bag')
        bagDef = bagDef[:i]
        i = bagDef.find(' ')
        amount = bagDef[:i]
        if amount == 'no':
            continue
        bagtype = bagDef[i:]
        value.append((int(amount),bagtype.strip()))
    return {key: value}

def canContain(bag1,bag2,n=0):
    global rules
    spacer = '  '*n
    print(spacer,bag1+':')
    if bag1 == bag2:
        print(spacer,bag1, 'is', bag2)
        return 1
    bagrules = rules[bag1]
    if bagrules == []:
        print(spacer,bag1, 'can contain no bags')
        return 0
    returnvalue = 0
    for rule in bagrules:
        print(spacer,bag1,'can contain',bag2)
        returnvalue += rule[0] * canContain(rule[1],bag2,n+1)
    return returnvalue

def contains(bag1,n=0,noOutput=False):
    global rules
    bagrules = rules[bag1]
    if bagrules == []:
        return 1
    if n > 0:
        returnvalue = 1
    else:
        returnvalue = 0
    for rule in bagrules:
        returnvalue += rule[0] * contains(rule[1],n+1)
    return returnvalue


def main():
    global rules
    input = "eta.txt"
    lines = open("../../input/"+input,"r").readlines()
    for line in lines:
        rarr = rule2array(line)
        rules = {**rules, **rarr}
    print(rules)
    i = contains('shiny gold')
    print(i)
#    containers = []
#    for bag in rules.keys():
#        if canContain(bag,'shiny gold') > 0:
#            containers.append(bag)
#    containers.remove('shiny gold')
#    print(len(containers))


main()