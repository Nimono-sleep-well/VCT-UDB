from dotenv import load_dotenv
load_dotenv()

import os
VCTUDB_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_VOTE = os.getenv("CHANNEL_VOTE")
CHANNEL_TEST = os.getenv("CHANNEL_TEST")
CHANNEL_BOT = os.getenv("CHANNEL_BOT")
CHANNEL_TEAM1 = os.getenv("CHANNEL_TEAM1")
CHANNEL_TEAM2 = os.getenv("CHANNEL_TEAM2")