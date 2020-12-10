
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
    input = "beta.txt"
    lines = open("../../input/"+input,"r").readlines()
    validEntries = 0
    for entry in lines:
        if isValidNew(entry):
            validEntries += 1
            print('valid')
    print(validEntries)

main()

#452 >
