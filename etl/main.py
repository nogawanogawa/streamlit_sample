import os
import glob
from metaflow import FlowSpec, step
from lib.es.document import Document
from lib.es.index import Index
from step.extract.extract import *
from lib.wakati.wakati import * 

class Workflow(FlowSpec):

    @step
    def start(self):
        self.next(self.initialize_index)

    @step
    def initialize_index(self):
        """indexを削除し、初期のマッピングを作成"""
        index = Index()

        # indexの一覧を取得
        index_list = index.get_all()

        # 残っているindexの削除
        for i in index_list:
            res = index.delete(i)
            assert res["acknowledged"] == True

        # mappingが存在するindexを作成
        path = os.getcwd()
        mapping_dir = os.path.join(path, "lib/es/mapping")
        mappings = glob.glob(os.path.join(mapping_dir, '*.json'))

        for mapping in mappings:
            filename = mapping.split("/")[-1]
            index_name = filename.split(".")[0]
            res = index.create(index_name=index_name)
            assert res["acknowledged"] == True

        self.next(self.extract_load)

    @step
    def extract_load(self):
        """dictの内容をESに挿入"""
        document = Document()

        PATH = "/app/text"
        for dir in corpus_subdirs(PATH):
            target_dir = os.path.join(PATH, dir)
            for corpus in corpus_filenames(target_dir):
                corpus_data = open(os.path.join(target_dir, corpus), "r")
                text = corpus_data.read()

                doc = {}
                doc["category"] = dir
                doc["content"] = ''.join(text.split("\n")[3:])
                doc["title"] = text.split("\n")[2]
                doc["date"] = text.split("\n")[1]
                doc["wakati"] = get_token(doc["content"])

                res = document.register(doc)
                print(res)

        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == '__main__':
    Workflow()