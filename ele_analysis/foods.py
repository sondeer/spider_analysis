# -*- coding: utf-8 -*-
import pymongo
import csv


class FoodsAnalysis(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="localhost")
        self.db = self.client["food"]
        self.shop_tb = self.db["shops"]
        self.tb = self.db["foods"]

    def shops(self, db, shop_table, food_table, out):
        self.db = self.client[db]
        self.shop_tb = self.db[shop_table]
        self.tb = self.db[food_table]

        with open("./{}".format(out), "w", newline='') as f:
            title = ["菜品ID", "名称", "价格", "店铺ID", "店铺名称", "月售"]

            writer = csv.writer(f)

            writer.writerow(title)

            result = self.tb.find().sort("month_sales", -1)

            for record in result:

                shop_id = record.get("shop_id")

                shop = self.shop_tb.find({"id": shop_id})

                # shop_name = ""
                shop_name = shop[0].get("name")

                price = record.get("sku")[0]["price"]

                result_row = [record.get("product_id"),
                              record.get("name"),
                              price,
                              shop_id,
                              shop_name,
                              record.get("month_sales")]

                try:
                    writer.writerow(result_row)
                except Exception as ex:
                    print(ex)

        print(self.tb.count())
