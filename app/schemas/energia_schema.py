from pydantic import BaseModel
from typing import Optional

class EnergiaRequest(BaseModel):
    proyecto: str
    tipo_sistema: Optional[str] = "Solar Fotovoltaico"
    potencia_requerida_kw: Optional[float] = 10.0
    norma_aplicada: Optional[str] = "NEC 690 / IEC 61730"
    nivel_criticidad: Optional[str] = "Media"
    rubro: Optional[str] = "Infraestructura"

class EnergiaResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
