x=input("Enter string:")
lower_case,upper_case = 0,0
for i in x:
    if (i>='a'and i<='z'):

        lower_case=lower_case+1   
                      
    if (i>='A'and i<='Z'):  

        upper_case=upper_case+1   
          
print('Lower case characters: ',lower_case)
print('Upper case characters: ',upper_case)