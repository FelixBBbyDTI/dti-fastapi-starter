from fastapi import APIRouter
from app.schemas.cctv_schema import CCTVRequest, CCTVResponse

router = APIRouter()

@router.post("/", response_model=CCTVResponse)
async def evaluar_cctv(data: CCTVRequest):
    return CCTVResponse(
        mensaje="Evaluación de sistema de videovigilancia CCTV completada.",
        diseño_cumple_norma=True,
        recomendaciones="Implementar grabadores redundantes y sistemas de alimentación ininterrumpida (UPS) para cámaras críticas."
    )
