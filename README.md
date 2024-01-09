[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


# Surveymonkey Connector Odoo

A connector module for Survey Monkey run under Odoo version 17

## Installation

Clone this module to your directory

```bash
 git clone https://github.com/rizalkororo/kororo_survey_monkey.git
```
```bash
 cp kororo_survey_monkey <YOUR_ODOO_PROJECT>/odoo/addons/kororo_survey_monkey
```
## Run Locally

cd to your <YOUR_ODOO_PROJECT> root

```bash
  python3 -m pip install --upgrade pip
```
```bash
  python3 -m pip install -r requirements.txt
```

## Usage

Execute this only at the first start to install module estate.

Inside Odoo root project run:
```python
python odoo-bin -c settings.conf -i base
```
Execute this line for further action
```python
python odoo-bin -c settings.conf
```
Next login to web page with current credential:
```
username: admin
password: admin
```
Change to developer mode by going to `settings -> Developer Tools -> Activate the developer mode`

![App Screenshot](https://i.ibb.co/6WnjYz9/Screenshot-2024-01-01-184455.png)

Back to `Apps` menu, and type `kororo estate` and do installation.

## How to start module

- Login with email and password

![App Screenshot](https://i.ibb.co/r2YdFB8/Screenshot-2024-01-09-101754.png)

- Select Survey Monkey Module

![App Screenshot](https://i.ibb.co/1Q8wNwb/Screenshot-2024-01-09-102420.png)

- Next Click New Button

![App Screenshot](https://i.ibb.co/ydHL03c/Screenshot-2024-01-09-102631.png)

- Select your own name from input field. Remember to only select your own name.

![App Screenshot](https://i.ibb.co/zXjFJc2/Screenshot-2024-01-09-102906.png)

- After saving, go back to previous page and now you will see a new record with your name. Please go to your right handside on the table and select kanban view

![App Screenshot](https://i.ibb.co/XS46NwD/Screenshot-2024-01-09-103136.png)

- Now you can click `Refresh Token` button and you will be redirected to Surveymonkey page

![App Screenshot](https://i.ibb.co/6vr0Wwb/Screenshot-2024-01-09-103411.png)

- Next please login to your `Surveymonkey Account` and then you will be redirected to your odoo login page again. But this only happens once due to your first start with authentication with `Surveymonkey`

![App Screenshot](https://i.ibb.co/r2YdFB8/Screenshot-2024-01-09-101754.png)

- Back to `Survey Monkey Module` in Odoo, now you will find your record with `Token Code` as shown image bellow

![App Screenshot](https://i.ibb.co/hXFV81Q/Screenshot-2024-01-09-103816.png)

- Kindly click the table record contains your `name` and `Access Token` to see your account detail coming from `Surveymonkey`

![App Screenshot](https://i.ibb.co/jydqx2F/Screenshot-2024-01-09-103952.png)

## Tech Stack

**Client:** Odoo, XML, Sass, Javascript

**Server:** Python, Postgres

![Logo](https://media.licdn.com/dms/image/C560BAQHQT2VfIyJNyw/company-logo_200_200/0/1630643115276/kororo_logo?e=2147483647&v=beta&t=8zCw-jiGACWxl4MPZyw-qXoUqGIftJJlsK5jFN5oZsg)