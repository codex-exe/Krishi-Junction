from django.http import HttpResponse
from django.shortcuts import render
import firebase_admin
from firebase_admin import firestore
import os

cred = firebase_admin.credentials.Certificate("D:\hackathon\GFG\KrishiJunctionBackend\soilapi\solvingforind-firebase-adminsdk-eeo83-44ba4946bc.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

# Create your views here.
def test(request):
    doc_ref = firestore_client.collection("npkvalue").document("hello")
    doc_ref.set({
        "Name": "Hello",
        "age": 21
    })
    return HttpResponse("done")

def npkvalue(request):
    nitrogen = request.GET['nitrogen']
    potassium = request.GET['potassium']
    phosphorous = request.GET['phos']
    return HttpResponse(f"{nitrogen} {potassium} {phosphorous}")
