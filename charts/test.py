from pyecharts.charts import Bar
from pyecharts import options as opts

# 导入输出图片工具
from pyecharts.render import make_snapshot
# 使用snapshot-selenium 渲染图片
from snapshot_selenium import snapshot

# 创建一个柱状图Bar实例

bar = (
    Bar()
    # 添加X轴数据
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    # 添加Y轴数据,系列的名称
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [8, 15, 60, 20, 25, 30])
    # 添加标题
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题: 双十一销量", subtitle="副标题:服饰类"))
)

# 输出保存为图片
make_snapshot(snapshot, bar.render(), "Options配置项_自定义样式_保存图片.png")