from fastapi import APIRouter
from app.schemas.deteccionincendio_schema import DeteccionIncendioRequest, DeteccionIncendioResponse

router = APIRouter()

@router.post("/", response_model=DeteccionIncendioResponse)
async def evaluar_deteccion_incendio(data: DeteccionIncendioRequest):
    return DeteccionIncendioResponse(
        mensaje="Evaluación del sistema de detección de incendio completada.",
        diseño_cumple_norma=True,
        recomendaciones="Considerar detección temprana en áreas críticas y mantenimiento de dispositivos de alarma según NFPA 72."
    )
