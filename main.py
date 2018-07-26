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
        