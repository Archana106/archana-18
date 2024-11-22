import streamlit as st
import math

# Define the Resonance function
def calculate_resonance(R, L, C):
    """Calculates resonance frequency, bandwidth, quality factor,
    upper cutoff frequency, and lower cutoff frequency for a series RLC circuit.

    Args:
        R (float): Resistance in ohms.
        L (float): Inductance in henrys.
        C (float): Capacitance in farads.

    Returns:
        tuple: A tuple containing the calculated resonance frequency (FR),
               bandwidth (BW), quality factor (Q), upper cutoff frequency (FU),
               and lower cutoff frequency (FL).
    """

    FR = 1 / (2 * math.pi * math.sqrt(L * C))  # Resonance Frequency (Hz)
    BW = R / (2 * math.pi * L)                 # Bandwidth (Hz)
    Q = FR / BW                               # Quality Factor
    FU = FR + (BW / 2)                         # Upper Cutoff Frequency (Hz)
    FL = FR - (BW / 2)                         # Lower Cutoff Frequency (Hz)
    return FR, BW, Q, FU, FL

# Streamlit Web App


st.title("2204A21064-PS3")
st.write("calculate resonance frequency(FR),band width(BW),quality factor(Q),upper cutoff frequency(FU),and lower frequency(FL)based on R,L,andCvalues for series resonance circuit")
# Create columns for input and output
col1, col2 = st.columns(2)

# Input section in the first column
with col1:
    st.header("Input Parameters")
    R = st.number_input("Resistance:ohms", value=1.0, min_value=0.0, step=0.1)
    L = st.number_input("Inductance:henrys", value=0.001, min_value=0.0, step=0.0001)
    C = st.number_input("Capacitance:farads", value=0.000001, min_value=0.0, step=0.0000001)

    # Add a button within the input section
    if st.button("Calculate", key="calculate_button"):
        if R > 0 and L > 0 and C > 0:
            FR, BW, Q, FU, FL = calculate_resonance(R, L, C)
            col2.success("Calculation Results:")
            # Output section in the second column
            with col2:
                st.write(f"Resonance Frequency (FR): {FR:.2f} Hz")
                st.write(f"Bandwidth (BW): {BW:.2f} Hz")
                st.write(f"Quality Factor (Q): {Q:.2f}")
                st.write(f"Upper Cutoff Frequency (FU): {FU:.2f} Hz")
                st.write(f"Lower Cutoff Frequency (FL): {FL:.2f} Hz")
        else:
            st.error("All input values must be greater than zero.")

# Information section below the inputs
st.info("2205a21064.")