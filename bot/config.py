import os
from dotenv import load_dotenv
from typing import Optional

class CONFIG:
    def __init__(self):
        """Initialize with None values"""
        self.bot_token: Optional[str] = None
        self.owner_id: Optional[int] = None
        self.show_bot_pic: bool = False # Default Value
        self.server_url: Optional[str] = None

        self.mongodb_uri: Optional[str] = None
        self.db_name: Optional[str] = None

        self.shrinkme_api: Optional[str] = None
        self.omdb_api: Optional[str] = None
        self.weather_api: Optional[str] = None

        self.max_video_size: int = 15728640  # Default 15 MB in bytes
        self.max_audio_size: int = 8388608  # Default 8 MB in bytes
        self.max_tg_file_size: int = 52428800  # Default 50 MB in bytes
        self.vip_user_id: int = 0
        self.err_loading_video_url: Optional[str] = None
        self.err_video_width: int = 640
        self.err_video_height: int = 480
        self.err_video_duration: int = 5
        self.ph_loading_video_url: Optional[str] = None
        self.ph_thumbnail_url: Optional[str] = None
        self.ph_video_width: int = 1024
        self.ph_video_height: int = 576
        self.ph_video_duration: int = 10
        self.media_chat_id: int = 0
        self.rate_limit_window_minutes: int = 1

    def load_config(self, config_file) -> None:
        """
        Load configuration from .env file\n
        :param config_file: .env file path
        """
        load_dotenv(config_file)

        # ----- BOT CONFIGURATION -----
        self.bot_token = os.getenv("BOT_TOKEN")
        self.owner_id = int(os.getenv("OWNER_ID") or 0)
        self.vip_user_id = self.owner_id
        
        # ----- DATABASE -----
        self.mongodb_uri = os.getenv("MONGODB_URI")
        self.db_name = os.getenv("DB_NAME")

        # ----- API KEYS -----
        self.shrinkme_api = os.getenv("SHRINKME_API")
        self.omdb_api = os.getenv("OMDB_API")
        self.weather_api = os.getenv("WEATHER_API")

        # ----- VIDEO CONFIGURATION -----
        self.max_video_size = int(os.getenv("MAX_VIDEO_SIZE", 15728640))
        self.max_audio_size = int(os.getenv("MAX_AUDIO_SIZE", 8388608))
        self.max_tg_file_size = int(os.getenv("MAX_TG_FILE_SIZE", 52428800))
        self.err_loading_video_url = os.getenv("ERR_LOADING_VIDEO_URL", "https://magicxor.github.io/static/ytdl-inline-bot/error_v1.mp4")
        self.err_video_width = int(os.getenv("ERR_VIDEO_WIDTH", 640))
        self.err_video_height = int(os.getenv("ERR_VIDEO_HEIGHT", 480))
        self.err_video_duration = int(os.getenv("ERR_VIDEO_DURATION", 5))
        self.ph_loading_video_url = os.getenv("PH_LOADING_VIDEO_URL", "https://magicxor.github.io/static/ytdl-inline-bot/loading_v2.mp4")
        self.ph_thumbnail_url = os.getenv("PH_THUMBNAIL_URL", "https://magicxor.github.io/static/ytdl-inline-bot/loading_v1.jpg")
        self.ph_video_width = int(os.getenv("PH_VIDEO_WIDTH", 1024))
        self.ph_video_height = int(os.getenv("PH_VIDEO_HEIGHT", 576))
        self.ph_video_duration = int(os.getenv("PH_VIDEO_DURATION", 10))
        self.media_chat_id = int(os.getenv("MEDIA_CHAT_ID", 0))
        self.rate_limit_window_minutes = int(os.getenv("RATE_LIMIT_WINDOW_MINUTES", 1))
    

    def validate(self) -> bool:
        """Check if required configurations are present"""
        required = [
            self.bot_token,
            self.mongodb_uri,
            self.db_name
        ]

        return all(required)
