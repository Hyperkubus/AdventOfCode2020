

def main():
    input = "alpha.txt"
    lines = open("../../input/"+input,"r").readlines()
    for a in lines:
        diff = 2020 - int(a);
        print("Value is",a,"looking for",diff)
        for b in lines:
            diff2 = diff - int(b);
            for c in lines:
                if (diff2 == int(c)):
                    print(int(c) * int(b) * int(a))
                    return

main()