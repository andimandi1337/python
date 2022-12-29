class dec_to_binary_conv:
    input_dec = int(input("Enter the number you would like to convert to binary: \n"))
    output = int
    stored = int
    check = bool
    def input_check(input_dec, check):  #Check input to be below 1024 so binary can only have 10 digits
        if input_dec > 1024:
            return check
        elif input_dec <= 1024:
            return check
    check = input_check(input_dec, check)

    def calculation(input_dec, check, output,stored):
        while check == True:
            for i in range(9, 0):
                stored=input_dec%(2**i)
                output = output + stored
            return output
    print(output)