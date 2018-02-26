# Kristjan von Bulow


##############################################################################
#  State Data Analysis Program
# 
#    Below is method on how program works
# 1. First input from user for file
# 2. Takes file and puts into read_file function to make it into a list
# 3. Puts list in adding_list function to add GDP per capita and income per
#    capita.
# 4. Prints input region's highest GDP per capita, lowest GDP per
#    capita, highest income per capita, and lowest income per capita
# 5. Prints formatted table of all information of input's region including
#    individual state's GDP per capita and income per capita
# 6. Asks user if plot shall be created
# 7. If user inputs yes, program will ask for x and y coordinates of plot 
#    to compare the regions to.
# 8. Prints plot chart with user's requested x and y coordinates with input 
#    region. Then shuts down program
#############################################################################
    
import pylab


REGION_LIST = ['Far_West',
 'Great_Lakes',
 'Mideast',
 'New_England',
 'Plains',
 'Rocky_Mountain',
 'Southeast',
 'Southwest',
 'all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "
def open_file():
    a = 0
    while a == 0:
        
        filename = input( "Name of file to be processed: \n" )

        try:
           subprocess.Popen([filename],shell=True)
           a = 1

        except FileNotFoundError:
            print( "Halting -- unable to open", filename )
            
    return file
    
def read_file (fp):
    ''' Reads file and puts all lines into a list of lists.
        Input: file name, and region inputed from user
        Returns: List made from inputed region'''
    fp.readline() # skips line
    new_list = list() # creates list
    for line in fp:
        line_list = line.strip().split(",")
        print(line)
def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
# this function is not according to coding standards ^^^ this is given function
    
def adding_list(map_list):
    ''' This function will add the gdp_per_capita and the income_per_capita
    to map_list
    Input: map_list 
    Returns: map_list with gdp_per_capita and income_per_capita'''
    for line in map_list:
        gdp = float(line[3]) * 1000000000 # sets decimal to right place
        income = float(line[4]) * 1000000000 # sets decimal to right place
        population = float(line[2]) * 1000000 # sets decimal to right place
        gdp_per_capita = gdp/population # calculates gdp_per_capita
        income_per_capita = income/population # calculates income_per_capita
        line.append(gdp_per_capita)
        line.append(income_per_capita)
    return(map_list)


        
def print_state_information(map_list):
    '''This wil take the map_list and determine highest GDP per capita, lowest
    GDP per capita, highest income per capita, and lowest income per capita
    Input: map_list
    Returns: Nothing'''
    g_gdp = 0 # sets variable to 0 
    for line in map_list:
        temp = line[8] # temp will be compared to g_gdp "greatest_gdp"
        temp = float(temp) # turns string to float
        if temp > g_gdp: # compares temp and g_gdp 
            g_gdp = float(line[8]) # line[8] is gdp_per_capita index
            state = line[0] # state is the 0 index of that line
    print("{} has the highest GDP per capita at ${:,.2f}".format(state,g_gdp))
    l_gdp = 9999999999999 # sets l_gdp "lowest_gdp" to max value
    for line in map_list:
        temp = line[8] # same as above but finding lowest
        temp = float(temp)
        if temp < l_gdp: # compare for lowest value
            l_gdp = float(line[8])
            state = line[0]
    print("{} has the lowest GDP per capita at ${:,.2f}".format(state,l_gdp))
    print()
    g_income = 0 # same as above but locating greatest income per capita
    for line in map_list:
        temp = line[9] # line[9] is income_per_capita index
        temp = float(temp)
        if temp > g_income: 
            g_income = float(line[9])
            state = line[0]
    print("{} has the highest income per capita at ${:,.2f}" \
          .format(state,g_income))
    l_income = 9999999999999999999 # same as above but locating lowest income
    for line in map_list:
        temp = line[9]
        temp = float(temp)
        if temp < l_income:
            l_income = float(line[9])
            state = line[0]
    print("{} has the lowest income per capita at ${:,.2f}" \
          .format(state,l_income))

def print_formatted_data(map_list):
    print("{:17}{:19}{:9}{:12}{:15}{:19}{:12}{:17}{:15}".format("State Name" \
          , *VALUES_NAMES))
    for line in map_list:
        line.remove(line[1])
        for i, ch in enumerate(line[1:9]):
            char_num = float(ch)
            line[i+1] = char_num
        print("{:15}{:15.2f}{:12,.2f}{:12.2f}{:15,.2f}{:18.2f}{:12.2f}" \
              "{:18,.2f}{:20,.2f}".format(*line))
    
    
    
            
        

def plot(map_list):   
    '''Plot the values in the parameters.'''
    
    
    # prompt for which values to plot; these will be the x and y
    xy = input(PROMPT2)
    xy = xy.split()
    x_index = VALUES_LIST.index(xy[0]) + 2
    y_index = VALUES_LIST.index(xy[1]) + 2
    x  = []
    y = []
    state_names = []
    # build x, the list of x values
    # build y, the list of y values
    for item in map_list:
        x.append(float(item[x_index]))
        y.append(float(item[y_index]))
        state_names.append(item[0])
    # hint: list comprehension is a slick way to build x and y

    # In the following you need to replace 'pass' with your own arguments
    pylab.title(xy[0] + " vs." + xy[1])   # plot title

    pylab.xlabel(xy[0])   #label x axis
    pylab.ylabel(xy[1])   #label y axis
    
    pylab.scatter(x,y)
    for i, txt in enumerate(state_names): 
        pylab.annotate(txt, (x[i],y[i]))
    
    plot_regression(x,y)
    
    # USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png
def name_fixer(region_input):
    ''' This will take the input of user and correctly change them to match
    up with the .csv file state names. This function wasn't necessary but
    made input more flexible
    Input: region_input "users input for region"
    Return: Modified region_input to help make other functions work'''
    a = 0 # boolean variable = 0
    if region_input == "new_england":
        region_input = "New_England" # changes to "correct" string
        a = 1 
    elif region_input == "far_west":
        region_input = "Far_West" # same as above
        a = 1
    elif region_input == "great_lakes":
        region_input = "Great_Lakes" # same as above
        a = 1
    elif region_input == "mideast":
        region_input = "Mideast" # same as above
        a = 1
    elif region_input == "plains":
        region_input = "Plains" # same as above
        a = 1
    elif region_input == "rocky_mountain":
        region_input = "Rocky_Mountain"  # same as above
        a = 1
    elif region_input == "southeast":
        region_input = "Southeast" # same as above
        a = 1
    elif region_input == "southwest":
        region_input = "Southwest" # same as above
        a = 1
    elif region_input == "all": # just passes this input through function
        a = 1
    if a == 0: # if input is something other than above strings
        region_input = "error" # helps decide if input needs to be re-entered 
    return region_input
    

def main():
    fp = open_file() # opens file
    map_list = list() # empty list creation
    map_list = read_file(fp) # fills map_list
    
    
if __name__ == "__main__":
    main()