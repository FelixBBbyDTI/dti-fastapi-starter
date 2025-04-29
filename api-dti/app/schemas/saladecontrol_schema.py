from pydantic import BaseModel
from typing import Optional

class SalaDeControlRequest(BaseModel):
    proyecto: str
    tipo_operacion: Optional[str] = "SCADA / HMI"
    norma_aplicada: Optional[str] = "ISA-101 / ISO 11064"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Minería / Oil&Gas / Infraestructura"

class SalaDeControlResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
