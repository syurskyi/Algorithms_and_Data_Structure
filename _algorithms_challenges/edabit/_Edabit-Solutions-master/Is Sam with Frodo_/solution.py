def middle_earth(lst):
    f = lst.index("Frodo")
    s = lst.index("Sam")
    if f - s == 1 or f - s == -1:
        return True
    else:
        return False
	
