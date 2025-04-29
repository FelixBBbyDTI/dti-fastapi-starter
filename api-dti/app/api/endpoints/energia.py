from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_energia():
    return {"mensaje": "Diseño de sistemas de energía renovable (solar/eólico) validado exitosamente."}
