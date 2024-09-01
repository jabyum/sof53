from flask import Blueprint, render_template, request
from forms import *
user_bp = Blueprint("user",
                    __name__,
                    url_prefix="/user")
users = [{"name": "Botir", "email": "123@mail.ru", "password": "123"},
         {"name": "Oleg", "email": "oleGG@mail.ru", "password": "1234"}]
@user_bp.route("/")
def home():
    reg_link = "<a href='/user/registration'> Регистрация </a><br>"
    login_link = "<a href='/user/login'> Вход в аккаунт </a><br>"
    return reg_link + login_link
@user_bp.route("/registration")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)
@user_bp.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
@user_bp.route("/reg", methods=["POST"])
def get_reg_info():
    all_info = request.form
    for i in users:
        if all_info.get("email") in i.get("email"):
            return "Данная почта уже занята"
    if all_info.get("password") != all_info.get("password2"):
        return "Пароли не совпадают"
    new_user = {}
    for k,v in all_info.items():
        if k != "password2" and k != "button":
            new_user[k] = v
    users.append(new_user)
    print(users)
    return "Вы успешно зарегистрированы"

@user_bp.route("/log", methods=["POST"])
def log_info():
    all_info = request.form
    email = all_info.get("email")
    password = all_info.get("password")
    check_email = False
    for i in users:
        for k,v in i.items():
            if k == "email" and v == email:
                check_email = True
                if i.get("password") == password:
                    return "Вы успешно вошли в свой аккаунт"
    if not check_email:
        return "Аккаунт с такой почтой не существует"
    return "Неверный пароль"
