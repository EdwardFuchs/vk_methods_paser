import requests
from bs4 import BeautifulSoup
import json

def generate_json(debug : bool = False):
    #url для полчения всех методов
    url = "https://vk.com/dev/methods"
    text = requests.get(url).text
    #Парсер
    soup = BeautifulSoup(text, 'html.parser')
    #Получаем все классы с вложенными в них функциями отдельно
    all_classes = soup.find_all('div', {'class': 'dev_methods_sect_rows'})
    #переменая для сохранения результата
    vk_class_dict = {}
    if debug:
        print("Получаем все классы и методы")
    for vk_class in all_classes:
            #название класса
            class_name = vk_class.find('div', {'class': 'wk_sub_header'}).text
            class_name = class_name[:1].lower() + class_name[1:]
            # TODO: сделать other
            if class_name != "other":
                vk_class_dict[class_name] = {}
                #получить список всех методов и убрать начало с классом
                class_methods = vk_class.find_all('span', {'class': 'dev_methods_list_span'})
                for class_method in class_methods:
                        class_method = class_method.text.split(".")[1]
                        vk_class_dict[class_name][class_method] = {}
    if debug:
        print("Парсим все методы")
    #парсим страниы с методами
    for vk_class in vk_class_dict:
        for method in vk_class_dict[vk_class]:
            try:
                url = f"https://vk.com/dev/{vk_class}.{method}"
                text = requests.get(url).text
                soup_full = BeautifulSoup(text, 'html.parser')
                #Находим блок параметров
                #dev_method_desc
                soup = soup_full.find('div', {'class': 'page_block', 'class': 'dev_method_block', 'class': 'dev_block_spoiler'})
                if soup == None:
                    print(f"{vk_class}.{method} не найден div с классами: page_block, dev_method_block, dev_block_spoiler")
                    continue
                #Описание функции
                method_desc = soup_full.find('div', {'class': 'dev_method_desc'})
                if method_desc == None:
                    print(f"{vk_class}.{method} не найден div с классом: dev_method_desc")
                    continue
                method_desc = method_desc.text
                #получаем все имена и описания параметров
                #Названия параметров
                params_names_all_row = soup.find_all('td', {'class': 'dev_param_name'})
                if params_names_all_row == None:
                    print(f"{vk_class}.{method} не найден td с классом: dev_param_name")
                    continue
                #Описания вместе с типами
                params_desc_all_row = soup.find_all('td', {'class': 'dev_param_desc fl_l'})
                if params_desc_all_row == None:
                    print(f"{vk_class}.{method} не найден td с классом: dev_param_desc fl_l")
                    continue
                #Типы параметров
                params_desc_type_row = soup.find_all('div', {'class': 'dev_param_opts'})
                if params_desc_all_row == None:
                    print(f"{vk_class}.{method} не найден td с классом: dev_param_opts")
                    continue
                required_params = []
                #создания поля параметров
                vk_class_dict[vk_class][method]["params"] = {}
                #Переделываем в строки все
                for i in range (len(params_desc_all_row)):
                    param_name = params_names_all_row[i].text
                    if param_name == "global":
                        param_name = "global_"
                    if param_name == "from":
                        param_name = "from_"
                    param_type = params_desc_type_row[i].text
                    #убираем тип переменной из описания
                    param_desc = params_desc_all_row[i].text#[:-len(param_type)]
                    param_type_python = None
                    if "число" in param_type:
                        param_type_python = "int"
                    elif "разделенных запятыми" in param_type:
                        param_type_python = "str"
                    elif " разделенных через запятую" in param_type:
                        param_type_python = "str"
                    elif "строка" in param_type:
                        param_type_python = "str"
                    elif "1 или 0" in param_type:
                        param_type_python = "bool"
                    elif "JSON-объект" in param_desc:
                        param_type_python = "str"
                    else:
                        param_type_python = "not defined"
                    default = "None"
                    #Заполнение обязательных параметров
                    if "обязательный параметр" in param_type:
                        required_params.append(param_name)
                    if "по умолчанию " in param_type:
                        default = param_type.split("по умолчанию ")[1].split(",")[0]
                    vk_class_dict[vk_class][method]["params"][param_name] = {'desc': param_desc, 'type': param_type_python, "default": default}
                #Добавление описания функции
                vk_class_dict[vk_class][method]["desc"] = method_desc
                #Добавление обязтельных параметров
                vk_class_dict[vk_class][method]["required_params"] = required_params
                if debug:
                    print(f"{vk_class}.{method} успешно пропарсен")
            except Exception as e:
                    print(f"{vk_class}.{method} с ошибкой: {e}")
            #input()
    return vk_class_dict

def create_vk_class_file(vk_class_dict : dict, debug : bool = False):
        if debug:
            print("Открываем файл")
        vk_class_file = open("vk_class.py", encoding="utf-8", mode="w")
        body = ""
        #создание класса Vk
        head = f"""# -*- coding: utf8 -*-
import json


class Vk:
    def __init__(self, event):
        self.event = event
        try:
            vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
            self.vk_class_dict = json.loads(vk_class_dict_file.read())
            vk_class_dict_file.close()
        except:
            self.vk_class_dict = None\n"""
        #vk_class_file.write()
        for vk_class in vk_class_dict:
            down_str = ""
            middle_str = ""
            #заполение класса вк другими классами
            head+= f"        self.{vk_class} = self.{vk_class}(self.exec_func)\n"
            #создание других классов
            middle_str+= f"""    class {vk_class}:
        def  __init__(self, exec_func):\n"""
            #создание методов для классов
            for method in vk_class_dict[vk_class]:
                args = vk_class_dict[vk_class][method]["params"]
                required_args= vk_class_dict[vk_class][method]["required_params"]
                #обработаем нужные парамаетры
                args_str = ""
                args_str_method = ""
                for arg in required_args:
                    args_str += f"{arg}, "
                for arg in args:
                    args_str_method += f"{arg} = {arg}, "
                    if arg not in required_args:
                        args_str += arg
                        if vk_class_dict[vk_class][method]["params"][arg]["type"] != "not defined":
                            args_str += f" : {vk_class_dict[vk_class][method]['params'][arg]['type']} = None, "
                        else:
                            args_str += " = None, "
                    else:
                        pass
                args_str = "(self, " + args_str + "v : str = None, access_token : str = None):\n"
                args_str_method += "v = v, access_token = access_token"
                middle_str+= f"            self.{method} = self.{method}(exec_func)\n"
                down_str+= f"""        class {method}:
            '''{vk_class_dict[vk_class][method]["desc"]}'''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {json.dumps(args, ensure_ascii=False)}
            def __call__"""
                down_str += args_str +f"""                self.exec_func("{vk_class}.{method}", {args_str_method})\n"""
            body += middle_str + down_str
        end = """    def exec_func(self, method, **kwargs):
        new_kwargs = {}
        for kwarg in kwargs:
            if kwargs[kwarg] != None:
                if kwarg == "global_":
                    new_kwargs["global"] = kwargs[kwarg]
                elif kwarg == "from_":
                    new_kwargs["from"] = kwargs[kwarg]
                else:
                    new_kwargs[kwarg] = kwargs[kwarg]
        print(f"Переданные аргументы: {new_kwargs}")

if __name__ == "__main__":
    Vk=Vk(123)
    Vk.widgets.getPages(widget_api_id = "123")
    print("widget_api_id - " + Vk.widgets.getPages.args["widget_api_id"]["desc"])"""
        res = head + "\n\n" + body + "\n\n" + end
        vk_class_file.write(res)
        if debug:
            print("Закрываем файл")
        vk_class_file.close()

if __name__ == '__main__':
    debug = True
    generate = False
    if generate:
        #генерируем dict
        vk_class_dict = generate_json(debug)
        vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="w")
        vk_class_dict_file.write(json.dumps(vk_class_dict))#, ensure_ascii=False))
        vk_class_dict_file.close()
    else:
        vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
        vk_class_dict = vk_class_dict_file.read()
        vk_class_dict_file.close()
        vk_class_dict = json.loads(vk_class_dict)
    create_vk_class_file(vk_class_dict, debug)
