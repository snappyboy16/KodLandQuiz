from flask_login import LoginManager
from app import app

if __name__ == '__main__':
    app.run(debug=True)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'