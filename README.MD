# Telegram Bot with Pyrogram

A Telegram bot that responds to all messages with a welcome message and webapp button, then deletes the original message after 5 seconds.

## Environment Variables

Required:
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API hash
- `BOT_TOKEN`: Your Telegram bot token from BotFather

Optional:
- `WEB_APP_URL`: URL for the web app button (default: https://example.com)
- `WEB_APP_BUTTON_TEXT`: Text for the web app button (default: "Open Web App")
- `WELCOME_MESSAGE`: Custom welcome message
- `DELETE_DELAY`: Delay in seconds before deleting messages (default: 5)

## Deployment on NorthFlank

1. Create a new project on NorthFlank
2. Add a new service using this repository
3. Set the environment variables in the NorthFlank dashboard
4. Deploy the service
