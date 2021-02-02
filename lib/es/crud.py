from elasticsearch import Elasticsearch
from typing import Dict, List
import pandas as pd


class CRUD():

    def __init__(self):
        super().__init__()
        host = "elasticsearch:9200"
        self.es = Elasticsearch(host)
        self.index = "index"
    
    def __del__(self):
        self.es.close()

    def execute_query(self, index:str, body:Dict, size:int) -> List[Dict]:
        """検索クエリを実行する
        Args:
            body (Dict): 検索クエリ
            size (int): 一度に検索する最大件数
        Returns:
            List[Dict]: 検索結果
        """
        response = self.es.search(index=index, body=body, size=size)

        result = []

        for doc in response['hits']['hits']:
            item = doc['_source']

            d1 = dict(id=doc['_id'])
            d2 = item
            d1.update(d2)

            result.append(d1)

        return result


    def register(self, document:Dict) -> Dict:
        """ドキュメントを登録する
        Args:
            document (Dict): 登録するdocumentの内容
        Returns:
            Dict: elasticsearchへのインデックス結果
        """
        return self.es.index(index=self.index, body=document)

    def search_all(self, size:int=10000) -> Dict:
        """ドキュメントを全件検索する
        Args:
            size (int, optional): 一度に検索する件数. Defaults to 10000.
        Returns:
            Dict: 検索結果
        """
        body = {"query": {"match_all": {}}}
        return self.execute_query(index=self.index, body=body, size=size)

    def search_by_id(self, _id:str,  size:int=1) -> List[Dict]:
        """ドキュメントをidで検索する
        Args:
            _id (str): 検索するid
            size (int, optional): 一度に検索するサイズ（該当は多くても1件）. Defaults to 1.
        Returns:
            List[Dict]: 検索結果
        """
        body = {
            "query": {
                "match": {"_id": _id}
            }
        }

        return self.execute_query(index=self.index, body=body, size=size)

    def update(self, doc_id: str, document: Dict) -> Dict:
        """ドキュメントを更新する
        Args:
            doc_id (str): 更新したいdocumentのid
            document (Dict): 更新内容
        Returns:
            Dict: 更新結果
        """
        return self.es.update(index=self.index, doc_type=index, id=doc_id, body={"doc": document})

    def delete_by_id(self, doc_id: str) -> Dict:
        """ドキュメントを削除する
        Args:
            doc_id (str): 削除対象のdocumentのid
        Returns:
            Dict: 削除結果
        """

        return self.es.delete(index=self.index, doc_type=index, id=doc_id)