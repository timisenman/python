from twilio.rest import TwilioRestClient

account_sid = "AC2b72cb08e65259dd4a25fe388c8f8525" # Your Account SID from www.twilio.com/console
auth_token  = "40e73b9b5ce81352170e6809294be8b8"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="BIRD UP",
    to="+15624578178",    # Replace with your phone number
    from_="+13106834199") # Replace with your Twilio number

print(message.sid)
