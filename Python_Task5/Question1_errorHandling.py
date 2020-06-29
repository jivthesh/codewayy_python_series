try :  
    a = 3
    if a < 4 : 

# throws ZeroDivisionError for a = 3  
        b = a/(a-3)
    
# throws NameError if a >= 4 
    raise NameError ("b is not a proper variable name")
  
# throws exceptions 
except(ZeroDivisionError, NameError): 
    print("\nError Occurred and Handled")

    
    raise # To determine whether the exception was raised or not 

finally:
    print("This is always executed")
