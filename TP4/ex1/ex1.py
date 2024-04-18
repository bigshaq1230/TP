ch = """Good morning
This is a write test in a file.
Python is a popular language for software development.
Like JavaScript or C++, Python is unquestionably regarded as one of the best programminglanguages.
Python's concise and clear syntax makes code easier to read and debug, which increases
productivity and speed."""

f = open("test.txt","w")
f.write(ch)
f.close()


f = open("test.txt","r")
ch1 = f.read()
f.close()



f = open("test.txt","r")
ch2= f.read(3)

ch3 = f.readline()
f.close()
f = open("test.txt","r")
ch4 = f.readlines()


f.close()

for i in ch4:
    print(i)

print("the number of times the Python appeared: ",ch1.count("Python"))

f = open("new.txt","w")

f.write(ch)
f.close()