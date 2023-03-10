from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from pathlib import Path
from starlette.responses import JSONResponse
from ..core.config import get_settings

class EmailSchema(BaseModel):
    email: List[EmailStr]

settings = get_settings()

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_FROM_NAME= settings.mail_from_name,
    TEMPLATE_FOLDER = Path(__file__).parent.parent / 'templates',
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True
)


async def send_email(email: EmailStr, data):
    message = MessageSchema(
        subject="Stori balance",
        recipients=[email],
        template_body = {
            "email": email,
            "total_balance": data.total,
            "debit": data.debit,
            "credit": data.credit,
            "monthly_transactions": data.monthly_transactions.__dict__,
        },
        subtype="html")

    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")
    return JSONResponse(status_code=200, content={"message": "email has been sent"})