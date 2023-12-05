import os #This program reads and downloads the programs you need to obtain in order to download a package
from upload import uploadfile, getintake
from info import file, filefun, killdir
list1 = []
list2 = []
t = ()
#var1 = file[0]
def clearbs():
    k = ''.join(t)
    c = k.split("Package")
    k = ''.join(c)
    c = k.split("is")
    k = ''.join(c)
    c = k.split('not')
    k = ''.join(c)
    c = k.split('installed')
    k = ''.join(c)
    c = k.split('.')
    k = ''.join(c)
    c = k.split('\n') #makes the txt file into a list of packages to get
def myfunc(e):
    return len(e)
def download():
    var1 = list1[0]
    os.system('apt-get -d download '+var1)
    list1.pop()
def attempt(): #basically the whole program
    #var1 = list1[0]
    #download()
    #os.system('Python3 info.py')
    #f = open("file.txt", 'a')
    #temp = ''.join(var1)
    #f.write(temp)
    uploadfile()
    #os.system('Python3 info.py')
    #list1.pop()
def popping(): #removes fluff from txt file
    t.pop(0)
    t.pop(0)
    t.pop(0)
    t.pop(-1)
    t.pop(-1)
    t.pop(-1)
    t.pop(-1)
    t.pop(-1)
def popping2(): #also removes fluff from txt file
    del t[0::2] 
getintake()
f = open('intake.txt', 'r')
for x in f:
    t = f.readlines()
f.close()
popping()
popping2()
k = ''.join(t)
c = k.split("Package")
k = ''.join(c)
c = k.split("is")
k = ''.join(c)
c = k.split('not')
k = ''.join(c)
c = k.split('installed')
k = ''.join(c)
c = k.split('.')
k = ''.join(c)
c = k.split('\n') #makes the txt file into a list of packages to get
#print(k)
#print(c)
k = ' '.join(c)
#c = k.split('\t')
#print(c)
#k = ' '.join(c)
#print(k)
#k.split(' ')
list1.append(k)
f = open("dump.txt" , "w")
f.write(k) #this saves the packages you got to a file
#var1 = ''.join(list1[0])
#print(list1)
#for item in os.listdir():
#    list1.append(item)
download()
filefun()
killdir()
print(file)
list2 = list(file)
for i in list2:
    attempt()
print('Finished!')
