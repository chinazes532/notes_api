from authx import AuthXConfig, AuthX
from src.config import load_config

custom_cfg = load_config()

config = AuthXConfig()
config.JWT_SECRET_KEY = custom_cfg.secret_key
config.JWT_ACCESS_COOKIE_NAME = custom_cfg.cookie_name
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)
