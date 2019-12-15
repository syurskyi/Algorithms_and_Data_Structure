# Read From File

# r read only, w write only
with open("writetofile.txt", "r") as open_file:
    print(open_file.read())
