# Bizcard
DS-BizCardX: Extracting Business Card Data with OCR

###  Objective:
Bizcard Extraction is a Python application built with Streamlit, EasyOCR, OpenCV, regex function, and MySQL database. It allows users to extract information from business cards and store it in a MySQL database for further analysis. We can update and delete those details with respect of choosing any column name given. 

###  Technologies Used
*  Streamlit
*  Streamlit_lottie
*  Python
*  RegEx
*  EasyOCR
*  openCV
*  MySQL

### PURPOSE 
*  Streamlit - For building interactive web applications with ease.
*  OpenCV - For image preprocessing and manipulation.
*  EasyOCR - For text extraction from images.
*  MySQL - For database management system.

####  HOMEPAGE
![image](https://github.com/vivekarajan/Bizcard/assets/46365159/f3b520d9-f702-4c33-a869-474a3aa81a7e)

###  IMAGE TO TEXT EXTRACTION
  #  STEP1: Click image to text button
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/0c300132-777b-464b-b64b-75e787d79da0)
  #  STEP2:  click 'browse the file' button and 'open' the required image file.
    note: image file should be JPG,JPEG,PNG formats only.
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/75f829b7-a303-4e95-8cd6-c66163874f10)
  #  STEP3:  You can see the uploaded image file
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/e03681ad-c67c-4260-ab02-b4ba14c10b36)
  #  STEP4:  click "extract and upload db" button 
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/6514fe34-1a1b-424d-b6be-1e781b463ad2)
  Thus, you have taken the text out of the picture and made it appear on that webpage. additionally added to the specific database.

### Database
  #  step1:  click "Database" 
    The options to update and delete data are opened here.
  ![Screenshot 2024-04-24 122921](https://github.com/vivekarajan/Bizcard/assets/46365159/4f620041-ca9e-4403-bf12-e501bb5e06b1)
  
  #  STEP2:   click "Update data"
  ![Screenshot 2024-04-24 124058](https://github.com/vivekarajan/Bizcard/assets/46365159/36c66425-dcaa-418f-8386-d2f112af16a4)
  
  #  step 3:  update the selected "card_holder_name" of company data "selva digitals" to "new Selva digitals"
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/9b269708-119c-49f6-a1ad-3910bb2a072d)
    here you can see the updated company data.

  #  STEP4:  Click "Delete data"
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/c90fb4ba-4a04-412f-92fd-fce2cbf6f5d5)

  #  STEP5: delete the information regarding selecting a name
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/fea32d11-6c39-49bf-85be-40443e92fdb6)
  and click "delete"

  you can see the data after delete that particular data
  ![image](https://github.com/vivekarajan/Bizcard/assets/46365159/67629fd9-8791-4cf7-b45a-087bd5bbf8c6)

###  Features
  1.  Extracts text information from business card images using EasyOCR.
  2.  Utilizes OpenCV for image preprocessing and getting a text from given image.
  3.  Uses regular expressions (RegEx) to parse and extract specific fields like name, designation, company name, contact, websites, email, address, city, state, pincode.
  4.  Stores the extracted information in a MySQL database for easy retrieval.
  5.  Provides a user-friendly interface built with Streamlit to upload images, extract information, and update/delete the data in database.

###  How to use
1.Run the Streamlit application:
"streamlit run ./bizproject.py"

2.Access the application in your browser at http://localhost:8501.

3.Upload a business card image to extract the information.

4.The application will preprocess the image using OpenCV.

5.The processed image will be passed to EasyOCR for text extraction.

6.The extracted information will be displayed on the screen, and it will be stored in the MySQL database.

7.Use the provided options to view, update and delete the extracted data in the database.


  
  

