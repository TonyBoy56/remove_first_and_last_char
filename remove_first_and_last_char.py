# Instructions:
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters.

my_string = "eloquent"

def remove_char(s):
    if len(s) < 2:
        print("Error: Cannot process string less than 2 characters in length.")
    else:
        new_string = s[1:-1]
            
        print(new_string)
    
remove_char(my_string)
