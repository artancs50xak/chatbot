from pathlib import Path

MODEL_PATH = "./Qwen2.5-0.5B-Instruct"
MAX_NEW_TOKENS = 512
TEMPERATURE = 0.7
TOP_P = 0.9

HISTORY_FILE = Path("chat_history.json")

USER_AVATAR = "https://api.dicebear.com/9.x/thumbs/svg?seed=user"
BOT_AVATAR = "https://ap.dicebear.com/9.x/bottts/svg?seed=qwen"