#pip install vonage
#pip install nexmo

import vonage
client = vonage.Client(key="your key", secret="your secret key")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "recievers phone number here",     #with country code
        "text": "hello, this is python generated text message",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
