import asyncio
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)

from config import config

app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

async def delete_message_after_delay(chat_id: int, message_id: int, delay: int):
    """Delete a message after a specified delay"""
    await asyncio.sleep(delay)
    try:
        await app.delete_messages(chat_id, message_id)
    except Exception as e:
        print(f"Error deleting message: {e}")

@app.on_message(filters.private & ~filters.command("start"))
async def handle_message(client: Client, message: Message):
    """Handle all private messages"""
    # Create webapp button
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            text=config.WEB_APP_BUTTON_TEXT,
            web_app={"url": config.WEB_APP_URL}
        )]]
    )
    
    # Send welcome message with button
    welcome_msg = await message.reply(
        config.WELCOME_MESSAGE2,
        reply_markup=keyboard
    )
    
    # Schedule original message for deletion
    asyncio.create_task(
        delete_message_after_delay(
            message.chat.id,
            message.id,
            config.DELETE_DELAY
        )
    )

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            text=config.WEB_APP_BUTTON_TEXT,
            web_app={"url": config.WEB_APP_URL}
        )]]
    )
    
    await message.reply(
        config.WELCOME_MESSAGE,
        reply_markup=keyboard
    )

if __name__ == "__main__":
    print("Starting bot...")
    app.run()
