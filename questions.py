from flask import Blueprint

questions_bp = Blueprint("question",
                    __name__,
                    url_prefix="/question")
@questions_bp.route("/")
def question():
    return "Hello from questions"