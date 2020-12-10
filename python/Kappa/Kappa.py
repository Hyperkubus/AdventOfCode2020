global gconnections

def getConnections(i, adapters,n=0):
    global gconnections
    if i in gconnections.keys():
        return gconnections[i]
    print(" "*n, i)
    connections = 0
    if i+1 in adapters:
        print(" "*n, "i+1:",i+1)
        connections += getConnections(i+1,adapters,n+1)
    if i+2 in adapters:
        print(" "*n, "i+2:", i + 2)
        connections += getConnections(i+2,adapters,n+1)
    if i+3 in adapters:
        print(" "*n, "i+3:", i + 3)
        connections += getConnections(i+3,adapters,n+1)
    gconnections[i] = connections
    return connections

def main():
    global gconnections
    gconnections = {}
    #reading and fixing vartypes
    input = "kappa.txt"
    lines = open("../../input/"+input,"r").readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    lines.append(0)
    lines = sorted(lines)
    lines.append(lines[-1]+3)
    lines = set(lines)
    gconnections[max(lines)] = 1
    print(lines)
    #collecting jumps
    #jolts = []
    #for i in range(len(lines)-1):
    #    jolts.append(lines[i+1]-lines[i])
    #count one and three jolt jumps
    print(getConnections(0,lines))
    return

main()