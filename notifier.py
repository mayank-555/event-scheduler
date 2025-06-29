import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


EMAIL_RECEIVERS = os.getenv("EMAIL_RECEIVER", "").split(",")

def send_email_notification(subject, body, receivers=None):
    """
    Send email to one or more recipients.

    :param subject: Email subject
    :param body: Email body
    :param receivers: Optional list of recipient emails (defaults to EMAIL_RECEIVERS)
    """
    if receivers is None:
        receivers = [r.strip() for r in EMAIL_RECEIVERS if r.strip()]

    if not receivers:
        print("❌ No email recipients provided.")
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(receivers)
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent to {msg['To']}!")
    except Exception as e:
        print("❌ Failed to send email:", e)


if __name__ == "__main__":
    send_email_notification(
        subject="📬 Test Email from Flask Event Scheduler",
        body="🎉 This is a test email sent via Gmail SMTP to multiple people!"
    )
