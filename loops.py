x = int(input("PLease enter a number for factorial calculation\n"))
fact = x
def fact_num(num,fact):
    if(num>1):
        temp_num3 = num-1
        fact = fact*temp_num3 
        fact_num(temp_num3,fact)  
        
        return 0
    else:
        print(fact)
        return 0
    
fact_num(x,fact)
