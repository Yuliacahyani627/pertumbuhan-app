import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("📈 Model Pertumbuhan & Peluruhan Eksponensial")

st.markdown("""
Model ini digunakan untuk memodelkan pertumbuhan populasi, investasi, atau peluruhan zat radioaktif.

### Rumus:
$P(t) = P_0 \\cdot e^{kt}$
""")

# Input parameter
P0 = st.number_input("Nilai awal (P₀)", value=100.0)
k = st.number_input("Laju perubahan (k)", value=0.1, help="Gunakan nilai negatif untuk peluruhan")
t_max = st.slider("Durasi waktu (t)", min_value=1, max_value=100, value=30)

# Hitung dan tampilkan hasil
t = np.linspace(0, t_max, 100)
P = P0 * np.exp(k * t)

st.subheader("📊 Grafik Pertumbuhan/Peluruhan")
fig, ax = plt.subplots()
ax.plot(t, P, label=f"P(t) = {P0}·e^({k}t)", color="green")
ax.set_xlabel("Waktu (t)")
ax.set_ylabel("Jumlah P(t)")
ax.legend()
st.pyplot(fig)

# Nilai akhir
st.success(f"Nilai akhir setelah t = {t_max} adalah: {P[-1]:.2f}")
