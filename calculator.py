def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2
    
def mul(n1,n2):
    return n1*n2
    
def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def perform_cal():
    n1=int(input("Enter the first number :"))
    for symbol  in operations:
        print(symbol)
    op=input("pick an operation:")
    n2=int(input("enter the second number :"))

    result = operations[op](n1,n2)
    print(result)
    calculate=True
    while calculate:
        choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ")
        if choice=='y':
            for symbol  in operations:
                print(symbol)
            op=input("pick an operation:")
            n2=int(input("What's the next number: "))
            result=print(operations[op](result,n2))
        else:
            perform_cal()

perform_cal()