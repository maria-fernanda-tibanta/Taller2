import turtle
t=turtle.Pen()
print("\tESTRELLA ")
a=int(input("Ingrese un numero : "))

if a%2==0:
    b=180/a
    c=b*10
    for i in range (a):
        t.forward(100)
        t.right(c)

else:
    b=180/a
    c=180-b
    for i in range (a):
        t.forward(100)
        t.right(c)
