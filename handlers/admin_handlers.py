from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from filters.is_admin import is_admin
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

router.message.filter(is_admin)


@router.message(CommandStart())
async def admin_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])
    await message.answer(text=LEXICON_RU['test_admin'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    await message.answer(text=LEXICON_RU['test_admin'])
