Python Code to send Text messages/SMS




import requests
from twilio.rest import Client

api_endpoint = "https://api.twilio.com/2010-04-01/Accounts/ACe34f0af9b106353af8754b667775ad05/Messages.json"
api_key = "164f724606d80fc117bf87d571e120a4"

phone_number = "+917014471298"
message = "This is a test message sent from Python using Twilio API."

data = {
    "To": phone_number,
    "Body": message,
    "From": "+917610805234"  # Replace with your Twilio phone number
}

try:
    response = requests.post(api_endpoint, auth=("ACe34f0af9b106353af8754b667775ad05", api_key), data=data)
    response.raise_for_status()
    print("SMS Successfully Sent")
except requests.exceptions.RequestException as e:
    print("Failed to send SMS. Error:", str(e))
