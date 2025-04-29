from pydantic import BaseModel
from typing import Optional

class InfraestructuraRequest(BaseModel):
    proyecto: str
    tipo_infraestructura: Optional[str] = (
        "Hospital / Museo / Centro Comercial / Túnel / Tren / Data Center / Aeropuerto / Muelle / Puerto Marítimo"
    )
    norma_aplicada: Optional[str] = "NFPA / NEC / ISO / ICAO / IMO"
    nivel_criticidad: Optional[str] = "Alta"
    rubro: Optional[str] = "Infraestructura"

class InfraestructuraResponse(BaseModel):
    mensaje: str
    diseño_cumple_norma: bool
    recomendaciones: Optional[str]
