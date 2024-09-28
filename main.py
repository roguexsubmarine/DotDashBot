import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from morse import morse
from morse_game import generate_random_word_and_answer
import random       
import os
from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv('TG_BOT_API')

bot = Bot(token=TG_API_KEY) 
dp = Dispatcher()

# storing user's game state
user_game_state = {}

# Command Handlers
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Hello! So you are here to master Morse_code\nA little sus don't you think.\nFear not! your secret is same with me.\nLets begin your training.\n\n/help to see actions.")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.reply(
        "Send any text to convert it to Morse code and vice versa.\n\n"
        "or use Available commands:\n"
        "/play - Start the game\n"
        "/exit - End the game\n"
        "/help - Show this help message\n"
        "/u - To display user_id and number of users"
    )   


@dp.message(Command("u"))
async def user_command(message: types.Message):
    user_id = message.from_user.id
    no_of_users = len(user_game_state)
    reply = f"Your user_id : {user_id}\nTotal users : {no_of_users}"
    await message.reply(reply)


@dp.message(Command("play"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_game_state[user_id] = {"playing": True, "score": 0}  # Mark the game as started and initialize score
    await message.reply("Welcome to the Morse Code Learning Game! Choose a difficulty level:", reply_markup=get_level_keyboard())


@dp.message(Command("exit"))
async def exit_game(message: types.Message):
    user_id = message.from_user.id
    
    if user_id in user_game_state and user_game_state[user_id]["playing"]:
        score = user_game_state[user_id]["score"]
        user_game_state[user_id]["playing"] = False 
        await message.reply(f"Thanks for playing! Your final score: {score}. Hope you enjoyed it.")
    else:
        await message.reply("You're not playing a game right now.")


# callback handler for level selection
@dp.callback_query(lambda c: c.data in ["1", "2", "3", "4"])
async def process_level_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_game_state.get(user_id, {}).get("playing", False):
        level = int(callback_query.data)
        user_game_state[user_id]["level"] = level  # Store the selected level
        await callback_query.answer()
        await send_new_question(user_id, level)


async def send_new_question(user_id, level):
    question, options = generate_random_word_and_answer(level)
    correct_ans = options[0]
    random.shuffle(options)
    user_game_state[user_id]["correct_answer"] = correct_ans
    score = user_game_state[user_id]["score"]
    await bot.send_message(
        user_id,
        f"Current Score: {score}\nMorse Code: {question}",
        reply_markup=get_quiz_keyboard(options)
    )


def get_quiz_keyboard(options):
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=option, callback_data=option) for option in options]
    ])
    return keyboard


@dp.callback_query()
async def process_answer_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_game_state.get(user_id, {}).get("playing", False):
        user_answer = callback_query.data
        correct_ans = user_game_state[user_id].get("correct_answer", "")
        if user_answer == correct_ans:
            user_game_state[user_id]["score"] += 5
            await callback_query.answer("✅ Correct!")
            level = user_game_state[user_id].get("level", 2)
            await send_new_question(user_id, level)
        else:
            final_score = user_game_state[user_id]["score"]
            user_game_state[user_id]["playing"] = False
            await callback_query.answer(f"❌ Wrong! The correct answer was: {correct_ans}")
            await bot.send_message(user_id, f"Game Over! Your final score: {final_score}")


@dp.message()
async def echo(message: types.Message):     
    morse_code = morse(message.text) 
    await message.reply(morse_code)  

def get_level_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Level 1", callback_data="1"),
            InlineKeyboardButton(text="Level 2", callback_data="2"),
            InlineKeyboardButton(text="Level 3", callback_data="3"),
            InlineKeyboardButton(text="Level 4", callback_data="4")
        ]
    ])
    return keyboard


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())