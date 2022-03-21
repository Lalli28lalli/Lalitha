import re
s=input("enter a string")
x=re.findall(r'\b\w{5}\b',s)
print(x)
