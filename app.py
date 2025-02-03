import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from kpi_data import INDUSTRY_DATA, calculate_sigma_score

def compute_derived_values(kpi, inputs):
    """ Compute intermediate values if required for a KPI """
    if kpi == "Days of Inventory on Hand (DOH)":
        if "COGS" in inputs:
            inputs["COGS"] = inputs["Opening Inventory"] + inputs["Purchases"] - inputs["Closing Inventory"]
        return (inputs["Average Inventory Value"] / inputs["COGS"]) * 365
    return None

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

for param in kpi_data["parameters"]:
    inputs[param] = st.number_input(f"Enter {param}", value=None, placeholder=f"Enter {param}")

# Step 4: Calculate KPI
if st.button("Calculate KPI"):
    derived_value = compute_derived_values(kpi, inputs)
    
    if derived_value is not None:
        kpi_value = derived_value
    else:
        kpi_value = kpi_data["formula"](**inputs)
    
    st.write(f"**{kpi}**: {kpi_value:.2f}%")
    
    # Generate Commentary
    benchmark_low, benchmark_high = kpi_data["benchmark"]
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
    st.write(f"Your {kpi} performance is **{kpi_value:.2f}%**, compared to the industry benchmark of **{benchmark_high}%**. ")
