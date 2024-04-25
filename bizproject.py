import streamlit as st
import mysql.connector  #databse connection MySQL
from streamlit_option_menu import option_menu
import easyocr
import cv2
import re    #text processing
import numpy as np
import pandas as pd


connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password="Happylife@1309",
        database="bizcard"
    )
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS image ("
                                    "id INT AUTO_INCREMENT PRIMARY KEY,"
                                    "company VARCHAR(255),"
                                    "name VARCHAR(255),"
                                    "designation VARCHAR(255),"
                                    "contact VARCHAR(255),"
                                    "email VARCHAR(255),"
                                    "website VARCHAR(255),"
                                    "address VARCHAR(255),"
                                    "city VARCHAR(255),"
                                    "state VARCHAR(255),"
                                    "pincode VARCHAR(255),"
                                    "image LONGBLOB )")
#------------------------------------------------------------------------------------------------
# Setting up page configuration
st.set_page_config(page_title= "bizcard project - Vivekarajan S",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Vivekarajan S*!
                                        for image to text bounding process"""})

st.sidebar.header(" :blue[**Hello! Welcome to my IMAGE TO TEXT EXTRACTION WEB APPLICATION**]")

#create option in side bar
with st.sidebar:
    selected = option_menu("Menu", ["Home","Image to Text","Database"], 
                icons=["house","file-earmark-font","gear"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#008DDA"},
                        "nav-link-selected": {"background-color": "#008DDA"}})
#------------------------------------------------------------------------------------------------
                  
#selected = option_menu('Main Menu', ['Home',"Image to Text","Database"],
 #                      icons=["house",'file-earmark-font','gear'],default_index=0)

if selected == "Home":
    st.markdown("## :blue[Streamlit's User-Friendly Move toward of Environment Creation]")
    st.write(" ")
    st.markdown("""### :blue[Technologies used :] 
                Python, MySQL, mysql-connector-python, 
                Streamlit, EasyOCR, RegularExpression""")
    st.markdown("""### :blue[Overview :] 
                In this streamlit web app, you can
                upload the business card and extract the text from image 
                and you can edit the name in the name of image data""")

if selected=='Image to Text':
        file,text = st.columns([3,2.5])
        with file:
            uploaded_file = st.file_uploader("Choose an image of a business card", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                file_bytes = uploaded_file.read()
                npa = np.frombuffer(file_bytes, np.uint8)
                image = cv2.imdecode(npa, cv2.IMREAD_COLOR)
                st.image(image,channels='BGR' ,use_column_width=True)
                
            if st.button('EXTRACT & UPLOAD TO DB'):
              reader=easyocr.Reader(['en'])
              results = reader.readtext(image)
              card_info = [i[1] for i in results]
              a = ' '
              card = a.join(card_info)  #convert the all info to string
              #st.write(card_info)    #check the o/p after join function
              #ease to find using regex
              replacement = [(";", ""),(',', ''),("WWW ", "www."),
                    ("www ", "www."),('www', 'www.'),('www.', 'www'),
                    ('wwW', 'www'),('wWW', 'www'),('.com', 'com'),('com', '.com')]
              for old, new in replacement:
                  card = card.replace(old, new)

              # ----------------------------------------------------------
              #phone content
              #card =Selva DATA MANAGER +123-456-7890 +123-456-7891 WWW XYZI.com hello@XYZ1.com 123 ABC St , Chennai; selva TamilNadu 600113 digitals
              ph_pattern = r"\+*\d{2,3}-\d{3}-\d{4}"
              ph = re.findall(ph_pattern, card)
              Phone = ''
              for num in ph:
                  Phone = Phone + ' ' + num
                  card = card.replace(num, '')

              # ------------------Mail id--------------------------------------------
              mail_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b"
              mail = re.findall(mail_pattern, card)
              Email_id = ''
              for ids in mail:
                  Email_id = Email_id + ids
                  card = card.replace(ids, '')

              # ---------------------------Website----------------------------------
              url_pattern = r"www\.[A-Za-z0-9]+\.[A-Za-z]{2,3}"
              url = re.findall(url_pattern, card)
              URL = ''
              for web in url:
                  URL = URL + web
                  card = card.replace(web, '')

              # ------------------------pincode-------------------------------------------
              pin_pattern = r'\d+'
              match = re.findall(pin_pattern, card)
              Pincode = ''
              for code in match:
                  if len(code) == 6 or len(code) == 7:
                      Pincode = Pincode + code
                      card = card.replace(code, '')

              # ---------------name ,designation, company name-------------------------------
              #card_info=[0:"Selva"1:"DATA MANAGER"2:"+123-456-7890"3:"+123-456-7891"4:"WWW XYZI.com"5:"hello@XYZ1.com"
                          #6:"123 ABC St , Chennai;"7:"selva"8:"TamilNadu 600113"9:"digitals"]
              name_pattern = r'^[A-Za-z]+ [A-Za-z]+$|^[A-Za-z]+$|^[A-Za-z]+ & [A-Za-z]+$'
              name_data = []  # empty list
              for i in card_info:
                  if re.findall(name_pattern, i):
                      if i not in 'WWW':
                          name_data.append(i)
                          card = card.replace(i, '')
              name = name_data[0]
              designation = name_data[1]

              if len(name_data) == 3:
                  company = name_data[2]
              else:
                  company = name_data[2] + ' ' + name_data[3]
              card = card.replace(name, '')
              card = card.replace(designation, '')

              #-----------------------------------------------------------------------

              #city,state,address
              new = card.split()
              if new[4] == 'St':
                  city = new[2]
              else:
                  city = new[3]
              # state
              if new[4] == 'St':
                  state = new[3]
              else:
                  state = new[4]
              # address
              if new[4] == 'St':
                  s = new[2]
                  s1 = new[4]
                  new[2] = s1
                  new[4] = s  # swapping the St variable
                  Address = new[0:3]
                  Address = ' '.join(Address)  # list to string
              else:
                  Address = new[0:3]
                  Address = ' '.join(Address)  # list to string
              st.write('')
              st.write('###### :red[Name]         :', name)
              st.write('###### :red[Designation]  :', designation)
              st.write('###### :red[Company name] :', company)
              st.write('###### :red[Contact]      :', Phone)
              st.write('###### :red[Email id]     :', Email_id)
              st.write('###### :red[URL]          :', URL)
              st.write('###### :red[Address]      :', Address)
              st.write('###### :red[City]         :', city)
              st.write('###### :red[State]        :', state)
              st.write('###### :red[Pincode]      :', Pincode)
              sql = """INSERT INTO image (company, name, designation, contact, email, 
                    website, address, city, state, pincode, image) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
              data = (company,name,designation,Phone,Email_id,URL,Address,city,state,Pincode,file_bytes)
              cur.execute(sql, data)
              #cur.execute("SELECT * FROM image").fetchall()
              connection.commit()
              cur.close()
              st.write('Text extracted & successfully uploaded to database')

#-------------------------------------------------------------------------------------------------------------
if selected=='Database':
        option = option_menu(None, ["Update data", "Delete data"],
                            icons=["image", "pencil-fill", 'exclamation-diamond'], default_index=0)
        cur.execute("SELECT * FROM image")
        myresult = cur.fetchall()
        #convert into dataframe using pandas
        df=pd.DataFrame(myresult,columns=['id','company', 'name','designation','contact','email','website','address','city','state','pincode','image'])
        df.set_index('id', drop=True, inplace=True)
        st.write(df)
        if option=='Update data':
            name,new_name=st.columns(2)
            with name:
                # Get the available row IDs from the database
                cur.execute("SELECT name FROM image")
                rows = cur.fetchall()
                row_name = [row[0] for row in rows]
                #row_designation = [row[1] for row in rows]

                # Display the selection box
                selection_name = st.selectbox("Select name to update", row_name)
                #selection_designation = st.selectbox("Select designation to update", row_designation)
            with new_name:
                # Get the column names from the table
                cur.execute("SHOW COLUMNS FROM image")
                columns = cur.fetchall()
                column_names = [i[0] for i in columns if i[0] not in ['id', 'image','name','designation']]

                # Display the selection box for column name
                selection = st.selectbox("Select specific column to update", column_names)
                new_data = st.text_input(f"Enter the new {selection}")

                # Define the SQL query to update the selected rows
                sql = f"UPDATE image SET {selection} = %s WHERE name = %s"

                # Execute the query with the new values
                if st.button("Update"):
                    cur.execute(sql, (new_data, selection_name))
                    # Commit the changes to the database
                    connection.commit()
                    st.experimental_rerun()

#-----------------------------------------------------------------------------------------------------------
        #delete data
        else:
            left,right=st.columns([2,2.5])
            with left:
                cur.execute("SELECT name FROM image")
                rows = cur.fetchall()    #collecting all the data
                row_name = [row[0] for row in rows]
                #row_designation = [row[1] for row in rows]
            # Display the selection box
                selection_name = st.selectbox("Select name to delete", row_name)
            #with right:
                #selection_designation = st.selectbox("Select designation to delete", row_designation)
        
                if st.button('DELETE'):
                    sql = "DELETE FROM image WHERE name = %s"
                # Execute the query with the values as a tuple
                    cur.execute(sql, (selection_name,))
                    connection.commit()
                    st.experimental_rerun()
            