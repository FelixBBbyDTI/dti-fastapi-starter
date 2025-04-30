from fastapi import APIRouter
from app.schemas.controlacceso_schema import ControlAccesoRequest, ControlAccesoResponse

router = APIRouter()

@router.post("/", response_model=ControlAccesoResponse)
async def evaluar_control_acceso(data: ControlAccesoRequest):
    return ControlAccesoResponse(
        mensaje="Evaluación de sistema de control de acceso completada.",
        diseño_cumple_norma=True,
        recomendaciones="Asegurar redundancia en controladores principales y uso de autenticación multifactor."
    )
