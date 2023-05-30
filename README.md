## Django-Ecommerce App

An ecommerce site built with django. I made this guided project based on Code with Stien's [Ecommerce Website With Multiple Vendors](https://www.youtube.com/watch?v=t7EIdIl8ZfQ&list=PLpyspNLjzwBkRti2Ur9I9EdEEkF3PHIr_&pp=iAQB). I used this to learn a database management and a bit of web development. Although it's essentially a clone of what Stien did in his video, I hope to keep updating this as I learn more web development. 

### Setup
Clone this repo, using the following command: 

```bash
git clone https://github.com/MoRevolution/DBM-Project_Ecommerce.git
```
Or, if you prefer using  GitHub CLI: 

```bash
git clone https://github.com/MoRevolution/DBM-Project_Ecommerce.git
```

To run this app, you will need to have django and other dependencies which I have included in "requirements.txt". Download django and other dependencies using:

```bash
pip install -r requirements.txt
```
Once all the dependencies have been installed, go to the cloned repo directory and run the following command: 

```bash
python3 manage.py makemigrations
```
This will create all the migrations file (database migrations) required to run this App.

To apply this migrations run the following command: 
```bash
python3 manage.py migrate
```

Before running the app, we need to create an admin user. In the terminal, type the following command and provide username, passoword, and optionally an email address to tset things up.

```bash
python3 manage.py createsuperuser
```
To make the app live, use the following command: 

```bash
python3 manage.py runserver
```

Once the server is hosted, head over to on your favorite browser and head to http://127.0.0.1:8000/ for the app.
