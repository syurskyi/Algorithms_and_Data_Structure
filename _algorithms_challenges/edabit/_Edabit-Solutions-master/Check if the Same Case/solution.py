def same_case(txt):
    if txt.islower() or txt.isupper() == True:
        return True
    else:
        return False



def test():
    print("Test has started")
    if same_case("mArmALadE") != False:
        print("error1")
    if same_case("MARMALADE") != True:
        print("error2")
