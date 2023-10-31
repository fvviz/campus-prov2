import streamlit as st
from app_utils import scan_for_user
import os

st.set_page_config(
    page_title="Campus Monitor",
    page_icon="🎥",
    layout='wide'
)

meta={'CCTV1':{'22:00, MG Auditorium - Floor 1'},'CCTV2':{'16:00, MG Auditorium - Floor 1'},'CCTV3':{'04:00, MG Auditorium - Floor 1'},'CCTV4':{'08:00, MG Auditorium - Floor 1'}}

st.title("CCTV Monitor")

col1, col2,col3 = st.columns(3)
with col1:
   stud_id = st.text_input("Enter student ID")
   if st.button("Scan CCTV Footage"):
        img = None
        for imgfile in os.listdir(r"C:\Users\vamsv\Downloads\campus-prov2-main\campus-prov2-main\training_set"):
            if imgfile.startswith(stud_id):
                img = os.path.join(r"C:\Users\vamsv\Downloads\campus-prov2-main\campus-prov2-main\training_set", imgfile)
        if img:
            cctv_base = r"C:\Users\vamsv\Downloads\campus-prov2-main\campus-prov2-main\cctv_footage"
            for footage in os.listdir("cctv_footage"):
                footage_path = os.path.join(cctv_base, footage)
                #st.text(footage_path)
                cam=scan_for_user(img,footage_path)
                st.write(f"Person found in MG by {cam}")
                #st.write(f"Person found in MG by {cam} at {meta[cam.split(".")[1]][0]}")
        else:
            raise FileNotFoundError("reg_id not provided in training set")



with col2:
    st.text("Column 2")


with col3: 
    myfile=st.file_uploader("Enter Image of the user")
    if myfile is not None:
        st.image(myfile)








      
      



