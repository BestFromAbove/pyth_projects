# Kristjan von Bulow

##############################################################################
#  Cooccurance of words program
# 
#    Below is method on how program works
# 1. First input from user for file
# 2. Takes file and puts into read_data function put words into dictinary.
#    The word is the key, the line number word is on is value
# 3. Dictionary is put into find_cooccurance function with user input of words
#    to find in dictionary
# 4. If the find_occurance function finds the words of user input, will print
#    the lines that those words are on 
# 5. Program loops asking user for more words to find unti user prints 'q' or
#    'Q' to close the program
#############################################################################


import string

def open_file():
    ''' Requests input from user, opens file
    Input: None
    Output: Filename'''
    a = 0 # boolean value to set loop
    while a == 0:
        
        filename = input( "Name of file to be processed: \n" )

        try:
           open(filename, 'r') # will open input filename
           a = 1

        except FileNotFoundError: #Error if cannot find file
            print( "Halting -- unable to open", filename )
            
    return filename
    
def read_data(fp):
    ''' Takes filename and puts text into dictionary, key being the word,
    value being the line numbers it is it
    Input: Filename (fp)
    Output: Dictionary'''
    fp = open(fp, "r") # opens file 
    dictionary = dict() # empty dictionary
    exclude = set(string.punctuation) # set that includes all punctuation
    i = 1
    for line in fp:
        line = ''.join(ch for ch in line if ch not in exclude) # removes 
        # punctuation by comparing string and set "exclude" 
        for word in line.lower().split(): #lowercase and split by whitespace
            if len(word) > 1: # removes words with length 1 or less
                if word in dictionary:
                    if i in dictionary[word]:
                        dictionary[word] = [i] #adds line number to key "word"
                    else:
                        dictionary[word].append(i) #adds line number to key
                else:
                    dictionary[word] = [i] #adds line number to key
        i = i + 1 # increments line number
    return(dictionary) 

def find_cooccurance(D, inp_str):
    ''' Takes dictionary and input_str (inp_str) and compares them to
    determine line numbers. line numbers are put into sets to be compared
    with intersection function
    Input: Dictionary (D), Input string (inp_str)
    Output: None.'''
    inp_str = inp_str.split() # separates string into list
    i = 0
    print("The co-occurance for: ", end = "")
    temp_set = set() #empty set
    x = 1
    for i in range (len(inp_str)): #from 0 to length of items in list
        if x:
            print(inp_str[i], end = "") #prints only first time without comma
            x = 0 # only runs this if statement one time
        else:
            print(",", inp_str[i], end = "") #prints input with comma
    print()
    if inp_str[i] in D.keys(): #if word from input is a key in dictionary
        a = 1
        temp_set = set(D[inp_str[0]]) # creates a set with first key's values
        for i in range (len(inp_str)): # from 0 to length of items in list
            if inp_str[i] in D.keys(): 
              temp_set = temp_set & set(D[inp_str[i]]) #intersection function
              # to find hte cooccurance of the set
    else:
        a = 0
        i = i+1
    if a == 0: # if the word from input isn't in the dictionary
        print("Lines: None.")
    else:
        print("Lines: ", end = "")
        temp_list = list(temp_set) #turns the set into a list
        x = 1
        for i in sorted(temp_list): #prints line numbers 
            if x:
                print(i, end = "") # prints first time without comma
                x = 0 # only runs this if statement one time
            else:
                print(",",i, end = "") # prints line number with comma
        
    
        
    
    

def main():
    fp = open_file() # opens file
    D = read_data(fp) # reads file and puts into dictionary
    inp_str = ""
    a = 0 
    exclude = set(string.punctuation) # set that has all punctuation
    while a == 0: #boolean loop
        inp_str = input("Enter space-separated words: ")
        inp_str = inp_str.lower() #input set lowercase
        inp_str = ''.join(ch for ch in inp_str if ch not in exclude)
        # removes punctuation from input
        if inp_str == "q": # if input is 'Q' or 'q', program will quit
            a = 1
            break
        elif inp_str == "": # if input is whitespace
            print("Lines: None.")
        else:
            find_cooccurance(D, inp_str) #function to find cooccurance

    
    
        
    
if __name__ == "__main__":
    main()