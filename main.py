# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:50:55 2018

@author: Varnit Goel
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, datetime, getpass, subprocess

appl = Flask(__name__)
api = Api(appl)

class main(): #Main Class
    def __init__():
        user_repo_no = int(input("Enter number of repositories/users: ")) #user input for no of repo
        git_user_name = []
        repo_name = []
        git_user = []
        while(user_repo_no != 0):
            name_of_user = input('Enter username: ')
            git_user_name.append(name_of_user)
            repository_name = input('Enter repository name: ')
            repo_name.append(repository_name)
            user_repo_no = user_repo_no - 1
            git_user.append(dict(zip(git_user_name,repo_name))) ##Created a dictionery to store
            
            
            
##1. Total number of commit contributions to any project to which a user has a contributed.
@app.route("/criteria1", methods=['GET'])
def criteria1():
    git_count = {}

    
         
   
##2. Total number of commit contributions as above, but restricted to projects that are 
##   members of the original submitted set.             
@app.route("/criteria2", methods=['GET'])

def criteria2():
    git_count = {}
    

##3. The number of known programming languages for each user (presuming that the languages of 
##   any repository committed to are known to the user)
@app.route("/criteria3", methods=['GET'])
def criteria3():
    prog_lang = {}
    

    
##4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted 
##  project set, for 2018.  
@app.route("/criteria4", methods=['GET'])

def criteria4():
    commit_rate = {}



##5. The average commit rate of each user to any project, for 2018."""
@app.route("/criteria5", methods=['GET'])

def criteria5():
    average_commit = {}


    
##6. The total number of collaborators in 2018 (ie. a count of other users who have 
##  contributed to any project that the user has contributed to).
@app.route("/criteria6", methods=['GET'])

def criteria6():
    collab = {}
    

    
##**********************************************************************************************
##Main function
    
def master(): 
    
if __name__ == "__main__":
    appl.run(port = 9619)