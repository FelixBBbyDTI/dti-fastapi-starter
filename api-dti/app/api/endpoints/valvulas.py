from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_valvulas():
    return {"mensaje": "Revisión de Válvulas de Control completada exitosamente."}
