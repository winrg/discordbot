import discord
import time
import pickle

#get a token
conf = 'n'
while conf != 'y':
    token = input("Please input a bot token.\n")
    print("You have entered '" + token + "'. Is this correct?")
    conf = input("(y/n): ")

#get owner id
conf = n
while conf != 'y':
    owner = input("Please input owner id. \n")
    print("You have entered '" + owner + "'. Is this correct?")
    conf = input("(y/n): ")

