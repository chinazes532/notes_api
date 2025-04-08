from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database_url: str


@dataclass
class Config:
    db: DatabaseConfig


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DatabaseConfig(database_url=env("DATABASE_URL"))
    )