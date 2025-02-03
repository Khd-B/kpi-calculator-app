from scipy.stats import norm

# Function to calculate Sigma Score
def calculate_sigma_score(dpm):
    return norm.ppf(1 - (dpm / 1_000_000)) + 1.5

# KPI Definitions
INDUSTRY_DATA = {
    "Rigid Plastics": {
        "On-Time Delivery Rate": {
            "formula": lambda on_time, total: (on_time / total) * 100,
            "parameters": ["on_time", "total"],
            "benchmark": (95, 98),
            "commentary": {
                "high": "Excellent performance! You are exceeding industry standards.",
                "medium": "Good performance, but there is room for improvement.",
                "low": "Performance is below industry standards. Investigate delays.",
            },
        },
        "Inventory Turnover Ratio": {
            "formula": lambda cogs, avg_inventory: cogs / avg_inventory,
            "parameters": ["cogs", "avg_inventory"],
            "benchmark": (5, 10),
            "commentary": {
                "high": "Excellent inventory turnover efficiency!",
                "medium": "Acceptable turnover, but there’s room for improvement.",
                "low": "Low turnover. Consider reducing excess stock.",
            },
        },
        "Days of Inventory on Hand (DOH)": {
            "formula": lambda avg_inventory, cogs: (avg_inventory / cogs) * 365,
            "parameters": ["avg_inventory", "cogs"],
            "benchmark": (30, 60),
            "commentary": {
                "high": "Inventory turnover is optimized.",
                "medium": "Holding inventory for a moderate time.",
                "low": "High inventory days. Consider adjusting stock levels.",
            },
        },
        "OEE (Overall Equipment Effectiveness)": {
            "formula": lambda availability, performance, quality: availability * performance * quality,
            "parameters": ["availability", "performance", "quality"],
            "benchmark": (85, 90),
            "commentary": {
                "high": "Excellent equipment utilization!",
                "medium": "Good, but there is room for improvement.",
                "low": "Low OEE. Investigate downtime, speed losses, or defects.",
            },
        },
    },
    "Food Production": {
        "Production Yield": {
            "formula": lambda good_units, total_units: (good_units / total_units) * 100,
            "parameters": ["good_units", "total_units"],
            "benchmark": (95, 98),
            "commentary": {
                "high": "High production yield! Very efficient.",
                "medium": "Yield is good, but improvement is possible.",
                "low": "Low production yield. Investigate causes.",
            },
        },
        "Thawing Yield": {
            "formula": lambda after, before: (after / before) * 100,
            "parameters": ["after", "before"],
            "benchmark": (95, 98),
            "commentary": {
                "high": "Excellent yield! Minimize weight loss during thawing.",
                "medium": "Yield is acceptable, but improvements are possible.",
                "low": "Yield is low. Investigate thawing process.",
            },
        },
    },
}
