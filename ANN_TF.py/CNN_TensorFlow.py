
input1=float(input("Please give input1 which need to be numeric: "))
input2 =float(input("please give second input value which is numeric: "))

print("first input is: ", input1)
print("second input is : ", input2)

operator_input=input("please provide the kind of operation you want to perform:  add, -:for subtract, *: for multiply, / :for divide)")

result=input1+input2


if(operator_input=="+"): 
    result=input1+input2
    print("result: ",result)
elif(operator_input=="-"):
    esult=input1-input2
    print("result: ",result )
elif(operator_input=="*"):
     result=input1*input2
     print("result: ",result)
elif(operator_input=="/"):
     result=input1/input2
     print("result: ",result)
else:
     print("you have given an invalid operator")