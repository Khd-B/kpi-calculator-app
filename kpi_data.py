## kpi_data.py

# Define KPI formulas, benchmarks, parameters, commentary, and whether higher values are better for each industry

INDUSTRY_DATA = {
    "Rigid Plastics": {
        "On-Time Delivery Rate": {
            "formula": lambda on_time, total: (on_time / total) * 100 if total else 0,
            "parameters": ["on_time", "total"],
            "benchmark": (95, 98),  # lower bound, upper bound (in %)
            "higher_is_better": True,
            "commentary": {
                "high": "Excellent performance! You are exceeding industry standards.",
                "medium": "Good performance, but there is room for improvement.",
                "low": "Performance is below industry standards. Investigate delays.",
            },
        },
        "Scrap Rate": {
            "formula": lambda scrap, total: (scrap / total) * 100 if total else 0,
            "parameters": ["scrap", "total"],
            "benchmark": (2, 5),  # lower is better (in %)
            "higher_is_better": False,
            "commentary": {
                "high": "High scrap rates indicate inefficiencies in production.",
                "medium": "Scrap rates are within acceptable limits.",
                "low": "Excellent! Scrap rates are minimal.",
            },
        },
        "OEE (Overall Equipment Effectiveness)": {
            "formula": lambda avail, perf, qual: avail * perf * qual * 100,
            "parameters": ["availability", "performance", "quality"],
            "benchmark": (85, 90),  # in %
            "higher_is_better": True,
            "commentary": {
                "high": "Outstanding OEE! Your equipment is highly effective.",
                "medium": "OEE is acceptable but could be improved.",
                "low": "OEE is below standards. Review your processes.",
            },
        },
        "Cycle Time": {
            "formula": lambda cycle: cycle,  # expecting cycle time in seconds
            "parameters": ["cycle_time"],
            "benchmark": (30, 60),  # seconds; lower is better
            "higher_is_better": False,
            "commentary": {
                "high": "Cycle time is too high, indicating inefficiencies.",
                "medium": "Cycle time is acceptable, but there's potential for improvement.",
                "low": "Excellent cycle time performance.",
            },
        },
        "Energy Consumption per Unit": {
            "formula": lambda energy, units: energy / units if units else 0,
            "parameters": ["total_energy (kWh)", "units_produced"],
            "benchmark": (0.5, 1.5),  # kWh/kg; lower is better
            "higher_is_better": False,
            "commentary": {
                "high": "Energy consumption is high. Consider optimizing machinery.",
                "medium": "Energy consumption is within acceptable limits.",
                "low": "Excellent energy efficiency.",
            },
        },
        "Customer Reject Rate": {
            "formula": lambda rejects, shipped: (rejects / shipped) * 100 if shipped else 0,
            "parameters": ["rejects", "shipped"],
            "benchmark": (0.5, 1),  # in %; lower is better
            "higher_is_better": False,
            "commentary": {
                "high": "Customer reject rate is high. Quality issues may exist.",
                "medium": "Reject rate is acceptable, but quality checks are recommended.",
                "low": "Excellent quality control.",
            },
        },
        # Additional KPIs can be added here following the same structure.
    },
    "Food Production": {
        "Thawing Yield": {
            "formula": lambda after, before: (after / before) * 100 if before else 0,
            "parameters": ["after", "before"],
            "benchmark": (95, 98),
            "higher_is_better": True,
            "commentary": {
                "high": "Excellent yield! Minimize weight loss during thawing.",
                "medium": "Yield is acceptable, but improvements are possible.",
                "low": "Yield is low. Investigate thawing process.",
            },
        },
        "Portioning Accuracy": {
            "formula": lambda accurate, total: (accurate / total) * 100 if total else 0,
            "parameters": ["accurate", "total"],
            "benchmark": (98, 99),
            "higher_is_better": True,
            "commentary": {
                "high": "Portioning is highly accurate. Great job!",
                "medium": "Accuracy is good, but aim for higher precision.",
                "low": "Portioning accuracy is below standards. Check equipment.",
            },
        },
        "Sanitation Compliance Rate": {
            "formula": lambda compliant, total: (compliant / total) * 100 if total else 0,
            "parameters": ["compliant", "total"],
            "benchmark": (100, 100),  # Must be 100%
            "higher_is_better": True,
            "commentary": {
                "high": "Outstanding sanitation compliance!",
                "medium": "Sanitation is acceptable, but strive for full compliance.",
                "low": "Sanitation compliance is low. Immediate action required.",
            },
        },
        "First Pass Yield (FPY)": {
            "formula": lambda good, total: (good / total) * 100 if total else 0,
            "parameters": ["good_units", "total_units"],
            "benchmark": (95, 97),
            "higher_is_better": True,
            "commentary": {
                "high": "Excellent first pass yield.",
                "medium": "First pass yield is acceptable.",
                "low": "FPY is below standards. Investigate production issues.",
            },
        },
        "Customer Reject Rate": {
            "formula": lambda rejects, shipped: (rejects / shipped) * 100 if shipped else 0,
            "parameters": ["rejects", "shipped"],
            "benchmark": (0.1, 0.5),
            "higher_is_better": False,
            "commentary": {
                "high": "Customer reject rate is high. Quality issues may exist.",
                "medium": "Reject rate is acceptable, but quality checks are recommended.",
                "low": "Excellent quality control.",
            },
        },
        # Additional KPIs can be added here following the same structure.
    },
}

# Sigma Score calculation (applies to any process where defects per million opportunities are calculated)
def calculate_sigma_score(dpm):
    from scipy.stats import norm
    return norm.ppf(1 - dpm / 1_000_000) + 1.5
