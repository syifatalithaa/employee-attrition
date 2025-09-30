import streamlit as st
import pandas as pd
import pickle

# Load model (pastikan kamu sudah simpan model ke rf_model.pkl)
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Sistem Prediksi Atrisi Karyawan")
st.write("Masukkan data karyawan yang ingin diprediksi:")

# Input data karyawan
age = st.number_input("Umur (Age)", 18, 65, 30)
gender = st.selectbox(
    "Jenis Kelamin (Gender)",
    options=[0, 1],
    format_func=lambda x: {
        0: "Male",
        1: "Female"
    }[x])

years_at_company = st.number_input("Lama Bekerja di PT ASDP Indonesia Ferry (Persero)", 0, 40, 5)
num_companies_worked = st.number_input("Jumlah Perusahaan Sebelumnya", 0, 10, 1)
total_working_years = st.number_input("Total Tahun Bekerja Keseluruhan (Terhitung sebelum di PT ASDP Indonesia Ferry)", 0, 50, 10)
years_with_curr_manager = st.number_input("Lama Bekerja dengan Manajer Sekarang (Years With CurrManager)", 0, 20, 3)
years_in_current_role = st.number_input("Lama Bekerja di Role Saat Ini (Years In CurrentRole)", 0, 20, 4)
business_travel = st.selectbox(
    "Perjalanan Dinas",
    options=[0,1,2],
    format_func=lambda x: {
    0: "Non-Dinas",
    1: "Jarang Dinas",
    2: "Sering Dinas"
    }[x])

jarak_rumah = st.number_input("Jarak Rumah (km)", 0, 100, 10)
status_pernikahan = st.selectbox(
    "Status Pernikahan",
    options=[0, 1, 2],
    format_func=lambda x: {
        0: "Divorced",
        1: "Single",
        2: "Married"
    }[x]
)

penghasilan_bulanan = st.number_input("Penghasilan Bulanan (isi 3 digit awal saja, contoh: 5000 = Rp 5.000.000)", 1000, 20000, 5000)

kepuasan_kerja = st.selectbox(
    "Kepuasan Kerja (JobSatisfaction)",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Very High"
    }[x]
)

# EnvironmentSatisfaction dengan pilihan level
environment_satisfaction = st.selectbox(
    "Kepuasan Lingkungan Kerja (EnvironmentSatisfaction)",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Very High"
    }[x]
)

work_life_balance = st.selectbox(
    "Work Life Balance",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Bad",
        2: "Good",
        3: "Better",
        4: "Best"
    }[x]
)

default_values = {
    'GajiHarian': 750,
    'Department': "1",
    'Pendidikan': 3,
    'BidangPendidikan': "2",
    'HourlyRate': 80,
    'JobInvolvement': 3,
    'JobLevel': 1,
    'JobRole': "7",
    'OverTime': "0",
    'PercentSalaryHike': 15,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 3,
    'StockOptionLevel': 0,
    'TrainingTimesLastYear': 3,
    'YearsSinceLastPromotion': 1
}

# Buat dataframe input
input_data = pd.DataFrame([{
    **default_values,
    'Age': age,
    'Gender': gender,
    'YearsAtCompany': years_at_company,
    'NumCompaniesWorked': num_companies_worked,
    'TotalWorkingYears': total_working_years,
    'YearsWithCurrManager': years_with_curr_manager,
    'YearsInCurrentRole': years_in_current_role,
    'BusinessTravel': business_travel,
    'JarakRumah': jarak_rumah,
    'StatusPernikahan': status_pernikahan,
    'PenghasilanBulanan': penghasilan_bulanan,
    'GajiBulanan': penghasilan_bulanan,   # samain
    'KepuasanKerja': kepuasan_kerja,
    'EnvironmentSatisfaction': environment_satisfaction,
    'WorkLifeBalance': work_life_balance
}])

# Tombol Prediksi
if st.button("Prediksi"):
    pred = model.predict(input_data)[0]
    if pred == 1:
        st.error("⚠️ Prediksi: Karyawan berisiko Attrition.")
    else:
        st.success("✅ Prediksi: Karyawan bertahan (Tidak Attrition).")
    st.write("Hasil prediksi ini berdasarkan model Random Forest dengan akurasi sekitar 87%.")