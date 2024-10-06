from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de FastAPI"}

# Definir el esquema de los datos que recibirá el webhook
class WebhookData(BaseModel):
    pregunta: str
    respuesta: str

# Crear el endpoint que recibirá los datos
@app.post("/webhook")
async def receive_webhook(data: WebhookData):
    # Procesar los datos recibidos
    print(f"Pregunta: {data.pregunta}")
    print(f"Respuesta: {data.respuesta}")
    return {"status": "Webhook received"}

