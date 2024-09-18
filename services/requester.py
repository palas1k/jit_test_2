import aiohttp
from fastapi import HTTPException


class UserService:

    @staticmethod
    async def get_user_data_from_external_api(user_id: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}") as response:
                if response.status != 200:
                    raise HTTPException(status_code=404, detail="User not found")
                return await response.json()
