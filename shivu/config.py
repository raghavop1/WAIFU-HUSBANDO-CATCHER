class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6325295720"
    sudo_users = "6768723634"
    GROUP_ID = "-1002100894623"
    TOKEN = "7055204971:AAHbREm4BeNyKXxXWidGWA4jXqn9KHKZVIo"
    mongo_url = "mongodb+srv://raghavvvv09:DpaQVcz8AJW8grFX@cluster0.edbvlbl.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/e82d9ba84396bf1b1a9ca.jpg", "https://telegra.ph/file/e370ab1aeea76df6024c8.jpg"]
    SUPPORT_CHAT = "raghavsupport"
    UPDATE_CHAT = "raghavsupport"
    BOT_USERNAME = "WAIFU_HUSBANDOBOT"
    CHARA_CHANNEL_ID = "-1002100894623"
    api_id = "23502611"
    api_hash = "c90db27ac20cdd45b4f349d21d531a79"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
