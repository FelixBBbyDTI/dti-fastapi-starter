from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_infraestructura():
    return {
        "mensaje": "Diseño y verificación de infraestructura crítica (hospitales, museos, centros comerciales, túneles, trenes, data centers, aeropuertos, muelles, puertos marítimos) completado exitosamente."
    }
