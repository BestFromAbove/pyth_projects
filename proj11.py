# Kristjan von Bulow


##############################################################################
#  TA Room Assignment Program
# 
#    Below is method on how program works:
# 1. User is asked to input file.
# 2. Program will first check int of rooms by checking first line in text file.
# 3. Program will create an adjacent matrix with the text file given.
# 4. Program will then start with TA int of 1 and import room set to
#    get all combinations of possible TA combinations.
# 5. If one of the combinations in the set assign TAs to all rooms, program 
#    will print the combination and print adjacent matrix.
# 6. If more TAs are needed, TA int will increase by 1 and run through 
#    combinations program again and compare until right combination is found.
#############################################################################


import itertools

class Matrix(object):
    '''Creates matrix'''
    
    def __init__(self):  
        '''Create and initialize your class attributes.'''
        self._matrix = ['x'] # this is in place to remove 0 index 
        self._rooms = 0 # sets default to 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        print()
        self._rooms = int(fp.readline()) #grabs first line and converts to int
        
        for i in range(self._rooms):
            self._matrix.append(set()) # appends sets into list self._matrix
         
        for line in fp:
            rooms = line.split() 
            self._matrix[int(rooms[0])].add(int(rooms[1])) 
            #connects rooms together in the sets
            self._matrix[int(rooms[1])].add(int(rooms[0]))
    
            
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = '' # s is declared an empty string 
        for item in self._matrix[1:]: #starts at index 1 to avoid 'x' char
            temp_list = [] #decalared an empty set
            for ch in item:
                temp_list.append(str(ch)) #converts matrix into str
            temp = ' '.join(temp_list) #list of rooms separated by spaces
            temp_i = self._matrix.index(item)  # room number index
            s +=  "{}: {}\n".format(temp_i,temp) # combines into string
        
            
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        # Hint: only one line, return something, is needed
        return self._matrix[index]

    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms
        
def open_file():
    ''' Asks user to input file name, if error, loops and asks user again'''
    b = 0 # sets boolean value to 0 
    while b == 0: #runs into b is not equal to 0
        fp = input("\nPlease enter file name\n")
        try: 
            filename = open(fp, "r") 
            b = 1 #stops the loop if file is found
        except FileNotFoundError:
            print("File not found")
   
        return filename
def combinations(room_set, ta_int):
    ''' Will run through all possible combinations given a room set and 
    a integer of TA's given. The combinations are ran through itertools'''
    
    return list(itertools.combinations(room_set, ta_int)) 
    

def main():
   fp = open_file() #asks input to open text file
   m = Matrix() # sets variable m to call Matrix class to simplify code
   m.read_file(fp) # will read file from user and build the adjacency matrix
   room_set = set() # declaring a set "room_set" 
   r = 1 
   for i in range(m._rooms):
       room_set.add(r) # will create indexes of rooms based on int of m._rooms
       r += 1
     
   a = 0  # boolean value to keep while loop running
   ta_int = 1 # starts TA at 1 and increases as while loop continues
   while a == 0: # comparing combinations until reaching correct combination
       c = combinations(room_set, ta_int) # runs function to get combinations
       for item in c:
           c_set = set() # creates new set
           for ch in item:
               c_set.add(ch) # adds the room that the TA is in
               c_set = c_set|m._matrix[ch] # unions to add adjacent rooms
               if c_set == room_set and a == 0: # "a == 0" stops printing loop
                   print("TAs needed: ", ta_int)
                   temp_list = [] # creates a new list
                   for x in item:
                       temp_list.append(str(x))  # this helps format printing
                   temp = ', '.join(temp_list)# separates "," between numbers
                   print("TAs assigned to rooms: {}".format(temp))
                   a = 1 # stops while loop
       ta_int += 1 # increments TAs by 1
   print()
   print("Adjacent matrix")
   print(m) # prints Adjacent matrix by going to __str__ method 
           
       
   
   
   




if __name__ == "__main__":
    main()
