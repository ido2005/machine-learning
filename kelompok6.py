import streamlit as st

# Fungsi prediksi worker_percent berdasarkan fertility_rate
def predict_worker_percent(fertility_rate):
    # Contoh formula prediksi sederhana (ganti dengan model prediksi Anda)
    return fertility_rate * 0.8 + 20  # Misalnya: prediksi berbasis formula sederhana

# Judul aplikasi dengan emoji pekerja
st.title("👷 Prediksi Worker Percent berdasarkan Fertility Rate")

# Input pengguna
fertility_rate_input = st.number_input(
    "Masukkan nilai Fertility Rate:",
    min_value=0.0,
    step=0.01,
    format="%.2f"
)

# Tombol untuk memprediksi
if st.button("Prediksi"):
    if fertility_rate_input is not None:
        try:
            # Lakukan prediksi
            worker_percent_prediction = predict_worker_percent(fertility_rate_input)
            # Tampilkan hasil
            st.success(f"Prediksi Worker Percent untuk Fertility Rate {fertility_rate_input:.2f}: {worker_percent_prediction:.2f}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")