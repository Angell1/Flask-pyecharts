from flask import Flask
from app.blueprints.Bar_bp import Barbp
from app.blueprints.Line_bp import Linebp

fpyeachrtapp = Flask(__name__)

# 注册蓝图
fpyeachrtapp.register_blueprint(Barbp)
fpyeachrtapp.register_blueprint(Linebp)

if __name__ == '__main__':
    fpyeachrtapp.run()