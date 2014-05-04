from brain import robot
r = robot()
def main():
    while(1):
        a=raw_input("> ")
        if a=="shell":
            shell()
        else:
            print r.think(a);

def shell():
    while(1):
        a=raw_input("# ")
        if a=="q":
            return
        r.console(a);
        

if __name__ == "__main__":
    main()
