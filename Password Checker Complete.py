# Write a function called password_checker that takes an input string, which is your password, 
# and returns a boolean True if the password meets the following requirements and False otherwise.

# 1. Password must be at least 14 characters in length
# 2. Password must contain at least one character from each of the four character sets defined below, and no other characters.
# 3. Passwords cannot contain more than three consecutive characters from the same character set as defined below.

# Character sets:
# Uppercase characters (string.ascii_uppercase)
# Lowercase characters (string.ascii_lowercase)
# Numerical digits (string.digits)
# Special characters (string.punctuation)

import string

def password_checker(passwd):
    if len(passwd) < 14:
        return False 
    upper = 0 # use these to see if found
    lower = 0
    digits = 0
    punctuation = 0
    upperrun = 0 # use these to count consecutive
    lowerrun = 0
    digitsrun = 0
    punctuationrun = 0
    for chr in passwd:
        if chr in string.ascii_uppercase:
            upper = 1 # I found an uppercase character
            upperrun += 1 # counting runs of Uppercase
            lowerrun = 0 # resetting other runs back to 0 
            digitsrun = 0
            punctuationrun = 0
        elif chr in string.ascii_lowercase:
            lower = 1
            lowerrun += 1
            upperrun = 0
            digitsrun = 0
            punctuationrun = 0
        elif chr in string.punctuation:
            punctuation = 1
            punctuationrun += 1
            upperrun = 0 
            lowerrun = 0
            digitsrun = 0
        elif chr in string.digits:
            digits = 1
            digitsrun += 1
            upperrun = 0
            lowerrun = 0
            punctuationrun = 0
        else:
            print("weird character found")
            return False # invalid character entered

        if upperrun == 4: # check to make sure I don't have too many characters in each category
            return False
        if lowerrun == 4:
            return False
        if digitsrun == 4:
            return False
        if punctuationrun == 4:
            return False  
    
    if upper != 1: # check to make sure that the character type was found.
        return False
    if lower != 1:
        return False
    if digits != 1:
        return False
    if punctuation != 1:
        return False

    return True
        
        # verify if character is uppercase
    # run through each character in passwd
        # check for uppercase, lowercase, number, and special
            # if not upper, lower, number, or special return false
        # count number, upper, lower, and special in passwd
    # return true            
    

if __name__ == "__main__":
    password_checker("AAAAAA")




    print(password_checker("abcABC123!@#abcABC123!@#") == True) # This is a good password
    print(password_checker("abcdefgABCDEFG1234567!@#$%^&") == False) # This is invalid because the runs of the same character set are too long
    print(password_checker("abcABC123abcABC123") == False) # This is invalid because there are no characters from string.punctuation
    print(password_checker("aaBB11@@") == False) # This is invalid because it is too short`