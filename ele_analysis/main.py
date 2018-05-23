# -*- coding: utf-8 -*-
import pymongo
import csv

from shops import ShopAnalysis
from foods import FoodsAnalysis


if __name__ == '__main__':
    #analysis = FoodsAnalysis()
    analysis_shop = ShopAnalysis()
    analysis_food = FoodsAnalysis()
    # analysis.shops(db="food_fh_01", shop_table="shops", food_table="foods", out="范湖附近简餐.csv")
    # analysis.shops(db="food_fh_p102", table="shops", out="范湖_店铺_奶茶_P102.csv")
    # analysis.shops(db="food_fh_2", table="shops", out="范湖_店铺_面点_2.csv")
    # analysis.shops(db="food_fh_215", table="shops", out="范湖_店铺_包子_215.csv")
    # analysis.shops(db="food_fh_p14", table="shops", out="范湖_店铺_包子_P14.csv")
    # analysis.shops(db="food_fh_235", table="shops", out="范湖_店铺_小吃_235.csv")
    # analysis.shops(db="food_fh_p22", table="shops", out="范湖_店铺_小吃_P22.csv")
    #
    # analysis.shops(db="food_gg_p102", table="shops", out="光谷_店铺_奶茶_P102.csv")
    # analysis.shops(db="food_gg_2", table="shops", out="光谷_店铺_面点_2.csv")
    # analysis.shops(db="food_gg_215", table="shops", out="光谷_店铺_包子_215.csv")
    # analysis.shops(db="food_gg_p14", table="shops", out="光谷_店铺_包子_P14.csv")
    # analysis.shops(db="food_gg_235", table="shops", out="光谷_店铺_小吃_235.csv")
    # analysis.shops(db="food_gg_p22", table="shops", out="光谷_店铺_小吃_P22.csv")

    # 简餐便当 1
    # 本地菜系 8
    # 奶茶 -102
    # 面点 2
    # 包子 215
    # 包子 -14
    # 小吃鸭脖 235， -22

    #日韩料理 229
    #西餐 230
    #披萨意面 211   -40
    #米粉面馆 213   -24  -33
    #甜品 9  -17
    #面包蛋糕 12   -20
    #奶茶果汁 11   -37  -16



    #analysis_food.shops(db="food_gg_230", shop_table="shops", food_table="foods", out="光谷_菜品_日韩料理_229.csv")

    analysis_shop.shops(db="food_fh_1", table="shops", out=" 范湖_店铺_简餐_1.csv")
    analysis_shop.shops(db="food_fh_8", table="shops",out="范湖_店铺_本地菜系_8.csv")
    analysis_shop.shops(db="food_fh_2", table="shops", out="范湖_店铺_面点_2.csv")
    analysis_shop.shops(db="food_fh_p102", table="shops", out="范湖_店铺_奶茶_P102.csv")
    analysis_shop.shops(db="food_fh_215", table="shops", out="范湖_店铺_包子_215.csv")
    analysis_shop.shops(db="food_fh_p14", table="shops", out="范湖_店铺_包子_P14.csv")
    analysis_shop.shops(db="food_fh_235", table="shops", out="范湖_店铺_小吃鸭脖_235.csv")
    analysis_shop.shops(db="food_fh_p22", table="shops", out="范湖_店铺_小吃鸭脖_P22.csv")


    analysis_shop.shops(db="food_fh_229", table="shops", out="范湖_店铺_日韩料理_229.csv")
    analysis_shop.shops(db="food_fh_230", table="shops",out="范湖_店铺_西餐_230.csv")
    analysis_shop.shops(db="food_fh_211", table="shops", out="范湖_店铺_披萨意面_211.csv")
    analysis_shop.shops(db="food_fh_p40", table="shops", out="范湖_店铺_披萨意面_P40.csv")
    analysis_shop.shops(db="food_fh_213", table="shops", out="范湖_店铺_米粉面馆_213.csv")
    analysis_shop.shops(db="food_fh_p24", table="shops", out="范湖_店铺_米粉面馆_p24.csv")
    analysis_shop.shops(db="food_fh_p33", table="shops", out="范湖_店铺_米粉面馆_p33.csv")
    analysis_shop.shops(db="food_fh_9", table="shops", out="范湖_店铺_甜品_9.csv")
    analysis_shop.shops(db="food_fh_12", table="shops", out="范湖_店铺_面包蛋糕 _12.csv")
    analysis_shop.shops(db="food_fh_p20", table="shops", out="范湖_店铺_面包蛋糕 _p20.csv")

    analysis_shop.shops(db="food_fh_11", table="shops", out="范湖_店铺_奶茶果汁_235.csv")
    analysis_shop.shops(db="food_fh_p37", table="shops", out="范湖_店铺_奶茶果汁_P37.csv")
    analysis_shop.shops(db="food_fh_p16", table="shops", out="范湖_店铺_奶茶果汁_P16.csv")


    ###############光谷
    analysis_shop.shops(db="food_gg_1", table="shops", out="光谷_店铺_简餐_1.csv")
    analysis_shop.shops(db="food_gg_8", table="shops",out="光谷_店铺_本地菜系_8.csv")
    analysis_shop.shops(db="food_gg_2", table="shops", out="光谷_店铺_面点_2.csv")
    analysis_shop.shops(db="food_gg_p102", table="shops", out="光谷_店铺_奶茶_P102.csv")
    analysis_shop.shops(db="food_gg_215", table="shops", out="光谷_店铺_包子_215.csv")
    analysis_shop.shops(db="food_gg_p14", table="shops", out="光谷_店铺_包子_P14.csv")
    analysis_shop.shops(db="food_gg_235", table="shops", out="光谷_店铺_小吃鸭脖_235.csv")
    analysis_shop.shops(db="food_gg_p22", table="shops", out="光谷_店铺_小吃鸭脖_P22.csv")


    analysis_shop.shops(db="food_gg_229", table="shops", out="光谷_店铺_日韩料理_229.csv")
    analysis_shop.shops(db="food_gg_230", table="shops",out="光谷_店铺_西餐_230.csv")
    analysis_shop.shops(db="food_gg_211", table="shops", out="光谷_店铺_披萨意面_211.csv")
    analysis_shop.shops(db="food_gg_p40", table="shops", out="光谷_店铺_披萨意面_P40.csv")
    analysis_shop.shops(db="food_gg_213", table="shops", out="光谷_店铺_米粉面馆_213.csv")
    analysis_shop.shops(db="food_gg_p24", table="shops", out="光谷_店铺_米粉面馆_p24.csv")
    analysis_shop.shops(db="food_gg_p33", table="shops", out="光谷_店铺_米粉面馆_p33.csv")
    analysis_shop.shops(db="food_gg_9", table="shops", out="光谷_店铺_甜品_9.csv")
    analysis_shop.shops(db="food_gg_12", table="shops", out="光谷_店铺_面包蛋糕 _12.csv")
    analysis_shop.shops(db="food_gg_p20", table="shops", out="光谷_店铺_面包蛋糕 _p20.csv")

    analysis_shop.shops(db="food_gg_11", table="shops", out="光谷_店铺_奶茶果汁_235.csv")
    analysis_shop.shops(db="food_gg_p37", table="shops", out="光谷_店铺_奶茶果汁_P37.csv")
    analysis_shop.shops(db="food_gg_p16", table="shops", out="光谷_店铺_奶茶果汁_P16.csv")