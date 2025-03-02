import streamlit as st
import pandas as pd

def test_b_view():
    # ส่วนหัว
    st.title("Joinzy - จอยซี่! 🎉")
    
    # ข้อมูลตัวอย่างของปาร์ตี้
    party_data = pd.DataFrame([
        {"Party Name": "ไปตีแบดกัน", "Activity Type": "Badminton", "Date": "02/03/2025", "Time": "18:00", "Location": "Winner Badminton", "Participant": "3/8"},
        {"Party Name": "บอร์ดเกมกัน", "Activity Type": "Boardgame", "Date": "03/03/2025", "Time": "19:00", "Location": "GameSmith", "Participant": "5/8"},
    ])
    
    # ตัวเลือกประเภทกิจกรรม
    activity_types = ["All"] + list(party_data["Activity Type"].unique())
    selected_activity = st.selectbox("Activity Type", activity_types)
    
    # Dropdown สำหรับค้นหา Party
    selected_party = st.selectbox("🔍 Search Party", ["All"] + list(party_data["Party Name"]))

    # ปุ่มสร้างปาร์ตี้
    st.button("➕ Create Party")
    
    # กรองตามประเภทกิจกรรม
    filtered_data = party_data.copy()
    if selected_activity != "All":
        filtered_data = filtered_data[filtered_data["Activity Type"] == selected_activity]
    
    # กรองตามชื่อปาร์ตี้
    if selected_party != "All":
        filtered_data = filtered_data[filtered_data["Party Name"] == selected_party]

    # แสดงตารางพร้อมปุ่ม View ในคอลัมน์สุดท้าย
    filtered_data["View"] = filtered_data["Party Name"].apply(lambda name: f"[🔍 View](#view-{name.replace(' ', '-')})")

    # แสดงข้อมูลในตาราง
    st.write(filtered_data[["Party Name", "Activity Type", "Date", "Time", "Location", "Participant", "View"]], unsafe_allow_html=True)
    
    # ส่วนแสดงรายละเอียดเมื่อคลิก View
    for _, row in filtered_data.iterrows():
        st.markdown(f'<h3 id="view-{row["Party Name"].replace(" ", "-")}">🔍 {row["Party Name"]}</h3>', unsafe_allow_html=True)
        st.write(f"**Activity Type:** {row['Activity Type']}")
        st.write(f"**Date:** {row['Date']}")
        st.write(f"**Time:** {row['Time']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Participants:** {row['Participant']}")
        st.button(f"Join {row['Party Name']}")
