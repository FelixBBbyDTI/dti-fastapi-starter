from pydantic import BaseModel
from typing import Optional

class DataCenterRequest(BaseModel):
    proyecto: str
    nivel_uptime: Optional[str] = "Tier III"
    sistema_refrigeracion: Optional[str] = "CRAC / InRow Cooling"
    norma_aplicada: Optional[str] = "TIA-942 / NFPA 75"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class DataCenterResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
