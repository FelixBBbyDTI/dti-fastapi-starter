from pydantic import BaseModel
from typing import Optional

class ValvulasRequest(BaseModel):
    proyecto: str
    tipo_valvula: str
    accionamiento: Optional[str] = "On/Off"
    norma_aplicada: Optional[str] = "API 6D"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Oil & Gas"

class ValvulasResponse(BaseModel):
    mensaje: str
    seleccion_valvula_correcta: bool
    recomendaciones: Optional[str]
