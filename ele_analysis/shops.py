# -*- coding: utf-8 -*-
import pymongo
import csv


class ShopAnalysis(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host="localhost")
        self.db = self.client["food_gg"]
        self.tb = self.db["shops"]

    def shops(self, db, table, out):
        self.db = self.client[db]
        self.tb = self.db[table]

        with open("./shop/{}".format(out), "w", newline='') as f:
            title = ["店铺ID","名称", "地址", "坐标", "月售"]

            writer = csv.writer(f)

            writer.writerow(title)

            result = self.tb.find().sort("sales", -1)

            for record in result:
                result_row = [record.get("id"),
                              record.get("name"),
                              record.get("address"),
                              record.get("position"),
                              record.get("sales"), ]

                try:
                    writer.writerow(result_row)
                except Exception as ex:
                    print(ex)

        print(self.tb.count())