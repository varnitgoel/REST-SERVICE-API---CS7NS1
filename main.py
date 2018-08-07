# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:50:55 2018

@author: Varnit Goel
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests
import time, getpass

appl = Flask(__name__)
api = Api(appl)

class main(): ##Main Class
    def __init__():
        user_repo_no = input("Enter number of repositories/users: ")
        git_name = []
        git_repo = []
        git_user = {}
        
        while(user_repo_no != 0):
            
            
            
#**********************************************************************************************
#1. Total number of commit contributions to any project to which a user has a contributed.
#**********************************************************************************************
@app.route("/criteria1")

def criteria1():
         
   
#**********************************************************************************************
#2. Total number of commit contributions as above, but restricted to projects that are 
#   members of the original submitted set.             
#**********************************************************************************************
@app.route("/criteria2")

def criteria2():


#**********************************************************************************************
#3. The number of known programming languages for each user (presuming that the languages of 
#  any repository committed to are known to the user)
#**********************************************************************************************  
@app.route("/criteria3")

def criteria3():

#**********************************************************************************************
#4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted 
#  project set, for 2018.  
#**********************************************************************************************
@app.route("/criteria4")

def criteria4():

#**********************************************************************************************
#5. The average commit rate of each user to any project, for 2018."""
#**********************************************************************************************
@app.route("/criteria5")

def criteria5():

#**********************************************************************************************
#6. The total number of collaborators in 2018 (ie. a count of other users who have 
#   contributed to any project that the user has contributed to).
#**********************************************************************************************
@app.route("/criteria6")

def criteria6():

#**********************************************************************************************

def master(): 
    
if __name__ == "__main__":
    appl.run()