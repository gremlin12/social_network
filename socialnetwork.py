example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. 
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string_input):
    network = {} #Sets up the basic structure of the network as a dictionary
    s = string_input
    #Now we set up a dictionary for each user inside the network.
    #A games list and connections list will be the values for each key.
    games = []
    connections = []
    #Define key names globally
    GAMES_KEY = 'games'
    CONN_KEY = 'connections'
    #Set up an inner dictionary for each user inside the network
    if s == '':
        user = ''
        network[user] = {CONN_KEY : connections, GAMES_KEY : games}
    #Isolate user, connections and games from input_string and add to dictionary
    while len(s) > 0:
        stop_one = s.find('.')
        stop_two = s.find('.',stop_one+1)
        user = s[:s.find(' ')] 
        connections = s[s.find('is connected to')+16 : stop_one].split(', ')
        games = s[s.find('likes to play')+14 : stop_two].split(', ')
        network[user] = {CONN_KEY : connections, GAMES_KEY : games}  
        s = s[stop_two + 1:] 
    return network 

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that was created with the create_data_structure procedure,    
# though it may be modified as new users or new connections are added. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.

def get_games_liked(network,user):
    if user in network:
        return network[user]['games']
    else:
        return None
# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    if user in network:
        return network[user]['connections']
    else:
        return None
    
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    else:
        if user_B not in get_connections(network, user_A):
            network[user_A]["connections"].append(user_B)
    return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
    
def add_new_user(network, user, games):
    if user in network:
        return network
    else:
        network[user] = {'games':games, 'connections':[]}
    return network   

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
   
def get_secondary_connections(network, user):
    secondary_connections = []
    if user not in network:
        return None
    for friend in get_connections(network, user):
        for friend_of_friend in get_connections(network, friend):
            if friend_of_friend not in secondary_connections:
                secondary_connections.append(friend_of_friend)
    return secondary_connections            

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.

def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    in_common = 0
    for friend in network[user_A]['connections']:
        if friend in network[user_B]['connections']:
            in_common = in_common + 1
    return in_common

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.

#  Citation: "Python Patterns: Implementing Graphs" (published on the website of
#  the Python Software foundation at https://www.python.org/doc/essays/graphs/)
#  was helpful in understanding the "path to friend" problem and finding a recursive
#  solution.

def path_to_friend(network, user_A, user_B, path = None):
    #Set a default parameter of path=None so that user-names added to path will be 
    #preserved when the procedure repeats. 
    if path is None:
        path = []	
    if user_A not in network or user_B not in network:
        return None
    #Add another user-name to the path each time the procedure loops (this
    #is accomplished by creating a new path list).
    path = path + [user_A]
    #Set up a base case which stops the loop when destination is reached
    if user_A == user_B:
        return path
    #Loop recursively to try each possibility until destination is reached
    for user in network[user_A]['connections']:
        if user not in path:
            newpath = path_to_friend(network,user,user_B, path)
            if newpath: 
                return newpath            
    return None


# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# my MYOP: 
#    Finds the best gaming partner for a user, based on the number of 
#    favorite games the user and a potential partner have in common. It consists of
#    a helper procedure, games_in_common, and the main procedure, find_best_partner.

# games_in_common(network, user_A, user_B):
#    Checks which games any two users have in common.

# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B

# Return:
#   A tuple containing a list of shared games, followed by the number of shared games.
#    - If user_A or user_B is not in network, returns False.
#    - If no games are shared, returns ([],0)

def games_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    shared_games_list = []
    total_shared_games = 0
    for game in network[user_A]['games']:
        if game in network[user_B]['games']:
            shared_games_list.append(game)
            total_shared_games += 1        
    return shared_games_list, total_shared_games           

# find_best_parter(network, user):
#   Uses the output from games_in_common to find the best new gaming
#   parter for the user. Since the purpose is to suggest a new connection
#   based on shared interests, only gamers who are not already connected
#   to the user are considered.

# Arguments:
#   network: the gamer network data structure
#   user:  a string containing the name of the user
#
# Return:
#   A tuple containing the name (string value) of the best partner, followed by a list
#   of shared games.
#    - If no suitable gaming partners are found, returns 'None.' 

def find_best_partner(network, user):
    partners = [] #Sets up a list of potential partners
    if user not in network:
        return None
    for gamer in network:
        #Check to make sure each gamer is not already connected to the user
        if gamer not in network[user]['connections']:
            #Check if each gamer shares at least one game with user
            if games_in_common(network, user, gamer)[1] > 0:
                #Prevent user's own name from being included in partners list
                if gamer != user:
                    partners.append(gamer)
    if partners == []:
        return None
    #Loop through partners list to select the gamer with highest total_shared_games value
    best_partner = partners[0]           
    for p in partners: 
        if games_in_common(network, user, p)[1] > games_in_common(network, user, best_partner)[1]:
            best_partner = p  
    return best_partner, games_in_common(network, user, best_partner)[0]

    

net = create_data_structure(example_input)
print net
#print path_to_friend(net, "John", "Ollie")
#print get_connections(net, "Walter")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "Olive")
#print add_connection(net, "John", "Freda")
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")
#print find_best_partner(net, "Freda")
#print games_in_common(net, 'Walter', 'Levi')
#print games_in_common(net, 'Robin', 'Ollie')

    
    
    
    
