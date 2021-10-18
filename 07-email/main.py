from fastapi import (
    FastAPI, 
    BackgroundTasks, 
    UploadFile, File, 
    Form, 
    Query,
    Body,
    Depends
)
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List, Dict, Any
from fastapi.templating import Jinja2Templates

from dotenv import dotenv_values
config = dotenv_values()




from fastapi_mail.email_utils import DefaultChecker
from pathlib import Path


mail_username = config.get('MAIL_USERNAME')
mail_password = config.get('MAIL_PASSWORD')
mail_from = config.get('MAIL_FROM')

class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: Dict[str, Any]


templates = Jinja2Templates(directory="templates")

conf = ConnectionConfig(
    MAIL_USERNAME = mail_username,
    MAIL_PASSWORD = mail_password,
    MAIL_FROM = mail_from,
    MAIL_PORT =  587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER = Path(__file__).parent / 'templates'
)

app = FastAPI()


@app.post("/email")
async def simple_send( email: EmailSchema = Body(...) ) -> JSONResponse:

#     {
#   "email": [
#     "coreeo@gmail.com"
#   ],
#   "body":
#    {
#     "name": "Nombre",
#     "title": "Mensaje"
# }
# 
# }
    print(email.dict().get('body'))
    message = MessageSchema(
        subject="Prueba de body2",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        template_body=email.dict().get('body'),
        )
 
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html") 
    #Manejar exceptiones                    
    return JSONResponse(status_code=200, content={"ok": True, 'msg': 'Mensaje enviado con exito'})