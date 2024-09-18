import aiohttp
from fastapi import FastAPI, HTTPException

from services.requester import UserService

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    try:
        user_data = await UserService.get_user_data_from_external_api(user_id)
        return {
            "name": user_data["name"],
            "email": user_data["email"]
        }
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=500, detail="Error communicating with external API")
