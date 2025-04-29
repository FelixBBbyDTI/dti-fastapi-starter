from pydantic import BaseModel
from typing import Optional

class ControlAccesoRequest(BaseModel):
    proyecto: str
    tipo_sistema: Optional[str] = "RFID"
    tecnologia_utilizada: Optional[str] = "Tarjetas Proximidad / Biometría"
    norma_aplicada: Optional[str] = "NFPA 731 / IEC 60839"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class ControlAccesoResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
