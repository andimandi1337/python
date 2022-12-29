class dec_to_binary_conv:
    input_dec = int(input("Enter the number you would like to convert to binary: \n"))
    output = []
    stored = int
    check = bool
    def input_check(input_dec, check):  #Check input to be below 1024 so binary can only have 10 digits
        if input_dec >= 1024:
            check = False
            return check
        elif input_dec < 1024:
            check = True
            return check
    check = input_check(input_dec, check)

    def calculation(input_dec, check, output,stored):
        while check == True:
            for i in range(0, 10):
                divisor = (2**(9-i))
                stored=input_dec//divisor
                input_dec = input_dec - stored * divisor
                output.append(stored)
            return output
        else: return "Number is too high!"
    print(calculation(input_dec, check, output, stored))