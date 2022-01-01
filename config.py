from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQAdUZuggMpOq-lPI4-NMrSvoiMhMkZb9CdgYLJya_TxVOf8Y_EUsUuMpl7qVizmjwqYzz_yiU0OrTqEhQ3BRedGGnxHEY8qw8KCZ2NQDHu5uRrh07ZV_uWGTdMG3jJVl8n4JCokZXPGPP0y-ubB9cunyRLozPqldonsRvCKjdxXZRI9Nn3E1htm53PQMSc1hCHju5VOlAFzwoA9_zr_WJrR-EvHnZgDIjt5dGLDdD9YDQN8E53ASoDM-qRB1H58e-5JHnsUnZtlCi_qwkn407-MQeXsyMuRzofG5ZVaHvuaa-mizFgYZ104V0L1y3S1DZPaRce9PI0SJj8OUY-J20UIfbIblgA")
BOT_TOKEN = getenv("2100234484:AAH5lDwl8OIHFNGUCeCZe6w8Gcoirzdxt9k")
API_ID = int(getenv("API_ID", "11461788"))
API_HASH = getenv("e090f8d649c80b63f6c0967689f4f160")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "100"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("mongodb+srv://Subhixd:subhivikalxd@cluster0.znhge.mongodb.net/Subhixd?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2140620978").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5032100535").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001755837985"))
MUSIC_BOT_NAME = getenv("Florenza_bot")
PING_IMG = getenv("PING_IMG")
if str(getenv("SUPPORT_CHANNEL")).strip() == "http//t.me/starz_bots":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "http//t.me/starz_support":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
