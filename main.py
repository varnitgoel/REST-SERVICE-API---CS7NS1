# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:50:55 2018
@author: Varnit Goel
"""

from flask import Flask, jsonify, json  #to return the results as a response from a flask view
from flask_restful import Resource, Api, reqparse
from github import emails, github
import json, requests, datetime, getpass, subprocess

##*********************************For Email module**************************************** 
import smtplib
from smtplib import SMTPException
#from email.message import EmailMessage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
##*****************************************************************************************  

#create instace of flask
appl = Flask(__name__) ##Flask knows where to look for templates, static files etc.
api = Api(appl)
tok = github.GitHub('myusername', 'mytoken')

##*****************************************************************************************  
class main(): #Main Class
    def __init__():
        user_no = int(input("Enter number of repositories/users: ")) #user input for no of repo
        user_name = []
        repo_name = []
        git_user = []
        while(user_no != 0):
            name_of_user = input('Enter username: ')  #Input for username
            user_name.append(name_of_user)  #store username
            repository_name = input('Enter repository name: ')  #input for repository name
            repo_name.append(repository_name)  #store repo name
            user_no = user_no - 1  
        git_user.append(dict(zip(user_name,repo_name))) ##Created a dictionery to store
            
##*****************************************************************************************         
##1. Total number of commit contributions to any project to which a user has a contributed.
##*****************************************************************************************
@appl.route("/criteria1", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria1():
    commit_count = {}
    for u in range(0,len(X.user_name))
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
    return count_repo_commits(next_url, _acc + n)

def find_next(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]

   
##*****************************************************************************************    
##2. Total number of commit contributions as above, but restricted to projects that are members of the original submitted set.             
##*****************************************************************************************
@appl.route("/criteria2", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria2():
    commit_count = {}
    for u in range(0,len(X.user_name)):
        link = requests.get("https://api.github.com/repos/" + X.user_name[u] + X.repo_name[u] +"/commits?since=2018-01-01", auth = (myusername, mytoken))
        data = json.loads(link.text)
        commit_count['{0}'.format(M.git_username[j])] = len(data)
    return jsonify(commit_count) 
##*****************************************************************************************
##3. The number of known programming languages for each user (presuming that the languages of any repository committed to are known to the user)
##*****************************************************************************************
@appl.route("/criteria3", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria3():
    prog_lang = {}
    for u in range(0,len(X.user_name)):
        link = requests.get("https://api.github.com/users/" + X.user_name[u] + X.repo_name[u]+"/repos", auth = (myusername, mytoken))        
        data = json.loads(link.text)
        
    return jsonify(prog_lang) 
##*****************************************************************************************
##4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted project set, for 2018.  
##*****************************************************************************************
@appl.route("/criteria4", methods=['GET'])  ##tell Flask what URL should trigger our function.

def criteria4():
    commit_rate = {}
    for u in range(0,len(X.user_name)):
        link = requests.get("https://api.github.com/repos/" + X.user_name[u] + X.repo_name[u]"/stats/commit_activity", auth = (myusername, mytoken))        
        json_data = json.loads(link.text)
        
    return jsonify(commit_rate)        
##*****************************************************************************************
##5. The average commit rate of each user to any project, for 2018."""
##*****************************************************************************************
@appl.route("/criteria5", methods=['GET'])  ##tell Flask what URL should trigger our function.

def criteria5():
    average_commit = {}



##*****************************************************************************************
##6. The total number of collaborators in 2018 (ie. a count of other users who have 
##  contributed to any project that the user has contributed to).
##*****************************************************************************************
@appl.route("/criteria6", methods=['GET'])  ##tell Flask what URL should trigger our function.

def criteria6():
    collab = {}
    
    
    
##*****************************************************************************************
##7. Email Module
##*****************************************************************************************
@appl.route('/email', methods = ['GET'])  ##tell Flask what URL should trigger our function.
def email():
    fromad = 'myusername'
    toad = ""
    msg = MIMEMultipart()
    msg['From'] = fromad
    msg['To'] = toaddr
    msg['Subject'] = "ANSWERS"
    
    body = "Answers to all the 6 criterias"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromad, 'mytoken')
    server.sendmail(fromad, toad, message)
    server.quit()
    
##	msg['Subject'] = 'The contents of file'
##	msg['From'] = ##From email id
##	msg['To'] = ##To Email id
	
# Send the message via our own SMTP server.
##X = smtplib.SMTP('localhost')
#X.send_message(msg)
#X.quit()

#print ("My repo names:")
#for r in tok.repos.forUser(me):
#    print(r.name)
##

##**********************************************************************************************
## Main function
    
def main(): 
    
if __name__ == "__main__":
    X = main()
    appl.run(port = 9619)	