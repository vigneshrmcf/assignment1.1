def reverse(x):
  str = ""
  for i in x:
    str = i + str
  return str
  
x ="1234abcd"
  
print ("The Expected Output is : ", (reverse(x)))
