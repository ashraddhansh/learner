import pywhatkit
import time

# List of phone numbers (with country codes)
numbers = ["+210", "+78901", "67890"]

# Message to be sent
message = "This is a WhatsApp message sent using Python!"

# Iterate through the list of numbers and send the message
for number in numbers:
    pywhatkit.sendwhatmsg_instantly(
        phone_no=number,
        message=message,
        wait_time=15  # Adjust wait time if needed
    )
    print(f"Message sent to {number}.")
    time.sleep(10)  # Add a delay between messages to avoid rate limits
