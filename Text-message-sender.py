# Python Code to send Text messages/SMS



from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

phone_number = "+91**********"  # Replace this with recipient's phone number
message = "This is a test message sent from Python using Twilio API."

message = client.messages.create(
    body=message,
    from_="your_twilio_phone_number",
    to=phone_number
)

print("SMS Sent with SID:", message.sid)
