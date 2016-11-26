from random import randint

def foo(list):
	while True:
		int = randint(min(list), max(list))
		if int in list and int % 2 == 0:
			return int

x = input("Enter string value: ")
y = int(input("Enter integer value for y: "))
z = int(input("Enter integer value for z: "))

mylist = []

x = x.strip()
x = x.split(",")
for i in range(len(x)):
	x[i] = int(x[i])

for rowx in range(y):
	newrow = []
	for columny in range(z):
		newrow.append(foo(x))
	mylist.append(newrow)
print(mylist)