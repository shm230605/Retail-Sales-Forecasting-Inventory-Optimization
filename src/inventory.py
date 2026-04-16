def calculate_inventory(df, service_level=0.95, lead_time=7, on_hand=200):
    import numpy as np
    from scipy.stats import norm

    demand_mean = float(df["forecast"].mean())
    demand_std = float(df["forecast"].std())

    z = norm.ppf(service_level)

    safety_stock = z * demand_std * np.sqrt(lead_time)
    reorder_point = demand_mean * lead_time + safety_stock

    order_qty = max(0, reorder_point - on_hand)

    return {
        "mean_demand": round(demand_mean, 2),
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "order_quantity": round(order_qty, 2)
    }