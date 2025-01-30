from typing import List
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

ROLES = ['admin', 'moderator', 'treasurer', 'gm', 'member', 'guest']

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    tg_id : Mapped[int] = mapped_column(BigInteger)
    nickname_tg : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    nickname_game : Mapped[str] = mapped_column(String(50),  unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String(50))
    user_role: Mapped[str] = mapped_column(String(30), default='guest')
    user_profession: Mapped[str] = mapped_column(String(30), default='Newbie')

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
