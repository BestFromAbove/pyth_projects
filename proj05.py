# Kristjan von Bulow

##############################################################################
# Decryption of Caesar cipher
# 
#    Below is method on how decryption works
# 1.  Ask user for input code
# 2. Run input through get_shift in order to find shift
# 3. run input through output_plaintext, which runs get_char
# 4. output_plaintext outputs decrpyted message  
# 5. Main function asks if the text is readable in english
#    if not, will put shift + 4 into string called 'ignore'
# 6. function get_shift is called again and compared with 'ignore'
# 7. get_shift should ignore characters in 'ignore' and go to second most
#    common character
# 8. Returns new shift to output_plaintext to translate again and asks user  
#    if new output is readable english
# 9. Will repeat until the output is readable english, and then will quit
#############################################################################

alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_char(ch,shift):

    if ch in alphabet_str: # if the character is in alphabet
        new_char = alphabet_str.index(ch) - shift # shifts character
        new_char1 = alphabet_str[new_char] 
        
        return(new_char1)
    else: #if a character other than part of alphabet, returns unchanged
        return(ch)
  
def get_shift(s, ignore):
    common_str = "" # holds most common character
    i = 0
    count_common_str = 0
    for char in s:
        if char == alphabet_str[0]: # checks if most common character is A
            common_str = alphabet_str[0]
            count_common_str += 1
        else:
            continue
    while i < 25: #checks rest of the alphabet
        i += 1
        count_testing = 0 
        for char in s:
            #for char in ignore:
                #if alphabet_str.index(char) == ignore: #if previous tests dont
# work, this compare character to 'ignore' to make sure it doesnt loop again 
                   # continue
            
            if char == alphabet_str[0+i]:
                count_testing += 1
            else:
                continue
        if count_testing > count_common_str: #compares counts of letters
            common_str = alphabet_str[0+i] # sets most common letter
            count_common_str = count_testing # sets count of most common letter
            
    
    shift = alphabet_str.index(common_str) - 4 
    # shift subtracts index number of most common character - 4 (E)
    return(shift)
        
def output_plaintext(s1,shift):
   i = 0
   s_new = ""
   while i < len(s1): # this should put every character in get_char function
       i += 1
       for ch in s1:
           ch_new = ""
           ch_new = get_char(ch, shift) # puts character in get_char to convert
           s_new += ch_new # should add character to empty string to get 
# a converted phrase
   print(s_new) # this should only print out answer once, however a bug prints
# out the answer len(s1) amount of times, I couldn't figure out why
       
def main():
   s = input("Input cipherText:\n")
   s1 = s.upper()
   ignore = ""
   shift = get_shift(s1, ignore)
   output_plaintext(s1, shift)
   a = 0
   while a == 0: # will ask if text is readable, if not, loops until answer yes
    is_answer = input("Is this plaintext readable in English (yes/no)\n")
    is_answer = is_answer.lower()
    if is_answer == "yes":
        break # ends loop and closes program
    if is_answer == "no":  # will redo the process until done correctly
        shift1 = shift + 4 
        ignore = ignore + str(shift1)
        shift = get_shift(s, ignore)
        output_plaintext(s1, shift)
        
    else:
        print("Please enter yes or no\n") #if input is other than yes/no, loop
# question again
        
   

# These two lines allow this program to be imported into other code
if __name__ == "__main__": 
    main()

