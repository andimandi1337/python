import math

pi = math.pi
input = float(input("Enter the value you would like to convert: "))
class Angular_to_Degrees:
    
    def Conversion(input):
        result = input*180
        return result
    
print(Angular_to_Degrees.Conversion(input), "is your entered value (", input, "pi) converted to degrees.")