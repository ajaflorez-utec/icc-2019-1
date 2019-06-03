#operaciones matematicas basicas
oper = input()
op1 = int(input())
op2 = int(input())

if oper == "+":
    print(op1 + op2)
elif oper == "-":
    print(op1 - op2)
elif oper == "*":
    print(op1 * op2)
elif oper == "/":
    print(op1 // op2)
else:
    print("Operador invalido")
    