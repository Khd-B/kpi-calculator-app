import scipy.stats

# Define KPI formulas, benchmarks, and commentary for each industry
INDUSTRY_DATA = {
    "Rigid Plastics": {
        "On-Time Delivery Rate": {
            "formula": lambda on_time, total: (on_time / total) * 100,
            "benchmark": (95, 98),
            "commentary": {
                "high": "Excellent performance! You are exceeding industry standards.",
                "medium": "Good performance, but there is room for improvement.",
                "low": "Performance is below industry standards. Investigate delays.",
            },
        },
        "Scrap Rate": {
            "formula": lambda scrap, total: (scrap / total) * 100,
            "benchmark": (2, 5),
            "commentary": {
                "high": "High scrap rates indicate inefficiencies in production.",
                "medium": "Scrap rates are within acceptable limits.",
                "low": "Excellent! Scrap rates are minimal.",
            },
        },
        "OEE (Overall Equipment Effectiveness)": {
            "formula": lambda availability, performance, quality: availability * performance * quality,
            "benchmark": (85, 90),
            "commentary": {
                "high": "Excellent equipment utilization!",
                "medium": "Good, but there is room for improvement.",
                "low": "Low OEE. Investigate downtime, speed losses, or defects.",
            },
        },
        "Inventory Turnover Ratio": {
            "formula": lambda cogs, avg_inventory: cogs / avg_inventory,
            "benchmark": (8, 12),
            "commentary": {
                "high": "High turnover indicates efficient inventory management.",
                "medium": "Turnover is acceptable, but improvements are possible.",
                "low": "Low turnover. Investigate overstocking or slow-moving items.",
            },
        },
    },
    "Food Production": {
        "Thawing Yield": {
            "formula": lambda after, before: (after / before) * 100,
            "benchmark": (95, 98),
            "commentary": {
                "high": "Excellent yield! Minimize weight loss during thawing.",
                "medium": "Yield is acceptable, but improvements are possible.",
                "low": "Yield is low. Investigate thawing process.",
            },
        },
        "Portioning Accuracy": {
            "formula": lambda accurate, total: (accurate / total) * 100,
            "benchmark": (98, 99),
            "commentary": {
                "high": "Portioning is highly accurate. Great job!",
                "medium": "Accuracy is good, but aim for higher precision.",
                "low": "Portioning accuracy is below standards. Check equipment.",
            },
        },
        "Cost of Goods Sold (COGS)": {
            "formula": lambda opening, purchases, closing: opening + purchases - closing,
            "benchmark": (None, None),  # No benchmark for COGS
            "commentary": {
                "high": "COGS is calculated. Use this value in other KPIs.",
                "medium": "COGS is calculated. Use this value in other KPIs.",
                "low": "COGS is calculated. Use this value in other KPIs.",
            },
        },
    },
}

# Sigma Score calculation
def calculate_sigma_score(dpm):
    return scipy.stats.norm.ppf(1 - dpm / 1_000_000) + 1.5
