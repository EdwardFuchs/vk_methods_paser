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
                soup = soup_full.find('div', {'class': 'page_block', 'class': 'dev_method_block', 'class': 'dev_block_spoiler'})
                if soup == None:
                    print(f"{vk_class}.{method} не найден div с классами: page_block, dev_method_block, dev_block_spoiler")
                    continue
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
                #Переделываем в строки все
                for i in range (len(params_desc_all_row)):
                    param_name = params_names_all_row[i].text
                    if param_name == "global":
                        param_name = "global_"
                    if param_name == "from":
                        param_name = "from_"
                    param_type = params_desc_type_row[i].text
                    #убираем тип переменной из описания
                    param_desc = params_desc_all_row[i].text[:-len(param_type)]
                    vk_class_dict[vk_class][method][param_name] = {'desc': param_desc, 'type': param_type}
                if debug:
                    print(f"{vk_class}.{method} успешно пропарсен")
            except Exception as e:
                    print(f"{vk_class}.{method} с ошибкой: {e}")
    return vk_class_dict

def create_vk_class_file(vk_class_dict : dict, debug : bool = False):
        if debug:
            print("Открываем файл")
        vk_class_file = open("vk_class.py", encoding="utf-8", mode="w")
        #создание класса Vk
        up_str = f"""class Vk:
    def __init__(self, event):
        self.event = event
        try:
            vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
            self.vk_class_dict = json.loads(vk_class_dict_file.read())
            vk_class_dict_file.close()
        except:
            self.vk_class_dict = None\n"""
        down_str = ""
        #vk_class_file.write()
        for vk_class in vk_class_dict:
            #заполение класса вк другими классами
            up_str+= f"        self.{vk_class} = self.{vk_class}(event)\n"
            #создание других классов
            down_str+= f"""    class {vk_class}:
        def  __init__(self, event):
            self.event = event\n"""
            #создание методов для классов
            for method in vk_class_dict[vk_class]:
                down_str+= f"        def {method}("
                args = vk_class_dict[vk_class][method]
                # TODO: помечать типы данных
                args_str = " = None, ".join(args)
                if args_str != "":
                    args_str = "v = None, access_token = None, " + args_str + " = None"
                else:
                    args_str = "v = None, access_token = None"
                down_str += f"""{args_str}):
            pass\n"""
            down_str+="\n\n"


        res = up_str + "\n\n" + down_str
        vk_class_file.write(res)
        if debug:
            print("Закрываем файл")
        vk_class_file.close()

if __name__ == '__main__':
    debug = True
    generate = False
    if generate:
        #генерируем dict
        # TODO: дефолтное значение сделать
        vk_class_dict = generate_json(debug)
        vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="w")
        vk_class_dict_file.write(json.dumps(vk_class_dict))
        vk_class_dict_file.close()
    else:
        vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
        vk_class_dict = vk_class_dict_file.read()
        vk_class_dict_file.close()
        vk_class_dict = json.loads(vk_class_dict)
    create_vk_class_file(vk_class_dict, debug)
