from typing import Optional

from aiogram.client.session import aiohttp


async def get_usd_price() -> Optional[float]:
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Aomo4Ir3j25XIKXLIz46YoDcRtE6ATqjVNB94gFk") as response:
            response_json = await response.json()
            return round(response_json['data']["RUB"], 2)
