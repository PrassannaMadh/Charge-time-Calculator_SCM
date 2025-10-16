import streamlit as st
import matplotlib.pyplot as plt

st.title("🔋 Supercapacitor Charge Time Calculator")

# --- User Inputs ---
C = st.number_input("Capacitance (F)", value=3000.0, min_value=0.0)
V_initial = st.number_input("Initial Voltage (V)", value=2.5, min_value=0.0)
V_final = st.number_input("Final Voltage (V)", value=4.2, min_value=0.0)
I = st.number_input("Charge Current (A)", value=50.0, min_value=0.0)

if st.button("Calculate"):
    if V_final <= V_initial:
        st.error("Final voltage must be greater than initial voltage.")
    elif I <= 0:
        st.error("Charge current must be greater than zero.")
    else:
        # --- Calculations ---
        t = C * (V_final - V_initial) / I
        e_final = 0.5 * C * (V_final ** 2)
        e_initial = 0.5 * C * (V_initial ** 2)
        delta_e = e_final - e_initial

        # --- Display results ---
        st.success(f"Charge time: {t:.2f} s \n= {t/60:.2f} min \n= {t/3600:.2f} hr")
        st.info(f"Energy added: {delta_e:.2f} J ({delta_e/3600:.4f} Wh)")

        # --- Plot ---
        t_values = [i * t / 100 for i in range(101)]
        v_values = [V_initial + (V_final - V_initial) * (ti / t) for ti in t_values]
        fig, ax = plt.subplots()
        ax.plot(t_values, v_values)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.set_title("Supercapacitor Voltage vs. Time (Constant Current)")
        ax.grid(True)
        st.pyplot(fig)