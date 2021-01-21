from django.shortcuts import render
from datetime import datetime
from .models import Phone
import base64
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
class generateKey:
    @staticmethod
    def returnValue(mobile):
        return str(mobile) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class Mobile_verification(APIView):
    
    @staticmethod
    def get(request, mobile):
        try:
            Mobile_number = Phone.objects.get(Mobile_number=mobile)
        except ObjectDoesNotExist:
            Phone.objects.create(Mobile_number=mobile)
            Mobile_number = Phone.objects.get(Mobile_number=mobile)
        Mobile_number.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(mobile).encode())
        OTP = pyotp.TOTP(key, interval=300)
        print (OTP.now())
        return Response({"OTP":OTP.now()},status=200)
    
    @staticmethod
    def post(request,mobile):
        try:
            Mobile_number = Phone.objects.get(Mobile_number=mobile)
        except ObjectDoesNotExist:
            return Response("User does not exist, check the number",status=404)
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(mobile).encode())
        OTP = pyotp.TOTP(key,interval=300)
        if OTP.verify(request.data["OTP"]):
            Mobile_number.isVerified = True
            Mobile_number.save()
            return Response("Verified",status=200)
        return Response("Wrong OTP",status=400)





