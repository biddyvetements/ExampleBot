from typing import Coroutine, Optional

from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

Base = declarative_base()
__factory__: Optional[sessionmaker] = None


async def global_init(SQLALCHEMY_DATABASE_URL: str):
    global __factory__
    if __factory__:
        return
    logger.info(f'Connecting to database on {SQLALCHEMY_DATABASE_URL}')
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL,
        future=True
    )
    __factory__ = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_session() -> AsyncSession:
    global __factory__
    return __factory__()
