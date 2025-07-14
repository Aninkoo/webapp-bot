import os

class Config:
    # Telegram API credentials
    API_ID = int(os.getenv('API_ID', 0))
    API_HASH = os.getenv('API_HASH', '')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')
    
    # Web App settings
    WEB_APP_URL = os.getenv('WEB_APP_URL', 'https://example.com')
    WEB_APP_BUTTON_TEXT = os.getenv('WEB_APP_BUTTON_TEXT', 'Open Catalog')
    
    # Message settings
    WELCOME_MESSAGE = os.getenv('WELCOME_MESSAGE', 
        "👋 <b>Welcome!</b>\n\n"
        "Click the button below to launch <b>PaxMOVIES Catalog</b> webapp:")

    WELCOME_MESSAGE2 = os.getenv('WELCOME_MESSAGE', 
        "🔎 <b>Search in Catalog!</b>\n\n"
        "Click the button below to launch <b>PaxMOVIES Catalog</b> webapp:")
    
    
    # Deletion delay in seconds
    DELETE_DELAY = int(os.getenv('DELETE_DELAY', 5))

# Create config instance
config = Config()
