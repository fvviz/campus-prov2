import streamlit as st
from app_utils import scan_for_user
import os
import shutil

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
   slider_value = st.slider("Select inference rate", min_value=0, max_value=10, value=7, step=1)


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
                cam=scan_for_user(img,footage_path,slider_value)
                st.write(f"Person found in MG by {cam}")
                #st.write(f"Person found in MG by {cam} at {meta[cam.split(".")[1]][0]}")
        else:
            raise FileNotFoundError("reg_id not provided in training set")



with col2:
    #st.text("Column 2")
    folder_path = r"C:\Users\vamsv\Downloads\campus-prov2-main\campus-prov2-main\detections"
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png') or f.endswith('.jpg')]
    st.header('Identified images')
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = open(image_path, 'rb').read()
        st.image(image, caption=image_file, use_column_width=True)



with col3: 
    uploaded_file=st.file_uploader("Enter Image of the user")
    if uploaded_file is not None:
        file_name = uploaded_file.name
        st.image(uploaded_file)
        destination_folder =r"C:\Users\vamsv\Downloads\campus-prov2-main\campus-prov2-main\training_set"
        destination_path = os.path.join(destination_folder, file_name)
        with open(destination_path, "wb") as f:
            f.write(uploaded_file.read())








      
      



