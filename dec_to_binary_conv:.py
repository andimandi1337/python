class dec_to_binary_conv:
    input_dec = int(input("Enter the number you would like to convert to binary: \n"))
    output = int
    check = bool
    
    def input_check(input_dec, check):  #Check input to be below 1024 so binary can only have 10 digits
        while input_dec > 1024:
            return check == False
        else: 
            return check == True
    
    def 