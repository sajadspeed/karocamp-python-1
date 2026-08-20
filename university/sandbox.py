"""
myfile = open("./myfile.txt") 

print( myfile.read() )

myfile.close()
"""

mystring = r"admin\n"

mystring = mystring.replace(r"\n", "")

print(mystring)