# kpi_data.py

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
        "Sanitation Compliance Rate": {
            "formula": lambda compliant, total: (compliant / total) * 100,
            "benchmark": (100, 100),
            "commentary": {
                "high": "Perfect compliance! Maintain high standards.",
                "medium": "Compliance is good, but aim for 100%.",
                "low": "Compliance is low. Address sanitation issues immediately.",
            },
        },
        # Add more KPIs here...
    },
}
