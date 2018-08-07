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
    def __init__(self):
        self.user_no = input("Enter repository number: ")
        self.git_name = []
        self.get_repo = []
        
        while(self.no_of_users != 0):
            
            
#**********************************************************************************************
#1. Total number of commit contributions to any project to which a user has a contributed.
#**********************************************************************************************
            
         
   
#**********************************************************************************************
#2. Total number of commit contributions as above, but restricted to projects that are 
#   members of the original submitted set.             
#**********************************************************************************************



#**********************************************************************************************
#3. The number of known programming languages for each user (presuming that the languages of 
#  any repository committed to are known to the user)
#**********************************************************************************************  



#**********************************************************************************************
#4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted 
#  project set, for 2018.  
#**********************************************************************************************



#**********************************************************************************************
#5. The average commit rate of each user to any project, for 2018."""
#**********************************************************************************************


#**********************************************************************************************
#6. The total number of collaborators in 2018 (ie. a count of other users who have 
#   contributed to any project that the user has contributed to).
#**********************************************************************************************