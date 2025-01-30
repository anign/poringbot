from  app.db.models import async_session
from app.db.models import User

from sqlalchemy import select, update, delete

async def set_user(tg_id: int, nickname_tg: str, name: str,
                   nickname_game:str='', user_profession:str='Newbie') -> None:
    async with async_session() as session:
        #user = await session.scalar(select(User).where(User.tg_id == tg_id))
        #user = await session.scalar(select(User).where(User.nickname_tg == nickname_tg))
        user = User(tg_id=tg_id,
                    nickname_tg=nickname_tg,
                    name=name,
                    nickname_game=nickname_game,
                    user_profession=user_profession)
        session.add(user)
        await session.commit()
        if not user:
            session.add(User(tg_id = tg_id,
                             nickname_tg = nickname_tg,
                             name=name,
                             nickname_game=nickname_game,
                             user_profession=user_profession))
            await session.commit()