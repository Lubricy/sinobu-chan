from brain import robot
import utils.io as io
r = robot()
def main():
    while(1):
        a=raw_input("> ")
        if a=="shell":
            shell()
        else:
            print r.think(a);

def shell():
    io.warning("shell mode")
    while(1):
        a=raw_input("# ")
        if a=="q":
            return
        r.console(a);
        

if __name__ == "__main__":
    main()
