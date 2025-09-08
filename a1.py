"""
My text isn’t impactful enough. In some applications, they allow for text editing, 
such as increasing its size. However, my problem lies where there is no such option. 
My solution? ASCII art. By utilizing ASCII art, I can make my text size grow to however 
large I would like it to be. For my purposes, having a 3x3 character size should suffice. 
But I don’t want to make ASCII art for every character and then have to copy and paste 
them whenever I want a word or sentence to be larger than usual. So what this program 
will do is automate the conversion process of normal-sized characters to my custom-made 
3x3 ASCII characters. It would do so by reading a prepared file that contains custom 
characters from “!” to “z” in order of their unicode values. The program will read the 
file line by line to extract and encode each character into an array. Then it will read 
another file, this time the input file, and convert the normal-sized characters into 
larger characters by iterating through every line and character in said lines. Lastly, 
it will write into an output file the newly converted word(s), keeping its original 
formatting.
"""

# This function is used to easily get a readable file and handles any IO errors and Value errors that may occur
# arg: filename - String
def ofile(filename, arg):
    try:
        return open(filename, arg)
    except IOError:
        # Raise an error if an IOError occurs
        raise IOError(filename + " NOT FOUND. PROGRAM HAS STOPPED")
    finally:
        if type(filename) != str or type(arg) != str:
            # Raise a ValueError if the filename or arg is not a string
            raise ValueError("PLEASE CHECK THAT THE FILE NAME IS A STRING AND THE ARGUEMENT IS \"r\" OR \"w\". PROGRAM HAS STOPPED")
        
# This function returns a "Letter" which is tuple of the top, middle, and bottom parts of a specified 3x3 letter in that order
# arg: letter - String (specifically of length 1)
# return: a tuple that consists of the top, middle, and bottom parts of the letter converted to 3x3
def getLetter(letter):
    # Get the unicode value of the letter and subtract the unicode value of "!"
    order = ord(letter) - ord('!') # This will be used as the index for the array "alphas"
    
    # Check if order is in range of the range of alphas
    if order >= 0 and order < len(alphas): 
        ls = alphas[order].split(SPLITTER) # If true: Take the string at index "order" and split it
    else:
        ls = alphas[-1].split(SPLITTER) # If false: Take the string at index -1 (white space) and split it
    
    return (ls[0], ls[1], ls[2]) # Return the list as a tuple

# This function makes a "Sentence" which is a list of tuples derived from a string
# arg: string - String
# return: list of tuples or "Letters"
def makeSentence(string):
    # "Fix" the string before conversion (this gets rid of any character not in the ASCII art database)
    fixedStr = "".join(x.upper() for x in string if x.isalnum() or x == " " or x in "!\"#$%&'()*+,-./:;<=>?@")
    sentence = []
    
    # Iterate through the fixed string
    for i in fixedStr:
        # Append tuples to the list by calling getLetter()
        sentence.append(getLetter(i))
    
    return sentence # return our list of tuples
    
# This function prints out the large text line by line
# arg: string - String, the string to be printed
def bigPrint(string):
    # Split our string into lines
    lines = string.split("\n")
    
    # Iterate through the lines
    for i in lines:
        # Get a list of tuples containing the parts of our ASCII characters
        sentence = makeSentence(i)
        
        # Print each line of the character one by one
        count = 0
        while count < 3:
            line = ''
            for char in sentence: # Interate through the list "sentence"
                line += char[count] # Add the line of ASCII character parts to a string
            print(line) # Print out the line of ASCII character parts
            count += 1 # Go to next line
            
# This function writes the large text into a text file for easy copy and pasting
# arg: string - String, the string to be written
def bigOut(string):
    # Split our string into lines
    lines = string.split("\n")
    output = "" # This variable will be return later
    
    # Iterate through the lines
    for i in lines:
        # Get a list of tuples containing the parts of our ASCII characters
        sentence = makeSentence(i)
        
        # Print each line of the character one by one
        count = 0
        while count < 3:
            line = ''
            for char in sentence: # Interate through the list "sentence"
                line += char[count] # Add the line of ASCII character parts to a string
            output += line + "\n" # Add the line to a string and add a next line
            count += 1 # Go to next line
            
    # Write the entire output string into the output file
    outputFile.write("```\n" + output + "```")
    
# END OF FUNCTION DEFINING -----------------------------------------------    
    
# File set up (open data streams)
textFile = ofile('a1input.txt', "r")
tft = textFile.read()
outputFile = ofile("a1output.txt", "w")
alphaFile = ofile('alpha.txt', "r")

# Set up the "alphas" list which holds all the 3x3 letters, numbers, and some characters in a specific format
alphas = [""] * 58
SPLITTER = "#" # .split Constant (should NOT be a character used in the 3x3 ascii art) 
# Extract and format data from the "alpha.txt" file
for line in alphaFile:
    for i in range(len(alphas)):
        alphas[i] += "".join(line[x] for x in range(len(line)) if x // 4 == i) + SPLITTER
alphas.append(("   " + SPLITTER) * 3) # add white space at the end

# Main -------------------------------------------
bigPrint(tft) # big print
bigOut(tft) # write the large text to our output file

# Close our data streams
textFile.close()
outputFile.close()
alphaFile.close()