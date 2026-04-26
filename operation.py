def operation(*args,**kwargs):
    for _,op in kwargs.items():
        match op:
            case "+":
                res=0
                for i in args:
                    res+=i
                print("addition is:",res)
            case "-":
                sub=args[0]
                for i in args[1:]:
                    sub-=i
                print("subtraction is:",sub)
            case "*":
                multi=1
                for i in args:
                    multi*=i
                print("multiplication is:",multi)
            case "/":
                div=args[0]
                for i in args[1:]:
                    if i==0:
                        print("division by zero not possible.")
                        return
                    div/=i
                print("division is:",div)    
            case"**":
                power=args[0]
                for i in args[1:]:
                    power**=i
                print("power is:",power)
            case "%":
                mod=args[0]
                for i in args[1:]:
                    if i==0:
                        print("modulo by zero not possible.")
                        return
                    mod%=i
                print("modulus is:",mod)

operation(1,2,3,4,op1="+",op2="-",op3="*",op4="/")
operation(1,0,3,op1="/",op2="*",op3="**",op4="%")
