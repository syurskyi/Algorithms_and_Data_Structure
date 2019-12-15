import odbchelper
params = { "server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print odbchelper.buildConnectionString(params)

print odbchelper.buildConnectionString.__doc__

# Traceback (most recent call last):
#   File "ex2.py", line 1, in <module>
#     import odbchelper
# ImportError: No module named odbchelper
