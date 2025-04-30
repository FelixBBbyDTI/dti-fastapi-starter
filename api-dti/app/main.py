from fastapi import FastAPI

from app.api.endpoints import (
    instrumentacion,
    valvulas,
    fibraoptica,
    energia,
    infraestructura,
    sistemacontrol,
    telecomunicaciones,
    controlacceso,
    cctv,
    datacenter,
    saladecontrol,
    deteccionincendio
)

app = FastAPI(
    title="API DTI Félix Blas",
    description="Servidor de apoyo para proyectos de Instrumentación, Control, Telecomunicaciones, Seguridad Electrónica, Infraestructura Crítica, Energía Renovable y Sistemas Contra Incendios.",
    version="2.0.0"
)

# Incluir routers principales
app.include_router(instrumentacion.router, prefix="/instrumentacion", tags=["Instrumentación"])
app.include_router(valvulas.router, prefix="/valvulas", tags=["Válvulas de Control"])
app.include_router(fibraoptica.router, prefix="/fibraoptica", tags=["Fibra Óptica"])
app.include_router(energia.router, prefix="/energia", tags=["Energía Renovable"])
app.include_router(infraestructura.router, prefix="/infraestructura", tags=["Infraestructura Crítica"])

# Nuevos sistemas añadidos
app.include_router(sistemacontrol.router, prefix="/sistemacontrol", tags=["Sistema de Control"])
app.include_router(telecomunicaciones.router, prefix="/telecomunicaciones", tags=["Telecomunicaciones"])
app.include_router(controlacceso.router, prefix="/controlacceso", tags=["Control de Acceso"])
app.include_router(cctv.router, prefix="/cctv", tags=["CCTV"])
app.include_router(datacenter.router, prefix="/datacenter", tags=["Data Centers"])
app.include_router(saladecontrol.router, prefix="/saladecontrol", tags=["Salas de Control"])
app.include_router(deteccionincendio.router, prefix="/deteccionincendio", tags=["Detección de Incendios"])

from app.whatsapp_bot import router as whatsapp_router
app.include_router(whatsapp_router, prefix="", tags=["WhatsApp"])


