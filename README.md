# web_eligibility
Web-Developer test

# SRMIST WebDeveloper Project

## Overview
This project is a simple version of our SRMIST Trichy collage website.

## Features
- **Home Page**: Introduction to the college, events, more about collage.
- **About Us**: Information about the college's history, vision, and administration.
- **Apply**: Application form to apply for the collage.
- **Login**: Login in to student portal.
- **Student portal**: Details of the student provided during registration.
- **Events**: Recent events.
- **Contact Us**: Contact number and address.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Version Control**: Git

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/JAGAN-KARTHICK-A/web_eligibility.git
    ```
2. Navigate to the project directory:
    ```bash
    cd web_eligibility/Source
    ```
3. Modify the utils.py file to setup database: (add the following lines to the end of the file `utls.py`)
   ```python
    self.HOST = "<ENTER YOUT HOST>"
    self.PORT = <ENTER YOUR PORT NUMBER>
    self.USER = "<ENTER YOUR USERNAME>"
    self.PASSWORD = "<ENTER YOUR PASSWORD>"
    self.DATABASE = "<ENTER YOUR DATABASENAME>"

    db = DB()
    db.setupDatabase()
    ```
4. Revert the changes after running the file `utils.py` (Only remove the last two lines and don't change the host, port, user, password and database details)
5. Install the dependencies:
    ```bash
    pip3 install flask
    pip3 install cryptography
    ```

## Author
A.Jagan Karthick (I'st year B.Tech CSE AIML at SRMIST, Tiruchirapalli)

