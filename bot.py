import threading
import time
from rubika_bot_api import Robot
from database import init_db
from handlers import handle_start, get_home_data, get_network_data, get_miner_data, handle_mine_action, handle_buy_miner

client = Robot(session="traxex_session", auth="TOKEN_HERE") # توکن خودت را اینجا بگذار

@client.on_message()
def on_message(msg):
    user_id = str(msg.author_object_guid)
    text = msg.text or ""
    
    if text.startswith("/start"):
        handle_start(user_id, msg.author_object_username or "", msg.author_object_first_name or "User", text)
    
    if text == "🏠 Home":
        msg.reply(get_home_data(user_id))
    elif text == "👥 Network":
        msg.reply(get_network_data(user_id))
    elif text == "⛏️ Miner":
        msg.reply(get_miner_data(user_id))

if __name__ == "__main__":
    init_db()
    client.run()
