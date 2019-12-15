def buildConnectionString(params):
    """Build a connection string from dictionary of parameters.

    Returns string."""
    return  ";".join(["%s=%s" %(k,v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrim",\
    "database":"master",\
    "uid":"sa",\
    "pwd":"secret"\
    }
    print buildConnectionString(myParams)
    print buildConnectionString.__doc__
