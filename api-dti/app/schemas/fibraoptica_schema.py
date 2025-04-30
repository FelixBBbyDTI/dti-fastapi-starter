from pydantic import BaseModel
from typing import Optional

class FibraOpticaRequest(BaseModel):
    proyecto: str
    tipo_fibra: Optional[str] = "Monomodo"
    tipo_tendido: Optional[str] = "Subterráneo"
    cantidad_postes: Optional[int] = 0
    norma_aplicada: Optional[str] = "TIA/EIA-568"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class FibraOpticaResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
