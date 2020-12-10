
def isValid(entry):
    policy = entry.split(':')
    password = policy[1]
    policy = policy[0].split(' ')
    character = policy[1]
    occurences = policy[0].split('-')
    count = password.count(character)
    if count < int(occurences[0]):
        return False
    if count > int(occurences[1]):
        return False
    return True

def isValidNew(entry):
    policy = entry.split(':')
    password = policy[1]
    policy = policy[0].split(' ')
    character = policy[1]
    position = policy[0].split('-')
    print(entry,password[int(position[0])],password[int(position[1])])
    if password[int(position[0])] == character:
        if password[int(position[1])] == character:
            return False
        return True
    if password[int(position[1])] == character:
        return True
    return False


def main():
    input = "gamma.txt"
    lines = open("../../input/"+input,"r").readlines()
    steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    treetimes = 1
    for step in steps:
        x = 0
        x_step = step[0]
        y_step = step[1]
        trees = 0
        skiplines = 0
        for entry in lines:
            entry = entry[:-1]
            if skiplines > 0:
                print(entry)
                skiplines -= 1
                continue
            index = x%(len(entry))
            if entry[index] == '#':
                entry = entry[:index] + 'X' + entry[index + 1:]
                trees += 1
                print(entry)
            else:
                entry = entry[:index] + 'O' + entry[index + 1:]
                print(entry)
            skiplines = y_step - 1
            x += x_step
        treetimes *= trees
    print(treetimes)
main()

#452 >
