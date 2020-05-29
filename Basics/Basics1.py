#Functions Basics

def star() : 
    for h in range(10) : 
        print ('**')

star()
#------------------------------------------
def star() : 
    for h in range(10) : 
        print ('**')

s=star
s()
#------------------------------------------
def find_avg(a,b):
        average = (a+b)/2
        print ("average is ",average)
find_avg(2,3)

# Functions Scope
xx = 5
def gg() : 
    xx = 14
gg()
print (xx)
#------------------------------------------
xx = 5

def gg() : 
    global xx
    xx = 14
 gg()
print (xx)

#List Basics
list remove
y.remove("b")

#------------------------------------------------

list sort
sorted(y)
y.sort()
sorted(y,reverse = True)

#------------------------------------------------

list sort lambda
sorted(y, key=lambda e: e[1])
sorted(y,reverse = True, key=lambda e: e[3])

student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
a = sorted(student_tuples, key=lambda student: student[2])
