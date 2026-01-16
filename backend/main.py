from fastapi import FastAPI
from routes.user_route import router


app= FastAPI(title="Task5")

app.include_router(router)



