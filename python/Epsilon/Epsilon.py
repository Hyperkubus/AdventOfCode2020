def code2id(code,verbose=False):
    if not isinstance(verbose, int):
        if not verbose: verbose = 0
        if verbose: verbose = 1
    min = 0
    max = 127
    step = 64
    for n in code[:7]:
        if n == 'F':
            max -= int(step)
            step /= 2
        else:
            min += int(step)
            step /= 2
        if verbose > 1: print(min, max)
    if min == max:
        row = min
    else:
        exit("ERROR code DOES NOT COMPUTE!")
    min = 0
    max = 7
    step = 4
    for n in code[7:]:
        if n == 'L':
            max -= int(step)
            step /= 2
        else:
            min += int(step)
            step /= 2
        if verbose > 1: print(min, max)
    if min == max:
        seat = min
    else:
        exit("ERROR code DOES NOT COMPUTE!")
    id = row*8+seat
    if verbose > 0: print("Row:", row, "Seat:", seat, "ID:", id)

    return id


def main():
    input = "Epsilon.txt"
    lines = open("../../input/"+input,"r").readlines()
    ids = list(range(0,1023))
    for line in lines:
        ids.remove(code2id(line))
    for k,v in enumerate(ids):
        if v+1 != ids[k+1]:
            print("Your seat is:",ids[k+1])
            break

main()