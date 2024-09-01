from flask import Flask
from users import user_bp
from questions import questions_bp
app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(questions_bp)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'test_token_123'
@app.route("/")
def home():
    user_link = "<a href='/user/'> Юзеры </a><br>"
    question_link = "<a href='/question/'> Вопросы </a><br>"
    return user_link + question_link
