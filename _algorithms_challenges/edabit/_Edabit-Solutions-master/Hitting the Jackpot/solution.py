def test_jackpot(result):
    if len(set(result)) == 1:
        return True
    else:
        return False

def test():
    print("test has started")
    if test_jackpot(['@', '@', '@', '@']) != True:
        print("error1")
    if test_jackpot(['SS', 'SS', 'SS', 'Ss']) != False:
        print("error2")
