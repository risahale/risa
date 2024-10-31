import streamlit as st

# Judul Aplikasi
st.title("BMI Calculator RISA")


# Input dari pengguna
st.write("Masukkan tinggi badan (dalam cm) dan berat badan (dalam kg):")
height = st.number_input("Tinggi badan (cm)", min_value=100.0, max_value=250.0, step=0.1)
weight = st.number_input("Berat badan (kg)", min_value=20.0, max_value=200.0, step=0.1)

# Fungsi untuk menghitung BMI
def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

# Hasil BMI
if st.button("Hitung BMI"):
    bmi = calculate_bmi(height, weight)
    st.write(f"**Hasil BMI Anda adalah:** {bmi:.2f}")

    # Kategori BMI
    if bmi < 18.5:
        st.write("Anda berada dalam kategori: **Kurus**")
    elif 18.5 <= bmi < 24.9:
        st.write("Anda berada dalam kategori: **Normal**")
    elif 24.9 <= bmi < 29.9:
        st.write("Anda berada dalam kategori: **Overweight**")
    else:
        st.write("Anda berada dalam kategori: **Obesitas**")
