from flask import Blueprint

test_bp = Blueprint('test', __name__)


@test_bp.route('/')
def test():
    return "Hello from Test Page"
