import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1702905977:AAEnCcpP3Djw3hqcGERz75kdeyDjjdG3jI4")

    APP_ID = int(os.environ.get("APP_ID", 2553309))

    API_HASH = os.environ.get("API_HASH", "5abb410f4fdb9661906bceaf12ead92a")
