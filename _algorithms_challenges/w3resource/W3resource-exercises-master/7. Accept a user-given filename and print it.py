#In this program, the extension of a filename will be separated to find the correct extension
filename = input("Enter the filename : ")
filename_extension = filename.split(".")
print("The filename extension is : " + repr(filename_extension[-1]))