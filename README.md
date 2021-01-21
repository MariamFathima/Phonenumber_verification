# Phonenumber_verification
Verify phone number via OTP
(This is Time based OTP generation)

Endpoints

To register the mobile number and get OTP
  http://127.0.0.1:8000/mobile_auth/<phone>
  
To Verify the OTP 
  http://127.0.0.1:8000/mobile_auth/<phone>/
  In the Json body fill in the OTP recieved from the above endpoint.
