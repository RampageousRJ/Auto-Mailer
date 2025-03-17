# Auto-Mailer

## Overview
This project is an **Auto-Mailer** built using Flask and Flask-Mail. It allows users to send bulk emails by uploading an Excel sheet containing recipient email addresses. The app also supports **email attachments** and ensures secure handling of file uploads.

#### Find the pre-deployed version - **[https://auto-mailer-sxh9.onrender.com/home](Auto-Mailer)**.


## Features
- Bulk email sending using **Flask-Mail**.
- Upload **Excel files** containing email addresses.
- Attach **image or document files** to emails.
- Temporary storage and automatic deletion of attachments after sending.
- Flask web interface with a form-based input system.

## Tech Stack
- **Backend**: Flask, Flask-Mail
- **Frontend**: HTML, Jinja Templates, CSS
- **Database**: Pandas for Excel Processing
- **Deployment**: Render

## Project Structure
```plaintext
.
├── mailer/
│   ├── __init__.py        
│   ├── routes.py          
│   ├── forms.py      
│   ├── tests.py        
│   ├── templates/    
│   │   ├── home.html     
│   ├── static/
│   │   ├── images/
|   |   |   |─── icon.ico  
│   │   ├── styles.css     
├── .env                   
├── requirements.txt       
├── app.py                
├── README.md              
```

## Installation
### 1️. Clone the Repository
```sh
$ git clone https://gitlab.com/YOUR_GITLAB_REPO.git
$ cd automated-mailing-app
```

### 2️. Create a Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️. Set Up Environment Variables
Create a `.env` file in the project root and add:
```ini
AUTOMAILER_SECRET_KEY=your_secret_key
MAIL_ID=your_email@gmail.com
MAIL_PASSWORD=your_email_password
AUTOMAILER_PUBLIC_KEY=your_recaptcha_public_key
AUTOMAILER_PRIVATE_KEY=your_recaptcha_private_key
UPLOAD_FOLDER=/tmp/
ATTACHMENT_FOLDER=/tmp/
```

### 5️. Run the Application
```sh
$ flask run --host=0.0.0.0 --port=5000
```
App will be available at **[http://localhost:5000](http://localhost:5000)**.

## Contributing
1. **Fork the repository**
2. **Create a new branch** (`feature-branch`)
3. **Commit changes**
4. **Push to your branch**
5. **Open a Pull Request**