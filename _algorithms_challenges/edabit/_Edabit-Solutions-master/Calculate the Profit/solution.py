def profit(info):
    return round((info["sell_price"] * info["inventory"]) - (info["cost_price"] * info["inventory"]))
