from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("20244017"))
API_HASH = getenv("05bfa0d1f85496c72804fa075c3d6846")

BOT_TOKEN = getenv("8210785668:AAHExai5uP3q73J7XkSDPgsqCQo3e4a6MoY", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5940151418"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQGyJToAjEknU4yqYVl8BX0rfuTtezSS55n2ZtiEsBcO2-BlQXDV9WKT2v42VSVH4l-cTJE8Ce1746AUc546nM5vDh0F4DA2G2zSLIgnmE-PjxfyW7BnIg5WDW9pinsv5g2W2OCDCj6cKYi74PhzFyc6Phriwsn0vh-_GM5lNMBH9U6kQa5YJipe-A1fr6fJAjHmiV9HA7xhFJYW2K3BDw4O0lmRPKD260gnRGgbgJ0mImry5aJfUiVB7PGTVTez_K1HrA9j1SCxnDoqgl_65BHcFUy6X1kANvvo0pWVAztDdMtk7t3R5O3vRWxNaL97-vsAA26iIrON5D0aCd98aBcLCN4w4gAAAAFEUNWrAA", None)

SUPPORT_CHAT = getenv("https://t.me/MRN__NETWORK", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("https://t.me/MRN_FED_NETWORK", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("5154856700", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
