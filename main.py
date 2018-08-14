# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:50:55 2018
@author: Varnit Goel
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, datetime, getpass, subprocess

##*************************************For Email module******************************************** 
import smtplib
from smtplib import SMTPException
from email.message import EmailMessage
##*************************************************************************************************

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
            
            
##********************************************************************************************************            
##1. Total number of commit contributions to any project to which a user has a contributed.
@app.route("/criteria1", methods=['GET'])
def criteria1():
    git_count = {}

#Function to get all the repos of a user
def count_user_commits(user):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repos = json.loads(r.content)
#iterate over all the repos
    for repo in repos:
        if repo['fork'] is True:
        
            continue
        n = count_repo_commits(repo['url'] + '/commits')
        repo['num_commits'] = n
        yield repo
#function to get repo commits
def count_repo_commits(commits_url, _acc=0):
    r = requests.get(commits_url)
    commits = json.loads(r.content)
    n = len(commits)
    if n == 0:
        return _acc
    link = r.headers.get('link')
    if link is None:
        return _acc + n
    next_url = find_next(r.headers['link'])
    if next_url is None:
        return _acc + n
    # try to be tail recursive, even when it doesn't matter in CPython
    return count_repo_commits(next_url, _acc + n)

def find_next(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]
##********************************************************************************************************			
			
##********************************************************************************************************   
##2. Total number of commit contributions as above, but restricted to projects that are 
##   members of the original submitted set.             
@app.route("/criteria2", methods=['GET'])
def criteria2():
    git_count = {}
    

##3. The number of known programming languages for each user (presuming that the languages of 
##   any repository committed to are known to the user)
@app.route("/criteria3", methods=['GET'])
def criteria3():
    prog_lang = {} ##List of languages used
	## Using this api 
	## GET https://api.github.com/repos/
	
    

    
##4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted 
##  project set, for 2018.  
@app.route("/criteria4", methods=['GET'])

def criteria4():
    commit_rate = {} ##The commit rate list
	##Using thi API
	##https://api.github.com/users/


##5. The average commit rate of each user to any project, for 2018."""
@app.route("/criteria5", methods=['GET'])

def criteria5():
    average_commit = {} ##List of average commits


    
##6. The total number of collaborators in 2018 (ie. a count of other users who have 
##  contributed to any project that the user has contributed to).
@app.route("/criteria6", methods=['GET'])

def criteria6():
    collab = {} ##List of Collaborators

	
	

##7. Email
@app.route('/mail', methods = ['POST','GET'])
def criteria7():
	msg['Subject'] = 'The contents of file'
	msg['From'] = ##From email id
	msg['To'] = ##To Email id
	
# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()



##**********************************************************************************************
##Main function
    
def master(): 
    
if __name__ == "__main__":
    appl.run(port = 9619)	