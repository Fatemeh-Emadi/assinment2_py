import math
from colorama import Fore,init

print(Fore.BLUE+"*****Python Calculator*****")

print(Fore.YELLOW+"Operators: 1.+  2.- 3.* 4./ 5.^")
number1=int(input("Enter Number1:"))
number2=int(input("Enter Number2:"))

operators=["+","-","*","/","^","sin","cos","tan","cot"]

result=0
op1=input(Fore.RED+"Choose Operator:")

if(op1==operators[0]):
   result=number1+number2
   print(Fore.GREEN,"RESULT:",result)
   
elif(op1==operators[1]):
   result=number1-number2
   print(Fore.GREEN,"RESULT:",result)
   
elif(op1==operators[2]):
   result=number1*number2
   print(Fore.GREEN,"RESULT:",result)
   
elif(op1==operators[3]):
   result=number1/number2
   print(Fore.GREEN,"RESULT:",result)

elif(op1==operators[4]):
   result=number1**number2
   print(Fore.GREEN,"RESULT:",result)
       
print(Fore.YELLOW+"Operators:  1.sin 2.cos 3.tan 4.cot")

op2=input(Fore.RED+"Choose Operator:")
deg=int(input("Enter Degree:"))

if(op2==operators[5]):
   result=math.sin(deg)
   print(Fore.GREEN,"RESULT:",result)

elif(op2==operators[6]):
   result=math.cos(deg)
   print(Fore.GREEN,"RESULT:",result)
   
elif(op2==operators[7]):
   result=math.tan(deg)
   print(Fore.GREEN,"RESULT:",result)

elif(op2==operators[8]):
   result=math.cot(deg)
   print(Fore.GREEN,"RESULT:",result)
   

