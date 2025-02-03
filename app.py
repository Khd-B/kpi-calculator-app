## app.py
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

# Retrieve KPI data
kpi_data = INDUSTRY_DATA[industry][kpi]
formula = kpi_data["formula"]
params = kpi_data.get("parameters", ["numerator", "denominator"])
benchmark_low, benchmark_high = kpi_data["benchmark"]
higher_is_better = kpi_data.get("higher_is_better", True)

# Step 3: Input Values (dynamically based on required parameters)
st.subheader("Input Values")
inputs = {}
for param in params:
    inputs[param] = st.number_input(f"Enter {param}", value=0.0)

# Step 4: Calculate KPI
if st.button("Calculate KPI"):
    # Calculate KPI value (unpack inputs in the defined order)
    try:
        kpi_value = formula(*[inputs[p] for p in params])
    except Exception as e:
        st.error(f"Error in calculation: {e}")
        kpi_value = None

    if kpi_value is not None:
        # Display KPI result
        st.write(f"**{kpi}**: {kpi_value:.2f}{'%' if higher_is_better or not isinstance(kpi_value, (int, float)) else ''}")

        # Generate Commentary using proper comparison logic
        if higher_is_better:
            if kpi_value >= benchmark_high:
                commentary = kpi_data["commentary"]["high"]
            elif kpi_value >= benchmark_low:
                commentary = kpi_data["commentary"]["medium"]
            else:
                commentary = kpi_data["commentary"]["low"]
        else:
            # For KPIs where lower values are better, reverse the logic
            if kpi_value <= benchmark_low:
                commentary = kpi_data["commentary"]["high"]
            elif kpi_value <= benchmark_high:
                commentary = kpi_data["commentary"]["medium"]
            else:
                commentary = kpi_data["commentary"]["low"]
        st.write(f"**Commentary**: {commentary}")

        # Generate Graph (simple comparison graph)
        fig, ax = plt.subplots()
        ax.bar(["Your Performance", "Industry Benchmark"], [kpi_value, benchmark_high if higher_is_better else benchmark_low], color=["blue", "green"])
        ylabel = "Percentage" if (higher_is_better and isinstance(kpi_value, (int, float))) else "Value"
        ax.set_ylabel(ylabel)
        ax.set_title(f"{kpi} Comparison")
        st.pyplot(fig)

        # Calculate Sigma Score if applicable (using first two parameters as defects and total opportunities)
        # This assumes that the first two parameters can represent defects and total opportunities.
        if len(params) >= 2 and inputs[params[1]] != 0:
            dpm = (inputs[params[0]] / inputs[params[1]]) * 1_000_000
            sigma_score = calculate_sigma_score(dpm)
            st.write(f"**Sigma Score**: {sigma_score:.2f}")
        else:
            st.write("Sigma Score cannot be calculated with the provided inputs.")

        # Final Conclusion
        st.subheader("Final Conclusion")
        performance_text = f"Your {kpi} performance is **{kpi_value:.2f}**, compared to the industry benchmark of **{benchmark_high if higher_is_better else benchmark_low}**."
        if len(params) >= 2 and inputs[params[1]] != 0:
            performance_text += f" Your Sigma Score is **{sigma_score:.2f}**."
        st.write(performance_text)
