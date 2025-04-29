from pydantic import BaseModel
from typing import Optional

class DeteccionIncendioRequest(BaseModel):
    proyecto: str
    tipo_sistema: Optional[str] = "Convencional / Direccionable"
    norma_aplicada: Optional[str] = "NFPA 72 / ISO 7240"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class DeteccionIncendioResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
