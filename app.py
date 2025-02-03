import streamlit as st
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

# Dynamic input fields based on KPI
if kpi == "OEE (Overall Equipment Effectiveness)":
    inputs["availability"] = st.number_input("Enter Availability (%)", value=None, placeholder="e.g., 90")
    inputs["performance"] = st.number_input("Enter Performance (%)", value=None, placeholder="e.g., 85")
    inputs["quality"] = st.number_input("Enter Quality (%)", value=None, placeholder="e.g., 95")
elif kpi == "Cost of Goods Sold (COGS)":
    inputs["opening"] = st.number_input("Enter Opening Inventory Value", value=None, placeholder="e.g., 10000")
    inputs["purchases"] = st.number_input("Enter Purchases Value", value=None, placeholder="e.g., 5000")
    inputs["closing"] = st.number_input("Enter Closing Inventory Value", value=None, placeholder="e.g., 7000")
else:
    inputs["numerator"] = st.number_input("Enter Numerator", value=None, placeholder="e.g., 50")
    inputs["denominator"] = st.number_input("Enter Denominator", value=None, placeholder="e.g., 100")

# Step 4: Calculate KPI
if st.button("Calculate KPI"):
    formula = kpi_data["formula"]
    benchmark_low, benchmark_high = kpi_data["benchmark"]
    
    # Calculate KPI value
    try:
        if kpi == "OEE (Overall Equipment Effectiveness)":
            kpi_value = formula(inputs["availability"], inputs["performance"], inputs["quality"])
        elif kpi == "Cost of Goods Sold (COGS)":
            kpi_value = formula(inputs["opening"], inputs["purchases"], inputs["closing"])
        else:
            kpi_value = formula(inputs["numerator"], inputs["denominator"])
        
        st.write(f"**{kpi}**: {kpi_value:.2f}")

        # Generate Commentary
        if benchmark_high is not None:
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

        # Calculate Sigma Score (if applicable)
        if kpi not in ["Cost of Goods Sold (COGS)"]:  # Skip Sigma for COGS
            dpm = (inputs.get("numerator", 0) / inputs.get("denominator", 1)) * 1_000_000
            sigma_score = calculate_sigma_score(dpm)
            st.write(f"**Sigma Score**: {sigma_score:.2f}")

            # Final Conclusion
            st.subheader("Final Conclusion")
            st.write(f"Your {kpi} performance is **{kpi_value:.2f}**, compared to the industry benchmark of **{benchmark_high}**. "
                     f"Your Sigma Score is **{sigma_score:.2f}**, indicating {'excellent' if sigma_score >= 4.5 else 'acceptable' if sigma_score >= 3 else 'room for improvement'} performance.")
    except Exception as e:
        st.error(f"Error calculating KPI: {e}. Please ensure all inputs are valid.")
