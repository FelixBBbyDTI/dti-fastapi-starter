from pydantic import BaseModel
from typing import Optional

class TelecomunicacionesRequest(BaseModel):
    proyecto: str
    tipo_red: Optional[str] = "LAN"
    tecnologia_utilizada: Optional[str] = "Ethernet / Fibra Óptica"
    norma_aplicada: Optional[str] = "TIA/EIA-568 / ISO/IEC 11801"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class TelecomunicacionesResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
