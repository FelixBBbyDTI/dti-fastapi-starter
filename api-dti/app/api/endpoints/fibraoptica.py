from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_fibraoptica():
    return {"mensaje": "Diseño y revisión de fibra óptica completado exitosamente."}
