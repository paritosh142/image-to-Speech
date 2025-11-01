import streamlit as st
import uuid 
import os 

def main():
    st.set_page_config(page_title="IMG2SPEECH", page_icon=":robot_face:")
    st.title("Image → Story  → Speech :robot_face:")


    st.write("Upload an image, and let the AI generate a captivating story and convert it to speech!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:


        os.makedirs("img", exist_ok=True)

        file_extension = uploaded_file.name.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join("img", unique_filename)

        byte_data = uploaded_file.getvalue()  

        with open(file_path, "wb") as f:
            f.write(byte_data)
        st.image(byte_data, caption='Uploaded Image.', use_column_width=True)
        st.write("Generating story and speech...")

if __name__ == "__main__":
    main()
