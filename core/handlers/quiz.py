from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from core.keyboards.for_questions import get_quiz_keyboard

router = Router()

@router.message(Command("start"))