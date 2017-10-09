# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:01:26 2016

@author: Sai Vegasena
"""
'''
Sai Vegasena
Creates a dictionary data structure from a file
of train stop information and prints it in an
organized manner based off user input
'''
def file_data_to_dict(filename): #creates the dictionary from the file and makes each train key value a list
    dictionary = {}  #the new dictionary with the trains as keys
    filename = open(filename,"r") 
    for line in filename:
        dictionary[line.split(',,')[0][0]] = [] #making each train key's list value
    dictionary.pop('s') #popping the first line
    filename.close()
    return dictionary
        
def stops_to_dict(dictionary, filename):
    filename = open(filename,"r")
    for line in filename:
        if line.split(',,')[0][0] != 's': #getting rid of the first line
            if line.split(',,')[1] not in dictionary[line.split(',,')[0][0]]: #preventing list repeats
                dictionary[line.split(',,')[0][0]].append(line.split(',,')[1]) #appending stops to list
    filename.close()

def main():
    filename = 'hw9 - mta train stop data.csv'
    dictionary = file_data_to_dict(filename)
    stops_to_dict(dictionary, filename)
    answer = input("Please enter a train line, or done to stop: ")
    while answer != "done":
        if answer in dictionary:
            print(answer,'line:',", ".join((dictionary[answer]))) #joins to print without list format
            answer = input("Please enter a train line, or done to stop: ")
        else: #prevents program crashing if line does not exist
            print("This is not a name of a train line")
            answer = input("Please enter a train line, or done to stop: ")
            while answer not in dictionary and answer != 'done':
                    print("That is still not a name of a train line") #joins to print without list format
                    answer = input("Please enter a train line, or done to stop: ")
main();
