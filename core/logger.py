from pathlib import Path
from loguru import logger
from pydantic import BaseModel, Field
from typing import Optional


class Logger(BaseModel):
    debug: bool = False
    logs_dir: Path = Field(default_factory=lambda: Path("logs"))
    default_log_path: Path = Field(default_factory=lambda: Path("logs/app.log"))

    log_format_console: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )

    log_format_file: str = (
        "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | "
        "{name}:{function}:{line} - {message}"
    )

    class Config:
        arbitrary_types_allowed = True

    def __post_init_post_parse__(self):
        self.logs_dir.mkdir(exist_ok=True)
        self.default_log_path = self.logs_dir / "app.log"

    def configure(self):
        log_level = "DEBUG" if self.debug else "INFO"
        logger.remove()

        # Console handler
        logger.add(
            sink=lambda msg: print(msg, end=""),
            level=log_level,
            format=self.log_format_console,
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )

        # Main log file
        logger.add(
            str(self.default_log_path),
            level=log_level,
            format=self.log_format_file,
            rotation="10 MB",
            retention="10 days",
            compression="zip",
            encoding="utf-8",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )

    def get_logger(self, name: str = "default"):
        """Returns a logger instance bound to the given module name."""
        self.configure()

        module_log_file = self.logs_dir / f"{name}.log"

        logger.add(
            str(module_log_file),
            level="DEBUG",
            format="{time} | {level} | {message}",
            rotation="5 MB",
            retention="5 days",
            compression="zip",
            encoding="utf-8",
        )

        return logger.bind(module=name)
