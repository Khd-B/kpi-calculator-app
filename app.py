import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from kpi_data import INDUSTRY_DATA, calculate_sigma_score

# App title
st.title("KPI Calculator App")
st.write("Select your industry and KPI to calculate performance.")

# Step 1: Industry Selection
industry = st.selectbox("Select Industry", list(INDUSTRY_DATA.keys()))

# Step 2: KPI Selection
kpi_list = list(INDUSTRY_DATA[industry].keys())
kpi = st.selectbox("Select KPI", kpi_list)

# Step 3: Input Values
st.subheader("Input Values")
kpi_data = INDUSTRY_DATA[industry][kpi]
inputs = {}

# Special Case: COGS Calculation (for KPIs that use COGS)
if any(term in kpi for term in ["Inventory Turnover Ratio", "Days of Inventory on Hand"]):
    st.subheader("COGS Calculation")
    opening_inventory = st.number_input("Enter Opening Inventory", value=None, placeholder="Opening Inventory Value")
    purchases = st.number_input("Enter Purchases", value=None, placeholder="Total Purchases")
    closing_inventory = st.number_input("Enter Closing Inventory", value=None, placeholder="Closing Inventory Value")

    if opening_inventory and purchases and closing_inventory:
        cogs = opening_inventory + purchases - closing_inventory
        st.write(f"**Calculated COGS:** {cogs}")
    else:
        st.warning("Please enter all required values to calculate COGS.")
        cogs = None
else:
    cogs = None

# General KPI Input Fields
for param in kpi_data["parameters"]:
    inputs[param] = st.number_input(f"Enter {param.replace('_', ' ').title()}", value=None, placeholder=param.replace('_', ' ').title())

# Step 4: Calculate KPI
if st.button("Calculate KPI"):
    formula = kpi_data["formula"]
    benchmark_low, benchmark_high = kpi_data["benchmark"]

    # Pass COGS if needed
    if "cogs" in kpi_data["parameters"]:
        inputs["cogs"] = cogs

    # Validate inputs before calculation
    if None in inputs.values():
        st.warning("Please enter all required values.")
    else:
        kpi_value = formula(**inputs)
        st.write(f"**{kpi}**: {kpi_value:.2f}%")

        # Generate Commentary
        if kpi_value >= benchmark_high:
            commentary = kpi_data["commentary"]["high"]
        elif kpi_value >= benchmark_low:
            commentary = kpi_data["commentary"]["medium"]
        else:
            commentary = kpi_data["commentary"]["low"]
        st.write(f"**Commentary**: {commentary}")

        # Generate Graph
        fig, ax = plt.subplots()
        ax.bar(["Your Performance", "Industry Benchmark"], [kpi_value, benchmark_high], color=["blue", "green"])
        ax.set_ylabel("Percentage")
        ax.set_title(f"{kpi} Comparison")
        st.pyplot(fig)

        # Calculate Sigma Score
        if kpi_value == 0:
            st.warning("Cannot calculate Sigma Score for zero defects.")
        else:
            dpm = (inputs.get("numerator", 0) / inputs.get("denominator", 1)) * 1_000_000
            sigma_score = calculate_sigma_score(dpm)
            st.write(f"**Sigma Score**: {sigma_score:.2f}")

        # Final Conclusion
        st.subheader("Final Conclusion")
        st.write(f"Your {kpi} performance is **{kpi_value:.2f}%**, compared to the industry benchmark of **{benchmark_high}%**. "
                 f"Your Sigma Score is **{sigma_score:.2f}**, indicating {'excellent' if sigma_score >= 4.5 else 'acceptable' if sigma_score >= 3 else 'room for improvement'} performance.")
