# -*- coding: utf-8 -*-
# author:LJ

import geopandas
import matplotlib.pyplot as plt
import requests
from shapely import geometry
import json


# 获取所有数据json文件
def download_json(url, name):
    print("正在下载json文件 %s" % url)
    try:
        # 将响应信息进行json格式化
        response = requests.get(url)
        versioninfo = response.text
        # print(versionInfo)
        versioninfopython = json.loads(versioninfo)
        # print(versionInfo)
        # 将json格式化的数据保存
        with open(name, "w", encoding="ANSI") as f1:
            f1.write(json.dumps(versioninfopython, indent=4))
        print("下载成功，文件保存位置：" + name)
    except:
        print("下载出错!!!")
        pass


def show_json(namei):
    data = geopandas.read_file(namei)
    cq = geopandas.GeoSeries([geometry.Point([116.0, 39.0])],
                             crs="EPSG:4326")

    fig, ax = plt.subplots()
    data.to_crs(crs="EPSG:4524").plot(ax=ax, color="#4C92C3",
                                      alpha=0.8)
    cq.to_crs(crs="EPSG:4524").plot(ax=ax, color="orange",
                                    markersize=100,
                                    marker="*")
    plt.xticks(roration=20)
    plt.savefig(".\\ttt.png")
    plt.show()


# 将json保存为shpfile
def saveshpfile(namei, filei):
    try:
        print(namei, type(namei))
        data = geopandas.read_file(namei)
        data.to_file(filei)
        print("WellDone!!!")
    except:
        print("Try Again!!!")


if __name__ == "__main__":
    folder = "c:\\users\\lj\\desktop\\"
    # print(os.getcwd())
    # file = folder + "ttt.json"
    # data = geopandas.read_file(file)
    # ax = data.plot()
    # localpath = folder + "xxx"
    # data.to_file(localpath, driver="ESRI Shapefile", encoding="utf-8")
    # print("Good!")

    # 下载json文件
    urls = [
        ("https://geo.datav.aliyun.com/areas/bound/330100_full.json", "hangzhou"),
        ("https://geo.datav.aliyun.com/areas/bound/geojson?code=310000_full", "shanghai"),
            ]
    # for i in range(len(urls)):
    for i in range(1, 2):
        uri = urls[i][0]
        # namei = os.getcwd() + "\\" + urls[i][1] + ".json"
        namei = folder + "\\" + urls[i][1] + ".json"
        filei = folder + urls[i][1]
        # 下载json
        download_json(uri, namei)
        # 显示行政区划
        # show_json(namei)
        # 转化为矢量
        saveshpfile(namei, filei)