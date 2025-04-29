from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body")
    sender = form.get("From")
    print(f"Mensaje recibido de {sender}: {incoming_msg}")
    return PlainTextResponse("Mensaje recibido", status_code=200)

