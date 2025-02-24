import streamlit as st
import pandas as pd
import os 
from io import BytesIO

#setting up out app
st.set_page_config(page_title="DataMorph📊",layout="wide")
st.title("📊 DataMorph")
st.write("Transform messy spreadsheets into clean, structured data with seamless CSV-to-Excel conversion and built-in visualization tools! 🔄📈")

# upload files button

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):",type=["csv","xlsx"],
accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()


        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        
        else:
            st.error("Unsupported file type: {file_ext}")
            continue

    # display info about the file

        st.write(f"File Name: {file.name}")
        st.write(f"File Size: {file.size/1024}")



       #Show 5 rows of our df

        st.write("Preview the Head of the Dataframe")

        #returns 5 ROWS  of data
        st.dataframe(df.head()) 


        # Options for data Cleaning
        st.subheader("Data Cleaning Options 🛠️")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1,col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed !!!")

            with col2:
                if st.button(f"Fill Missing Values For {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns  
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been Filled !!!")

         #Choose specific columns to keep or convert

        st.subheader("🎯 Select Columns to Convert ")
        columns=st.multiselect (f"choose columns for {file.name}",df.columns,default=df.columns)
        df = df[columns]

         # Create Some Visualizations
    
        st.subheader("📈 Data Visualization ")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
            if numeric_df.shape[1] >= 1:  # Ensure at least one numeric column exists
                st.bar_chart(numeric_df)
            else:
                st.error("No numeric columns available for visualization!")
  




        #Convert th file -> CSV to EXCEl
         

        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"convert {file.name} to:",["CSV","Excel"],key=file.name) 
        if st.button(f"Convert {file.name} 📂"):
            buffer = BytesIO()
            if conversion_type == "CSV":
               df.to_csv(buffer,index=False)
               file_name = file.name.replace(file_ext, ".csv")  
               mime_type="text/csv"
              

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext,".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)


            #Download Button

            st.download_button(
                label=f"Download {file_name} as {conversion_type} 📥" ,
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )    

            st.success("✅ All Files are Processed! 🎉") 