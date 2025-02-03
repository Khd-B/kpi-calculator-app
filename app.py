# app.py
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
inputs = {}
for param in ["numerator", "denominator"]:  # Adjust based on KPI formula
    inputs[param] = st.number_input(f"Enter {param}", value=0.0)

# Step 4: Calculate KPI
if st.button("Calculate KPI"):
    kpi_data = INDUSTRY_DATA[industry][kpi]
    formula = kpi_data["formula"]
    benchmark_low, benchmark_high = kpi_data["benchmark"]
    
    # Calculate KPI value
    kpi_value = formula(inputs["numerator"], inputs["denominator"])
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
    dpm = (inputs["numerator"] / inputs["denominator"]) * 1_000_000
    sigma_score = calculate_sigma_score(dpm)
    st.write(f"**Sigma Score**: {sigma_score:.2f}")

    # Final Conclusion
    st.subheader("Final Conclusion")
    st.write(f"Your {kpi} performance is **{kpi_value:.2f}%**, compared to the industry benchmark of **{benchmark_high}%**. "
             f"Your Sigma Score is **{sigma_score:.2f}**, indicating {'excellent' if sigma_score >= 4.5 else 'acceptable' if sigma_score >= 3 else 'room for improvement'} performance.")
