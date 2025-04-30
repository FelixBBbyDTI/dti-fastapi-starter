from pydantic import BaseModel
from typing import Optional

class InstrumentacionRequest(BaseModel):
    proyecto: str
    norma_aplicada: Optional[str] = "ISA/IEC"
    tipo_sistema: Optional[str] = "Instrumentación de proceso"
    nivel_criticidad: Optional[str] = "Media"
    rubro: Optional[str] = "Oil & Gas"

class InstrumentacionResponse(BaseModel):
    mensaje: str
    cumplimiento_normas: bool
    recomendaciones: Optional[str]
