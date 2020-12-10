
def validate(lines,i,scanrange):
    if i < scanrange:
        return True
    for j in range(i-scanrange, i-1):
        search = lines[i] - lines[j]
        if search in lines[j:i]:
            return True
    return False

def main():
    input = "iota.txt"
    lines = open("../../input/"+input,"r").readlines()
    scanrange = 25
    n = 0
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    for i in range(len(lines)):
        if not validate(lines,i,scanrange):
            n = lines[i]
            break
    for i in range(len(lines)):
        for j in range(i,len(lines)):
            if sum(lines[i:j]) == n:
                print(lines[i:j])
                print(min(lines[i:j])+max(lines[i:j]))
                exit(2)
            if sum(lines[i:j]) > n:
                break



main()