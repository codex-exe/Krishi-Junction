from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import firebase_admin
from firebase_admin import firestore
import os

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

cred = firebase_admin.credentials.Certificate("D:\hackathon\GFG\KrishiJunctionBackend\soilapi\solvingforind-firebase-adminsdk-eeo83-44ba4946bc.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

# Create your views here.
def test(request):
    doc_ref = firestore_client.collection("npkvalue/devices/shivam").document("hello")
    doc_ref.set({
        "Name": "Hello",
        "age": 21
    })
    return HttpResponse("done")

# String date = dateStr;         // Replace with the current date
#   String Time = timeStr;       // Replace with the current time
#   String nitrogen = "10";      // Replace with the nitrogen value
#   String phosphorus = "5";     // Replace with the phosphorus value
#   String potassium = "7";      // Replace with the potassium value
#   String pH = "6.5";           // Replace with the pH value

def npkvalue(request):
    deviceId = request.GET['id']
    dateunit = request.GET['dateunit']
    timeunit = request.GET['timeunit']
    nitrogen = request.GET['nitrogen']
    potassium = request.GET['potassium']
    phosphorous = request.GET['phos']
    ph = request.GET['ph']
    doc_ref = firestore_client.collection(f"npkvalue/devices/{deviceId}").document(f"{timeunit}")
    doc_ref.set({
        "dateunit": dateunit,
        "timeunit": timeunit,
        "nitrogen": nitrogen,
        "potassium": potassium,
        "phosphorous": phosphorous,
        "pH": ph
    })
    return JsonResponse({
        "status": "success"
    }, safe=False)

def crop_pred(request):
    n = request.GET['nitrogen']
    p = request.GET['phosphorous']
    k = request.GET['potassium']
    temp = request.GET['temperature']
    humid = request.GET['humidity']
    ph = request.GET['ph']
    rainfall = request.GET['rainfall']
    model = pickle.load(open('D:\hackathon\GFG\KrishiJunctionBackend\soilapi\crop_pred.pkl','rb'))
    output = model.predict([[n, p, k, temp, humid, ph, rainfall]])[0]
    return JsonResponse({
        "status":"success",
        "data": output
    }, safe=False)