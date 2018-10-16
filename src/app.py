from flask import Flask
from routes.UserAPI import user
from routes.LanguageAPI import language

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(language)

@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)