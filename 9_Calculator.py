#simple calculator
a=10
b=0
operator="/"
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    if b!=0:
      print(a/b)
    else:
        print("cannot divisible")
elif operator=="%":
    print(a%b)
