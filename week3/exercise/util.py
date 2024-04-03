
# notice the differences between the general and the specific cases


def printGeneral(line:str)->None:
    print(line)


def printSoftEng(debugMsg:str,*vars):
    print(debugMsg)

    for var in vars:
        print(f"{var.__name__} is {var}")


def printUser(Msg:str,file:str):
    File = open(file,'w')
    File.write(Msg)
    File.close()

