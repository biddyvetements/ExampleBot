from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.user import User
from db.utils.common import create_session


async def get_user_by_tg_id(user_id: int) -> Union[User, None]:
    session = await create_session()
    async with session.begin():
        result = await session.execute(select(User).where(User.id == user_id))
        result = result.scalars().first()
    return result


async def insert_user(user: User):
    session = await create_session()
    async with session.begin():
        session.add(user)
