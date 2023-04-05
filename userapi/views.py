from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
import os
import pyrebase

FIREBASE_CONFIG = {
  "apiKey": "AIzaSyDkAu8EB4WwJsYRUJx-XAWE4vPWBIeJAlg",
  "authDomain": "solvingforind.firebaseapp.com",
  "projectId": "solvingforind",
  "storageBucket": "solvingforind.appspot.com",
  "messagingSenderId": "295357938280",
  "appId": "1:295357938280:web:ea1d82d9344fa38a6619dd",
  "measurementId": "G-5XQ1CF977S",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = firebase.auth()

# Create your views here.
def signup(request):
    return HttpResponse("Hello world")

def signin(request):
    pass

def logout(request):
    pass

def createUser(request):
    auth.create_user_with_email_and_password("shivam@gmail.com", "abc@12345")
    return HttpResponse("done!")

def updateProfile(request):
    pass