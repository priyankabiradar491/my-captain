# Take file from user and print it's extension
print

filename = input("Input the Filename: ")

f_extns = filename.split(".")

print ("The extension of the file is : " + (f_extns[-1]))
