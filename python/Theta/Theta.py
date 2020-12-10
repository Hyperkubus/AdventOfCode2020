global acc
global pnt
global lines
global visited_lines

def debug(instruction,value,n=0):
    print('['+instruction+']('+str(value)+') ACC:',acc,'PNT',pnt,'N',n)

def process(n=0):
    global acc
    global pnt
    global lines
    global visited_lines
    if pnt in visited_lines:
        debug('TERMINATE','INF_LOOP',n)
        return (False)
    visited_lines.append(pnt)
    instruction = lines[pnt]
    instruction = instruction.split(' ')
    value = int(instruction[1].strip())
    instruction = instruction[0].strip()
    #debug(instruction,value)
    if instruction == 'acc':
        acc += value
        pnt += 1
    elif instruction == 'jmp':
        pnt += value
    elif instruction == 'nop':
        pnt += 1
    return True

def newLines(myLines, n=0):
    value = myLines.copy()
    inst = value[n]
    if inst[:3] == 'jmp':
        inst = inst.replace('jmp', 'nop')
    elif inst[:3] == 'nop':
        inst = inst.replace('nop', 'jmp')
    value[n] = inst
    return value



def main():
    global acc
    global pnt
    global lines
    global visited_lines
    acc = 0
    pnt = 0
    input = "theta.txt"
    myLines = open("../../input/"+input,"r").readlines()
    n = 0
    print(len(myLines))
    while n < len(myLines):
        lines = newLines(myLines, n)
        visited_lines = []
        acc = 0
        pnt = 0
        print('processing')
        while pnt < len(lines):
            if not process(n):
                break
        n += 1
        if pnt >= len(lines):
            debug('TERMINATE', 'DONE',n)
            return


main()