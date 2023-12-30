import pywhatkit

# Install PyWhatKit if not already installed
try:
  import pywhatkit
except ImportError:
  print("Installing PyWhatKit...")
  import os
  os.system("pip install pywhatkit")  # Install using pip

# Set recipient's phone number (including country code)
phone_number = "+1234567890"  # Replace with the actual recipient's number

# Set the message to be sent
message = "Hello from Python! This is an automated WhatsApp message."

# Options for sending the message:

# 1. Send instantly:
pywhatkit.sendwhatmsg_instantly(phone_number, message)

# 2. Schedule for a specific time (24-hour format):
# pywhatkit.sendwhatmsg(phone_number, message, time_hour=10, time_min=30)  # Send at 10:30 AM

# Crucial steps before running the code:

# 1. Make sure you have WhatsApp Web enabled on your browser.
# 2. Scan the QR code using your phone to log in to WhatsApp Web.
# 3. Keep WhatsApp Web running in the background while executing the code.

