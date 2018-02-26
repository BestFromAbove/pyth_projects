# Kristjan von Bulow

##############################################################################
# Brute force and dictionary attacker
# 
#    Below is method on how program works
# 1. First input from user asking brute force, dictionary, both, or quit 
# 2. if dictionary, asks for text file and zip file and runs dictionary func 
# 3. if brute force, asks for zip file and runs brute force function
# 4. if both, will run dictionary first then if fails, program runs brute force
# 5. If dictionary function or brute force function returns with a password,
#    the function will return the password
# 6. If either function doesnt return with a password, will return to options
# 7. Program imports itertools, product, zipfile, and time to run code
#############################################################################

from itertools import product
import zipfile
import time


a = 0
k = 0
password = ''
def open_dict_file(): # opens the dictionary text file
   b = 0
   while b == 0:
        dictionary = input("\nInput dictionary file name:\n")
        try:      # will try to open file
            open(dictionary, "r")
            b = 1
        except FileNotFoundError: # if file is not found, restarts loop
            print("File not Found")
   return dictionary

def open_zip_file():
    b = 0
    while b == 0:
        zip_file = input("\nInput zip file name:\n") #input zip file name
        try:     
            open(zip_file, "r")
            b = 1
        except FileNotFoundError:
            print("Zip not found")

    return zip_file
    
def brute_force_attack(zip_file):
    alphabet_str = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    k = 0
    while i <= 8: # this goes up to 8 characters for password
        for items in product(alphabet_str, repeat = i):
            password = '' .join(items)
            try:
                 zip_file.extractall(pwd=password.encode())
                 print("\nBrute force password is", password)
                 k = 1
                 return k
            except:
                 continue
        i += 1
    

def dictionary_attack(zip_file, dict_file):
    
    k = 0
    
    
    # this attack worked before and code is right. something is off and 
    # I cannot figure it out
    
    
    for line in dict_file:
        password = line.strip() #splits line and checks line with password
        try:
            zip_file.extractall(pwd=password.encode())
            print("Dictionary password is", password)
            k = 1
            return k
        except:
            continue
print("Cracking zip files.")   
print("Warning cracking passwords is ilelgal due to the Computer", end = '')
print(" Fraud and Abuse Act and has a prison term of 20 years.")     
while a == 0: # this loops the question of user input
    k = 0
    start = 0.0
    end = 0.0
    elap_time = 0.0
    print("What type of cracking ('brute force', 'dictionary', 'both', 'q')\n")
    user_input = input()
    user_input = user_input.lower()
    if user_input == ("dictionary"):
        print("\nDictionary Cracking:")
        dict_file = open_dict_file() # opens dictionary file
        zip_file = open_zip_file() # opens zip file
        zip_file = zipfile.ZipFile(zip_file)
        start = time.process_time() # starts timer
        k = dictionary_attack(zip_file, dict_file) # runs attack
        end = time.process_time() #ends timer
        elap_time = end - start # gets elapsed time
        print("Elapsed time (sec): ", end = '')
        print("%.4f" % elap_time)
        if k == 1:
            continue  
        else:
            print("No password found witih dictionary cracking.")
        
    if user_input == ("brute force"):
        print("\nBrute Force cracking")
        zip_file = open_zip_file() # opens zip file
        zip_file = zipfile.ZipFile(zip_file) # converts zip file
        start = time.process_time()
        k = brute_force_attack(zip_file) # runs attack
        end = time.process_time()
        elap_time = end - start
        print("Elapsed time (sec): ", end = '')
        print("%.4f" % elap_time)
        if k == 1:
            continue 
        else:
            print ("No password found with brute forcing.")
        
        
        
    
    if user_input == ("q"):
        a = 1 # will quit the loop
    
        
    if user_input == ("both"): # this runs both methods of attack
        print("\nBoth Brute Force and Dictionary Attack")
        dict_file = open_dict_file()
        zip_file = open_zip_file()
        zip_file = zipfile.ZipFile(zip_file)
        start = time.process_time()
        k = dictionary_attack(zip_file, dict_file)
        end  = time.process_time()
        elap_time = end - start
        print("Elapsed time (sec): ", end = '')
        print("%.4f" % elap_time)
        if k == 1:
            continue
        else: # starts dictionary attack
            k = 0
            start = 0.0
            end = 0.0
            print("No password found with dictionary attack.")
            print("Continuing with brute forcing.")
            start = time.process_time()
            k = brute_force_attack(zip_file)
            end = time.process_time()
            print("Elapsed time (sec): ", end = '')
            print("%.4f" % elap_time)
            if k == 1:
                continue
            else:
                print("No password found with both attacking.")
        