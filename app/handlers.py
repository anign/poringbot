from aiogram import F, Router

from sqlalchemy.exc import IntegrityError

from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.keybords import main_keyboard, reply_keyboard
from app.parsers import parse_castles
import app.db.requests as rq

from app.validators import *

router = Router()
class Register(StatesGroup):
    nickname_game = State()
    about = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! Пожалуйста, зарегистрируйтесь(кнопка ниже)', reply_markup=reply_keyboard)


@router.callback_query(F.data == 'castles')
async def castles(callback: CallbackQuery):
    await callback.answer('')
    #await callback.message.answer(f'Наши замки: {await parse_castles()}')
    cstls = await parse_castles()
    if len(cstls) > 1:
        await callback.message.answer(f'Наши доблестные WoE`ны захватили: {cstls}')
    await callback.message.answer(f'Замки: {cstls}')

@router.message(F.text == 'Регистрация')
async def register(message: Message, state:FSMContext):
    await message.answer('Введите ник основного персонажа(кем ходите на ГВ)')
    await state.set_state(Register.nickname_game)


@router.message(F.text == 'О нас')
async def with_puree(message: Message):
    await message.answer('Мы сильные, смелые, ловкие, умелые - JOIN US!')

@router.message(F.text == 'Вакансии')
async def with_puree(message: Message):
    await message.answer('Ты нам нужен - JOIN US!')


@router.message(Register.nickname_game)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(nickname_game=message.text)
    data = await state.get_data()

    try:
        await rq.set_user(message.from_user.id,
                            message.from_user.username,
                            message.from_user.full_name,
                            nickname_game=data['nickname_game'])
        await message.answer(f'{message.from_user.full_name}, благодарю за регистрацию!',
                                    reply_keyboard=main_keyboard)
    except IntegrityError:
        await message.answer('Похоже вы уже зарегистрированы')
        
    await state.clear()