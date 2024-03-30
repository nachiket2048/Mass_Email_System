import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'test@gmail.com'  # Replace with your email
sender_password = 'password'  # Replace with your password or app-specific password
subject = 'Test Mail'

# Read the email body from a text file
with open('email_body.txt', 'r') as file:
    body = file.read()

# Function to send email
def send_email(recipient):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Convert the message to a string and send it
    server.sendmail(sender_email, recipient, msg.as_string())

# Set up the email server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Upgrade the connection to secure
server.login(sender_email, sender_password)

# Read recipients from CSV and send emails
with open('recipients.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        send_email(row['email'])

# Close the server connection
server.quit()

print("Emails sent successfully!")
