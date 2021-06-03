# flask-2fa

Flask-2fa is a demo application for two factor authentication using flask and pyotp library.

### Steps to run the app

```
$ cd flask-2fa
$ python3 -m venv .
$ source bin/active
$ pip install -r src/requirements.txt
$ python src/app.py
```

Open the app in the browser using [http://localhost:5000](http://localhost:5000)

### Using the app

* Run the app using  above steps
* Browse the app
* Create account
* Login into the app
* Scan the QR code shown on the home page using [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator) or [Authy](https://authy.com/) APP and save the 2FA settings
* Enable the 2FA on the account in the [app](http://localhost:5000/home)
* Logout
* Try logging in again
* This time it will ask for code in addition to user and password login
* Using the Google Authenticator or Authy get the code and use it
* You should be logged in successfully

Note: This is not production ready app. If you see any errors, use private or incognito window (to start clean session without cookies).

