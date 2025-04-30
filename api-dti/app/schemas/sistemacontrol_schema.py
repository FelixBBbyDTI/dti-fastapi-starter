from pydantic import BaseModel
from typing import Optional

class SistemaControlRequest(BaseModel):
    proyecto: str
    tipo_control: Optional[str] = "DCS"
    fabricante_preferido: Optional[str] = "ABB / Siemens / Yokogawa / Rockwell"
    norma_aplicada: Optional[str] = "ISA / IEC 61508 / IEC 61131"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Oil & Gas"

class SistemaControlResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
