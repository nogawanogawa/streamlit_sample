from elasticsearch import Elasticsearch
from typing import Dict, List
import json
import os

class Index():
    
    def __init__(self):
        super().__init__()
        host = "elasticsearch:9200"
        self.es = Elasticsearch(host)
        self.index = "index"

    def get_all(self) -> List[str]:
        """インデックスの一覧を取得する
        Returns:
            List[str]: ユーザー定義のindexの一覧 
        """

        indices = self.es.cat.indices(index='*', h='index').splitlines()

        index_list = []

        for i in indices:
            if not i.startswith("."):
                index_list.append(i)

        return index_list

    def create(self, index_name: str) -> Dict:
        """mappingにしたがってindexを作成する
        Args:
            index_name (str): インデックスの名前
        Returns:
            Dict: インデックスの作成結果
        
        Note:
            lib/es/mapping/index名.jsonというファイルが定義されている必要がある
        """
        FILENAME = index_name + ".json"
        path = os.getcwd()
        fd = open(os.path.join(path, "lib/es/mapping", FILENAME), mode='r')
        mapping = json.load(fd)
        fd.close()

        return self.es.indices.create(index=index_name, body=mapping)

    def delete(self, index_name:str) -> Dict:
        """指定されたindexを削除する
        Args:
            index_name (str): 削除対象のindex名
        Returns:
            Dict: 削除処理の結果
        """
        return self.es.indices.delete(index=index_name)