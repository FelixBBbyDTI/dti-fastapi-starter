from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_instrumentacion():
    return {"mensaje": "Revisión de Instrumentación completada exitosamente."}
