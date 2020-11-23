from flask import Flask

from app.blueprints.Bar_bp import Bar

fpyeachrtapp = Flask(__name__)

# 注册蓝图
fpyeachrtapp.register_blueprint(Bar)


if __name__ == '__main__':
    fpyeachrtapp.run()