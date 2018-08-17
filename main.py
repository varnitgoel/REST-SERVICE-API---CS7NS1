# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:50:55 2018
@author: Varnit Goel
"""

from flask import Flask, jsonify, json  #to return the results as a response from a flask view
from flask_restful import Resource, Api, reqparse
from github import emails, github
from nested_lookup import nested_lookup
import json, requests, getpass, subprocess

##*********************************For Email module**************************************** 
import smtplib
from smtplib import SMTPException
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
##*****************************************************************************************  

#create instace of flask
appl = Flask(__name__) ##Flask knows where to look for templates, static files etc.
api = Api(appl)
tok = github.GitHub('myusername', 'mytoken')

##*****************************************************************************************  
class main(): #Main Class
    
@appl.route('/users', methods = ['GET'])
def users():
    return jsonify(X.users)

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
    commits = json.loads(file.text)
    n = len(commits)
    if n == 0:
        return _acc
    file = r.headers.get('file')
    if file is None:
        return _acc + n
    next_url = find_next(r.headers['file'])
    if next_url is None:
        return _acc + n
    return count_repo_commits(next_url, _acc + n)

def find_next(file):
    for l in file.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]

return jsonify(commit_count) 
##*****************************************************************************************    
##2. Total number of commit contributions as above, but restricted to projects that are members of the original submitted set.             
##*****************************************************************************************
@appl.route("/criteria2", methods = ['GET'])  ##tell Flask what URL should trigger our function.
def criteria2():
    commit_count = {}
    for u in range(0,len(X.user_name)):
        file = requests.get("https://api.github.com/repos/" + X.user_name[u] + X.repo_name[u] +"/commits?since=2018-01-01", auth = (myusername, mytoken))
        data = json.loads(file.text)
        commit_count['{0}'.format(M.git_username[j])] = len(data)
    return jsonify(commit_count) 
##*****************************************************************************************
##3. The number of known programming languages for each user (presuming that the languages of any repository committed to are known to the user)
##*****************************************************************************************
@appl.route("/criteria3", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria3():
    prog_lang = {}
    for u in range(0,len(X.user_name)):
        file = requests.get("https://api.github.com/users/" + X.user_name[u] + "/repos", auth = (myusername, mytoken))        
        data = json.loads(file.text)
        output = nested_lookup(key = 'name', document = json_data, wild = True, with_keys = False)
        
        lang = []
        for x in range(0,len(output)):
            file = requests.get("https://api.github.com/repos/" + output[x] + "/languages", auth = (myusername, mytoken)) 
            lang_data = json.loads(file.text)
            for y in range(0,len(lang_data)):
                lang.append(list(lang_data)[x])
            git_language['{0}'.format(X.user_name[j])] = list(set(lang))            
    return jsonify(prog_lang) 
##*****************************************************************************************
##4. The weekly commit rate of users (provide a weekly rank ordering) for the submitted project set, for 2018.  
##*****************************************************************************************
@appl.route("/criteria4", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria4():
    commit_rate = {}
    for u in range(0,len(X.user_name)):
        file = requests.get("https://api.github.com/repos/" + X.user_name[u] + X.repo_name[u]"/stats/commit_activity", auth = (myusername, mytoken))        
        json_data = json.loads(file.text)
        
    return jsonify(commit_rate)        
##*****************************************************************************************
##5. The average commit rate of each user to any project, for 2018."""
##*****************************************************************************************
@appl.route("/criteria5", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria5():
    average_commit = {}
    for u in X.user_name:
        flag = 0
        flag1 = 0
        file = requests.get("https://api.github.com/users/" + u + "/repos?per_page=100", auth=(myusername, mytoken))
        json_data = json.loads(file.text)
        output = nested_lookup(key = 'name', document = json_data, wild = False, with_keys = False)
    
        for j in output:
            file = requests.get("https://api.github.com/repos/" + u + j + "/commits?since=2018-01-01", auth = (myusername, mytoken))
            json_data = json.loads(file.text)
            if (len(json_data) != 0):
                flag = flag + 1
                flag1 = len(json_data) + flag1
            else:
                continue
        average_commit['{0}'.format(u)] = (flag1/flag)
    return jsonify(average_commit)  
##*****************************************************************************************
##6. The total number of collaborators in 2018 (ie. a count of other users who have 
##  contributed to any project that the user has contributed to).
##*****************************************************************************************
@appl.route("/criteria6", methods=['GET'])  ##tell Flask what URL should trigger our function.
def criteria6():
    collab = {}
    for u in X.user_name:
        file = requests.get("https://api.github.com/users/" + u + "/repos?per_page=100", auth=(myusername, mytoken))
        json_data = json.loads(file.text)
        output = nested_lookup(key = 'name', document = json_data, wild = False, with_keys = False)
        
    return jsonify(collab)
##*****************************************************************************************
##7. Email Module
##*****************************************************************************************
@appl.route('/email', methods = ['GET','POST'])  ##tell Flask what URL should trigger our function.
def email(SUBJECT, BODY, TO, FROM):
#    if request.method == 'POST':
#        fromad = 'myusername'
#        toad = ""
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = toaddr
        msg['From'] = fromad
        msg.preamble = ""
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        password = 'mytoken'
        server.starttls()
        server.login(fromad, 'mytoken')
        server.sendmail(fromad, toad, msg.as_string())
        server.quit()
        
##**********************************************************************************************
## Main function

if __name__ == "__main__":
    X = main()
    appl.run(port = 9619)	

##**********************************************************************************************
## Email Main function       
    
    server.set_debuglevel(1)  ##To Debug if problem while sending
    
    email_content = ""
    toaddr = 'varnit.g519@gmail.com'
    fromad ='goelv@tcd.ie'
 
    email("Answers to 6 Criteria's", email_content, toaddr, fromad)