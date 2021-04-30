name = "ahmed mahmoud mohamed farag"
age = 24
mymoney = 500134014

#formating the old way 
print("my name is : %s \nand my age is : %d \nand my balance is : %.2f" %(name,age,mymoney))

#formating the new way 
print("my name is : {:s} \nand my age is : {:d} \nand my balance is : {:.2f}" .format(name,age,mymoney))

#formating for version 3.6 + 

print(f"my name is : {name} \nand my age is : {age} \nand my balance is : {mymoney}")

