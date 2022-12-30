input_string = input("Enter the String you want to count the vowels in: \n")
char_array = [*input_string]
print(char_array)
  

def counting(char_array):
        vowel_count = 0
        for i in range(1, len(char_array)): 
            if char_array[i] == "a":
                vowel_count+=1
            elif char_array[i] == "e":
                vowel_count+=1
            elif char_array[i] == 'i':
                vowel_count+=1
            elif char_array[i] == "o":
                vowel_count+=1
            elif char_array[i] == "u":
                vowel_count+=1
            else: vowel_count = vowel_count
        return vowel_count
print(counting(char_array))