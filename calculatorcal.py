def add():
    a = float(input ("Enter your first number : "))
    b = float(input ("Enter your second number : "))
    sum = a + b
    print ("The answer is" , sum)
def sub():
    a = float(input ("Enter your first to subtract : "))
    b = float(input ("Enter your second number to subtract : "))
    sum = a - b
    print ("The answer is" , sum)
def mul():
    a = float(input ("Enter your first number to multiply : "))
    b = float(input ("Enter your second number to multiply : "))
    sum = a * b
    print ("The answer is" , sum)
def div():
    a = float(input ("Enter the dividend : "))
    b = float(input ("Enter the divisor : "))
    sum = a / b
    print ("The answer is" , sum)

sel = input ("Enter the operator (+,-,*,/ ) : ")
if sel == "+":
    add()
elif sel == "-":
    sub()
elif sel == "*":
    mul()
elif sel == "/":
    div()
else:
    print ("Invalid symbol or code")
    