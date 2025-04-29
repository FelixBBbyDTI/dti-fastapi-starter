from pydantic import BaseModel
from typing import Optional

class CCTVRequest(BaseModel):
    proyecto: str
    tipo_camara: Optional[str] = "IP"
    resolucion: Optional[str] = "1080p / 4K"
    norma_aplicada: Optional[str] = "NFPA 731 / IEC 62676"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class CCTVResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
