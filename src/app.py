from flask import Flask
from pages.pages import pages_bp

app = Flask(__name__)
app.secret_key = 'any random string'
app.config['db_store'] ={'users':{}}
app.register_blueprint(pages_bp,url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

