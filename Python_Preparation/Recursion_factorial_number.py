# Find the factorial of the number 

def Factorial_num(n):
  
  
  # This is the BASE Condition Recursion calling stops once condition is met ... 
  # To avoid overloading of Stack memory, make sure to sure the function that works towards the base condtion to cease or Infinite loop !
  
  if(n==1):
  	return(n)
  
  # Below is the recursion calling n * Factorial_num(n-1)
  # (n-1) is the factor in that equation which decreases to meet the if equation to cease !

  return n * Factorial_num(n-1)

  # NOTE: Recursion can be used without return and store the value in the variable like Result and print it... not necessarily , it has to be on the return statement
	
	

# n is the user input
n = 9
#function calling and prints the data to the screen 
print(printFun(n))
