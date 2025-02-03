# kpi_data.py

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
        # Add more KPIs here...
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
        # Add more KPIs here...
    },
}

# Sigma Score calculation
def calculate_sigma_score(dpm):
    from scipy.stats import norm
    return norm.ppf(1 - dpm / 1_000_000) + 1.5
