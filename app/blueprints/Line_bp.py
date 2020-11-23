
import base64
import json
import uuid
from flask import Blueprint,jsonify,request
from marshmallow import ValidationError
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from snapshot_selenium import snapshot
from app.validates.validate import norlineSchema

Linebp = Blueprint("Line", __name__, url_prefix="/Line")


@Linebp.route('/norline')
def create_norline():
    # 反序列化
    data = request.get_data()
    data = json.loads(data)
    returnres = {"state": 200, "msg": "succsuful", "result": ''}
    print(data)
    try:
        schema = norlineSchema()
        data = schema.load(data)
        data = schema.dump(data)
        print(data)
    except ValidationError as err:
        error = err.messages
        print(error)
        returnres['result'] = error
        return jsonify(returnres)
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add_xaxis(data['xaxis'])
            .add_yaxis(data['typelist'][0], data['yaxis'])
            .set_global_opts(
                title_opts=opts.TitleOpts(title=data['maintitle']),
        )
    )
    # 输出保存为图片
    imagesname = str(uuid.uuid4())
    make_snapshot(engine=snapshot, file_name=line.render(), output_name="../charts/image/%s.png" % imagesname,is_remove_html=True)
    image_data = open("../charts/image/%s.png" % imagesname, "rb").read()
    result = base64.b64encode(image_data)
    returnres = {"state": 200, "msg": "succsuful", "result": result}
    return jsonify(returnres)


@Linebp.route('/mulline')
def create_mulline():
    # 反序列化
    data = request.get_data()
    data = json.loads(data)
    returnres = {"state": 200, "msg": "succsuful", "result": ''}
    print(data)
    try:
        schema = norlineSchema()
        data = schema.load(data)
        data = schema.dump(data)
        print(data)
    except ValidationError as err:
        error = err.messages
        print(error)
        returnres['result'] = error
        return jsonify(returnres)
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 10, 100])
            .add_yaxis("商家B", [55, 60, 16, 20, 15, 80])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="mulLine"),
        )
    )
    # 输出保存为图片
    imagesname = str(uuid.uuid4())
    make_snapshot(engine=snapshot, file_name=line.render(), output_name="../charts/image/%s.png" % imagesname,is_remove_html=True)
    image_data = open("../charts/image/%s.png" % imagesname, "rb").read()
    result = base64.b64encode(image_data)
    returnres = {"state": 200, "msg": "succsuful", "result": result}
    return jsonify(returnres)


#反序列化测试
@Linebp.route('/test')
def test():
    # 反序列化
    data = request.get_data()
    data = json.loads(data)
    print(data)
    try:
        schema = norlineSchema()
        data = schema.load(data)
        data = schema.dump(data)
        print(data)
    except ValidationError as err:
        error = err.messages
        print(error)
    returnres = {"state": 200, "msg": "succsuful", "result": 'result'}
    return jsonify(returnres)