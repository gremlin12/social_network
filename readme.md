This Python program, socialnetwork.py, was created as a final project for Udacity's Introduction to Computer Science course, taught by Professor David Evans.

The program takes as input a string of sentences containing user-names, social connections and gaming preferences, such as: "John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner."

With this simple input string, socialnetwork.py then sets up a fictional gamers' network in the form of a Python dictionary.

Various procedures embedded in socialnetwork.py can retrieve and manipulate the network data in order to provide useful information. For example:
- Finding a path from one player in the network to another.
- Listing the preferred games or connections of any given user.
- Finding secondary connections (friends of friends).
- Suggesting new social connections based on users' gaming preferences.

Try out the program yourself! You will need to open the file socialnetwork.py in a Python IDLE or terminal to make it work. At the bottom of the file you will find a list of print commands that have been commented out:

#print net
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

To run a command, follow these steps:
1. Uncomment the command you want to test by removing the '#' symbol in front.
2. Save the file.
3. Run the file.

This project was a lot of fun to put together and taught me a lot about the basics of computer programming. Thanks for checking it out!

