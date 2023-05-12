from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import firebase_admin
from firebase_admin import firestore
import os

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
    doc_ref = firestore_client.collection(f"npkvalue/devices/{deviceId}").document(f"timeunit")
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
    # return HttpResponse(f"{nitrogen} {potassium} {phosphorous} {deviceId} {timeunit} {ph}")
