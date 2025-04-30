from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook")
def recibir_mensaje():
    return {"mensaje": "Webhook recibido exitosamente"}


