# Kristjan von Bulow


##############################################################################
#  imitation of Facebook Finder Program
# 
#    Below is method on how program works
# 1. First input from user for file
# 2. Takes file and puts into read_file function to make it into a list
# 3. Take list and put list into calc_similiaity and return sim_matrix
# 4. Asks user for index of user and put index in recommend fuction
# 5. recommend function will compare similarity of friends with other friends
#    to determine who to recommend
# 6. Will recommend a friend to user input 
# 7. Program will ask if user inputs another index of user or quit
#############################################################################

def open_file():
    ''' Asks user to input file name, if error, loops and asks user again'''
    b = 0
    while b == 0:
        fp = input("\nPlease enter file name\n")
        try: 
            open(fp, "r")
            b = 1
        except FileNotFoundError:
            print("File not found")
    return fp
        
  


def read_file(fp):  
    ''' Creates empty list called network,sorts list with users with friends'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    fp = open(fp, "r")
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])
    for line in fp:
        entry = line.split()
        entry[0] = int(entry[0])
        entry[1] = int(entry[1])
        network[entry[0]].append(entry[1])
        network[entry[1]].append(entry[0])
    return network

def num_in_common_between_lists(list1, list2):
    ''' compares list one to list two, if similarity, adds one to variable'''
    similiarity = 0
    for friend in list1:
        if friend in list2:
            similiarity += 1
    return similiarity

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Takes index and puts into num_in_common function to check for
    similiarty, then compares similairties scores and puts into sim_matrix '''
    
    n = len(network)
    sim_matrix = init_matrix(n) # creates new list with n rows 
    index1 = 0 
    while index1 < n:
        list1 = network[index1]
        index2 = 0
        while index2 < n:
            list2 = network[index2]
            common = num_in_common_between_lists(list1, list2)
            sim_matrix[index1][index2] = common
            index2 += 1
        index1 += 1
    return sim_matrix
            
   

def recommend(user_id,network,similarity_matrix):
    ''' This will check the user id in similairty matrix and see if the 
    user id has any comparisons with other users to determine a match for
    recommendation'''
    maximum_friends = 0
    friends_index = 0
    for i, item in enumerate(similarity_matrix[user_id]):
        if i == user_id: # cannot befriend oneself
            continue
        elif i in network[user_id]: # avoid recommending one's friends
            continue
                    # only recommends highest related friend 
        elif item > maximum_friends: 
            maximum_friends = 0
            friends_index = i
        else:
            continue
        recommendation = friends_index
        return recommendation
            
        
            
    
def main():
    a = 0
    fp = open_file()
    network = read_file(fp)
    n = len(network)
    similiarity_matrix = calc_similarity_scores(network)
    while a == 0:
        print("Please enter an integer from range 0 to", n-1)
        user_id = int(input(""))
        answer = recommend(user_id, network, similiarity_matrix)
        print("The suggusted user for", user_id, "is", answer)
        print("\nDo you want to continue? (yes/no)\n")
        answer = input("")
        answer = answer.lower()
        if answer == "no":
            a = 1
        elif answer == "yes":
            continue
        else:
            print("Invalid answer try again\n")
            
        
    
if __name__ == "__main__":
    main()

