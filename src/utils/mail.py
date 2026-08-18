import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from typing import List
from dotenv import load_dotenv

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Musify",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


async def send_registration_email(email: List[str]):
    html = """<p>Hi, Thanks for the registration. Our team will connect with you soon.</p>"""

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=email,
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "Email has been sent"}