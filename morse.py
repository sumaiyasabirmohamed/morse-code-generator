#!/usr/bin/python

#...........................................................................
# Author:  Sumaiya Sabir Mohamed
# Github:  https://github.com/sumaiyasabirmohamed
#...........................................................................

# Creating the Dictionary data types for English alphabets, numerals, and
# some specialcharacters with their corresponding Morse code
# (https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf)

Morse_Codes = {"a":".-",
               "b":"-...",
               "c":"-.-.",
               "d":"-..",
               "e":".",
               "f":"..-.",
               "g":"--.",
               "h":"....",
               "i":"..",
               "j":".---",
               "k":"-.-",
               "l":".-..",
               "m":"--",
               "n":"-.",
               "o":"---",
               "p":".--.",
               "q":"--.-",
               "r":".-.",
               "s":"...",
               "t":"-",
               "u":"..-",
               "v":"...-",
               "w":".--",
               "x":"-..-",
               "y":"-.--",
               "z":"--..",
               "?":"..--..",
               "!":"-.-.--",
               ".":".-.-.-",
               ",":"--..--",
               ";":"-.-.-.",
               ":":"---...",
               "+":".-.-.",
               "-":"-....-",
               "/":"-..-.",
               "=":"-...-",
               "@":".--.-.",
               "(":"-.--.",
               ")":"-.--.-",
               "'":".----.",
               "1":".----",
               "2":"..---",
               "3":"...--",
               "4":"....-",
               "5":".....",
               "6":"-....",
               "7":"--...",
               "8":"---..",
               "9":"----.",
               "0":"-----",
               " ":"......."}

def Morse_Code_Converter (Sentence):
    """
    This function convert the English sentence to Morse Code.
    Creating the empty String
    Check whether the character is present in the created dictionary 
    Every single character is concatenated to form a string
    Each character is separated with space, 
    The Untranslatable characters (error) are represented by eight dots(.........)
        
    Input:
     1. String              -             Generates Morse Code
      
    """
    Converted_Sentence = ''
    for Character in Sentence:
        if Character in Morse_Codes:
            Converted_Sentence += Morse_Codes[Character] + (' ')
        else:
            Converted_Sentence += ('........') + (' ')
    return Converted_Sentence 

# Parsing the Sentence from the user to print the Morse Code 
print ("Morse Code: ", Morse_Code_Converter (input("Enter the text: ").lower()))