new=open('file.txt','r')

value=new.read(100)
# read 0->10
value2=new.read(100)
#read 10->20
print(value)
print(value2)
with open('file.txt','r')as new:
    print(new.closed)
    
    print(new.name)
    print(new.mode) # read or write
    print(new)
    pass

      

value=new.readline()
print(value)


new.seek(0)
# to return the cursor so that it can print againt or read again

value2=new.readline()
print(value2)

print(new.tell())
#tell coursor current position 17..


test=open('my.txt','w')

with open('my.txt','w') as test:
    test.write("TEST")
    test.seek(0)
    test.write("b")
    
image
with open('file/image.jpg','rb'):
    with(....write)
    import os
    
os.walk
