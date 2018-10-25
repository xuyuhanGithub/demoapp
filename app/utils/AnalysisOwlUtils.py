from owlready2 import *
import json

#本体文件解析类
class AnalysisOwlUtils:
    #读OWL文件
    def readOwl(filepath):
        #OWL文件加载
        onto = get_ontology(filepath).load()
        return onto

    #存储OWL文件
    def saveOwl(filepath,onto):
        onto.save(file=filepath)

    #读取OWL文件内的所有本体对象
    #返回:List
    #例：['检查', 'FPG', 'OGTT', '妊娠期检测', '子宫张力', '宫高曲线', '眼科检查', '血糖检查']
    def getAllClasses(onto):
        classlists = []
        ontolists = list(onto.classes())
        for li in ontolists:
            classlists.append(li.name)
        return classlists

    #获取所有对象及子对象信息，List返回
    #输入：本体对象
    #输出：列表[{'name':'*','children':[*]},{'name':'**','children':[**]}]，列表元素为字典
    # 例：[{'name':'检查'，'children':[{'name':'血糖检查','children':[]},{...},{...}]},{***},{***}]
    def getAllClassesInfo(onto):
        classesContent = []
        list_dicts = []
        for owlclass in list(onto.classes()):
            #获取子对象，存入set中
            sets = owlclass.descendants()
            sets.remove(owlclass)
            for set in sets:
                #子对象信息存入content列表中
                classesContent.append(set.name)
            dict_Content = {'name': owlclass.name, 'children': classesContent}
            classesContent = []
            list_dicts.append(dict_Content)
        for list_dict in list_dicts:
            for i in range(len(list_dict['children'])):
                for j in range(len(list_dicts)):
                    if (list_dict['children'][i] == list_dicts[j]['name']):
                        list_dict['children'][i] = list_dicts[j]
        removeLists = []
        for listutil in list_dicts:
            if len(listutil['children']):
                removeLists.append(listutil)
        return removeLists

    #按照关键字进行查询
    # 输入 本体名 （String:'FRG'）
    # 输出 例：{'Name': 'FPG', 'Children': []}  （字典）
    def getClassInfo(ContentList,ClassName):
        for ClassDir in ContentList:
            if ClassDir['name'] == ClassName:
                return ClassDir

    # json数据返回
    def returnByJson(lists):
        dict_Thing = {'name': 'Thing', 'children': lists}
        jsonValue = json.dumps(dict_Thing, ensure_ascii=False)
        return jsonValue

#测试
if __name__ == '__main__':
    filepath = 'onto.owl'
    #步骤：
    #   Step1:读取owl文件
    #   Step2:获取本体中所有的类
    #   Step3:单独本体信息的查询
    #   Step4:包装为JSON格式的数据
    ## Step1
    onto = AnalysisOwlUtils.readOwl(filepath)
    ## Step2
    removeLists = AnalysisOwlUtils.getAllClassesInfo(onto)
    ## Step3
    dir = AnalysisOwlUtils.getClassInfo(removeLists,'检查')
    ## Step4
    js = AnalysisOwlUtils.returnByJson(removeLists)
    #打印
    print(onto)
    print(removeLists)
    print(dir)
    print(js)
