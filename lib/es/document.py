from typing import Dict, List
from lib.es.crud import CRUD


class Document(CRUD):

    def __init__(self):
        super().__init__()
        self.index = "document"

    def search(self, text:str, category:str) -> List[Dict]:
        """キーワードで検索

        Args:
            text (str): 検索したいキーワード

        Returns:
            List[Dict]: 検索結果
        """
        if category == "":
            body = {
                "query": {
                    "match": {"content": text}
                }
            }
        else : 
            body = {
                "query": {
                    "bool" : {
                        "must" : [
                            {"match" : { "category" : category}}
                        ],
                        "should" : [
                            {"match": {"content": text}}
                        ]
                    }
                }
            }

        return self.execute_query(index=self.index, body=body, size=1000)