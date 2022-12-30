
input_string = input("Enter the String you would like to convert to morse code: \n").upper()
char_array=[*input_string]
print(char_array)
def conversion(input_string):
        dict = {
            "A":	".-",
            "B":	"-...",
            "C":	"-.-.",
            "D":	"-..",
            "E":	".",
            "F":	"..-.",
            "G":	"--.",
            "H":	"....",
            "I":	"..",
            "J":	".---",
            "K":	"-.-",
            "L":	".-..",
            "M":	"--",
            "N":	"-.",
            "O":	"---",
            "P":	".--.",
            "Q":	"--.-",
            "R":	".-.",
            "S":	"...",
            "T":	"-",
            "U":	"..-",
            "V":	"...-",
            "W":	".--",
            "X":	"-..-",
            "Y":	"-.--",
            "Z":	"--..",
            "1":	".----",
            "2":	"..---",
            "3":	"...--",
            "4":	"....-",
            "5":	".....",
            "6":	"-....",
            "7":	"--...",
            "8":	"---..",
            "9":	"----.",
            "0":	"-----",
            ",":	"--..--",
            "?":	"..--..",
            ":":	"---...",
            "&":	".-...",
        }
        return dict.get(input_string, "Not a valid char :(")

result = ""
for i in range(1, len(char_array)):
    result = result + conversion(char_array[i-1])
print(result)