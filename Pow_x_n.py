# LC - 50 

# Overflow conditions check

# Approaches :
        # - Recursive Approach 
        # - Simple Maths - ( Binary Exponentiation )
    
        # 
      
        # If n is negative , check and make x as 1/x as we know the what negative power does
        # also make n positive for easy calculation
        if n < 0 :
            
            x = 1/x
            n = -n
        
        # ANS is a variable to save the value
        ans = 1
        
        # TRICK PART : now if we multiply a number twice the power doubles right ?!! ... so here what we
        # will do is , we will  multiply the x as many times possible and brake the power to half every time 
        # until we reach to an end point of 1 , or 0. BUT BEFORE ALL THAT , if the power is ODD then it cannot be broken into
        # half , so if it is half then just remove x^1 from it to make it even and then multiply at last , that what we are doing here
        # in the  IF part.
        while n :
            
            if n % 2 == 1 :
                
                ans = ans * x
                n -= 1
            
            else:
                
                x = x*x
                n = n/2
        
        return ans
                
