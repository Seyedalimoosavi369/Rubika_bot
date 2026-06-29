def handle_start(user_id, username, name, text):
    return "سلام! خوش آمدی."

def get_home_data(user_id):
    return "به خانه خوش آمدی!"

def get_network_data(user_id):
    return "شبکه شما:"

def get_miner_data(user_id):
    return "بخش استخراج:"

def handle_mine_action(user_id):
    return True, "استخراج انجام شد."

def handle_buy_miner(user_id, miner_type):
    return True, "خرید موفق بود."
