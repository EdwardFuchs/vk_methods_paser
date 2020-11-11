# -*- coding: utf8 -*-
import json


class Vk:
    def __init__(self, event):
        self.event = event
        try:
            vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
            self.vk_class_dict = json.loads(vk_class_dict_file.read())
            vk_class_dict_file.close()
        except:
            self.vk_class_dict = None
        self.execute = self.execute(self.exec_func)
        self.account = self.account(self.exec_func)
        self.appWidgets = self.appWidgets(self.exec_func)
        self.apps = self.apps(self.exec_func)
        self.auth = self.auth(self.exec_func)
        self.board = self.board(self.exec_func)
        self.database = self.database(self.exec_func)
        self.docs = self.docs(self.exec_func)
        self.donut = self.donut(self.exec_func)
        self.downloadedGames = self.downloadedGames(self.exec_func)
        self.fave = self.fave(self.exec_func)
        self.friends = self.friends(self.exec_func)
        self.gifts = self.gifts(self.exec_func)
        self.groups = self.groups(self.exec_func)
        self.leadForms = self.leadForms(self.exec_func)
        self.likes = self.likes(self.exec_func)
        self.market = self.market(self.exec_func)
        self.messages = self.messages(self.exec_func)
        self.newsfeed = self.newsfeed(self.exec_func)
        self.notes = self.notes(self.exec_func)
        self.notifications = self.notifications(self.exec_func)
        self.pages = self.pages(self.exec_func)
        self.photos = self.photos(self.exec_func)
        self.polls = self.polls(self.exec_func)
        self.prettyCards = self.prettyCards(self.exec_func)
        self.search = self.search(self.exec_func)
        self.stats = self.stats(self.exec_func)
        self.status = self.status(self.exec_func)
        self.storage = self.storage(self.exec_func)
        self.stories = self.stories(self.exec_func)
        self.streaming = self.streaming(self.exec_func)
        self.users = self.users(self.exec_func)
        self.utils = self.utils(self.exec_func)
        self.video = self.video(self.exec_func)
        self.wall = self.wall(self.exec_func)
        self.widgets = self.widgets(self.exec_func)


    class account:
        def  __init__(self, exec_func):
            self.ban = self.ban(exec_func)
            self.changePassword = self.changePassword(exec_func)
            self.getActiveOffers = self.getActiveOffers(exec_func)
            self.getAppPermissions = self.getAppPermissions(exec_func)
            self.getBanned = self.getBanned(exec_func)
            self.getCounters = self.getCounters(exec_func)
            self.getInfo = self.getInfo(exec_func)
            self.getProfileInfo = self.getProfileInfo(exec_func)
            self.getPushSettings = self.getPushSettings(exec_func)
            self.registerDevice = self.registerDevice(exec_func)
            self.saveProfileInfo = self.saveProfileInfo(exec_func)
            self.setInfo = self.setInfo(exec_func)
            self.setNameInMenu = self.setNameInMenu(exec_func)
            self.setOffline = self.setOffline(exec_func)
            self.setOnline = self.setOnline(exec_func)
            self.setPushSettings = self.setPushSettings(exec_func)
            self.setSilenceMode = self.setSilenceMode(exec_func)
            self.unban = self.unban(exec_func)
            self.unregisterDevice = self.unregisterDevice(exec_func)
        class ban:
            '''Добавляет пользователя или группу в черный список. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которое будет добавлено в черный список. целое число", "type": "int", "default": "None"}}
            def __call__(self, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("account.ban", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class changePassword:
            '''Позволяет сменить пароль пользователя после успешного восстановления доступа к аккаунту через СМС, используя метод auth.restore. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"restore_sid": {"desc": "идентификатор сессии, полученный при восстановлении доступа используя метод auth.restore. (В случае если пароль меняется сразу после восстановления доступа) строка", "type": "str", "default": "None"}, "change_password_hash": {"desc": "хэш, полученный при успешной OAuth авторизации по коду полученному по СМС (В случае если пароль меняется сразу после восстановления доступа) строка", "type": "str", "default": "None"}, "old_password": {"desc": "текущий пароль пользователя. строка", "type": "str", "default": "None"}, "new_password": {"desc": "новый пароль, который будет установлен в качестве текущего. строка, минимальная длина 6, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, new_password, restore_sid : str = None, change_password_hash : str = None, old_password : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.changePassword", restore_sid = restore_sid, change_password_hash = change_password_hash, old_password = old_password, new_password = new_password, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getActiveOffers:
            '''Возвращает список активных рекламных предложений (офферов), выполнив которые пользователь сможет получить соответствующее количество голосов на свой счёт внутри приложения. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определенного подмножества офферов. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество офферов, которое необходимо получить положительное число, по умолчанию 100, максимальное значение 100", "type": "int", "default": "100"}}
            def __call__(self, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("account.getActiveOffers", offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAppPermissions:
            '''Получает настройки текущего пользователя в данном приложении. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, информацию о настройках которого необходимо получить. По умолчанию — текущий пользователь. положительное число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, user_id, v : str = None, access_token : str = None):
                self.exec_func("account.getAppPermissions", user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getBanned:
            '''Возвращает список пользователей, находящихся в черном списке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определенного подмножества черного списка. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество объектов, информацию о которых необходимо вернуть. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}}
            def __call__(self, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("account.getBanned", offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCounters:
            '''Возвращает ненулевые значения счетчиков пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"filter": {"desc": "счетчики, информацию о которых нужно вернуть. Может включать следующие значения: \n\nfriends — новые заявки в друзья; \nfriends_suggestions — предлагаемые друзья; \nmessages — новые сообщения; \nphotos — новые отметки на фотографиях; \nvideos — новые отметки на видеозаписях; \ngifts — подарки; \nevents — события; \ngroups — сообщества; \nnotifications — ответы; \nsdk — запросы в мобильных играх; \napp_requests — уведомления от приложений. \nfriends_recommendations — рекомендации друзей. \nсписок слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, filter : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.getCounters", filter = filter, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getInfo:
            '''Возвращает информацию о текущем аккаунте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"fields": {"desc": "список полей, которые необходимо вернуть. Возможные значения: \n\ncountry \nhttps_required \nown_posts_default \nno_wall_replies \nintro \nlang \nПо умолчанию будут возвращены все поля. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.getInfo", fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getProfileInfo:
            '''Возвращает информацию о текущем профиле. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("account.getProfileInfo", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPushSettings:
            '''Позволяет получать настройки Push-уведомлений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"device_id": {"desc": "уникальный идентификатор устройства. строка, доступен начиная с версии 5.31", "type": "str", "default": "None"}, "token": {"desc": "Идентификатор устройства, используемый для отправки уведомлений. (для mpns идентификатор должен представлять из себя URL для отправки уведомлений) строка, устаревший параметр, доступен только для версий меньше 5.31", "type": "str", "default": "None"}}
            def __call__(self, device_id : str = None, token : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.getPushSettings", device_id = device_id, token = token, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class registerDevice:
            '''Подписывает устройство на базе iOS, Android, Windows Phone или Mac на получение Push-уведомлений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"token": {"desc": "идентификатор устройства, используемый для отправки уведомлений. (для mpns идентификатор должен представлять из себя URL для отправки уведомлений). строка, обязательный параметр", "type": "str", "default": "None"}, "device_model": {"desc": "cтроковое название модели устройства. строка", "type": "str", "default": "None"}, "device_year": {"desc": "год устройства. целое число", "type": "int", "default": "None"}, "device_id": {"desc": "уникальный идентификатор устройства. строка, обязательный параметр", "type": "str", "default": "None"}, "system_version": {"desc": "строковая версия операционной системы устройства. строка", "type": "str", "default": "None"}, "settings": {"desc": "сериализованный JSON-объект, описывающий настройки уведомлений в специальном формате. данные в формате JSON, доступен начиная с версии 5.31", "type": "str", "default": "None"}, "sandbox": {"desc": "флаг предназначен для iOS устройств. 1 — использовать sandbox сервер для отправки push-уведомлений, 0 — не использовать. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "no_text": {"desc": "1 — не передавать текст сообщения в push уведомлении. 0 — (по умолчанию) текст сообщения передаётся. целое число, устаревший параметр, доступен только для версий меньше 5.31", "type": "int", "default": "None"}, "subscribe": {"desc": "Список типов уведомлений, которые следует присылать. Могут быть переданы следующие типы: msg, friend, call, reply, mention, group, like. По умолчанию присылаются: msg, friend. строка, устаревший параметр, доступен только для версий меньше 5.31", "type": "str", "default": "None"}}
            def __call__(self, token, device_id, device_model : str = None, device_year : int = None, system_version : str = None, settings : str = None, sandbox : bool = None, no_text : int = None, subscribe : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.registerDevice", token = token, device_model = device_model, device_year = device_year, device_id = device_id, system_version = system_version, settings = settings, sandbox = sandbox, no_text = no_text, subscribe = subscribe, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveProfileInfo:
            '''Редактирует информацию текущего профиля. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"first_name": {"desc": "имя пользователя. Обязательно с большой буквы. строка", "type": "str", "default": "None"}, "last_name": {"desc": "фамилия пользователя. Обязательно с большой буквы. строка", "type": "str", "default": "None"}, "maiden_name": {"desc": "девичья фамилия пользователя (только для женского пола). строка", "type": "str", "default": "None"}, "screen_name": {"desc": "короткое имя страницы. строка", "type": "str", "default": "None"}, "cancel_request_id": {"desc": "идентификатор заявки на смену имени, которую необходимо отменить. \nЕсли передан этот параметр, все остальные параметры игнорируются. положительное число", "type": "int", "default": "None"}, "sex": {"desc": "пол пользователя. Возможные значения: \n\n1 — женский; \n2 — мужской. \nположительное число", "type": "int", "default": "None"}, "relation": {"desc": "семейное положение пользователя. Возможные значения: \n\n1 — не женат/не замужем; \n2 — есть друг/есть подруга; \n3 — помолвлен/помолвлена; \n4 — женат/замужем; \n5 — всё сложно; \n6 — в активном поиске; \n7 — влюблён/влюблена; \n8 — в гражданском браке; \n0 — не указано. \nположительное число", "type": "int", "default": "None"}, "relation_partner_id": {"desc": "идентификатор пользователя, с которым связано семейное положение. положительное число", "type": "int", "default": "None"}, "bdate": {"desc": "дата рождения пользователя в формате DD.MM.YYYY, например \"15.11.1984\". строка", "type": "str", "default": "None"}, "bdate_visibility": {"desc": "видимость даты рождения. Возможные значения: \n\n1 — показывать дату рождения; \n2 — показывать только месяц и день; \n0 — не показывать дату рождения. \nположительное число", "type": "int", "default": "None"}, "home_town": {"desc": "родной город пользователя. строка", "type": "str", "default": "None"}, "country_id": {"desc": "идентификатор страны пользователя. положительное число", "type": "int", "default": "None"}, "city_id": {"desc": "идентификатор города пользователя. положительное число", "type": "int", "default": "None"}, "status": {"desc": "статус пользователя, который также может быть изменен методом status.set строка", "type": "str", "default": "None"}}
            def __call__(self, first_name : str = None, last_name : str = None, maiden_name : str = None, screen_name : str = None, cancel_request_id : int = None, sex : int = None, relation : int = None, relation_partner_id : int = None, bdate : str = None, bdate_visibility : int = None, home_town : str = None, country_id : int = None, city_id : int = None, status : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.saveProfileInfo", first_name = first_name, last_name = last_name, maiden_name = maiden_name, screen_name = screen_name, cancel_request_id = cancel_request_id, sex = sex, relation = relation, relation_partner_id = relation_partner_id, bdate = bdate, bdate_visibility = bdate_visibility, home_town = home_town, country_id = country_id, city_id = city_id, status = status, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setInfo:
            '''Позволяет редактировать информацию о текущем аккаунте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"name": {"desc": "имя настройки строка, доступен начиная с версии 5.49", "type": "str", "default": "None"}, "value": {"desc": "значение настройки строка, доступен начиная с версии 5.49", "type": "str", "default": "None"}, "intro": {"desc": "битовая маска, отвечающая за прохождение обучения в мобильных клиентах. положительное число, устаревший параметр, доступен только для версий меньше 5.49", "type": "int", "default": "None"}, "own_posts_default": {"desc": "1 – на стене пользователя по-умолчанию должны отображаться только собственные записи; \n0 – на стене пользователя должны отображаться все записи. флаг, может принимать значения 1 или 0, устаревший параметр, доступен только для версий меньше 5.49", "type": "bool", "default": "None"}, "no_wall_replies": {"desc": "1 – отключить комментирование записей на стене; \n0 – разрешить комментирование. флаг, может принимать значения 1 или 0, устаревший параметр, доступен только для версий меньше 5.49", "type": "bool", "default": "None"}}
            def __call__(self, name : str = None, value : str = None, intro : int = None, own_posts_default : bool = None, no_wall_replies : bool = None, v : str = None, access_token : str = None):
                self.exec_func("account.setInfo", name = name, value = value, intro = intro, own_posts_default = own_posts_default, no_wall_replies = no_wall_replies, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setNameInMenu:
            '''Устанавливает короткое название приложения (до 17 символов), которое выводится пользователю в левом меню. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}, "name": {"desc": "короткое название приложения. строка", "type": "str", "default": "None"}}
            def __call__(self, user_id, name : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.setNameInMenu", user_id = user_id, name = name, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setOffline:
            '''Помечает текущего пользователя как offline (только в текущем приложении). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("account.setOffline", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setOnline:
            '''Помечает текущего пользователя как online на 5 минут. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"voip": {"desc": "возможны ли видеозвонки для данного устройства флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, voip : bool = None, v : str = None, access_token : str = None):
                self.exec_func("account.setOnline", voip = voip, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setPushSettings:
            '''Изменяет настройку Push-уведомлений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"device_id": {"desc": "уникальный идентификатор устройства. строка, обязательный параметр", "type": "str", "default": "None"}, "settings": {"desc": "сериализованный JSON-объект, описывающий настройки уведомлений в специальном формате. данные в формате JSON", "type": "str", "default": "None"}, "key": {"desc": "ключ уведомления. строка", "type": "str", "default": "None"}, "value": {"desc": "новое значение уведомления в специальном формате. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, device_id, settings : str = None, key : str = None, value : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.setPushSettings", device_id = device_id, settings = settings, key = key, value = value, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setSilenceMode:
            '''Отключает push-уведомления на заданный промежуток времени. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"device_id": {"desc": "уникальный идентификатор устройства. строка, доступен начиная с версии 5.31", "type": "str", "default": "None"}, "time": {"desc": "время в секундах на которое требуется отключить уведомления, -1 отключить навсегда целое число", "type": "int", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. Для пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, доступен начиная с версии 5.46", "type": "int", "default": "None"}, "sound": {"desc": "1 — включить звук в этом диалоге, 0 — отключить звук (параметр работает, только если в peer_id передан идентификатор групповой беседы или пользователя). целое число", "type": "int", "default": "None"}, "token": {"desc": "идентификатор устройства для сервиса push уведомлений. строка, устаревший параметр, доступен только для версий меньше 5.31", "type": "str", "default": "None"}, "chat_id": {"desc": "идентификатор чата, для которого следует отключить уведомления целое число, устаревший параметр, доступен только для версий меньше 5.46", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, для которого следует отключить уведомления целое число, устаревший параметр, доступен только для версий меньше 5.46", "type": "int", "default": "None"}}
            def __call__(self, device_id : str = None, time : int = None, peer_id : int = None, sound : int = None, token : str = None, chat_id : int = None, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("account.setSilenceMode", device_id = device_id, time = time, peer_id = peer_id, sound = sound, token = token, chat_id = chat_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unban:
            '''Удаляет пользователя или группу из черного списка. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или группы, которого нужно удалить из черного списка. целое число", "type": "int", "default": "None"}}
            def __call__(self, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("account.unban", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unregisterDevice:
            '''Отписывает устройство от Push уведомлений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"device_id": {"desc": "уникальный идентификатор устройства. строка, доступен начиная с версии 5.31", "type": "str", "default": "None"}, "sandbox": {"desc": "флаг предназначен для iOS устройств. Возможные значения: \n\n1 — отписать устройство, использующего sandbox сервер для отправки push-уведомлений; \n0 — отписать устройство, не использующее sandbox сервер. \nфлаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "token": {"desc": "идентификатор устройства, используемый для отправки уведомлений. строка, устаревший параметр, доступен только для версий меньше 5.31", "type": "str", "default": "None"}}
            def __call__(self, device_id : str = None, sandbox : bool = None, token : str = None, v : str = None, access_token : str = None):
                self.exec_func("account.unregisterDevice", device_id = device_id, sandbox = sandbox, token = token, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class appWidgets:
        def  __init__(self, exec_func):
            self.getAppImageUploadServer = self.getAppImageUploadServer(exec_func)
            self.getAppImages = self.getAppImages(exec_func)
            self.getGroupImageUploadServer = self.getGroupImageUploadServer(exec_func)
            self.getGroupImages = self.getGroupImages(exec_func)
            self.getImagesById = self.getImagesById(exec_func)
            self.saveAppImage = self.saveAppImage(exec_func)
            self.saveGroupImage = self.saveGroupImage(exec_func)
            self.update = self.update(exec_func)
        class getAppImageUploadServer:
            '''Позволяет получить адрес для загрузки фотографии в коллекцию приложения для виджетов приложений сообществ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"image_type": {"desc": "тип изображения. Возможные значения: \n\n24x24; \n50x50; \n160x160; \n160x240; \n510x128. \nобязательный параметр", "type": "not defined", "default": "None"}}
            def __call__(self, image_type, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.getAppImageUploadServer", image_type = image_type, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAppImages:
            '''Позволяет получить коллекцию изображений, загруженных для приложения, в виджетах приложений сообществ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.getAppImages", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getGroupImageUploadServer:
            '''Позволяет получить адрес для загрузки фотографии в коллекцию сообщества для виджетов приложений сообществ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.getGroupImageUploadServer", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getGroupImages:
            '''Позволяет получить коллекцию изображений, загруженных для приложения, в виджетах приложений сообществ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.getGroupImages", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getImagesById:
            '''Позволяет получить изображение для виджетов приложений сообществ по его идентификатору. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.getImagesById", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveAppImage:
            '''Позволяет сохранить изображение в коллекцию приложения для виджетов приложений сообществ после загрузки на сервер. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"hash": {"desc": "параметр hash, полученный после загрузки на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "image": {"desc": "параметр image, полученный после загрузки на сервер. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, hash, image, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.saveAppImage", hash = hash, image = image, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveGroupImage:
            '''Позволяет сохранить изображение в коллекцию сообщества для виджетов приложений сообществ. после загрузки на сервер. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.saveGroupImage", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class update:
            '''Позволяет обновить виджет приложения сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("appWidgets.update", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class apps:
        def  __init__(self, exec_func):
            self.deleteAppRequests = self.deleteAppRequests(exec_func)
            self.get = self.get(exec_func)
            self.getCatalog = self.getCatalog(exec_func)
            self.getFriendsList = self.getFriendsList(exec_func)
            self.getLeaderboard = self.getLeaderboard(exec_func)
            self.getScopes = self.getScopes(exec_func)
            self.getScore = self.getScore(exec_func)
            self.promoHasActiveGift = self.promoHasActiveGift(exec_func)
            self.promoUseGift = self.promoUseGift(exec_func)
            self.sendRequest = self.sendRequest(exec_func)
        class deleteAppRequests:
            '''Удаляет все уведомления о запросах, отправленных из текущего приложения '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("apps.deleteAppRequests", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает данные о запрошенном приложении. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"app_id": {"desc": "идентификатор приложения, данные которого необходимо получить. \nЕсли этот параметр и параметр app_ids не указан, возвращается идентификатор приложения, через которое выдан ключ доступа (access_token). положительное число", "type": "int", "default": "None"}, "app_ids": {"desc": "список идентификаторов приложений, данные которых необходимо получить. список слов, разделенных через запятую, количество элементов должно составлять не более 100", "type": "str", "default": "None"}, "platform": {"desc": "платформа, для которой необходимо вернуть данные. Возможные значения: \n\nios — iOS; \nandroid — Android; \nwinphone — Windows Phone; \nweb — приложения на vk.com. \nПо умолчанию: web. строка, по умолчанию web", "type": "str", "default": "web"}, "extended": {"desc": "1 — возвращать дополнительные поля. По умолчанию возвращает только основные поля приложений. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "return_friends": {"desc": "1 – возвращать список друзей, установивших это приложение. По умолчанию: 0. \nПараметр учитывается только при передаче access_token. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть для профилей пользователей. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters,screen_name,timezone \nПараметр учитывается только при return_friends = 1. список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователей. Возможные значения: * nom — именительный (по умолчанию); \n\ngen — родительный; \ndat — дательный; \nacc — винительный; \nins — творительный; \nabl — предложный; \n\nПараметр учитывается только при return_friends = 1. строка", "type": "str", "default": "None"}}
            def __call__(self, app_id : int = None, app_ids : str = None, platform : str = None, extended : bool = None, return_friends : bool = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("apps.get", app_id = app_id, app_ids = app_ids, platform = platform, extended = extended, return_friends = return_friends, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCatalog:
            '''Возвращает список приложений, доступных для пользователей сайта через каталог приложений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"sort": {"desc": "способ сортировки приложений. Возможные значения: \n\npopular_today — популярные за день; \nvisitors — по посещаемости; \ncreate_date — по дате создания приложения; \ngrowth_rate — по скорости роста; \npopular_week — популярные за неделю. \nПо умолчанию: popular_today. строка", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества приложений. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество приложений, информацию о которых необходимо вернуть. положительное число, по умолчанию 100, обязательный параметр", "type": "int", "default": "100"}, "platform": {"desc": "платформа, для которой необходимо вернуть приложения. Возможные значения: \n\nios — iOS; \nandroid — Android; \nwinphone — Windows Phone; \nweb — приложения на vk.com; \nhtml5 — Direct Games. \nПо умолчанию: web. строка", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительные поля приложений. Если указан extended – count не должен быть больше 100. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "return_friends": {"desc": "1 – возвращать список друзей, установивших это приложение. По умолчанию: 0. \nПараметр учитывается только при передаче access_token. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть для профилей пользователей. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters,screen_name,timezone \nПараметр учитывается только при return_friends = 1. список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователей. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию: nom. \nПараметр учитывается только при return_friends = 1. строка", "type": "str", "default": "None"}, "q": {"desc": "поисковая строка для поиска по каталогу приложений. строка", "type": "str", "default": "None"}, "genre_id": {"desc": "идентификатор жанра положительное число", "type": "int", "default": "None"}, "filter": {"desc": "installed — возвращает список установленных приложений (только для мобильных приложений), \nfeatured — возвращает список приложений, установленных в \"Выбор редакции\" (только для мобильных приложений). строка", "type": "str", "default": "None"}}
            def __call__(self, count, sort : str = None, offset : int = None, platform : str = None, extended : bool = None, return_friends : bool = None, fields : str = None, name_case : str = None, q : str = None, genre_id : int = None, filter : str = None, v : str = None, access_token : str = None):
                self.exec_func("apps.getCatalog", sort = sort, offset = offset, count = count, platform = platform, extended = extended, return_friends = return_friends, fields = fields, name_case = name_case, q = q, genre_id = genre_id, filter = filter, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getFriendsList:
            '''Создает список друзей, который будет использоваться при отправке пользователем приглашений в приложение и игровых запросов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"extended": {"desc": "параметр, определяющий необходимость возвращать расширенную информацию о пользователях. Возможные значения: \n\n0 — возвращаются только идентификаторы; \n1 — будут дополнительно возвращены имя и фамилия. \n\nПо умолчанию: 0. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "count": {"desc": "количество пользователей в создаваемом списке. положительное число, по умолчанию 20, максимальное значение 5000", "type": "int", "default": "20"}, "offset": {"desc": "смещение относительно первого пользователя для выборки определенного подмножества. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "type": {"desc": "тип создаваемого списка друзей. Возможные значения: \n\ninvite — доступные для приглашения (не играют в игру); \nrequest — доступные для отправки запроса (уже играют). \n\nПо умолчанию: invite. строка, по умолчанию invite", "type": "str", "default": "invite"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, extended : bool = None, count : int = None, offset : int = None, type : str = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("apps.getFriendsList", extended = extended, count = count, offset = offset, type = type, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLeaderboard:
            '''Возвращает рейтинг пользователей в игре. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип турнирной таблицы. Возможные значения: \n\nlevel — по уровням; \npoints — по очкам, начисленным за выполнение миссий; \nscore — по очкам, начисленным напрямую (apps.getScore). \nстрока, обязательный параметр", "type": "str", "default": "None"}, "global_": {"desc": "тип рейтинга. Возможные значения: \n\n1 — глобальный рейтинг по всем игрокам (возвращается не более 20 результатов); \n0 — рейтинг по друзьям пользователя. \nфлаг, может принимать значения 1 или 0, по умолчанию 1", "type": "bool", "default": "1"}, "extended": {"desc": "1 — возвращать дополнительную информацию о пользователе. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, type, global_ : bool = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("apps.getLeaderboard", type = type, global_ = global_, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getScopes:
            ''''''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "строка, по умолчанию user", "type": "str", "default": "user"}}
            def __call__(self, type : str = None, v : str = None, access_token : str = None):
                self.exec_func("apps.getScopes", type = type, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getScore:
            '''Метод возвращает количество очков пользователя в этой игре. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, user_id, v : str = None, access_token : str = None):
                self.exec_func("apps.getScore", user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class promoHasActiveGift:
            '''Проверить есть ли у пользователя подарок в игре. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"promo_id": {"desc": "Идентификатор промо-акции положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "Идентификатор пользователя. Используется только при запросе с сервисным токеном положительное число", "type": "int", "default": "None"}}
            def __call__(self, promo_id, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("apps.promoHasActiveGift", promo_id = promo_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class promoUseGift:
            '''Использовать подарок, полученный пользователем в промо-акции. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"promo_id": {"desc": "Идентификатор акции. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "Идентификатор пользователя. Используется только при запросе с сервисным токеном. положительное число", "type": "int", "default": "None"}}
            def __call__(self, promo_id, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("apps.promoUseGift", promo_id = promo_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class sendRequest:
            '''Позволяет отправить запрос другому пользователю в приложении, использующем авторизацию ВКонтакте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которому следует отправить запрос. положительное число, обязательный параметр", "type": "int", "default": "None"}, "text": {"desc": "текст запроса. строка", "type": "str", "default": "None"}, "type": {"desc": "тип запроса. Возможные значения: \n\ninvite – если запрос отправляется пользователю, не установившему приложение; \nrequest – если пользователь уже установил приложение. \n\nОбратите внимание! Для запросов с type = invite действует ограничение — одному и тому же пользователю нельзя отправить запрос чаще одного раза в неделю. строка, по умолчанию request", "type": "str", "default": "request"}, "name": {"desc": "уникальное в рамках приложения имя для каждого вида отправляемого запроса. строка, максимальная длина 128", "type": "str", "default": "None"}, "key": {"desc": "строка, которая будет возвращена назад при переходе пользователя по запросу в приложение. Может использоваться для подсчета конверсии. строка", "type": "str", "default": "None"}, "separate": {"desc": "запрет на группировку запроса с другими, имеющими тот же name. 1 — группировка запрещена, 0 — группировка разрешена. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, user_id, text : str = None, type : str = None, name : str = None, key : str = None, separate : bool = None, v : str = None, access_token : str = None):
                self.exec_func("apps.sendRequest", user_id = user_id, text = text, type = type, name = name, key = key, separate = separate, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class auth:
        def  __init__(self, exec_func):
            self.checkPhone = self.checkPhone(exec_func)
            self.restore = self.restore(exec_func)
        class checkPhone:
            '''Проверяет правильность введённого номера (возможность его использования для регистрации или авторизации). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"phone": {"desc": "номер телефона регистрируемого пользователя. строка, обязательный параметр", "type": "str", "default": "None"}, "client_id": {"desc": "идентификатор Вашего приложения. целое число", "type": "int", "default": "None"}, "client_secret": {"desc": "секретный ключ приложения, доступный в разделе редактирования приложения. строка", "type": "str", "default": "None"}, "auth_by_phone": {"desc": "1 — проверить правильность номера для авторизации, а не для регистрации нового аккаунта. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, phone, client_id : int = None, client_secret : str = None, auth_by_phone : bool = None, v : str = None, access_token : str = None):
                self.exec_func("auth.checkPhone", phone = phone, client_id = client_id, client_secret = client_secret, auth_by_phone = auth_by_phone, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Позволяет восстановить доступ к аккаунту, используя код, полученный через SMS.
Данный метод доступен только приложениям, имеющим доступ к Прямой авторизации. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"phone": {"desc": "номер телефона пользователя. строка, обязательный параметр", "type": "str", "default": "None"}, "last_name": {"desc": "фамилия пользователя. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, phone, last_name, v : str = None, access_token : str = None):
                self.exec_func("auth.restore", phone = phone, last_name = last_name, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class board:
        def  __init__(self, exec_func):
            self.addTopic = self.addTopic(exec_func)
            self.closeTopic = self.closeTopic(exec_func)
            self.createComment = self.createComment(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.deleteTopic = self.deleteTopic(exec_func)
            self.editComment = self.editComment(exec_func)
            self.editTopic = self.editTopic(exec_func)
            self.fixTopic = self.fixTopic(exec_func)
            self.getComments = self.getComments(exec_func)
            self.getTopics = self.getTopics(exec_func)
            self.openTopic = self.openTopic(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
            self.unfixTopic = self.unfixTopic(exec_func)
        class addTopic:
            '''Создает новую тему в списке обсуждений группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "название обсуждения. строка, обязательный параметр", "type": "str", "default": "None"}, "text": {"desc": "текст первого сообщения в обсуждении. строка", "type": "str", "default": "None"}, "from_group": {"desc": "1 — тема будет создана от имени группы, 0 — тема будет создана от имени пользователя (по умолчанию). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к записи, в формате: <type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-приложения: \n\nphoto — фотография; \nvideo — видеозапись ; \naudio — аудиозапись; \ndoc — документ; \n\n<owner_id> — идентификатор владельца медиа-приложения \n<media_id> — идентификатор медиа-приложения. \nНапример:photo100172_166443618,photo66748_265827614 \nПараметр является обязательным, если не задан параметр text. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, title, text : str = None, from_group : bool = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("board.addTopic", group_id = group_id, title = title, text = text, from_group = from_group, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class closeTopic:
            '''Закрывает тему в списке обсуждений группы (в такой теме невозможно оставлять новые сообщения). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, v : str = None, access_token : str = None):
                self.exec_func("board.closeTopic", group_id = group_id, topic_id = topic_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Добавляет новый комментарий в обсуждении. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором находится обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор темы, в которой необходимо оставить комментарий. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст комментария. Обязательный параметр, если не передано значение attachments. строка, строка", "type": "str", "default": "None"}, "attachments": {"desc": "Список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-вложения:\nphoto — фотография;\nvideo — видеозапись;\naudio — аудиозапись;\ndoc — документ;\n\n<owner_id> — идентификатор владельца медиа-вложения;\n<media_id> — идентификатор медиа-вложения.\n\nНапример:\nphoto100172_166443618,photo66748_265827614 список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_group": {"desc": "1 — сообщение будет опубликовано от имени группы, 0 — сообщение будет опубликовано от имени пользователя (по умолчанию). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, topic_id, message : str = None, attachments : str = None, from_group : bool = None, sticker_id : int = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("board.createComment", group_id = group_id, topic_id = topic_id, message = message, attachments = attachments, from_group = from_group, sticker_id = sticker_id, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет сообщение темы в обсуждениях сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария в обсуждении. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, comment_id, v : str = None, access_token : str = None):
                self.exec_func("board.deleteComment", group_id = group_id, topic_id = topic_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteTopic:
            '''Удаляет тему в обсуждениях группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, v : str = None, access_token : str = None):
                self.exec_func("board.deleteTopic", group_id = group_id, topic_id = topic_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Редактирует одно из сообщений в обсуждении сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария в обсуждении. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "новый текст комментария (является обязательным, если не задан параметр attachments). строка, строка", "type": "str", "default": "None"}, "attachments": {"desc": "новый список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, topic_id, comment_id, message : str = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("board.editComment", group_id = group_id, topic_id = topic_id, comment_id = comment_id, message = message, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editTopic:
            '''Изменяет заголовок темы в списке обсуждений группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "новое название обсуждения. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, group_id, topic_id, title, v : str = None, access_token : str = None):
                self.exec_func("board.editTopic", group_id = group_id, topic_id = topic_id, title = title, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class fixTopic:
            '''Закрепляет тему в списке обсуждений группы (такая тема при любой сортировке выводится выше остальных). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, v : str = None, access_token : str = None):
                self.exec_func("board.fixTopic", group_id = group_id, topic_id = topic_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список сообщений в указанной теме. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, информацию об обсуждениях которого нужно получить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — будет возвращено дополнительное поле likes. По умолчанию поле likes не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_comment_id": {"desc": "идентификатор комментария, начиная с которого нужно вернуть список (подробности см. ниже). положительное число, доступен начиная с версии 5.33", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества сообщений. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество сообщений, которое необходимо получить (но не более 100). По умолчанию — 20. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "extended": {"desc": "Если указать в качестве этого параметра 1, то будет возвращена информация о пользователях, являющихся авторами сообщений. По умолчанию 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "sort": {"desc": "порядок сортировки комментариев:\nasc — хронологический\ndesc — антихронологический строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, topic_id, need_likes : bool = None, start_comment_id : int = None, offset : int = None, count : int = None, extended : bool = None, sort : str = None, v : str = None, access_token : str = None):
                self.exec_func("board.getComments", group_id = group_id, topic_id = topic_id, need_likes = need_likes, start_comment_id = start_comment_id, offset = offset, count = count, extended = extended, sort = sort, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTopics:
            '''Возвращает список тем в обсуждениях указанной группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, информацию об обсуждениях которого необходимо получить. Если сообщество закрытое или частное, для вызова метода потребуется право доступа groups. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_ids": {"desc": "список идентификаторов тем, которые необходимо получить (не более 100). По умолчанию возвращаются все темы. Если указан данный параметр, игнорируются параметры order, offset и count (возвращаются все запрошенные темы в указанном порядке). список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "order": {"desc": "Порядок, в котором необходимо вернуть список тем. Возможные значения: \n\n1 — по убыванию даты обновления; \n2 — по убыванию даты создания; \n-1 — по возрастанию даты обновления; \n-2 — по возрастанию даты создания. \nПо умолчанию темы возвращаются в порядке, установленном администратором группы. \"Прилепленные\" темы при любой сортировке возвращаются первыми в списке. целое число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества тем. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество тем, которое необходимо получить (но не более 100). По умолчанию — 40. положительное число, по умолчанию 40, максимальное значение 100", "type": "int", "default": "40"}, "extended": {"desc": "Если указать в качестве этого параметра 1, то будет возвращена информация о пользователях, являющихся создателями тем или оставившими в них последнее сообщение. По умолчанию 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "preview": {"desc": "Набор флагов, определяющий, необходимо ли вернуть вместе с информацией о темах текст первых и последних сообщений в них. Является суммой флагов: \n\n1 — вернуть первое сообщение в каждой теме (поле first_comment); \n2 — вернуть последнее сообщение в каждой теме (поле last_comment). По умолчанию — 0 (не возвращать текст сообщений). \nцелое число", "type": "int", "default": "None"}, "preview_length": {"desc": "Количество символов, по которому нужно обрезать первое и последнее сообщение. Укажите 0, если Вы не хотите обрезать сообщение. (по умолчанию — 90). положительное число, по умолчанию 90", "type": "int", "default": "90"}}
            def __call__(self, group_id, topic_ids : str = None, order : int = None, offset : int = None, count : int = None, extended : bool = None, preview : int = None, preview_length : int = None, v : str = None, access_token : str = None):
                self.exec_func("board.getTopics", group_id = group_id, topic_ids = topic_ids, order = order, offset = offset, count = count, extended = extended, preview = preview, preview_length = preview_length, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class openTopic:
            '''Открывает ранее закрытую тему (в ней станет возможно оставлять новые сообщения). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, v : str = None, access_token : str = None):
                self.exec_func("board.openTopic", group_id = group_id, topic_id = topic_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удаленное сообщение темы в обсуждениях группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, comment_id, v : str = None, access_token : str = None):
                self.exec_func("board.restoreComment", group_id = group_id, topic_id = topic_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unfixTopic:
            '''Отменяет прикрепление темы в списке обсуждений группы (тема будет выводиться согласно выбранной сортировке). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором размещено обсуждение. положительное число, обязательный параметр", "type": "int", "default": "None"}, "topic_id": {"desc": "идентификатор обсуждения. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, topic_id, v : str = None, access_token : str = None):
                self.exec_func("board.unfixTopic", group_id = group_id, topic_id = topic_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class database:
        def  __init__(self, exec_func):
            self.getChairs = self.getChairs(exec_func)
            self.getCities = self.getCities(exec_func)
            self.getCitiesById = self.getCitiesById(exec_func)
            self.getCountries = self.getCountries(exec_func)
            self.getCountriesById = self.getCountriesById(exec_func)
            self.getFaculties = self.getFaculties(exec_func)
            self.getMetroStations = self.getMetroStations(exec_func)
            self.getMetroStationsById = self.getMetroStationsById(exec_func)
            self.getRegions = self.getRegions(exec_func)
            self.getSchoolClasses = self.getSchoolClasses(exec_func)
            self.getSchools = self.getSchools(exec_func)
            self.getUniversities = self.getUniversities(exec_func)
        class getChairs:
            '''Возвращает список кафедр университета по указанному факультету. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"faculty_id": {"desc": "идентификатор факультета, кафедры которого необходимо получить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества кафедр. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество кафедр которое необходимо получить. положительное число, по умолчанию 100, максимальное значение 10000", "type": "int", "default": "100"}}
            def __call__(self, faculty_id, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getChairs", faculty_id = faculty_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCities:
            '''Возвращает список городов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"country_id": {"desc": "идентификатор страны, полученный  database.getCountries. положительное число, обязательный параметр", "type": "int", "default": "None"}, "region_id": {"desc": "идентификатор региона, города которого необходимо получить. положительное число", "type": "int", "default": "None"}, "q": {"desc": "строка поискового запроса. Например, Санкт. \nМаксимальная длина строки — 15 символов. строка", "type": "str", "default": "None"}, "need_all": {"desc": "\n\n1 – возвращать все города. \n0 – возвращать только основные города. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества городов. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество городов, которые необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}}
            def __call__(self, country_id, region_id : int = None, q : str = None, need_all : bool = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getCities", country_id = country_id, region_id = region_id, q = q, need_all = need_all, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCitiesById:
            '''Возвращает информацию о городах и регионах по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"city_ids": {"desc": "идентификаторы городов и регионов. список положительных чисел, разделенных запятыми, количество элементов должно составлять не более 1000", "type": "str", "default": "None"}}
            def __call__(self, city_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("database.getCitiesById", city_ids = city_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCountries:
            '''Возвращает список стран. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"need_all": {"desc": "1 — вернуть список всех стран. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "code": {"desc": "перечисленные через запятую двухбуквенные коды стран в стандарте ISO 3166-1 alpha-2, для которых необходимо выдать информацию.\nПример значения code:\nRU,UA,BY строка", "type": "str", "default": "None"}, "offset": {"desc": "отступ, необходимый для выбора определенного подмножества стран. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество стран, которое необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}}
            def __call__(self, need_all : bool = None, code : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getCountries", need_all = need_all, code = code, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCountriesById:
            '''Возвращает информацию о странах по их идентификаторам '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"country_ids": {"desc": "идентификаторы стран. список положительных чисел, разделенных запятыми, количество элементов должно составлять не более 1000", "type": "str", "default": "None"}}
            def __call__(self, country_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("database.getCountriesById", country_ids = country_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getFaculties:
            '''Возвращает список факультетов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"university_id": {"desc": "идентификатор университета, факультеты которого необходимо получить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества факультетов. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество факультетов которое необходимо получить. положительное число, по умолчанию 100, максимальное значение 10000", "type": "int", "default": "100"}}
            def __call__(self, university_id, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getFaculties", university_id = university_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMetroStations:
            '''Возвращает список станций метро '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"city_id": {"desc": "идентификатор города, полученный методом database.getCities. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "отступ, необходимый для выбора определенного подмножества станций. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество станций, которое необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 500", "type": "int", "default": "100"}, "extended": {"desc": "флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, city_id, offset : int = None, count : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("database.getMetroStations", city_id = city_id, offset = offset, count = count, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMetroStationsById:
            '''Возвращает информацию об одной или нескольких станциях метро по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"station_ids": {"desc": "список идентификаторов станций метро список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, station_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("database.getMetroStationsById", station_ids = station_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getRegions:
            '''Возвращает список регионов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"country_id": {"desc": "идентификатор страны, полученный в методе database.getCountries. положительное число, обязательный параметр", "type": "int", "default": "None"}, "q": {"desc": "строка поискового запроса. Например, Лен. строка", "type": "str", "default": "None"}, "offset": {"desc": "отступ, необходимый для выбора определенного подмножества регионов. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество регионов, которое необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}}
            def __call__(self, country_id, q : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getRegions", country_id = country_id, q = q, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSchoolClasses:
            '''Возвращает список классов, характерных для школ определенной страны. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"country_id": {"desc": "идентификатор страны, доступные классы в которой необходимо вернуть. положительное число", "type": "int", "default": "None"}}
            def __call__(self, country_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getSchoolClasses", country_id = country_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSchools:
            '''Возвращает список школ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса. Например, гимназия. строка", "type": "str", "default": "None"}, "city_id": {"desc": "идентификатор города, школы которого необходимо вернуть. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества школ. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество школ, которое необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 10000", "type": "int", "default": "100"}}
            def __call__(self, city_id, q : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getSchools", q = q, city_id = city_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUniversities:
            '''Возвращает список высших учебных заведений. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса. Например, СПБ. строка", "type": "str", "default": "None"}, "country_id": {"desc": "идентификатор страны, учебные заведения которой необходимо вернуть. положительное число", "type": "int", "default": "None"}, "city_id": {"desc": "идентификатор города, учебные заведения которого необходимо вернуть. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества учебных заведений. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество учебных заведений, которое необходимо вернуть. положительное число, по умолчанию 100, максимальное значение 10000", "type": "int", "default": "100"}}
            def __call__(self, q : str = None, country_id : int = None, city_id : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("database.getUniversities", q = q, country_id = country_id, city_id = city_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class docs:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.delete = self.delete(exec_func)
            self.edit = self.edit(exec_func)
            self.get = self.get(exec_func)
            self.getById = self.getById(exec_func)
            self.getMessagesUploadServer = self.getMessagesUploadServer(exec_func)
            self.getTypes = self.getTypes(exec_func)
            self.getUploadServer = self.getUploadServer(exec_func)
            self.getWallUploadServer = self.getWallUploadServer(exec_func)
            self.save = self.save(exec_func)
            self.search = self.search(exec_func)
        class add:
            '''Копирует документ в документы текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит документ. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "doc_id": {"desc": "идентификатор документа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "ключ доступа документа. Этот параметр следует передать, если вместе с остальными данными о документе было возвращено поле access_key. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, doc_id, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("docs.add", owner_id = owner_id, doc_id = doc_id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет документ пользователя или группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит документ. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "doc_id": {"desc": "идентификатор документа. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, doc_id, v : str = None, access_token : str = None):
                self.exec_func("docs.delete", owner_id = owner_id, doc_id = doc_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует документ пользователя или группы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит документ. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}, "doc_id": {"desc": "идентификатор документа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "название документа. строка, максимальная длина 128", "type": "str", "default": "None"}, "tags": {"desc": "метки для поиска. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id, doc_id, title : str = None, tags : str = None, v : str = None, access_token : str = None):
                self.exec_func("docs.edit", owner_id = owner_id, doc_id = doc_id, title = title, tags = tags, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает расширенную информацию о документах пользователя или сообщества.
'''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "количество документов, информацию о которых нужно вернуть. \nПо умолчанию: все документы. Максимальное количество документов, которое можно получить: 2000. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества документов. Максимальное значение: 1999. положительное число", "type": "int", "default": "None"}, "type": {"desc": "фильтр по типу документа. \nВозможные варианты: \n\n1 — текстовые документы; \n2 — архивы; \n3 — gif; \n4 — изображения; \n5 — аудио; \n6 — видео; \n7 — электронные книги; \n8 — неизвестно. \nположительное число, по умолчанию 0", "type": "int", "default": "0"}, "owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежат документы. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "return_tags": {"desc": "флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, count : int = None, offset : int = None, type : int = None, owner_id : int = None, return_tags : bool = None, v : str = None, access_token : str = None):
                self.exec_func("docs.get", count = count, offset = offset, type = type, owner_id = owner_id, return_tags = return_tags, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию о документах по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"docs": {"desc": "идентификаторы документов, информацию о которых нужно вернуть. Пример значения docs: \n66748_91488,66748_91455. \nМетод поддерживает передачу access_key. список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}, "return_tags": {"desc": "флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, docs, return_tags : bool = None, v : str = None, access_token : str = None):
                self.exec_func("docs.getById", docs = docs, return_tags = return_tags, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMessagesUploadServer:
            '''Получает адрес сервера для загрузки документа в личное сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип документа. Возможные значения: \n\ndoc — обычный документ; \naudio_message — голосовое сообщение; \ngraffiti — граффити. \nстрока, по умолчанию doc", "type": "str", "default": "doc"}, "peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число", "type": "int", "default": "None"}}
            def __call__(self, type : str = None, peer_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("docs.getMessagesUploadServer", type = type, peer_id = peer_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTypes:
            '''Возвращает доступные для пользователя типы документов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежат документы. целое число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, owner_id, v : str = None, access_token : str = None):
                self.exec_func("docs.getTypes", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUploadServer:
            '''Возвращает адрес сервера для загрузки документов.
'''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (если необходимо загрузить документ в список документов сообщества). Если документ нужно загрузить в список пользователя, метод вызывается без дополнительных параметров. положительное число", "type": "int", "default": "None"}}
            def __call__(self, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("docs.getUploadServer", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getWallUploadServer:
            '''Возвращает адрес сервера для загрузки документов в папку Отправленные, для последующей отправки документа на стену или личным сообщением. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в которое нужно загрузить документ. положительное число", "type": "int", "default": "None"}}
            def __call__(self, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("docs.getWallUploadServer", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class save:
            '''Сохраняет документ после его успешной  загрузки на сервер. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"file": {"desc": "параметр, возвращаемый в результате  загрузки файла на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "title": {"desc": "название документа. строка", "type": "str", "default": "None"}, "tags": {"desc": "метки для поиска. строка", "type": "str", "default": "None"}, "return_tags": {"desc": "флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, file, title : str = None, tags : str = None, return_tags : bool = None, v : str = None, access_token : str = None):
                self.exec_func("docs.save", file = file, title = title, tags = tags, return_tags = return_tags, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает результаты поиска по документам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса. Например, зеленые тапочки. строка, обязательный параметр, максимальная длина 512", "type": "str", "default": "None"}, "search_own": {"desc": "1 — искать среди собственных документов пользователя. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "count": {"desc": "количество документов, информацию о которых нужно вернуть. Обратите внимание — даже при использовании параметра offset для получения информации доступны только первые 1000 результатов. \n положительное число, по умолчанию 20", "type": "int", "default": "20"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества документов. положительное число", "type": "int", "default": "None"}, "return_tags": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, q, search_own : bool = None, count : int = None, offset : int = None, return_tags : bool = None, v : str = None, access_token : str = None):
                self.exec_func("docs.search", q = q, search_own = search_own, count = count, offset = offset, return_tags = return_tags, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class donut:
        def  __init__(self, exec_func):
            self.getFriends = self.getFriends(exec_func)
            self.getSubscription = self.getSubscription(exec_func)
            self.getSubscriptions = self.getSubscriptions(exec_func)
            self.isDon = self.isDon(exec_func)
        class getFriends:
            '''Возвращает список донов, которые подписаны на определенные сообщества, из числа друзей пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества друзей. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество друзей, информацию о которых необходимо вернуть. положительное число, по умолчанию 10, максимальное значение 100", "type": "int", "default": "10"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id, offset : int = None, count : int = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("donut.getFriends", owner_id = owner_id, offset = offset, count = count, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSubscription:
            '''Возвращает информацию о подписке VK Donut. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, v : str = None, access_token : str = None):
                self.exec_func("donut.getSubscription", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSubscriptions:
            '''Возвращает информацию о подписках пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"fields": {"desc": "список дополнительных полей профиля, которые необходимо вернуть. См. подробное описание. список слов, разделенных через запятую", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества подписок. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество подписок, информацию о которых необходимо вернуть. положительное число, по умолчанию 10, максимальное значение 100", "type": "int", "default": "10"}}
            def __call__(self, fields : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("donut.getSubscriptions", fields = fields, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class isDon:
            '''Возвращает информацию о том, подписан ли пользователь на платный контент (является доном). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, v : str = None, access_token : str = None):
                self.exec_func("donut.isDon", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class downloadedGames:
        def  __init__(self, exec_func):
            self.getPaidStatus = self.getPaidStatus(exec_func)
        class getPaidStatus:
            ''''''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "ID пользователя возможно купившего приложение положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("downloadedGames.getPaidStatus", user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class fave:
        def  __init__(self, exec_func):
            self.addArticle = self.addArticle(exec_func)
            self.addLink = self.addLink(exec_func)
            self.addPage = self.addPage(exec_func)
            self.addPost = self.addPost(exec_func)
            self.addProduct = self.addProduct(exec_func)
            self.addTag = self.addTag(exec_func)
            self.addVideo = self.addVideo(exec_func)
            self.editTag = self.editTag(exec_func)
            self.get = self.get(exec_func)
            self.getPages = self.getPages(exec_func)
            self.getTags = self.getTags(exec_func)
            self.markSeen = self.markSeen(exec_func)
            self.removeArticle = self.removeArticle(exec_func)
            self.removeLink = self.removeLink(exec_func)
            self.removePage = self.removePage(exec_func)
            self.removePost = self.removePost(exec_func)
            self.removeProduct = self.removeProduct(exec_func)
            self.removeTag = self.removeTag(exec_func)
            self.removeVideo = self.removeVideo(exec_func)
            self.reorderTags = self.reorderTags(exec_func)
            self.setPageTags = self.setPageTags(exec_func)
            self.setTags = self.setTags(exec_func)
            self.trackPageInteraction = self.trackPageInteraction(exec_func)
        class addArticle:
            '''Добавляет статью в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"url": {"desc": "ссылка на добавляемую статью. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, url, v : str = None, access_token : str = None):
                self.exec_func("fave.addArticle", url = url, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addLink:
            '''Добавляет ссылку в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"link": {"desc": "адрес добавляемой ссылки строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, link, v : str = None, access_token : str = None):
                self.exec_func("fave.addLink", link = link, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addPage:
            '''Добавляет сообщество или пользователя в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которого нужно добавить в закладки. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которое нужно добавить в закладки. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("fave.addPage", user_id = user_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addPost:
            '''Добавляет запись со стены пользователя или сообщества в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, чью запись со стены требуется добавить в закладки. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор записи, которую необходимо добавить в закладки. целое число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "специальный код доступа для приватных постов. строка", "type": "str", "default": "None"}, "ref": {"desc": "строка", "type": "str", "default": "None"}, "track_code": {"desc": "строка", "type": "str", "default": "None"}, "source": {"desc": "строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, id, access_key : str = None, ref : str = None, track_code : str = None, source : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.addPost", owner_id = owner_id, id = id, access_key = access_key, ref = ref, track_code = track_code, source = source, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addProduct:
            '''Добавляет товар в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, чей товар требуется добавить в закладки. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор товара. целое число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "специальный код доступа для приватных товаров. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, id, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.addProduct", owner_id = owner_id, id = id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addTag:
            '''Создает метку закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"name": {"desc": "название метки. строка, максимальная длина 50", "type": "str", "default": "None"}, "position": {"desc": "положение метки. \nВозможные значения: \n\nfront - начало списка, \nback - конец списка. \nстрока, по умолчанию back", "type": "str", "default": "back"}}
            def __call__(self, name : str = None, position : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.addTag", name = name, position = position, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addVideo:
            '''Добавляет видеозапись в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, владельца видеозаписи, которую требуется добавить в закладки. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор видеозаписи. целое число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "специальный код доступа для приватных видеозаписей. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, id, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.addVideo", owner_id = owner_id, id = id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editTag:
            '''Редактирует метку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"id": {"desc": "идентификатор метки. целое число, обязательный параметр", "type": "int", "default": "None"}, "name": {"desc": "новое название метки. строка, обязательный параметр, максимальная длина 50", "type": "str", "default": "None"}}
            def __call__(self, id, name, v : str = None, access_token : str = None):
                self.exec_func("fave.editTag", id = id, name = name, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает объекты, добавленные в закладки пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"extended": {"desc": "1, если необходимо получить информацию о пользователе. По умолчанию: 0. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "item_type": {"desc": "Типы объектов, которые необходимо вернуть. Возможные значения: \n\npost — записи; \nvideo — видеозаписи; \nproduct — товары; \narticle — статьи; \nlink — ссылки. \nстрока", "type": "str", "default": "None"}, "tag_id": {"desc": "идентификатор метки, закладки отмеченные которой требуется вернуть. целое число", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первого объекта в закладках пользователя для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых закладок. целое число, по умолчанию 50, минимальное значение 1, максимальное значение 100", "type": "int", "default": "50"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. строка", "type": "str", "default": "None"}, "is_from_snackbar": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, extended : bool = None, item_type : str = None, tag_id : int = None, offset : int = None, count : int = None, fields : str = None, is_from_snackbar : bool = None, v : str = None, access_token : str = None):
                self.exec_func("fave.get", extended = extended, item_type = item_type, tag_id = tag_id, offset = offset, count = count, fields = fields, is_from_snackbar = is_from_snackbar, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPages:
            '''Возвращает страницы пользователей и сообществ, добавленных в закладки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение относительно первого объекта в закладках пользователя для выборки определенного подмножества. положительное число, максимальное значение 10000", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых закладок. положительное число, по умолчанию 50, минимальное значение 1, максимальное значение 500", "type": "int", "default": "50"}, "type": {"desc": "Типы объектов, которые необходимо вернуть. Возможные значения: \n\nusers — вернуть только пользователей; \ngroups — вернуть только сообщества; \nhints — топ сообществ и пользователей. \n\nЕсли параметр не указан — вернутся объекты пользователей и сообществ, добавленных в закладки, в порядке добавления. строка", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей для объектов user и group, которые необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}, "tag_id": {"desc": "идентификатор метки, закладки отмеченные которой требуется вернуть. целое число", "type": "int", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, type : str = None, fields : str = None, tag_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("fave.getPages", offset = offset, count = count, type = type, fields = fields, tag_id = tag_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTags:
            '''Возвращает список меток в закладках. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("fave.getTags", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markSeen:
            '''Отмечает закладки как просмотренные. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("fave.markSeen", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeArticle:
            '''Удаляет статью из закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца статьи. целое число, обязательный параметр", "type": "int", "default": "None"}, "article_id": {"desc": "идентификатор статьи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "ref": {"desc": "строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, article_id, ref : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.removeArticle", owner_id = owner_id, article_id = article_id, ref = ref, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeLink:
            '''Удаляет ссылку из списка закладок пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"link_id": {"desc": "идентификатор ссылки. строка", "type": "str", "default": "None"}}
            def __call__(self, link_id : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.removeLink", link_id = link_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removePage:
            '''Удаляет из закладок сообщество или страницу пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которого следует удалить из закладок. целое число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которое следует удалить из закладок. целое число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("fave.removePage", user_id = user_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removePost:
            '''Удаляет из закладок запись на стене пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца записи. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор записи на стене. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, id, v : str = None, access_token : str = None):
                self.exec_func("fave.removePost", owner_id = owner_id, id = id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeProduct:
            '''Удаляет товар из закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, чей товар требуется удалить из закладок. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор товара. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, id, v : str = None, access_token : str = None):
                self.exec_func("fave.removeProduct", owner_id = owner_id, id = id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeTag:
            '''Удаляет метку закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"id": {"desc": "идентификатор метки. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, id, v : str = None, access_token : str = None):
                self.exec_func("fave.removeTag", id = id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeVideo:
            '''Удаляет видеозапись из списка закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, владельца видеозаписи, которую требуется удалить из закладок. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "id": {"desc": "идентификатор видеозаписи. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, id, v : str = None, access_token : str = None):
                self.exec_func("fave.removeVideo", owner_id = owner_id, id = id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderTags:
            '''Меняет порядок меток закладок в списке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"ids": {"desc": "перечисленные через запятую все идентификаторы меток пользователя в том порядке, в котором их требуется отображать. список целых чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, ids, v : str = None, access_token : str = None):
                self.exec_func("fave.reorderTags", ids = ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setPageTags:
            '''Устанавливает метку странице пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которому требуется проставить метку в закладках. Обязательный параметр, если не задан параметр group_id. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому требуется проставить метку в закладках. Обязательный параметр, если не задан параметр user_id. положительное число", "type": "int", "default": "None"}, "tag_ids": {"desc": "перечисленные через запятую идентификаторы тегов, которые требуется присвоить странице. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, tag_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.setPageTags", user_id = user_id, group_id = group_id, tag_ids = tag_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setTags:
            '''Устанавливает метку выбранному объекту в списке закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"item_type": {"desc": "Тип объекта, которому необходимо присвоить метку. Возможные значения: \n\npost — запись на стене; \nvideo — видеозапись; \nproduct — товар; \narticle — статья; \nlink — ссылка. \n\nДля работы с объектами пользователя или сообщества используйте метод fave.setPageTags строка", "type": "str", "default": "None"}, "item_owner_id": {"desc": "идентификатор владельца объекта, которому требуется присвоить метку. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор объекта. целое число", "type": "int", "default": "None"}, "tag_ids": {"desc": "идентификатор метки, которую требуется присвоить объекту. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "link_id": {"desc": "идентификатор ссылки, которой требуется присвоить метку. строка", "type": "str", "default": "None"}, "link_url": {"desc": "строка", "type": "str", "default": "None"}}
            def __call__(self, item_type : str = None, item_owner_id : int = None, item_id : int = None, tag_ids : str = None, link_id : str = None, link_url : str = None, v : str = None, access_token : str = None):
                self.exec_func("fave.setTags", item_type = item_type, item_owner_id = item_owner_id, item_id = item_id, tag_ids = tag_ids, link_id = link_id, link_url = link_url, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class trackPageInteraction:
            '''Устанавливает страницу пользователя или сообщества в топ закладок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которому требуется проставить метку в закладках. Обязательный параметр, если не задан параметр group_id. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому требуется проставить метку в закладках. Обязательный параметр, если не задан параметр user_id. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("fave.trackPageInteraction", user_id = user_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class friends:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.addList = self.addList(exec_func)
            self.areFriends = self.areFriends(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteAllRequests = self.deleteAllRequests(exec_func)
            self.deleteList = self.deleteList(exec_func)
            self.edit = self.edit(exec_func)
            self.editList = self.editList(exec_func)
            self.get = self.get(exec_func)
            self.getAppUsers = self.getAppUsers(exec_func)
            self.getByPhones = self.getByPhones(exec_func)
            self.getLists = self.getLists(exec_func)
            self.getMutual = self.getMutual(exec_func)
            self.getOnline = self.getOnline(exec_func)
            self.getRecent = self.getRecent(exec_func)
            self.getRequests = self.getRequests(exec_func)
            self.getSuggestions = self.getSuggestions(exec_func)
            self.search = self.search(exec_func)
        class add:
            '''Одобряет или создает заявку на добавление в друзья. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которому необходимо отправить заявку, либо заявку от которого необходимо одобрить. положительное число", "type": "int", "default": "None"}, "text": {"desc": "текст сопроводительного сообщения для заявки на добавление в друзья. Максимальная длина сообщения — 500 символов. строка", "type": "str", "default": "None"}, "follow": {"desc": "1, если необходимо отклонить входящую заявку (оставить пользователя в подписчиках). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, user_id : int = None, text : str = None, follow : bool = None, v : str = None, access_token : str = None):
                self.exec_func("friends.add", user_id = user_id, text = text, follow = follow, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addList:
            '''Создает новый список друзей у текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"name": {"desc": "название создаваемого списка друзей. строка, обязательный параметр", "type": "str", "default": "None"}, "user_ids": {"desc": "идентификаторы пользователей, которых необходимо поместить в созданный список. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, name, user_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.addList", name = name, user_ids = user_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class areFriends:
            '''Возвращает информацию о том, добавлен ли текущий пользователь в друзья у указанных пользователей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "идентификаторы пользователей, статус дружбы с которыми нужно проверить. список целых чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "need_sign": {"desc": "1 – необходимо вернуть поле sign которое равно: \nmd5(\"{id}_{user_id}_{friends_status}_{application_secret}\"), где id - это идентификатор пользователя, для которого выполняется запрос. \nи позволяет на сервере убедиться что данные не были подделаны на клиенте. \n0 – поле sign возвращать не нужно. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "extended": {"desc": "1  – необходимо вернуть is_request_unread, если есть непрочитанная заявка в друзья. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, user_ids, need_sign : bool = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("friends.areFriends", user_ids = user_ids, need_sign = need_sign, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет пользователя из списка друзей или отклоняет заявку в друзья. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которого необходимо удалить из списка друзей, либо заявку от которого необходимо отклонить. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("friends.delete", user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteAllRequests:
            '''Отмечает все входящие заявки на добавление в друзья как просмотренные. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("friends.deleteAllRequests", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteList:
            '''Удаляет существующий список друзей текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"list_id": {"desc": "идентификатор списка друзей, который необходимо удалить. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, list_id, v : str = None, access_token : str = None):
                self.exec_func("friends.deleteList", list_id = list_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует списки друзей для выбранного друга. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя (из числа друзей), для которого необходимо отредактировать списки друзей. положительное число, обязательный параметр", "type": "int", "default": "None"}, "list_ids": {"desc": "идентификаторы списков друзей, в которые нужно добавить пользователя. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, user_id, list_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.edit", user_id = user_id, list_ids = list_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editList:
            '''Редактирует существующий список друзей текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"name": {"desc": "название списка друзей. строка", "type": "str", "default": "None"}, "list_id": {"desc": "идентификатор списка друзей. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_ids": {"desc": "идентификаторы пользователей, включенных в список. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "add_user_ids": {"desc": "идентификаторы пользователей, которых необходимо добавить в список. (в случае если не передан user_ids) список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "delete_user_ids": {"desc": "идентификаторы пользователей, которых необходимо изъять из списка. (в случае если не передан user_ids) список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, list_id, name : str = None, user_ids : str = None, add_user_ids : str = None, delete_user_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.editList", name = name, list_id = list_id, user_ids = user_ids, add_user_ids = add_user_ids, delete_user_ids = delete_user_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список идентификаторов друзей пользователя или расширенную информацию о друзьях пользователя (при использовании параметра fields). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, для которого необходимо получить список друзей. Если параметр не задан, то считается, что он равен идентификатору текущего пользователя (справедливо для вызова с передачей access_token). целое число", "type": "int", "default": "None"}, "order": {"desc": "порядок, в котором нужно вернуть список друзей. Допустимые значения: \n\nhints — сортировать по рейтингу, аналогично тому, как друзья сортируются в разделе Мои друзья (Это значение доступно только для Standalone-приложений с ключом доступа, полученным по схеме Implicit Flow.). \nrandom — возвращает друзей в случайном порядке. \nmobile — возвращает выше тех друзей, у которых установлены мобильные приложения. \nname — сортировать по имени. Данный тип сортировки работает медленно, так как сервер будет получать всех друзей а не только указанное количество count. (работает только при переданном параметре fields). \n\nПо умолчанию список сортируется в порядке возрастания идентификаторов пользователей. строка", "type": "str", "default": "None"}, "list_id": {"desc": "идентификатор списка друзей, полученный методом friends.getLists, друзей из которого необходимо получить. Данный параметр учитывается, только когда параметр user_id равен идентификатору текущего пользователя.\n\nЭтот параметр доступен только для Standalone-приложений с ключом доступа, полученным по схеме Implicit Flow. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество друзей, которое нужно вернуть. положительное число, по умолчанию 5000", "type": "int", "default": "5000"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества друзей. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}, "ref": {"desc": "строка, максимальная длина 255", "type": "str", "default": "None"}}
            def __call__(self, user_id : int = None, order : str = None, list_id : int = None, count : int = None, offset : int = None, fields : str = None, name_case : str = None, ref : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.get", user_id = user_id, order = order, list_id = list_id, count = count, offset = offset, fields = fields, name_case = name_case, ref = ref, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAppUsers:
            '''Возвращает список идентификаторов друзей текущего пользователя, которые установили данное приложение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("friends.getAppUsers", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getByPhones:
            '''Возвращает список друзей пользователя, у которых завалидированные или указанные в профиле телефонные номера входят в заданный список. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"phones": {"desc": "список телефонных номеров в формате MSISDN, разделеннных запятыми. Например\n+79219876543,+79111234567\nМаксимальное количество номеров в списке — 1000. список слов, разделенных через запятую", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, phones : str = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getByPhones", phones = phones, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLists:
            '''Возвращает список меток друзей пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "return_system": {"desc": "возвращать ли системный список публичных меток друзей пользователя. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, user_id : int = None, return_system : bool = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getLists", user_id = user_id, return_system = return_system, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMutual:
            '''Возвращает список идентификаторов общих друзей между парой пользователей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"source_uid": {"desc": "идентификатор пользователя, чьи друзья пересекаются с друзьями пользователя с идентификатором target_uid. Если параметр не задан, то считается, что source_uid равен идентификатору текущего пользователя. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "target_uid": {"desc": "идентификатор пользователя, с которым необходимо искать общих друзей. положительное число", "type": "int", "default": "None"}, "target_uids": {"desc": "список идентификаторов пользователей, с которыми необходимо искать общих друзей. список положительных чисел, разделенных запятыми, количество элементов должно составлять не более 100", "type": "str", "default": "None"}, "order": {"desc": "порядок, в котором нужно вернуть список общих друзей. Допустимые значения: random - возвращает друзей в случайном порядке. По умолчанию — в порядке возрастания идентификаторов. строка", "type": "str", "default": "None"}, "count": {"desc": "количество общих друзей, которое нужно вернуть. (по умолчанию – все общие друзья) положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества общих друзей. положительное число", "type": "int", "default": "None"}}
            def __call__(self, source_uid : int = None, target_uid : int = None, target_uids : str = None, order : str = None, count : int = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getMutual", source_uid = source_uid, target_uid = target_uid, target_uids = target_uids, order = order, count = count, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOnline:
            '''Возвращает список идентификаторов друзей пользователя, находящихся на сайте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, для которого необходимо получить список друзей онлайн. Если параметр не задан, то считается, что он равен идентификатору текущего пользователя. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "list_id": {"desc": "идентификатор списка друзей. Если параметр не задан, возвращается информация обо всех друзьях, находящихся на сайте. положительное число", "type": "int", "default": "None"}, "online_mobile": {"desc": "1 — будет возвращено дополнительное поле online_mobile. \nПо умолчанию — 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "order": {"desc": "порядок, в котором нужно вернуть список друзей, находящихся на сайте. Допустимые значения: random - возвращает друзей в случайном порядке, hints - сортировать по рейтингу, аналогично тому, как друзья сортируются в разделе Мои друзья (данный параметр доступен только для Desktop-приложений). \nПо умолчанию список сортируется в порядке возрастания идентификаторов пользователей. строка", "type": "str", "default": "None"}, "count": {"desc": "количество друзей онлайн, которое нужно вернуть. (по умолчанию – все друзья онлайн) положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества друзей онлайн. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, list_id : int = None, online_mobile : bool = None, order : str = None, count : int = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getOnline", user_id = user_id, list_id = list_id, online_mobile = online_mobile, order = order, count = count, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getRecent:
            '''Возвращает список идентификаторов недавно добавленных друзей текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "максимальное количество недавно добавленных друзей, которое необходимо получить. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}}
            def __call__(self, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getRecent", count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getRequests:
            '''Возвращает информацию о полученных или отправленных заявках на добавление в друзья для текущего пользователя.
'''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определенного подмножества заявок на добавление в друзья. положительное число", "type": "int", "default": "None"}, "count": {"desc": "максимальное количество заявок на добавление в друзья, которые необходимо получить (не более 1000). \nПо умолчанию — 100. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}, "extended": {"desc": "определяет, требуется ли возвращать в ответе сообщения от пользователей, подавших заявку на добавление в друзья. И отправителя рекомендации при suggested = 1. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "need_mutual": {"desc": "определяет, требуется ли возвращать в ответе список общих друзей, если они есть. Обратите внимание, что при использовании need_mutual будет возвращено не более 2 заявок. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "out": {"desc": "0 — возвращать полученные заявки в друзья (по умолчанию), 1 — возвращать отправленные пользователем заявки. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "sort": {"desc": "0 — сортировать по дате добавления, 1 — сортировать по количеству общих друзей. (Если out = 1, этот параметр не учитывается). положительное число", "type": "int", "default": "None"}, "need_viewed": {"desc": "0 - не возвращать просмотренные заявки, 1 — возвращать просмотренные заявки. (Если out = 1, данный параметр не учитывается). флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "suggested": {"desc": "1 — возвращать рекомендованных другими пользователями друзей, 0 — возвращать заявки в друзья (по умолчанию). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "ref": {"desc": "строка, максимальная длина 255", "type": "str", "default": "None"}, "fields": {"desc": "список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, extended : bool = None, need_mutual : bool = None, out : bool = None, sort : int = None, need_viewed : bool = None, suggested : bool = None, ref : str = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getRequests", offset = offset, count = count, extended = extended, need_mutual = need_mutual, out = out, sort = sort, need_viewed = need_viewed, suggested = suggested, ref = ref, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSuggestions:
            '''Возвращает список профилей пользователей, которые могут быть друзьями текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"filter": {"desc": "типы предлагаемых друзей, которые нужно вернуть, перечисленные через запятую. \nМожет принимать следующие значения: \nmutual — пользователи, с которыми много общих друзей; По умолчанию будут возвращены все возможные друзья. список слов, разделенных через запятую", "type": "str", "default": "None"}, "count": {"desc": "количество рекомендаций, которое необходимо вернуть. положительное число, максимальное значение 500, по умолчанию 500", "type": "int", "default": "500"}, "offset": {"desc": "смещение, необходимое для выбора определённого подмножества списка. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, filter : str = None, count : int = None, offset : int = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("friends.getSuggestions", filter = filter, count = count, offset = offset, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Позволяет искать по списку друзей пользователей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, по списку друзей которого необходимо произвести поиск. положительное число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}, "q": {"desc": "строка запроса. строка", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities, domain список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка, по умолчанию Nom", "type": "str", "default": "Nom"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества друзей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество друзей, которое нужно вернуть. положительное число, по умолчанию 20, максимальное значение 1000", "type": "int", "default": "20"}}
            def __call__(self, user_id, q : str = None, fields : str = None, name_case : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("friends.search", user_id = user_id, q = q, fields = fields, name_case = name_case, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class gifts:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
        class get:
            '''Возвращает список полученных подарков пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, для которого необходимо получить список подарков. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "count": {"desc": "количество подарков, которое нужно вернуть. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества подарков. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, count : int = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("gifts.get", user_id = user_id, count = count, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class groups:
        def  __init__(self, exec_func):
            self.addAddress = self.addAddress(exec_func)
            self.addCallbackServer = self.addCallbackServer(exec_func)
            self.addLink = self.addLink(exec_func)
            self.approveRequest = self.approveRequest(exec_func)
            self.ban = self.ban(exec_func)
            self.create = self.create(exec_func)
            self.deleteAddress = self.deleteAddress(exec_func)
            self.deleteCallbackServer = self.deleteCallbackServer(exec_func)
            self.deleteLink = self.deleteLink(exec_func)
            self.disableOnline = self.disableOnline(exec_func)
            self.edit = self.edit(exec_func)
            self.editAddress = self.editAddress(exec_func)
            self.editCallbackServer = self.editCallbackServer(exec_func)
            self.editLink = self.editLink(exec_func)
            self.editManager = self.editManager(exec_func)
            self.enableOnline = self.enableOnline(exec_func)
            self.get = self.get(exec_func)
            self.getAddresses = self.getAddresses(exec_func)
            self.getBanned = self.getBanned(exec_func)
            self.getById = self.getById(exec_func)
            self.getCallbackConfirmationCode = self.getCallbackConfirmationCode(exec_func)
            self.getCallbackServers = self.getCallbackServers(exec_func)
            self.getCallbackSettings = self.getCallbackSettings(exec_func)
            self.getCatalog = self.getCatalog(exec_func)
            self.getCatalogInfo = self.getCatalogInfo(exec_func)
            self.getInvitedUsers = self.getInvitedUsers(exec_func)
            self.getInvites = self.getInvites(exec_func)
            self.getLongPollServer = self.getLongPollServer(exec_func)
            self.getLongPollSettings = self.getLongPollSettings(exec_func)
            self.getMembers = self.getMembers(exec_func)
            self.getOnlineStatus = self.getOnlineStatus(exec_func)
            self.getRequests = self.getRequests(exec_func)
            self.getSettings = self.getSettings(exec_func)
            self.getTagList = self.getTagList(exec_func)
            self.getTokenPermissions = self.getTokenPermissions(exec_func)
            self.invite = self.invite(exec_func)
            self.isMember = self.isMember(exec_func)
            self.join = self.join(exec_func)
            self.leave = self.leave(exec_func)
            self.removeUser = self.removeUser(exec_func)
            self.reorderLink = self.reorderLink(exec_func)
            self.search = self.search(exec_func)
            self.setCallbackSettings = self.setCallbackSettings(exec_func)
            self.setLongPollSettings = self.setLongPollSettings(exec_func)
            self.setSettings = self.setSettings(exec_func)
            self.setUserNote = self.setUserNote(exec_func)
            self.tagAdd = self.tagAdd(exec_func)
            self.tagBind = self.tagBind(exec_func)
            self.tagDelete = self.tagDelete(exec_func)
            self.tagUpdate = self.tagUpdate(exec_func)
            self.toggleMarket = self.toggleMarket(exec_func)
            self.unban = self.unban(exec_func)
        class addAddress:
            '''Позволяет добавить адрес в сообщество.
Список адресов может быть получен методом groups.getAddresses.
Для того, чтобы воспользоваться этим методом, Вы должны быть администратором сообщества '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в которое добавляется адрес. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "заголовок адреса строка, обязательный параметр, максимальная длина 255", "type": "str", "default": "None"}, "address": {"desc": "строка адреса Невский проспект, дом 28 строка, обязательный параметр, максимальная длина 255", "type": "str", "default": "None"}, "additional_address": {"desc": "дополнительное описание адреса. Второй этаж, налево строка, максимальная длина 400", "type": "str", "default": "None"}, "country_id": {"desc": "идентификатор  страны. Для получения можно использовать database.getCountries положительное число, обязательный параметр, минимальное значение 1", "type": "int", "default": "None"}, "city_id": {"desc": "идентификатор города. Для получения можно использовать database.getCities положительное число, обязательный параметр, минимальное значение 1", "type": "int", "default": "None"}, "metro_id": {"desc": "идентификатор станции метро.  Для получения можно использовать database.getMetroStations положительное число, минимальное значение 0", "type": "int", "default": "None"}, "latitude": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число, обязательный параметр, минимальное значение -90, максимальное значение 90", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число, обязательный параметр, минимальное значение -180, максимальное значение 180", "type": "int", "default": "None"}, "phone": {"desc": "номер телефона строка", "type": "str", "default": "None"}, "work_info_status": {"desc": "тип расписания. Возможные значения: \n\nno_information — нет информации о расписании; \ntemporarily_closed — временно закрыто; \nalways_opened — открыто круглосуточно; \nforever_closed —  закрыто навсегда; \ntimetable —  открыто в указанные часы работы. Для этого типа расписания необходимо передать параметр timetable; \nстрока, по умолчанию no_information", "type": "str", "default": "no_information"}, "timetable": {"desc": "для типа timetable можно передать расписание в формате json. Время передается в минутах от 0 часов. Ключ по дню означает, что день рабочий. open_time, close_time - начало и конец рабочего дня. break_open_time, break_close_time —  время перерыва. { \n  \"mon\": { \n    \"open_time\": 1080, \n    \"close_time\": 1380 \n  }, \n  \"tue\": { \n    \"open_time\": 1080, \n    \"close_time\": 1380 \n  }, \n  \"wed\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"thu\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"fri\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"sat\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320, \n    \"break_open_time\": 1200, \n    \"break_close_time\": 1230 \n  } \n} \n данные в формате JSON", "type": "not defined", "default": "None"}, "is_main_address": {"desc": "установить адрес основным. Информация об основном адресе сразу показывается в сообществе. Для получения информации об остальных адресах нужно перейти к списку адресов. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, title, address, country_id, city_id, latitude, longitude, additional_address : str = None, metro_id : int = None, phone : str = None, work_info_status : str = None, timetable = None, is_main_address : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.addAddress", group_id = group_id, title = title, address = address, additional_address = additional_address, country_id = country_id, city_id = city_id, metro_id = metro_id, latitude = latitude, longitude = longitude, phone = phone, work_info_status = work_info_status, timetable = timetable, is_main_address = is_main_address, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addCallbackServer:
            '''Добавляет сервер для Callback API в сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "url": {"desc": "URL сервера. строка, обязательный параметр", "type": "str", "default": "None"}, "title": {"desc": "название сервера. строка, обязательный параметр, максимальная длина 14", "type": "str", "default": "None"}, "secret_key": {"desc": "секретный ключ. строка, максимальная длина 50", "type": "str", "default": "None"}}
            def __call__(self, group_id, url, title, secret_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.addCallbackServer", group_id = group_id, url = url, title = title, secret_key = secret_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addLink:
            '''Позволяет добавлять ссылки в сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в которое добавляется ссылка. положительное число, обязательный параметр", "type": "int", "default": "None"}, "link": {"desc": "адрес ссылки. строка, обязательный параметр", "type": "str", "default": "None"}, "text": {"desc": "текст ссылки. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, link, text : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.addLink", group_id = group_id, link = link, text = text, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class approveRequest:
            '''Позволяет одобрить заявку в группу от пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, заявку в которую необходимо одобрить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, заявку которого необходимо одобрить. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, user_id, v : str = None, access_token : str = None):
                self.exec_func("groups.approveRequest", group_id = group_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class ban:
            '''Добавляет пользователя или группу в черный список сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор пользователя или сообщества, которое будет добавлено в черный список. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}, "end_date": {"desc": "дата завершения срока действия бана в формате unixtime. Максимальный возможный срок окончания бана, который можно указать, — один год с его начала. Если параметр не указан, пользователь будет заблокирован навсегда. положительное число", "type": "int", "default": "None"}, "reason": {"desc": "причина бана: \n\n0 — другое (по умолчанию); \n1 — спам; \n2 — оскорбление участников; \n3 — нецензурные выражения; \n4 — сообщения не по теме. \nположительное число", "type": "int", "default": "None"}, "comment": {"desc": "текст комментария к бану. строка", "type": "str", "default": "None"}, "comment_visible": {"desc": "1 – текст комментария будет отображаться пользователю. \n0 – текст комментария не доступен пользователю. (по умолчанию) флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, owner_id : int = None, end_date : int = None, reason : int = None, comment : str = None, comment_visible : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.ban", group_id = group_id, owner_id = owner_id, end_date = end_date, reason = reason, comment = comment, comment_visible = comment_visible, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class create:
            '''Создает новое сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"title": {"desc": "название сообщества. строка, обязательный параметр", "type": "str", "default": "None"}, "description": {"desc": "описание сообщества, (не учитывается при type=public). строка", "type": "str", "default": "None"}, "type": {"desc": "тип создаваемого сообщества: \n\ngroup — группа; \nevent — мероприятие; \npublic — публичная страница. \nстрока, по умолчанию group", "type": "str", "default": "group"}, "public_category": {"desc": "категория публичной страницы (только для type = public). положительное число", "type": "int", "default": "None"}, "subtype": {"desc": "вид публичной страницы (только при type=public): \n\n1 — место или небольшая компания; \n2 — компания, организация или веб-сайт; \n3 — известная личность или коллектив; \n4 — произведение или продукция. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, title, description : str = None, type : str = None, public_category : int = None, subtype : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.create", title = title, description = description, type = type, public_category = public_category, subtype = subtype, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteAddress:
            '''Удаляет адрес сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Id группы положительное число, обязательный параметр", "type": "int", "default": "None"}, "address_id": {"desc": "Id адреса положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, address_id, v : str = None, access_token : str = None):
                self.exec_func("groups.deleteAddress", group_id = group_id, address_id = address_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteCallbackServer:
            '''Удаляет сервер для Callback API из сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "server_id": {"desc": "идентификатор сервера, который нужно удалить. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, server_id, v : str = None, access_token : str = None):
                self.exec_func("groups.deleteCallbackServer", group_id = group_id, server_id = server_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteLink:
            '''Позволяет удалить ссылки из сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, ссылки которого нужно удалить положительное число, обязательный параметр", "type": "int", "default": "None"}, "link_id": {"desc": "идентификатор ссылки, которую необходимо удалить положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, link_id, v : str = None, access_token : str = None):
                self.exec_func("groups.deleteLink", group_id = group_id, link_id = link_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class disableOnline:
            '''Выключает статус «онлайн» в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.disableOnline", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "название сообщества. строка", "type": "str", "default": "None"}, "description": {"desc": "описание сообщества. строка", "type": "str", "default": "None"}, "screen_name": {"desc": "короткое имя сообщества. строка", "type": "str", "default": "None"}, "access": {"desc": "тип группы. Возможные значения: \n\n0 — открытая; \n1 — закрытая; \n2 — частная. \nположительное число", "type": "int", "default": "None"}, "website": {"desc": "адрес сайта, который будет указан в информации о группе. строка", "type": "str", "default": "None"}, "subject": {"desc": "тематика сообщества. Возможные значения: \n\n1 — авто/мото; \n2 — активный отдых; \n3 — бизнес; \n4 — домашние животные; \n5 — здоровье; \n6 — знакомство и общение; \n7 — игры; \n8 — ИТ (компьютеры и софт); \n9 — кино; \n10 — красота и мода; \n11 — кулинария; \n12 — культура и искусство; \n13 — литература; \n14 — мобильная связь и интернет; \n15 — музыка; \n16 — наука и техника; \n17 — недвижимость; \n18 — новости и СМИ; \n19 — безопасность; \n20 — образование; \n21 — обустройство и ремонт; \n22 — политика; \n23 — продукты питания; \n24 — промышленность; \n25 — путешествия; \n26 — работа; \n27 — развлечения; \n28 — религия; \n29 — дом и семья; \n30 — спорт; \n31 — страхование; \n32 — телевидение; \n33 — товары и услуги; \n34 — увлечения и хобби; \n35 — финансы; \n36 — фото; \n37 — эзотерика; \n38 — электроника и бытовая техника; \n39 — эротика; \n40 — юмор; \n41 — общество, гуманитарные науки; \n42 — дизайн и графика. \nстрока", "type": "str", "default": "None"}, "email": {"desc": "электронный адрес организатора (для мероприятий). строка", "type": "str", "default": "None"}, "phone": {"desc": "номер телефона организатора (для мероприятий). строка", "type": "str", "default": "None"}, "rss": {"desc": "адрес rss для импорта новостей (доступен только группам, получившим соответствующее разрешение, обратитесь в http://vk.com/support для получения разрешения). строка", "type": "str", "default": "None"}, "event_start_date": {"desc": "дата начала события. положительное число", "type": "int", "default": "None"}, "event_finish_date": {"desc": "дата окончания события. положительное число", "type": "int", "default": "None"}, "event_group_id": {"desc": "идентификатор группы, которая является организатором события (только для событий). положительное число", "type": "int", "default": "None"}, "public_category": {"desc": "категория публичной страницы. положительное число", "type": "int", "default": "None"}, "public_subcategory": {"desc": "подкатегория публичной станицы. Список подкатегорий можно получить методом groups.getSettings. положительное число", "type": "int", "default": "None"}, "public_date": {"desc": "дата основания компании, организации, которой посвящена публичная страница в виде строки формата \"dd.mm.YYYY\". строка", "type": "str", "default": "None"}, "wall": {"desc": "стена. Возможные значения: \n\n0 — выключена; \n1 — открытая; \n2 — ограниченная (доступно только для групп и событий); \n3 — закрытая (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "topics": {"desc": "обсуждения. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "photos": {"desc": "фотографии. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "video": {"desc": "видеозаписи. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "audio": {"desc": "аудиозаписи. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "links": {"desc": "ссылки (доступно только для публичных страниц). \nВозможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "events": {"desc": "события (доступно только для публичных страниц). \nВозможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "places": {"desc": "места (доступно только для публичных страниц). Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "contacts": {"desc": "контакты (доступно только для публичных страниц). Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "docs": {"desc": "документы сообщества. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "wiki": {"desc": "wiki-материалы сообщества. Возможные значения: \n\n0 — выключены; \n1 — открытые; \n2 — ограниченные (доступно только для групп и событий). \nположительное число", "type": "int", "default": "None"}, "messages": {"desc": "сообщения сообщества. Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "articles": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "addresses": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "age_limits": {"desc": "возрастное ограничение для сообщества. Возможные значения: \n\n1 — нет ограничений; \n2 — 16+; \n3 — 18+. \nположительное число, по умолчанию 1", "type": "int", "default": "1"}, "market": {"desc": "товары. Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comments": {"desc": "комментарии к товарам. Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_country": {"desc": "регионы доставки товаров. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "market_city": {"desc": "города доставки товаров (в случае если указана одна страна). список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "market_currency": {"desc": "идентификатор валюты магазина. Возможные значения: \n\n643 — российский рубль; \n980 — украинская гривна; \n398 — казахстанский тенге; \n978 — евро; \n840 — доллар США. \nположительное число", "type": "int", "default": "None"}, "market_contact": {"desc": "контакт для связи для продавцом. \nДля использования сообщений сообщества следует включить их и передать значение 0. положительное число", "type": "int", "default": "None"}, "market_wiki": {"desc": "идентификатор wiki-страницы с описанием магазина. положительное число", "type": "int", "default": "None"}, "obscene_filter": {"desc": "фильтр нецензурных выражений в комментариях. Возможные значения: \n\n0 — выключен; \n1 — включен. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "obscene_stopwords": {"desc": "фильтр по ключевым словам в комментариях. Возможные значения: \n\n0 — выключен; \n1 — включен. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "obscene_words": {"desc": "ключевые слова для фильтра комментариев. список слов, разделенных через запятую", "type": "str", "default": "None"}, "main_section": {"desc": "положительное число", "type": "int", "default": "None"}, "secondary_section": {"desc": "положительное число", "type": "int", "default": "None"}, "country": {"desc": "положительное число", "type": "int", "default": "None"}, "city": {"desc": "положительное число", "type": "int", "default": "None"}}
            def __call__(self, group_id, title : str = None, description : str = None, screen_name : str = None, access : int = None, website : str = None, subject : str = None, email : str = None, phone : str = None, rss : str = None, event_start_date : int = None, event_finish_date : int = None, event_group_id : int = None, public_category : int = None, public_subcategory : int = None, public_date : str = None, wall : int = None, topics : int = None, photos : int = None, video : int = None, audio : int = None, links : bool = None, events : bool = None, places : bool = None, contacts : bool = None, docs : int = None, wiki : int = None, messages : bool = None, articles : bool = None, addresses : bool = None, age_limits : int = None, market : bool = None, market_comments : bool = None, market_country : str = None, market_city : str = None, market_currency : int = None, market_contact : int = None, market_wiki : int = None, obscene_filter : bool = None, obscene_stopwords : bool = None, obscene_words : str = None, main_section : int = None, secondary_section : int = None, country : int = None, city : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.edit", group_id = group_id, title = title, description = description, screen_name = screen_name, access = access, website = website, subject = subject, email = email, phone = phone, rss = rss, event_start_date = event_start_date, event_finish_date = event_finish_date, event_group_id = event_group_id, public_category = public_category, public_subcategory = public_subcategory, public_date = public_date, wall = wall, topics = topics, photos = photos, video = video, audio = audio, links = links, events = events, places = places, contacts = contacts, docs = docs, wiki = wiki, messages = messages, articles = articles, addresses = addresses, age_limits = age_limits, market = market, market_comments = market_comments, market_country = market_country, market_city = market_city, market_currency = market_currency, market_contact = market_contact, market_wiki = market_wiki, obscene_filter = obscene_filter, obscene_stopwords = obscene_stopwords, obscene_words = obscene_words, main_section = main_section, secondary_section = secondary_section, country = country, city = city, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editAddress:
            '''Позволяет отредактировать адрес в сообществе.
Список адресов может быть получен методом groups.getAddresses.
Для того, чтобы воспользоваться этим методом, Вы должны быть администратором сообщества '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в которое добавляется адрес. положительное число, обязательный параметр", "type": "int", "default": "None"}, "address_id": {"desc": "идентификатор адреса положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "заголовок адреса строка, максимальная длина 255", "type": "str", "default": "None"}, "address": {"desc": "строка адреса Невский проспект, дом 28 строка, максимальная длина 255", "type": "str", "default": "None"}, "additional_address": {"desc": "дополнительное описание адреса. Второй этаж, налево строка, максимальная длина 400", "type": "str", "default": "None"}, "country_id": {"desc": "идентификатор  страны. Для получения можно использовать database.getCountries положительное число, минимальное значение 0", "type": "int", "default": "None"}, "city_id": {"desc": "идентификатор города. Для получения можно использовать database.getCities положительное число, минимальное значение 0", "type": "int", "default": "None"}, "metro_id": {"desc": "идентификатор станции метро.  Для получения можно использовать database.getMetroStations положительное число, минимальное значение 0", "type": "int", "default": "None"}, "latitude": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число, минимальное значение -90, максимальное значение 90", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число, минимальное значение -180, максимальное значение 180", "type": "int", "default": "None"}, "phone": {"desc": "номер телефона строка", "type": "str", "default": "None"}, "work_info_status": {"desc": "тип расписания. Возможные значения: \n\nno_information — нет информации о расписании; \ntemporarily_closed — временно закрыто; \nalways_opened — открыто круглосуточно; \nforever_closed —  закрыто навсегда; \ntimetable —  открыто в указанные часы работы. Для этого типа расписания необходимо передать параметр timetable; \nстрока", "type": "str", "default": "None"}, "timetable": {"desc": "для типа timetable можно передать расписание в формате json. Время передается в минутах от 0 часов. Ключ по дню означает, что день рабочий. open_time, close_time —  начало и конец рабочего дня. break_open_time, break_close_time - время перерыва { \n  \"mon\": { \n    \"open_time\": 1080, \n    \"close_time\": 1380 \n  }, \n  \"tue\": { \n    \"open_time\": 1080, \n    \"close_time\": 1380 \n  }, \n  \"wed\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"thu\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"fri\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320 \n  }, \n  \"sat\": { \n    \"open_time\": 1080, \n    \"close_time\": 1320, \n    \"break_open_time\": 1200, \n    \"break_close_time\": 1230 \n  } \n} \n данные в формате JSON", "type": "not defined", "default": "None"}, "is_main_address": {"desc": "установить адрес основным. Информация об основном адресе сразу показывается в сообществе. Для получения информации об остальных адресах нужно перейти к списку адресов. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, address_id, title : str = None, address : str = None, additional_address : str = None, country_id : int = None, city_id : int = None, metro_id : int = None, latitude : int = None, longitude : int = None, phone : str = None, work_info_status : str = None, timetable = None, is_main_address : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.editAddress", group_id = group_id, address_id = address_id, title = title, address = address, additional_address = additional_address, country_id = country_id, city_id = city_id, metro_id = metro_id, latitude = latitude, longitude = longitude, phone = phone, work_info_status = work_info_status, timetable = timetable, is_main_address = is_main_address, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editCallbackServer:
            '''Редактирует данные сервера для Callback API в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "server_id": {"desc": "идентификатор сервера, данные которого нужно отредактировать. положительное число, обязательный параметр", "type": "int", "default": "None"}, "url": {"desc": "новый URL сервера. строка, обязательный параметр", "type": "str", "default": "None"}, "title": {"desc": "новое название сервера. строка, обязательный параметр, максимальная длина 14", "type": "str", "default": "None"}, "secret_key": {"desc": "новый секретный ключ сервера. строка, максимальная длина 50", "type": "str", "default": "None"}}
            def __call__(self, group_id, server_id, url, title, secret_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.editCallbackServer", group_id = group_id, server_id = server_id, url = url, title = title, secret_key = secret_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editLink:
            '''Позволяет редактировать ссылки в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в которое добавляется ссылка. положительное число, обязательный параметр", "type": "int", "default": "None"}, "link_id": {"desc": "идентификатор ссылки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "text": {"desc": "новый текст описания для ссылки. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, link_id, text : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.editLink", group_id = group_id, link_id = link_id, text = text, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editManager:
            '''Позволяет назначить/разжаловать руководителя в сообществе или изменить уровень его полномочий. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (указывается без знака «минус»). положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, чьи полномочия в сообществе нужно изменить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "role": {"desc": "уровень полномочий: \n\nmoderator — модератор; \neditor — редактор; \nadministrator — администратор. \nadvertiser — рекламодатель \n\nЕсли параметр не задан, с пользователя user_id снимаются полномочия руководителя. строка", "type": "str", "default": "None"}, "is_contact": {"desc": "отображать ли пользователя в блоке контактов сообщества. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "contact_position": {"desc": "должность пользователя, отображаемая в блоке контактов. строка", "type": "str", "default": "None"}, "contact_phone": {"desc": "телефон пользователя, отображаемый в блоке контактов. строка", "type": "str", "default": "None"}, "contact_email": {"desc": "email пользователя, отображаемый в блоке контактов. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, user_id, role : str = None, is_contact : bool = None, contact_position : str = None, contact_phone : str = None, contact_email : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.editManager", group_id = group_id, user_id = user_id, role = role, is_contact = is_contact, contact_position = contact_position, contact_phone = contact_phone, contact_email = contact_email, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class enableOnline:
            '''Включает статус «онлайн» в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.enableOnline", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список сообществ указанного пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, информацию о сообществах которого требуется получить. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "extended": {"desc": "если указать в качестве этого параметра 1, то будет возвращена полная информация о группах пользователя. По умолчанию 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "filter": {"desc": "список фильтров сообществ, которые необходимо вернуть, перечисленные через запятую. Доступны значения admin, editor, moder, advertiser, groups, publics, events, hasAddress. По умолчанию возвращаются все сообщества пользователя. \nПри указании фильтра hasAddress вернутся сообщества, в которых указаны адреса в соответствующем блоке, admin будут возвращены сообщества, в которых пользователь является администратором, editor — администратором или редактором, moder — администратором, редактором или модератором, advertiser — рекламодателем. Если передано несколько фильтров, то их результат объединяется. список слов, разделенных через запятую", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. Возможные значения: city, country, place, description, wiki_page, members_count, counters, start_date, finish_date, can_post, can_see_all_posts, activity, status, contacts, links, fixed_post, verified, site, can_create_topic. Подробнее см. описание полей объекта group. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определённого подмножества сообществ. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество сообществ, информацию о которых нужно вернуть. положительное число, максимальное значение 1000", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, extended : bool = None, filter : str = None, fields : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.get", user_id = user_id, extended = extended, filter = filter, fields = fields, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAddresses:
            '''Возвращает адрес указанного сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "address_ids": {"desc": "перечисленные через запятую идентификаторы адресов, информацию о которых необходимо вернуть. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "latitude": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число, минимальное значение -90, максимальное значение 90", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число, минимальное значение -180, максимальное значение 180", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества черного списка. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество адресов, которое необходимо вернуть. положительное число, по умолчанию 10", "type": "int", "default": "10"}, "fields": {"desc": "список дополнительных полей сообществ, которые необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, address_ids : str = None, latitude : int = None, longitude : int = None, offset : int = None, count : int = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getAddresses", group_id = group_id, address_ids = address_ids, latitude = latitude, longitude = longitude, offset = offset, count = count, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getBanned:
            '''Возвращает список забаненных пользователей и сообществ в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества черного списка. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество пользователей, которое необходимо вернуть. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "fields": {"desc": "список дополнительных полей профилей и сообществ, которые необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор пользователя или сообщества из чёрного списка, информацию о котором нужно получить. целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id, offset : int = None, count : int = None, fields : str = None, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getBanned", group_id = group_id, offset = offset, count = count, fields = fields, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию о заданном сообществе или о нескольких сообществах. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_ids": {"desc": "идентификаторы или короткие имена сообществ. Максимальное число идентификаторов — 500. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор или короткое имя сообщества. строка", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. Например: city, country, place, description, wiki_page, market, members_count, counters, start_date, finish_date, can_post, can_see_all_posts, activity, status, contacts, links, fixed_post, verified, site, ban_info, cover. Полный список полей доступен на этой странице. \nОбратите внимание, для получения некоторых полей требуется право доступа groups. Подробнее см. описание полей объекта group список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_ids : str = None, group_id : str = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getById", group_ids = group_ids, group_id = group_id, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCallbackConfirmationCode:
            '''Позволяет получить строку, необходимую для подтверждения адреса сервера в Callback API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getCallbackConfirmationCode", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCallbackServers:
            '''Получает информацию о серверах для Callback API в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "server_ids": {"desc": "идентификаторы серверов, данные о которых нужно получить. По умолчанию возвращаются все серверы. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, group_id, server_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getCallbackServers", group_id = group_id, server_ids = server_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCallbackSettings:
            '''Позволяет получить настройки уведомлений Callback API для сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "server_id": {"desc": "идентификатор сервера. положительное число", "type": "int", "default": "None"}}
            def __call__(self, group_id, server_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getCallbackSettings", group_id = group_id, server_id = server_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCatalog:
            '''Возвращает список сообществ выбранной категории каталога. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"category_id": {"desc": "идентификатор категории, полученный в методе groups.getCatalogInfo. положительное число", "type": "int", "default": "None"}, "subcategory_id": {"desc": "идентификатор подкатегории, полученный в методе groups.getCatalogInfo. положительное число, максимальное значение 99", "type": "int", "default": "None"}}
            def __call__(self, category_id : int = None, subcategory_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getCatalog", category_id = category_id, subcategory_id = subcategory_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCatalogInfo:
            '''Возвращает список категорий для каталога сообществ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"extended": {"desc": "1 — вернуть информацию о количестве сообществ в категории и три сообщества для предпросмотра. \nПо умолчанию 0. флаг, может принимать значения 1 или 0, по умолчанию 0, доступен начиная с версии 5.37", "type": "bool", "default": "0"}, "subcategories": {"desc": "1 — вернуть информацию об подкатегориях. \nПо умолчанию 0. флаг, может принимать значения 1 или 0, по умолчанию 0, доступен начиная с версии 5.37", "type": "bool", "default": "0"}}
            def __call__(self, extended : bool = None, subcategories : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getCatalogInfo", extended = extended, subcategories = subcategories, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getInvitedUsers:
            '''Возвращает список пользователей, которые были приглашены в группу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, список приглашенных в которую пользователей нужно вернуть. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определённого подмножества пользователей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество пользователей, информацию о которых нужно вернуть. положительное число, по умолчанию 20", "type": "int", "default": "20"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, offset : int = None, count : int = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getInvitedUsers", group_id = group_id, offset = offset, count = count, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getInvites:
            '''Данный метод возвращает список приглашений в сообщества и встречи текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определённого подмножества приглашений. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество приглашений, которое необходимо вернуть. положительное число, по умолчанию 20", "type": "int", "default": "20"}, "extended": {"desc": "1 — вернуть дополнительную информацию о пользователях, отправлявших приглашения. По умолчанию — 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getInvites", offset = offset, count = count, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLongPollServer:
            '''Возвращает данные для подключения к Bots Longpoll API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getLongPollServer", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLongPollSettings:
            '''Получает настройки Bots Longpoll API для сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getLongPollSettings", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMembers:
            '''Возвращает список участников сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор или короткое имя сообщества. строка", "type": "str", "default": "None"}, "sort": {"desc": "сортировка, с которой необходимо вернуть список участников. Может принимать значения: \n\nid_asc — в порядке возрастания id; \nid_desc — в порядке убывания id; \ntime_asc — в хронологическом порядке по вступлению в сообщество; \ntime_desc — в антихронологическом порядке по вступлению в сообщество. \nСортировка по time_asc и time_desc возможна только при вызове от модератора сообщества. строка, по умолчанию id_asc", "type": "str", "default": "id_asc"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества участников. По умолчанию 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество участников сообщества, информацию о которых необходимо получить. положительное число, по умолчанию 1000, максимальное значение 1000", "type": "int", "default": "1000"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives список слов, разделенных через запятую", "type": "str", "default": "None"}, "filter": {"desc": "\n\nfriends — будут возвращены только друзья в этом сообществе. \nunsure — будут возвращены пользователи, которые выбрали «Возможно пойду» (если сообщество относится к мероприятиям). \nmanagers — будут возвращены только руководители сообщества (доступно при запросе с передачей access_token от имени администратора сообщества). \ndonut — будут возвращены только доны (пользователи, у которых есть платная подписка VK Donut). \nстрока", "type": "str", "default": "None"}}
            def __call__(self, group_id : str = None, sort : str = None, offset : int = None, count : int = None, fields : str = None, filter : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getMembers", group_id = group_id, sort = sort, offset = offset, count = count, fields = fields, filter = filter, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOnlineStatus:
            '''Получает информацию о статусе «онлайн» в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getOnlineStatus", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getRequests:
            '''Возвращает список заявок на вступление в сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (указывается без знака «минус»). положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества результатов. По умолчанию — 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "число результатов, которые необходимо вернуть. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, offset : int = None, count : int = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.getRequests", group_id = group_id, offset = offset, count = count, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSettings:
            '''Позволяет получать данные, необходимые для отображения страницы редактирования данных сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, данные которого необходимо получить. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getSettings", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTagList:
            '''Возвращает список тегов сообщества '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.getTagList", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTokenPermissions:
            '''Возвращает настройки прав для ключа доступа сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("groups.getTokenPermissions", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class invite:
            '''Позволяет приглашать друзей в группу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, в которую необходимо выслать приглашение положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, которому необходимо выслать приглашение положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, user_id, v : str = None, access_token : str = None):
                self.exec_func("groups.invite", group_id = group_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class isMember:
            '''Возвращает информацию о том, является ли пользователь участником сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор или короткое имя сообщества. строка, обязательный параметр", "type": "str", "default": "None"}, "user_id": {"desc": "идентификатор пользователя. положительное число", "type": "int", "default": "None"}, "user_ids": {"desc": "идентификаторы пользователей, не более 500. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "extended": {"desc": "1  — вернуть ответ в расширенной форме. По умолчанию — 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, user_id : int = None, user_ids : str = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.isMember", group_id = group_id, user_id = user_id, user_ids = user_ids, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class join:
            '''Данный метод позволяет вступить в группу, публичную страницу, а также подтвердить участие во встрече. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число", "type": "int", "default": "None"}, "not_sure": {"desc": "опциональный параметр, учитываемый, если group_id принадлежит встрече. 1 — Возможно пойду. 0 — Точно пойду. По умолчанию 0. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id : int = None, not_sure : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.join", group_id = group_id, not_sure = not_sure, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class leave:
            '''Позволяет покинуть сообщество или отклонить приглашение в сообщество. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("groups.leave", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeUser:
            '''Позволяет исключить пользователя из группы или отклонить заявку на вступление. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, из которой необходимо исключить пользователя. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, которого нужно исключить. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, user_id, v : str = None, access_token : str = None):
                self.exec_func("groups.removeUser", group_id = group_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderLink:
            '''Позволяет менять местоположение ссылки в списке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, внутри которой перемещается ссылка положительное число, обязательный параметр", "type": "int", "default": "None"}, "link_id": {"desc": "идентификатор ссылки, которую необходимо переместить положительное число, обязательный параметр", "type": "int", "default": "None"}, "after": {"desc": "идентификатор ссылки после которой необходимо разместить перемещаемую ссылку. 0 – если ссылку нужно разместить в начале списка. положительное число", "type": "int", "default": "None"}}
            def __call__(self, group_id, link_id, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.reorderLink", group_id = group_id, link_id = link_id, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Осуществляет поиск сообществ по заданной подстроке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "текст поискового запроса. строка, обязательный параметр", "type": "str", "default": "None"}, "type": {"desc": "тип сообщества. Возможные значения: group, page, event. строка", "type": "str", "default": "None"}, "country_id": {"desc": "идентификатор страны. положительное число", "type": "int", "default": "None"}, "city_id": {"desc": "идентификатор города. При передаче этого параметра поле country_id игнорируется. положительное число", "type": "int", "default": "None"}, "future": {"desc": "при передаче значения 1 будут выведены предстоящие события. Учитывается только при передаче в качестве type значения event. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market": {"desc": "при передаче значения 1 будут выведены сообщества с включенными товарами. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "sort": {"desc": "\n\n0 — сортировать по умолчанию (аналогично результатам поиска в полной версии сайта); \n1 — сортировать по скорости роста; \n2 — сортировать по отношению дневной посещаемости к количеству пользователей; \n3 — сортировать по отношению количества лайков к количеству пользователей; \n4 — сортировать по отношению количества комментариев к количеству пользователей; \n5 — сортировать по отношению количества записей в обсуждениях к количеству пользователей. \nцелое число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определённого подмножества результатов поиска. По умолчанию — 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество результатов поиска, которое необходимо вернуть. Обратите внимание — даже при использовании параметра offset для получения информации доступны только первые 1000 результатов. \n положительное число, по умолчанию 20, максимальное значение 1000", "type": "int", "default": "20"}}
            def __call__(self, q, type : str = None, country_id : int = None, city_id : int = None, future : bool = None, market : bool = None, sort : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.search", q = q, type = type, country_id = country_id, city_id = city_id, future = future, market = market, sort = sort, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setCallbackSettings:
            '''Позволяет задать настройки уведомлений о событиях в Callback API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "server_id": {"desc": "идентификатор сервера. положительное число", "type": "int", "default": "None"}, "api_version": {"desc": "версия Callback API строка", "type": "str", "default": "None"}, "message_new": {"desc": "уведомления о новых сообщениях (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_reply": {"desc": "уведомления об исходящем сообщении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_allow": {"desc": "уведомления о подписке на сообщения  (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_edit": {"desc": "уведомления о редактировании сообщения (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_deny": {"desc": "уведомления о запрете на сообщения (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_typing_state": {"desc": "уведомления о наборе текста сообщения ('0 — выключить, 1'' — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_new": {"desc": "уведомления о добавлении новой фотографии (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "audio_new": {"desc": "уведомления о добавлении новой аудиозаписи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_new": {"desc": "уведомления о добавлении новой видеозаписи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_new": {"desc": "уведомления о добавлении нового комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_edit": {"desc": "уведомления о редактировании комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_delete": {"desc": "уведомления об удалении комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_restore": {"desc": "уведомления о восстановлении комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_post_new": {"desc": "уведомления о новой записи на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_repost": {"desc": "уведомления о репосте записи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_new": {"desc": "уведомления о создании комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_edit": {"desc": "уведомления о редактировании комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_restore": {"desc": "уведомление о восстановлении комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_delete": {"desc": "уведомления об удалении комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_new": {"desc": "уведомления о добавлении нового комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_edit": {"desc": "уведомления о редактировании комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_delete": {"desc": "уведомления об удалении комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_restore": {"desc": "уведомления о восстановлении комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_new": {"desc": "уведомления о добавлении нового комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_edit": {"desc": "уведомления о редактировании комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_delete": {"desc": "уведомления об удалении комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_restore": {"desc": "уведомления о восстановлении комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_new": {"desc": "уведомления о добавлении нового комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_edit": {"desc": "уведомления о редактировании комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_delete": {"desc": "уведомления об удалении комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_restore": {"desc": "уведомления о восстановлении комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_order_new": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_order_edit": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "poll_vote_new": {"desc": "уведомления о новом голосе в публичных опросах (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_join": {"desc": "уведомления о вступлении в сообщество (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_leave": {"desc": "уведомления о выходе из сообщества (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_change_settings": {"desc": "уведомления об изменении настроек (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_change_photo": {"desc": "уведомления об изменении главной фотографии (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_officers_edit": {"desc": "уведомления об изменении руководства (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_block": {"desc": "уведомления об внесении пользователя в чёрный список (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_unblock": {"desc": "уведомления об исключении пользователя из чёрного списка (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "lead_forms_new": {"desc": "уведомления о заполнении формы флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "like_add": {"desc": "уведомления о новой отметке \"Мне нравится\" (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "like_remove": {"desc": "уведомления о снятии отметки \"Мне нравится\" (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_event": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, server_id : int = None, api_version : str = None, message_new : bool = None, message_reply : bool = None, message_allow : bool = None, message_edit : bool = None, message_deny : bool = None, message_typing_state : bool = None, photo_new : bool = None, audio_new : bool = None, video_new : bool = None, wall_reply_new : bool = None, wall_reply_edit : bool = None, wall_reply_delete : bool = None, wall_reply_restore : bool = None, wall_post_new : bool = None, wall_repost : bool = None, board_post_new : bool = None, board_post_edit : bool = None, board_post_restore : bool = None, board_post_delete : bool = None, photo_comment_new : bool = None, photo_comment_edit : bool = None, photo_comment_delete : bool = None, photo_comment_restore : bool = None, video_comment_new : bool = None, video_comment_edit : bool = None, video_comment_delete : bool = None, video_comment_restore : bool = None, market_comment_new : bool = None, market_comment_edit : bool = None, market_comment_delete : bool = None, market_comment_restore : bool = None, market_order_new : bool = None, market_order_edit : bool = None, poll_vote_new : bool = None, group_join : bool = None, group_leave : bool = None, group_change_settings : bool = None, group_change_photo : bool = None, group_officers_edit : bool = None, user_block : bool = None, user_unblock : bool = None, lead_forms_new : bool = None, like_add : bool = None, like_remove : bool = None, message_event : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.setCallbackSettings", group_id = group_id, server_id = server_id, api_version = api_version, message_new = message_new, message_reply = message_reply, message_allow = message_allow, message_edit = message_edit, message_deny = message_deny, message_typing_state = message_typing_state, photo_new = photo_new, audio_new = audio_new, video_new = video_new, wall_reply_new = wall_reply_new, wall_reply_edit = wall_reply_edit, wall_reply_delete = wall_reply_delete, wall_reply_restore = wall_reply_restore, wall_post_new = wall_post_new, wall_repost = wall_repost, board_post_new = board_post_new, board_post_edit = board_post_edit, board_post_restore = board_post_restore, board_post_delete = board_post_delete, photo_comment_new = photo_comment_new, photo_comment_edit = photo_comment_edit, photo_comment_delete = photo_comment_delete, photo_comment_restore = photo_comment_restore, video_comment_new = video_comment_new, video_comment_edit = video_comment_edit, video_comment_delete = video_comment_delete, video_comment_restore = video_comment_restore, market_comment_new = market_comment_new, market_comment_edit = market_comment_edit, market_comment_delete = market_comment_delete, market_comment_restore = market_comment_restore, market_order_new = market_order_new, market_order_edit = market_order_edit, poll_vote_new = poll_vote_new, group_join = group_join, group_leave = group_leave, group_change_settings = group_change_settings, group_change_photo = group_change_photo, group_officers_edit = group_officers_edit, user_block = user_block, user_unblock = user_unblock, lead_forms_new = lead_forms_new, like_add = like_add, like_remove = like_remove, message_event = message_event, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setLongPollSettings:
            '''Задаёт настройки для Bots Long Poll API в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "enabled": {"desc": "1 — включить Bots Long Poll, 0 — отключить. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "api_version": {"desc": "версия API. По умолчанию — 5.50 строка", "type": "str", "default": "None"}, "message_new": {"desc": "уведомления о новых сообщениях (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_reply": {"desc": "уведомления об исходящем сообщении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_allow": {"desc": "уведомления о подписке на сообщения  (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_deny": {"desc": "уведомления о запрете на сообщения (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_edit": {"desc": "уведомления о редактировании сообщения (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_typing_state": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_new": {"desc": "уведомления о добавлении новой фотографии (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "audio_new": {"desc": "уведомления о добавлении новой аудиозаписи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_new": {"desc": "уведомления о добавлении новой видеозаписи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_new": {"desc": "уведомления о добавлении нового комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_edit": {"desc": "уведомления о редактировании комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_delete": {"desc": "уведомления об удалении комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_reply_restore": {"desc": "уведомления о восстановлении комментария на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_post_new": {"desc": "уведомления о новой записи на стене (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wall_repost": {"desc": "уведомления о репосте записи (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_new": {"desc": "уведомления о создании комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_edit": {"desc": "уведомления о редактировании комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_restore": {"desc": "уведомление о восстановлении комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "board_post_delete": {"desc": "уведомления об удалении комментария в обсуждении (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_new": {"desc": "уведомления о добавлении нового комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_edit": {"desc": "уведомления о редактировании комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_delete": {"desc": "уведомления об удалении комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_comment_restore": {"desc": "уведомления о восстановлении комментария к фото (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_new": {"desc": "уведомления о добавлении нового комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_edit": {"desc": "уведомления о редактировании комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_delete": {"desc": "уведомления об удалении комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "video_comment_restore": {"desc": "уведомления о восстановлении комментария к видео (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_new": {"desc": "уведомления о добавлении нового комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_edit": {"desc": "уведомления о редактировании комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_delete": {"desc": "уведомления об удалении комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "market_comment_restore": {"desc": "уведомления о восстановлении комментария к товару (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "poll_vote_new": {"desc": "уведомления о новом голосе в публичных опросах (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_join": {"desc": "уведомления о вступлении в сообщество (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_leave": {"desc": "уведомления о выходе из сообщества (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_change_settings": {"desc": "уведомления об изменении настроек (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_change_photo": {"desc": "уведомления об изменении главной фотографии (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_officers_edit": {"desc": "уведомления об изменении руководства (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_block": {"desc": "уведомления об внесении пользователя в чёрный список (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_unblock": {"desc": "уведомления об исключении пользователя из чёрного списка (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "like_add": {"desc": "уведомления о новой отметке \"Мне нравится\" (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "like_remove": {"desc": "уведомления о снятии отметки \"Мне нравится\" (0 — выключить, 1 — включить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message_event": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, enabled : bool = None, api_version : str = None, message_new : bool = None, message_reply : bool = None, message_allow : bool = None, message_deny : bool = None, message_edit : bool = None, message_typing_state : bool = None, photo_new : bool = None, audio_new : bool = None, video_new : bool = None, wall_reply_new : bool = None, wall_reply_edit : bool = None, wall_reply_delete : bool = None, wall_reply_restore : bool = None, wall_post_new : bool = None, wall_repost : bool = None, board_post_new : bool = None, board_post_edit : bool = None, board_post_restore : bool = None, board_post_delete : bool = None, photo_comment_new : bool = None, photo_comment_edit : bool = None, photo_comment_delete : bool = None, photo_comment_restore : bool = None, video_comment_new : bool = None, video_comment_edit : bool = None, video_comment_delete : bool = None, video_comment_restore : bool = None, market_comment_new : bool = None, market_comment_edit : bool = None, market_comment_delete : bool = None, market_comment_restore : bool = None, poll_vote_new : bool = None, group_join : bool = None, group_leave : bool = None, group_change_settings : bool = None, group_change_photo : bool = None, group_officers_edit : bool = None, user_block : bool = None, user_unblock : bool = None, like_add : bool = None, like_remove : bool = None, message_event : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.setLongPollSettings", group_id = group_id, enabled = enabled, api_version = api_version, message_new = message_new, message_reply = message_reply, message_allow = message_allow, message_deny = message_deny, message_edit = message_edit, message_typing_state = message_typing_state, photo_new = photo_new, audio_new = audio_new, video_new = video_new, wall_reply_new = wall_reply_new, wall_reply_edit = wall_reply_edit, wall_reply_delete = wall_reply_delete, wall_reply_restore = wall_reply_restore, wall_post_new = wall_post_new, wall_repost = wall_repost, board_post_new = board_post_new, board_post_edit = board_post_edit, board_post_restore = board_post_restore, board_post_delete = board_post_delete, photo_comment_new = photo_comment_new, photo_comment_edit = photo_comment_edit, photo_comment_delete = photo_comment_delete, photo_comment_restore = photo_comment_restore, video_comment_new = video_comment_new, video_comment_edit = video_comment_edit, video_comment_delete = video_comment_delete, video_comment_restore = video_comment_restore, market_comment_new = market_comment_new, market_comment_edit = market_comment_edit, market_comment_delete = market_comment_delete, market_comment_restore = market_comment_restore, poll_vote_new = poll_vote_new, group_join = group_join, group_leave = group_leave, group_change_settings = group_change_settings, group_change_photo = group_change_photo, group_officers_edit = group_officers_edit, user_block = user_block, user_unblock = user_unblock, like_add = like_add, like_remove = like_remove, message_event = message_event, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setSettings:
            '''Устанавливает настройки сообщества '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "messages": {"desc": "сообщения сообщества. Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "bots_capabilities": {"desc": "возможности ботов (использование клавиатуры, добавление в беседу). Возможные значения: \n\n0 — выключены; \n1 — включены. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "bots_start_button": {"desc": "кнопка «Начать» в диалоге с сообществом. \nРаботает, в случае если bots_capabilities=1. \nЕсли эта настройка включена, то при заходе в беседу с Вашим сообществом в первый раз пользователь увидит кнопку с командой «Начать», которая отправляет команду start. Payload этого сообщения будет выглядеть так: {\"command\":\"start\"} \n \nВозможные значения: \n\n0 — выключена; \n1 — включена. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "bots_add_to_chat": {"desc": "добавление бота в беседы. \nРаботает, в случае если bots_capabilities=1. \nВозможные значения: \n\n0 — запрещено; \n1 — разрешено. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, group_id, messages : bool = None, bots_capabilities : bool = None, bots_start_button : bool = None, bots_add_to_chat : bool = None, v : str = None, access_token : str = None):
                self.exec_func("groups.setSettings", group_id = group_id, messages = messages, bots_capabilities = bots_capabilities, bots_start_button = bots_start_button, bots_add_to_chat = bots_add_to_chat, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setUserNote:
            '''Позволяет создать или отредактировать заметку о пользователе в рамках переписки пользователя с сообществом '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "Идентификатор пользователя положительное число, обязательный параметр", "type": "int", "default": "None"}, "note": {"desc": "содержимое заметки, максимальная длина - 96 символов строка, максимальная длина 96", "type": "str", "default": "None"}}
            def __call__(self, group_id, user_id, note : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.setUserNote", group_id = group_id, user_id = user_id, note = note, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class tagAdd:
            '''Позволяет добавить новый тег в сообщество '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества положительное число, обязательный параметр", "type": "int", "default": "None"}, "tag_name": {"desc": "Имя тега строка, максимальная длина 20, обязательный параметр", "type": "str", "default": "None"}, "tag_color": {"desc": "Цвет тега. Разрешается использовать следующие цвета: 4bb34b, 5c9ce6, e64646, 792ec0, 63b9ba, ffa000, ffc107, 76787a, 9e8d6b, 45678f, 539b9c, 454647, 7a6c4f, 6bc76b, 5181b8, ff5c5c, a162de, 7ececf, aaaeb3, bbaa84 строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, tag_name, tag_color : str = None, v : str = None, access_token : str = None):
                self.exec_func("groups.tagAdd", group_id = group_id, tag_name = tag_name, tag_color = tag_color, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class tagBind:
            '''Позволяет "привязывать" и "отвязывать" теги сообщества к беседам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы положительное число, обязательный параметр", "type": "int", "default": "None"}, "tag_id": {"desc": "Идентификатор тега положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "положительное число, обязательный параметр", "type": "int", "default": "None"}, "act": {"desc": "Действие с тегом \n\n\"bind\" -  привязать \n\"unbind\" - отвязать \nстрока, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, group_id, tag_id, user_id, act, v : str = None, access_token : str = None):
                self.exec_func("groups.tagBind", group_id = group_id, tag_id = tag_id, user_id = user_id, act = act, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class tagDelete:
            '''Позволяет удалить тег сообщества '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы положительное число, обязательный параметр", "type": "int", "default": "None"}, "tag_id": {"desc": "Идентификатор удаляемого тега положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, tag_id, v : str = None, access_token : str = None):
                self.exec_func("groups.tagDelete", group_id = group_id, tag_id = tag_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class tagUpdate:
            '''Позволяет переименовать существующий тег '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества положительное число, обязательный параметр", "type": "int", "default": "None"}, "tag_id": {"desc": "Идентификатор тега положительное число, обязательный параметр", "type": "int", "default": "None"}, "tag_name": {"desc": "Имя тега строка, максимальная длина 20, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, group_id, tag_id, tag_name, v : str = None, access_token : str = None):
                self.exec_func("groups.tagUpdate", group_id = group_id, tag_id = tag_id, tag_name = tag_name, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class toggleMarket:
            '''переключает функционал раздела "Товаров" в выбранной группе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества, в котором необходимо переключить функционал магазина. положительное число, обязательный параметр", "type": "int", "default": "None"}, "state": {"desc": "Значение переключателя. Возможные значения: \n\nnone — товары отключены; \nbasic — базовые товары; \nadvanced — расширенные товары. \nстрока, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, group_id, state, v : str = None, access_token : str = None):
                self.exec_func("groups.toggleMarket", group_id = group_id, state = state, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unban:
            '''Убирает пользователя или группу из черного списка сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор пользователя или группы, которого нужно убрать из черного списка. целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("groups.unban", group_id = group_id, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class leadForms:
        def  __init__(self, exec_func):
            self.create = self.create(exec_func)
            self.delete = self.delete(exec_func)
            self.get = self.get(exec_func)
            self.getLeads = self.getLeads(exec_func)
            self.getUploadURL = self.getUploadURL(exec_func)
            self.list = self.list(exec_func)
            self.update = self.update(exec_func)
        class create:
            '''Создаёт форму сбора заявок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы, в которой надо создать форму. обязательный параметр, целое число", "type": "int", "default": "None"}, "name": {"desc": "Название формы (видно только администратору). обязательный параметр, строка, максимальная длина 100", "type": "str", "default": "None"}, "title": {"desc": "Заголовок формы (видят пользователи). обязательный параметр, строка, максимальная длина 60", "type": "str", "default": "None"}, "description": {"desc": "Описание формы. обязательный параметр, строка, максимальная длина 600", "type": "str", "default": "None"}, "questions": {"desc": "Информация о вопросах формы. Массив структур следующего формата: \n\ntype — тип вопроса; \nlabel — заголовок вопроса (только для нестандартных вопросов); \nkey — уникальный ключ вопроса (необязательно; только для нестандартных вопросов); \noptions — массив возможных ответов на вопрос (только для нестандартных вопросов типа radio, select, checkbox); \n\nТипы стандартных вопросов: \n\nfirst_name — имя; \npatronymic_name — отчество; \nlast_name — фамилия; \nemail — адрес электронной почты; \nphone_number — номер телефона; \nage — возраст; \nbirthday — день рождения; \nlocation — город и страна. \n\nТипы нестандартных вопросов: \n\ninput — простое текстовое поле (строка); \ntextarea — большое текстовое поле (абзац); \nradio — выбор одного из нескольких вариантов; \ncheckbox — выбор нескольких вариантов; \nselect — выбор одного варианта из выпадающего списка. \n\noptions должен быть массивом структур, описывающих варианты ответа: \n\nlabel — текст ответа; \nkey — ключ ответа (необязательно). \n\nПример:[ \n   { \n      \"type\":\"first_name\" \n   }, \n   { \n      \"type\":\"input\", \n      \"label\":\"Кличка кота\" \n   }, \n   { \n      \"type\":\"select\", \n      \"key\":\"favorite_color\", \n      \"label\":\"Любимый цвет\", \n      \"options\":[{ \n        \"key\":\"red\", \n        \"label\":\"Красный\" \n      },{ \n        \"key\":\"green\", \n        \"label\":\"Зелёный\" \n      }] \n   }, \n   { \n      \"type\":\"radio\", \n      \"label\":\"Я ношу часы...\", \n      \"options\":[{ \n         \"key\":\"left\", \n         \"label\":\"на левой руке\" \n      },{ \n         \"key\":\"right\", \n         \"label\":\"на правой руке\" \n      }] \n   }, \n   { \n      \"type\":\"checkbox\", \n      \"key\":\"visited_cities\", \n      \"label\":\"Города, в которых я был\", \n      \"options\":[{ \n         \"label\":\"Екатеринбург\" \n      },{ \n         \"label\":\"Волгоград\" \n      },{ \n         \"label\":\"Санкт-Петербург\" \n      }] \n   } \n] \n данные в формате JSON, обязательный параметр", "type": "not defined", "default": "None"}, "policy_link_url": {"desc": "Ссылка на политику конфиденциальности. строка, обязательный параметр, максимальная длина 200", "type": "str", "default": "None"}, "photo": {"desc": "Обложка формы. \nИспользуйте значение, полученное после загрузки фотографии на сервер. См. метод leadForms.getUploadURL. \nТакже можно переиспользовать существующую фотографию из другой формы. Используйте значение поля photo, которое возвращает метод leadForms.get или leadForms.list. строка", "type": "str", "default": "None"}, "confirmation": {"desc": "Текст подтверждения, который увидит пользователь после отправки формы. строка, максимальная длина 300", "type": "str", "default": "None"}, "site_link_url": {"desc": "Ссылка на сайт или сообщество автора формы. строка, максимальная длина 200", "type": "str", "default": "None"}, "active": {"desc": "Передайте 1, чтобы активировать форму сразу после создания. Пользователи могут оставлять заявки только в активных формах. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "once_per_user": {"desc": "Передайте 1, чтобы разрешить каждому пользователю заполнять форму только один раз. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "pixel_code": {"desc": "Передайте код пикселя ретаргетинга ВКонтакте в виде VK-RTRG-000000-XXXXX. По этому пикселю будет собираться аудитория пользователей, открывших форму. Подробнее о пикселе см. здесь. строка", "type": "str", "default": "None"}, "notify_admins": {"desc": "Передайте список идентификаторов пользователей, которым будут отправлены оповещения о заполнении пользователями формы. Оповещения могут быть отправлены только администраторам сообщества. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "notify_emails": {"desc": "Передайте список email-адресов, разделённых запятой, на которые будут отправлены оповещения о заполнении пользователями формы. Можно указать до 10 адресов. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, name, title, description, questions, policy_link_url, photo : str = None, confirmation : str = None, site_link_url : str = None, active : bool = None, once_per_user : bool = None, pixel_code : str = None, notify_admins : str = None, notify_emails : str = None, v : str = None, access_token : str = None):
                self.exec_func("leadForms.create", group_id = group_id, name = name, title = title, description = description, questions = questions, policy_link_url = policy_link_url, photo = photo, confirmation = confirmation, site_link_url = site_link_url, active = active, once_per_user = once_per_user, pixel_code = pixel_code, notify_admins = notify_admins, notify_emails = notify_emails, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет форму сбора заявок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы, из которой надо удалить форму. обязательный параметр, целое число", "type": "int", "default": "None"}, "form_id": {"desc": "Идентификатор удаляемой формы. обязательный параметр, целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id, form_id, v : str = None, access_token : str = None):
                self.exec_func("leadForms.delete", group_id = group_id, form_id = form_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает информацию о форме сбора заявок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы, в которой находится форма. обязательный параметр, целое число", "type": "int", "default": "None"}, "form_id": {"desc": "Идентификатор формы. обязательный параметр, целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id, form_id, v : str = None, access_token : str = None):
                self.exec_func("leadForms.get", group_id = group_id, form_id = form_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLeads:
            '''Возвращает заявки формы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, в котором находится форма. обязательный параметр, целое число", "type": "int", "default": "None"}, "form_id": {"desc": "идентификатор формы. обязательный параметр, целое число", "type": "int", "default": "None"}, "limit": {"desc": "количество возвращаемых заявок за один запрос. положительное число, по умолчанию 10, максимальное значение 1000, минимальное значение 1", "type": "int", "default": "10"}, "next_page_token": {"desc": "строка, полученная из предыдущего запроса для получения следующей порции результатов. строка", "type": "str", "default": "None"}}
            def __call__(self, group_id, form_id, limit : int = None, next_page_token : str = None, v : str = None, access_token : str = None):
                self.exec_func("leadForms.getLeads", group_id = group_id, form_id = form_id, limit = limit, next_page_token = next_page_token, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUploadURL:
            '''Возвращает URL для загрузки обложки для формы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("leadForms.getUploadURL", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class list:
            '''Возвращает список форм сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор сообщества. обязательный параметр, целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("leadForms.list", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class update:
            '''Обновляет форму сбора заявок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "Идентификатор группы, в которой надо обновить форму. обязательный параметр, целое число", "type": "int", "default": "None"}, "form_id": {"desc": "Идентификатор формы, которую надо обновить. обязательный параметр, целое число", "type": "int", "default": "None"}, "name": {"desc": "Новое название формы (видно только администратору). обязательный параметр, строка, максимальная длина 100", "type": "str", "default": "None"}, "title": {"desc": "Новый заголовок формы (видят пользователи). обязательный параметр, строка, максимальная длина 60", "type": "str", "default": "None"}, "description": {"desc": "Новое описание формы. обязательный параметр, строка, максимальная длина 600", "type": "str", "default": "None"}, "questions": {"desc": "Новые вопросы формы. Подробнее см. метод leadForms.create. данные в формате JSON, обязательный параметр", "type": "not defined", "default": "None"}, "policy_link_url": {"desc": "Новая ссылка на политику конфиденциальности. строка, обязательный параметр, максимальная длина 200", "type": "str", "default": "None"}, "photo": {"desc": "Новая обложка формы. строка", "type": "str", "default": "None"}, "confirmation": {"desc": "Новый текст подтверждения, который увидит пользователь после отправки формы. строка, максимальная длина 300", "type": "str", "default": "None"}, "site_link_url": {"desc": "Новая ссылка на сайт или сообщество автора формы. строка, максимальная длина 200", "type": "str", "default": "None"}, "active": {"desc": "Передайте 1, чтобы активировать форму. Пользователи могут оставлять заявки только в активных формах. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "once_per_user": {"desc": "Передайте 1, чтобы разрешить каждому пользователю заполнять форму только один раз. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "pixel_code": {"desc": "Новый код пикселя ретаргетинга ВКонтакте. строка", "type": "str", "default": "None"}, "notify_admins": {"desc": "Новый список идентификаторов пользователей, которым будут отправлены оповещения о заполнении пользователями формы. Оповещения могут быть отправлены только администраторам сообщества. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "notify_emails": {"desc": "Новый список email-адресов, разделённых запятой, на которые будут отправлены оповещения о заполнении пользователями формы. Можно указать до 10 адресов. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id, form_id, name, title, description, questions, policy_link_url, photo : str = None, confirmation : str = None, site_link_url : str = None, active : bool = None, once_per_user : bool = None, pixel_code : str = None, notify_admins : str = None, notify_emails : str = None, v : str = None, access_token : str = None):
                self.exec_func("leadForms.update", group_id = group_id, form_id = form_id, name = name, title = title, description = description, questions = questions, policy_link_url = policy_link_url, photo = photo, confirmation = confirmation, site_link_url = site_link_url, active = active, once_per_user = once_per_user, pixel_code = pixel_code, notify_admins = notify_admins, notify_emails = notify_emails, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class likes:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.delete = self.delete(exec_func)
            self.getList = self.getList(exec_func)
            self.isLiked = self.isLiked(exec_func)
        class add:
            '''Добавляет указанный объект в список Мне нравится текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип объекта. \nВозможные типы:\npost — запись на стене пользователя или группы;\ncomment — комментарий к записи на стене;\nphoto — фотография;\naudio — аудиозапись;\nvideo — видеозапись;\nnote — заметка;\nmarket — товар;\nphoto_comment — комментарий к фотографии;\nvideo_comment — комментарий к видеозаписи;\ntopic_comment — комментарий в обсуждении;\nmarket_comment — комментарий к товару; строка, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца объекта. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "item_id": {"desc": "идентификатор объекта. положительное число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "ключ доступа в случае работы с приватными объектами. строка", "type": "str", "default": "None"}}
            def __call__(self, type, item_id, owner_id : int = None, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("likes.add", type = type, owner_id = owner_id, item_id = item_id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет указанный объект из списка Мне нравится текущего пользователя '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип объекта. \nВозможные типы:\npost — запись на стене пользователя или группы;\nstory — история;\ncomment — комментарий к записи на стене;\nphoto — фотография;\naudio — аудиозапись;\nvideo — видеозапись;\nnote — заметка;\nphoto_comment — комментарий к фотографии;\nvideo_comment — комментарий к видеозаписи;\ntopic_comment — комментарий в обсуждении;\nsitepage — страница сайта, на котором установлен виджет «Мне нравится». строка, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца объекта. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "item_id": {"desc": "идентификатор объекта. положительное число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "строка", "type": "str", "default": "None"}}
            def __call__(self, type, item_id, owner_id : int = None, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("likes.delete", type = type, owner_id = owner_id, item_id = item_id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getList:
            '''Получает список идентификаторов пользователей, которые добавили заданный объект в свой список Мне нравится. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип объекта. \nВозможные типы:\npost — запись на стене пользователя или группы;\ncomment — комментарий к записи на стене;\nphoto — фотография;\naudio — аудиозапись;\nvideo — видеозапись;\nnote — заметка;\nmarket — товар;\nphoto_comment — комментарий к фотографии;\nvideo_comment — комментарий к видеозаписи;\ntopic_comment — комментарий в обсуждении;\nmarket_comment — комментарий к товару;\nsitepage — страница сайта, на котором установлен виджет «Мне нравится». строка, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца Like-объекта: id пользователя, id сообщества (со знаком «минус») или id приложения. Если параметр type равен sitepage, то в качестве owner_id необходимо передавать id приложения. Если параметр не задан, то считается, что он равен либо идентификатору текущего пользователя, либо идентификатору текущего приложения (если type равен sitepage). целое число", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор Like-объекта. Если type равен sitepage, то параметр item_id может содержать значение параметра page_id, используемый при инициализации  виджета «Мне нравится». целое число", "type": "int", "default": "None"}, "page_url": {"desc": "url страницы, на которой установлен виджет «Мне нравится». Используется вместо параметра item_id, если при размещении виджета не был указан page_id. строка", "type": "str", "default": "None"}, "filter": {"desc": "указывает, следует ли вернуть всех пользователей, добавивших объект в список \"Мне нравится\" или только тех, которые рассказали о нем друзьям. Параметр может принимать следующие значения: \n\nlikes — возвращать информацию обо всех пользователях; \ncopies — возвращать информацию только о пользователях, рассказавших об объекте друзьям.\nПо умолчанию возвращается информация обо всех пользователях. \nстрока", "type": "str", "default": "None"}, "friends_only": {"desc": "указывает, необходимо ли возвращать только пользователей, которые являются друзьями текущего пользователя. Параметр может принимать следующие значения: \n\n0 — возвращать всех пользователей в порядке убывания времени добавления объекта; \n1 — возвращать только друзей текущего пользователя в порядке убывания времени добавления объекта;\nЕсли метод был вызван без авторизации или параметр не был задан, то считается, что он равен 0. \n целое число, по умолчанию 0", "type": "int", "default": "0"}, "extended": {"desc": "1 — возвращать расширенную информацию о пользователях и сообществах из списка поставивших отметку «Мне нравится» или сделавших репост. По умолчанию — 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение, относительно начала списка, для выборки определенного подмножества. Если параметр не задан, то считается, что он равен 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых идентификаторов пользователей.\nЕсли параметр не задан, то считается, что он равен 100, если не задан параметр friends_only, в противном случае 10.\nМаксимальное значение параметра 1000, если не задан параметр friends_only, в противном случае 100. положительное число, максимальное значение 1000", "type": "int", "default": "None"}, "skip_own": {"desc": "не возвращать самого пользователя. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, type, owner_id : int = None, item_id : int = None, page_url : str = None, filter : str = None, friends_only : int = None, extended : bool = None, offset : int = None, count : int = None, skip_own : bool = None, v : str = None, access_token : str = None):
                self.exec_func("likes.getList", type = type, owner_id = owner_id, item_id = item_id, page_url = page_url, filter = filter, friends_only = friends_only, extended = extended, offset = offset, count = count, skip_own = skip_own, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class isLiked:
            '''Проверяет, находится ли объект в списке Мне нравится заданного пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, у которого необходимо проверить наличие объекта в списке «Мне нравится». Если параметр не задан, то считается, что он равен идентификатору текущего пользователя. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "type": {"desc": "тип объекта. \nВозможные типы:\npost — запись на стене пользователя или группы;\ncomment — комментарий к записи на стене;\nphoto — фотография;\naudio — аудиозапись;\nvideo — видеозапись;\nnote — заметка;\nphoto_comment — комментарий к фотографии;\nvideo_comment — комментарий к видеозаписи;\ntopic_comment — комментарий в обсуждении; строка, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца Like-объекта. Если параметр не задан, то считается, что он равен идентификатору текущего пользователя. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "item_id": {"desc": "идентификатор объекта. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, type, item_id, user_id : int = None, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("likes.isLiked", user_id = user_id, type = type, owner_id = owner_id, item_id = item_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class market:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.addAlbum = self.addAlbum(exec_func)
            self.addToAlbum = self.addToAlbum(exec_func)
            self.createComment = self.createComment(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteAlbum = self.deleteAlbum(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.edit = self.edit(exec_func)
            self.editAlbum = self.editAlbum(exec_func)
            self.editComment = self.editComment(exec_func)
            self.editOrder = self.editOrder(exec_func)
            self.get = self.get(exec_func)
            self.getAlbumById = self.getAlbumById(exec_func)
            self.getAlbums = self.getAlbums(exec_func)
            self.getById = self.getById(exec_func)
            self.getCategories = self.getCategories(exec_func)
            self.getComments = self.getComments(exec_func)
            self.getGroupOrders = self.getGroupOrders(exec_func)
            self.getOrderById = self.getOrderById(exec_func)
            self.getOrderItems = self.getOrderItems(exec_func)
            self.getOrders = self.getOrders(exec_func)
            self.removeFromAlbum = self.removeFromAlbum(exec_func)
            self.reorderAlbums = self.reorderAlbums(exec_func)
            self.reorderItems = self.reorderItems(exec_func)
            self.report = self.report(exec_func)
            self.reportComment = self.reportComment(exec_func)
            self.restore = self.restore(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
            self.search = self.search(exec_func)
        class add:
            '''Добавляет новый товар. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "name": {"desc": "название товара. Ограничение по длине считается в кодировке cp1251. строка, минимальная длина 4, максимальная длина 100, обязательный параметр", "type": "str", "default": "None"}, "description": {"desc": "описание товара. строка, минимальная длина 10, обязательный параметр", "type": "str", "default": "None"}, "category_id": {"desc": "идентификатор категории товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "price": {"desc": "цена товара. дробное число, минимальное значение 0.01", "type": "int", "default": "None"}, "old_price": {"desc": "старая цена товара. дробное число, минимальное значение 0.01", "type": "int", "default": "None"}, "deleted": {"desc": "статус товара (1 — товар удален, 0 — товар не удален). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "main_photo_id": {"desc": "идентификатор фотографии обложки товара. \nФотография должна быть загружена с помощью метода photos.getMarketUploadServer, передав параметр main_photo. См. подробную информацию о загрузке фотографии товаров положительное число", "type": "int", "default": "None"}, "photo_ids": {"desc": "идентификаторы дополнительных фотографий товара. \nФотография должна быть загружена с помощью метода photos.getMarketUploadServer. См. подробную информацию о загрузке фотографии товаров список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "url": {"desc": "ссылка на сайт товара. строка, минимальная длина 0, максимальная длина 320", "type": "str", "default": "None"}, "dimension_width": {"desc": "ширина в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "dimension_height": {"desc": "высота в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "dimension_length": {"desc": "глубина в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "weight": {"desc": "вес в граммах. положительное число, минимальное значение 0, максимальное значение 100000000", "type": "int", "default": "None"}, "sku": {"desc": "артикул товара, произвольная строка строка, максимальная длина 50, доступен начиная с версии 5.131", "type": "str", "default": "None"}}
            def __call__(self, owner_id, name, description, category_id, price : int = None, old_price : int = None, deleted : bool = None, main_photo_id : int = None, photo_ids : str = None, url : str = None, dimension_width : int = None, dimension_height : int = None, dimension_length : int = None, weight : int = None, sku : str = None, v : str = None, access_token : str = None):
                self.exec_func("market.add", owner_id = owner_id, name = name, description = description, category_id = category_id, price = price, old_price = old_price, deleted = deleted, main_photo_id = main_photo_id, photo_ids = photo_ids, url = url, dimension_width = dimension_width, dimension_height = dimension_height, dimension_length = dimension_length, weight = weight, sku = sku, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addAlbum:
            '''Добавляет новую подборку с товарами. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца подборки. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "название подборки. строка, обязательный параметр, максимальная длина 128", "type": "str", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии-обложки подборки. \nФотография должна быть загружена с помощью метода photos.getMarketAlbumUploadServer. См. подробную информацию о загрузке фотографии товаров. положительное число", "type": "int", "default": "None"}, "main_album": {"desc": "назначить подборку основной (1 — назначить, 0 — нет). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id, title, photo_id : int = None, main_album : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.addAlbum", owner_id = owner_id, title = title, photo_id = photo_id, main_album = main_album, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addToAlbum:
            '''Добавляет товар в одну или несколько выбранных подборок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "album_ids": {"desc": "идентификаторы подборок, в которые нужно добавить товар. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owner_id, item_id, album_ids, v : str = None, access_token : str = None):
                self.exec_func("market.addToAlbum", owner_id = owner_id, item_id = item_id, album_ids = album_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Создает новый комментарий к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст комментария (является обязательным, если не задан параметр attachments). строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_group": {"desc": "1 — комментарий будет опубликован от имени группы, 0 — комментарий будет опубликован от имени пользователя (по умолчанию). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "reply_to_comment": {"desc": "идентификатор комментария, в ответ на который должен быть добавлен новый комментарий. положительное число", "type": "int", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, item_id, message : str = None, attachments : str = None, from_group : bool = None, reply_to_comment : int = None, sticker_id : int = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("market.createComment", owner_id = owner_id, item_id = item_id, message = message, attachments = attachments, from_group = from_group, reply_to_comment = reply_to_comment, sticker_id = sticker_id, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет товар. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, item_id, v : str = None, access_token : str = None):
                self.exec_func("market.delete", owner_id = owner_id, item_id = item_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteAlbum:
            '''Удаляет подборку с товарами. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца подборки. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор подборки. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, album_id, v : str = None, access_token : str = None):
                self.exec_func("market.deleteAlbum", owner_id = owner_id, album_id = album_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет комментарий к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, v : str = None, access_token : str = None):
                self.exec_func("market.deleteComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует товар. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "name": {"desc": "новое название товара. строка", "type": "str", "default": "None"}, "description": {"desc": "новое описание товара. строка", "type": "str", "default": "None"}, "category_id": {"desc": "идентификатор категории товара. положительное число", "type": "int", "default": "None"}, "price": {"desc": "цена товара. дробное число, минимальное значение 0.01", "type": "int", "default": "None"}, "old_price": {"desc": "старая цена. дробное число, минимальное значение 0.01", "type": "int", "default": "None"}, "deleted": {"desc": "статус товара (1 — товар удален, 0 — товар не удален). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "main_photo_id": {"desc": "идентификатор фотографии для обложки товара. \nФотография может быть загружена с помощью метода photos.getMarketUploadServer (параметр main_photo). См. подробную информацию о загрузке фотографии товаров. \nИдентификатор фотографии может быть также получен методами market.get или market.getById (если Вы хотите использовать существующую фотографию товара). положительное число", "type": "int", "default": "None"}, "photo_ids": {"desc": "идентификаторы дополнительных фотографией товара. \nФотография должна быть загружена с помощью метода photos.getMarketUploadServer. См. подробную информацию о загрузке фотографии товаров. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "url": {"desc": "ссылка на сайт товара. строка, минимальная длина 0, максимальная длина 320", "type": "str", "default": "None"}, "dimension_width": {"desc": "ширина в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "dimension_height": {"desc": "высота в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "dimension_length": {"desc": "глубина в миллиметрах. положительное число, минимальное значение 0, максимальное значение 100000", "type": "int", "default": "None"}, "weight": {"desc": "вес в граммах. положительное число, минимальное значение 0, максимальное значение 100000000", "type": "int", "default": "None"}, "sku": {"desc": "артикул товара, произвольная строка строка, максимальная длина 50, доступен начиная с версии 5.131", "type": "str", "default": "None"}}
            def __call__(self, owner_id, item_id, name : str = None, description : str = None, category_id : int = None, price : int = None, old_price : int = None, deleted : bool = None, main_photo_id : int = None, photo_ids : str = None, url : str = None, dimension_width : int = None, dimension_height : int = None, dimension_length : int = None, weight : int = None, sku : str = None, v : str = None, access_token : str = None):
                self.exec_func("market.edit", owner_id = owner_id, item_id = item_id, name = name, description = description, category_id = category_id, price = price, old_price = old_price, deleted = deleted, main_photo_id = main_photo_id, photo_ids = photo_ids, url = url, dimension_width = dimension_width, dimension_height = dimension_height, dimension_length = dimension_length, weight = weight, sku = sku, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editAlbum:
            '''Редактирует подборку с товарами. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца подборки. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор подборки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "название подборки. строка, обязательный параметр, максимальная длина 128", "type": "str", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии-обложки подборки. \nФотография должна быть загружена с помощью метода photos.getMarkeAlbumUploadServer. См. подробную информацию о загрузке фотографии товаров. положительное число", "type": "int", "default": "None"}, "main_album": {"desc": "назначить подборку основной (1 — назначить, 0 — нет). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id, album_id, title, photo_id : int = None, main_album : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.editAlbum", owner_id = owner_id, album_id = album_id, title = title, photo_id = photo_id, main_album = main_album, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Изменяет текст комментария к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "новый текст комментария (является обязательным, если не задан параметр attachments). \nМаксимальное количество символов: 2048. строка", "type": "str", "default": "None"}, "attachments": {"desc": "новый список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id, comment_id, message : str = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("market.editComment", owner_id = owner_id, comment_id = comment_id, message = message, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editOrder:
            '''Редактирует заказ. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число, обязательный параметр", "type": "int", "default": "None"}, "order_id": {"desc": "идентификатор заказа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "merchant_comment": {"desc": "комментарий продавца. строка, максимальная длина 400", "type": "str", "default": "None"}, "status": {"desc": "статус заказа. Возможные значения: \n\n0 - новый; \n1 - согласуется; \n2 - собирается; \n3 - доставляется; \n4 - выполнен; \n5 - отменен; \n6 - возвращен. \nположительное число", "type": "int", "default": "None"}, "track_number": {"desc": "строка, максимальная длина 60, доступен начиная с версии 5.130", "type": "str", "default": "None"}, "payment_status": {"desc": "строка, доступен начиная с версии 5.130", "type": "str", "default": "None"}, "delivery_price": {"desc": "положительное число, доступен начиная с версии 5.130", "type": "int", "default": "None"}, "width": {"desc": "положительное число, максимальное значение 100000, доступен начиная с версии 5.130", "type": "int", "default": "None"}, "length": {"desc": "положительное число, максимальное значение 100000, доступен начиная с версии 5.130", "type": "int", "default": "None"}, "height": {"desc": "положительное число, максимальное значение 100000, доступен начиная с версии 5.130", "type": "int", "default": "None"}, "weight": {"desc": "положительное число, максимальное значение 100000000, доступен начиная с версии 5.130", "type": "int", "default": "None"}}
            def __call__(self, user_id, order_id, merchant_comment : str = None, status : int = None, track_number : str = None, payment_status : str = None, delivery_price : int = None, width : int = None, length : int = None, height : int = None, weight : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.editOrder", user_id = user_id, order_id = order_id, merchant_comment = merchant_comment, status = status, track_number = track_number, payment_status = payment_status, delivery_price = delivery_price, width = width, length = length, height = height, weight = weight, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список товаров в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товаров. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  обязательный параметр", "type": "not defined", "default": "None"}, "album_id": {"desc": "идентификатор подборки, товары из которой нужно вернуть. по умолчанию 0", "type": "not defined", "default": "0"}, "count": {"desc": "количество возвращаемых товаров. положительное число, максимальное значение 200, по умолчанию 100", "type": "int", "default": "100"}, "offset": {"desc": "смещение относительно первого найденного товара для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos, views_count. По умолчанию эти поля не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id, album_id = None, count : int = None, offset : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.get", owner_id = owner_id, album_id = album_id, count = count, offset = offset, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbumById:
            '''Возвращает данные подборки с товарами. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца подборки. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "album_ids": {"desc": "идентификаторы подборок, данные о которых нужно получить. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owner_id, album_ids, v : str = None, access_token : str = None):
                self.exec_func("market.getAlbumById", owner_id = owner_id, album_ids = album_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbums:
            '''Возвращает список подборок с товарами. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товаров. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первой найденной подборки для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых подборок. положительное число, по умолчанию 50, максимальное значение 100", "type": "int", "default": "50"}}
            def __call__(self, owner_id, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.getAlbums", owner_id = owner_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию о товарах по идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"item_ids": {"desc": "перечисленные через запятую идентификаторы — идущие через знак подчеркивания id владельцев товаров и id самих товаров. Если товар принадлежит сообществу, то в качестве первого параметра используется -id сообщества.\nПример значения item_ids: \n-4363_136089719,13245770_137352259 список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos, views_count. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, item_ids, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.getById", item_ids = item_ids, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getCategories:
            '''Возвращает список категорий для товаров. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("market.getCategories", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список комментариев к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — возвращать информацию о лайках. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_comment_id": {"desc": "идентификатор комментария, начиная с которого нужно вернуть список (подробности см. ниже). положительное число", "type": "int", "default": "None"}, "offset": {"desc": "сдвиг, необходимый для получения конкретной выборки результатов. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "число комментариев, которые необходимо получить. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "sort": {"desc": "порядок сортировки комментариев (asc — от старых к новым, desc - от новых к старым) строка, по умолчанию asc", "type": "str", "default": "asc"}, "extended": {"desc": "1 — комментарии в ответе будут возвращены в виде пронумерованных объектов, дополнительно будут возвращены списки объектов profiles, groups. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes, personal, friend_status, military, career список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id, item_id, need_likes : bool = None, start_comment_id : int = None, offset : int = None, count : int = None, sort : str = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("market.getComments", owner_id = owner_id, item_id = item_id, need_likes = need_likes, start_comment_id = start_comment_id, offset = offset, count = count, sort = sort, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getGroupOrders:
            '''Возвращает заказы сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор или короткое имя сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первого найденного заказа для выборки определенного подмножества. положительное число, по умолчанию 0, минимальное значение 0", "type": "int", "default": "0"}, "count": {"desc": "количество возвращаемых заказов. положительное число, по умолчанию 10, минимальное значение 1, максимальное значение 50", "type": "int", "default": "10"}}
            def __call__(self, group_id, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.getGroupOrders", group_id = group_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOrderById:
            '''Возвращает заказ по идентификатору. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число", "type": "int", "default": "None"}, "order_id": {"desc": "идентификатор заказа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "extended": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, order_id, user_id : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.getOrderById", user_id = user_id, order_id = order_id, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOrderItems:
            '''Возвращает товары в заказе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "id пользователя, который сделал заказ. положительное число, доступен начиная с версии 5.131", "type": "int", "default": "None"}, "order_id": {"desc": "идентификатор заказа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первого найденного товара в заказе для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых товаров в заказе. положительное число, по умолчанию 50, минимальное значение 0", "type": "int", "default": "50"}}
            def __call__(self, order_id, user_id : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.getOrderItems", user_id = user_id, order_id = order_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOrders:
            '''Возвращает заказы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение относительно первого найденного заказа для выборки определенного подмножества. положительное число, по умолчанию 0, минимальное значение 0", "type": "int", "default": "0"}, "count": {"desc": "число заказов, которые необходимо получить. положительное число, по умолчанию 10, минимальное значение 0, максимальное значение 10", "type": "int", "default": "10"}, "extended": {"desc": "1 – вернуть в ответе дополнительное поле groups (array), содержащее список объектов сообществ. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("market.getOrders", offset = offset, count = count, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeFromAlbum:
            '''Удаляет товар из одной или нескольких выбранных подборок. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "album_ids": {"desc": "идентификаторы подборок, из которых нужно удалить товар. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owner_id, item_id, album_ids, v : str = None, access_token : str = None):
                self.exec_func("market.removeFromAlbum", owner_id = owner_id, item_id = item_id, album_ids = album_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderAlbums:
            '''Изменяет положение подборки с товарами в списке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца альбома. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор подборки. целое число, обязательный параметр", "type": "int", "default": "None"}, "before": {"desc": "идентификатор подборки, перед которой следует поместить текущую. положительное число", "type": "int", "default": "None"}, "after": {"desc": "идентификатор подборки, после которой следует поместить текущую. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, album_id, before : int = None, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.reorderAlbums", owner_id = owner_id, album_id = album_id, before = before, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderItems:
            '''Изменяет положение товара в подборке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор подборки, в которой находится товар.  0 — для сортировки общего списка товаров. целое число", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "before": {"desc": "идентификатор товара, перед которым следует поместить текущий. положительное число", "type": "int", "default": "None"}, "after": {"desc": "идентификатор товара, после которого следует поместить текущий. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, item_id, album_id : int = None, before : int = None, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.reorderItems", owner_id = owner_id, album_id = album_id, item_id = item_id, before = before, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class report:
            '''Позволяет отправить жалобу на товар. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товаров. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, item_id, reason, v : str = None, access_token : str = None):
                self.exec_func("market.report", owner_id = owner_id, item_id = item_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reportComment:
            '''Позволяет оставить жалобу на комментарий к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, reason, v : str = None, access_token : str = None):
                self.exec_func("market.reportComment", owner_id = owner_id, comment_id = comment_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Восстанавливает удаленный товар. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "идентификатор товара. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, item_id, v : str = None, access_token : str = None):
                self.exec_func("market.restore", owner_id = owner_id, item_id = item_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удаленный комментарий к товару. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца товара. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор удаленного комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, v : str = None, access_token : str = None):
                self.exec_func("market.restoreComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Ищет товары в каталоге сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества, которому принадлежат товары. целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор подборки, товары из которой нужно вернуть. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "q": {"desc": "строка поискового запроса. Например, зеленые тапочки. строка", "type": "str", "default": "None"}, "price_from": {"desc": "минимальное значение цены товаров в сотых долях единицы валюты. Например, 100000. положительное число", "type": "int", "default": "None"}, "price_to": {"desc": "максимальное значение цены товаров  в сотых долях единицы валюты. Например, 1410000. положительное число", "type": "int", "default": "None"}, "sort": {"desc": "вид сортировки.  0 — пользовательская расстановка,  1 — по дате добавления товара, 2 — по цене, 3 — по популярности. целое число, по умолчанию 0", "type": "int", "default": "0"}, "rev": {"desc": "0 — не использовать обратный порядок, 1 — использовать обратный порядок. положительное число, по умолчанию 1", "type": "int", "default": "1"}, "offset": {"desc": "смещение относительно первого найденного товара для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых товаров. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, can_comment, can_repost, photos, views_count. По умолчанию эти поля не возвращается. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}, "status": {"desc": "положительное число, по умолчанию 0", "type": "int", "default": "0"}}
            def __call__(self, owner_id, album_id : int = None, q : str = None, price_from : int = None, price_to : int = None, sort : int = None, rev : int = None, offset : int = None, count : int = None, extended : bool = None, status : int = None, v : str = None, access_token : str = None):
                self.exec_func("market.search", owner_id = owner_id, album_id = album_id, q = q, price_from = price_from, price_to = price_to, sort = sort, rev = rev, offset = offset, count = count, extended = extended, status = status, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class messages:
        def  __init__(self, exec_func):
            self.addChatUser = self.addChatUser(exec_func)
            self.allowMessagesFromGroup = self.allowMessagesFromGroup(exec_func)
            self.createChat = self.createChat(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteChatPhoto = self.deleteChatPhoto(exec_func)
            self.deleteConversation = self.deleteConversation(exec_func)
            self.denyMessagesFromGroup = self.denyMessagesFromGroup(exec_func)
            self.edit = self.edit(exec_func)
            self.editChat = self.editChat(exec_func)
            self.getByConversationMessageId = self.getByConversationMessageId(exec_func)
            self.getById = self.getById(exec_func)
            self.getChat = self.getChat(exec_func)
            self.getChatPreview = self.getChatPreview(exec_func)
            self.getConversationMembers = self.getConversationMembers(exec_func)
            self.getConversations = self.getConversations(exec_func)
            self.getConversationsById = self.getConversationsById(exec_func)
            self.getHistory = self.getHistory(exec_func)
            self.getHistoryAttachments = self.getHistoryAttachments(exec_func)
            self.getImportantMessages = self.getImportantMessages(exec_func)
            self.getInviteLink = self.getInviteLink(exec_func)
            self.getLastActivity = self.getLastActivity(exec_func)
            self.getLongPollHistory = self.getLongPollHistory(exec_func)
            self.getLongPollServer = self.getLongPollServer(exec_func)
            self.isMessagesFromGroupAllowed = self.isMessagesFromGroupAllowed(exec_func)
            self.joinChatByInviteLink = self.joinChatByInviteLink(exec_func)
            self.markAsAnsweredConversation = self.markAsAnsweredConversation(exec_func)
            self.markAsImportant = self.markAsImportant(exec_func)
            self.markAsImportantConversation = self.markAsImportantConversation(exec_func)
            self.markAsRead = self.markAsRead(exec_func)
            self.pin = self.pin(exec_func)
            self.removeChatUser = self.removeChatUser(exec_func)
            self.restore = self.restore(exec_func)
            self.search = self.search(exec_func)
            self.searchConversations = self.searchConversations(exec_func)
            self.send = self.send(exec_func)
            self.sendMessageEventAnswer = self.sendMessageEventAnswer(exec_func)
            self.setActivity = self.setActivity(exec_func)
            self.setChatPhoto = self.setChatPhoto(exec_func)
            self.unpin = self.unpin(exec_func)
        class addChatUser:
            '''Добавляет в мультидиалог нового пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы. положительное число, обязательный параметр, максимальное значение 100000000", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, которого необходимо включить в беседу. положительное число", "type": "int", "default": "None"}, "visible_messages_count": {"desc": "положительное число, максимальное значение 1000", "type": "int", "default": "None"}}
            def __call__(self, chat_id, user_id : int = None, visible_messages_count : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.addChatUser", chat_id = chat_id, user_id = user_id, visible_messages_count = visible_messages_count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class allowMessagesFromGroup:
            '''Позволяет разрешить отправку сообщений от сообщества текущему пользователю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "key": {"desc": "произвольная строка. Этот параметр можно использовать для идентификации пользователя. Его значение будет возвращено в событии message_allow Callback API. строка, максимальная длина 256", "type": "str", "default": "None"}}
            def __call__(self, group_id, key : str = None, v : str = None, access_token : str = None):
                self.exec_func("messages.allowMessagesFromGroup", group_id = group_id, key = key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createChat:
            '''Создаёт беседу с несколькими участниками. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "идентификаторы пользователей, которых нужно включить в мультидиалог. Должны быть в друзьях у текущего пользователя. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "title": {"desc": "название беседы. строка", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_ids : str = None, title : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.createChat", user_ids = user_ids, title = title, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"message_ids": {"desc": "список идентификаторов сообщений, разделённых через запятую. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "spam": {"desc": "пометить сообщения как спам. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "delete_for_all": {"desc": "1 — если сообщение нужно удалить для получателей (если с момента отправки сообщения прошло не более 24 часов ). флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, message_ids : str = None, spam : bool = None, group_id : int = None, delete_for_all : bool = None, v : str = None, access_token : str = None):
                self.exec_func("messages.delete", message_ids = message_ids, spam = spam, group_id = group_id, delete_for_all = delete_for_all, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteChatPhoto:
            '''Позволяет удалить фотографию мультидиалога. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы. положительное число, обязательный параметр, максимальное значение 100000000", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, chat_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.deleteChatPhoto", chat_id = chat_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteConversation:
            '''Удаляет беседу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. Если требуется очистить историю беседы, используйте peer_id. строка", "type": "str", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. \nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, доступен начиная с версии 5.38", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "offset": {"desc": "начиная с какого сообщения нужно удалить переписку. (По умолчанию удаляются все сообщения начиная с первого). положительное число, по умолчанию 0, устаревший параметр, доступен только для версий меньше 5.100", "type": "int", "default": "0"}, "count": {"desc": "сколько сообщений нужно удалить. Обратите внимание, что на метод наложено ограничение, за один вызов нельзя удалить больше 10000 сообщений, поэтому если сообщений в переписке больше — метод нужно вызывать несколько раз. положительное число, максимальное значение 10000, устаревший параметр, доступен только для версий меньше 5.100", "type": "int", "default": "None"}}
            def __call__(self, user_id : str = None, peer_id : int = None, group_id : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.deleteConversation", user_id = user_id, peer_id = peer_id, group_id = group_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class denyMessagesFromGroup:
            '''Позволяет запретить отправку сообщений от сообщества текущему пользователю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("messages.denyMessagesFromGroup", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст  сообщения. Обязательный параметр, если не задан параметр attachment. строка", "type": "str", "default": "None"}, "lat": {"desc": "географическая широта (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота (от -180 до 180). дробное число", "type": "int", "default": "None"}, "attachment": {"desc": "медиавложения к личному сообщению, перечисленные через запятую. Каждое прикрепление представлено в формате:\n<type><owner_id>_<media_id>\n\n<type> — тип медиавложения: \n\nphoto — фотография; \nvideo — видеозапись; \naudio — аудиозапись; \ndoc — документ; \nwall — запись на стене; \nmarket — товар. \n\n\n\n<owner_id> — идентификатор владельца медиавложения (обратите внимание, если объект находится в сообществе, этот параметр должен быть отрицательным).\n<media_id> — идентификатор медиавложения.\n\nНапример:\nphoto100172_166443618\n\nПараметр является обязательным, если не задан параметр message. \nВ случае, если прикрепляется объект, принадлежащий другому пользователю следует добавлять к вложению его access_key в формате <type><owner_id>_<media_id>_<access_key>, Например: video85635407_165186811_69dff3de4372ae9b6e строка", "type": "str", "default": "None"}, "keep_forward_messages": {"desc": "1, чтобы сохранить прикреплённые пересланные сообщения. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "keep_snippets": {"desc": "1, чтобы сохранить прикреплённые внешние ссылки (сниппеты). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "dont_parse_links": {"desc": "1 — не создавать сниппет ссылки из сообщения флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "message_id": {"desc": "идентификатор сообщения. положительное число", "type": "int", "default": "None"}, "conversation_message_id": {"desc": "идентификатор сообщения в беседе. положительное число", "type": "int", "default": "None"}, "template": {"desc": "объект, описывающий шаблоны сообщений. ", "type": "not defined", "default": "None"}, "keyboard": {"desc": "объект, описывающий клавиатуру бота. ", "type": "not defined", "default": "None"}}
            def __call__(self, peer_id, message : str = None, lat : int = None, long : int = None, attachment : str = None, keep_forward_messages : bool = None, keep_snippets : bool = None, group_id : int = None, dont_parse_links : bool = None, message_id : int = None, conversation_message_id : int = None, template = None, keyboard = None, v : str = None, access_token : str = None):
                self.exec_func("messages.edit", peer_id = peer_id, message = message, lat = lat, long = long, attachment = attachment, keep_forward_messages = keep_forward_messages, keep_snippets = keep_snippets, group_id = group_id, dont_parse_links = dont_parse_links, message_id = message_id, conversation_message_id = conversation_message_id, template = template, keyboard = keyboard, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editChat:
            '''Изменяет название беседы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы. положительное число, обязательный параметр, максимальное значение 100000000", "type": "int", "default": "None"}, "title": {"desc": "новое название для беседы. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, chat_id, title, v : str = None, access_token : str = None):
                self.exec_func("messages.editChat", chat_id = chat_id, title = title, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getByConversationMessageId:
            '''Возвращает сообщения по их идентификаторам в рамках беседы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "2000000000 + id беседы (недоступно с ключом сообщества) целое число, обязательный параметр", "type": "int", "default": "None"}, "conversation_message_ids": {"desc": "идентификаторы сообщений. Максимум 100 идентификаторов. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительные поля. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, conversation_message_ids, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getByConversationMessageId", peer_id = peer_id, conversation_message_ids = conversation_message_ids, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает сообщения по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"message_ids": {"desc": "идентификаторы сообщений. Максимум 100 идентификаторов. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "preview_length": {"desc": "количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы не хотите обрезать сообщение. (по умолчанию сообщения не обрезаются). положительное число, по умолчанию 0", "type": "int", "default": "0"}, "extended": {"desc": "1 — возвращать дополнительные поля. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для пользователей и сообществ. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, message_ids, preview_length : int = None, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getById", message_ids = message_ids, preview_length = preview_length, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getChat:
            '''Возвращает информацию о беседе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы. положительное число, максимальное значение 100000000", "type": "int", "default": "None"}, "chat_ids": {"desc": "список идентификаторов бесед. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. \nДоступные значения: nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: \n\nnom — именительный; \ngen — родительный; \ndat — дательный; \nacc — винительный; \nins — творительный; \nabl — предложный. \nПо умолчанию: nom. строка", "type": "str", "default": "None"}}
            def __call__(self, chat_id : int = None, chat_ids : str = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getChat", chat_id = chat_id, chat_ids = chat_ids, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getChatPreview:
            '''Получает данные для превью чата с приглашением по ссылке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "положительное число", "type": "int", "default": "None"}, "link": {"desc": "ссылка-приглашение. строка", "type": "str", "default": "None"}, "fields": {"desc": "список полей профилей, данные о которых нужно получить. Полный список смотрите на этой странице. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, peer_id : int = None, link : str = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getChatPreview", peer_id = peer_id, link = link, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getConversationMembers:
            '''Позволяет получить список участников беседы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n обязательный параметр", "type": "not defined", "default": "None"}, "fields": {"desc": "дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getConversationMembers", peer_id = peer_id, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getConversations:
            '''Возвращает список бесед пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определенного подмножества результатов. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "максимальное число результатов, которые нужно получить. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "filter": {"desc": "фильтр. Возможные значения: \n\nall — все беседы; \nunread — беседы с непрочитанными сообщениями; \nimportant — беседы, помеченные как важные (только для сообщений сообществ); \nunanswered — беседы, помеченные как неотвеченные (только для сообщений сообществ). \n \nПо умолчанию: all. строка, по умолчанию all", "type": "str", "default": "all"}, "extended": {"desc": "1 — возвращать дополнительные поля для пользователей и сообществ. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_message_id": {"desc": "идентификатор сообщения, начиная с которого нужно возвращать беседы. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей для пользователей и сообществ. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). ", "type": "not defined", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, filter : str = None, extended : bool = None, start_message_id : int = None, fields : str = None, group_id = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getConversations", offset = offset, count = count, filter = filter, extended = extended, start_message_id = start_message_id, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getConversationsById:
            '''Позволяет получить беседу по её идентификатору. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_ids": {"desc": "идентификаторы назначений, разделённые запятой. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n \nМаксимум – 100 идентификаторов. список целых чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительные поля. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_ids, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getConversationsById", peer_ids = peer_ids, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getHistory:
            '''Возвращает историю сообщений для указанного диалога. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для выборки определенного подмножества сообщений, должен быть >= 0, если не передан параметр start_message_id, и должен быть <= 0, если передан. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество сообщений, которое необходимо получить (но не более 200). положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "user_id": {"desc": "идентификатор пользователя, историю переписки с которым необходимо вернуть. строка", "type": "str", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. (недоступно для вызовов от имени сообщества) \n\nДля сообщества: \n-id сообщества. \n целое число, доступен начиная с версии 5.38", "type": "int", "default": "None"}, "start_message_id": {"desc": "если значение > 0, то это идентификатор сообщения, начиная с которого нужно вернуть историю переписки, если передано значение 0 то вернутся сообщения с самого начала переписки, если же передано значение -1, то к значению параметра offset прибавляется количество входящих непрочитанных сообщений в конце диалога (подробности см. ниже) целое число", "type": "int", "default": "None"}, "rev": {"desc": "1 – возвращать сообщения в хронологическом порядке. 0 – возвращать сообщения в обратном хронологическом порядке (по умолчанию). целое число", "type": "int", "default": "None"}, "extended": {"desc": "Если указать в качестве этого параметра 1, то будет возвращена информация о пользователях, являющихся авторами сообщений. По умолчанию 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, user_id : str = None, peer_id : int = None, start_message_id : int = None, rev : int = None, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getHistory", offset = offset, count = count, user_id = user_id, peer_id = peer_id, start_message_id = start_message_id, rev = rev, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getHistoryAttachments:
            '''Возвращает материалы диалога или беседы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. Для групповой беседы: \n2000000000 + id беседы. \n\nДля пользователя: \nid пользователя. \n\nДля сообщества: \n-id сообщества. \n целое число, обязательный параметр", "type": "int", "default": "None"}, "media_type": {"desc": "тип материалов, который необходимо вернуть. \nДоступные значения: \n\nphoto — фотографии; \nvideo — видеозаписи; \naudio — аудиозаписи; \ndoc — документы; \nlink — ссылки; \nmarket — товары; \nwall — записи; \nshare — ссылки, товары и записи. \n\nОбратите внимание — существует ограничение по дате отправки вложений. Так, для получения доступны вложения типов photo,video,audio,doc , отправленные не ранее 25.03.2013, link — не ранее 20.05.13, market,wall — 01.02.2016. строка, по умолчанию photo", "type": "str", "default": "photo"}, "start_from": {"desc": "смещение, необходимое для выборки определенного подмножества объектов. строка", "type": "str", "default": "None"}, "count": {"desc": "количество объектов, которое необходимо получить (но не более 200). положительное число, максимальное значение 200, по умолчанию 30", "type": "int", "default": "30"}, "photo_sizes": {"desc": "параметр, указывающий нужно ли возвращать ли доступные размеры фотографии в специальном формате. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "дополнительные поля профилей пользователей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "preserve_order": {"desc": "параметр, указывающий нужно ли возвращать вложения в оригинальном порядке. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "max_forwards_level": {"desc": "максимальная глубина вложенности пересланных сообщений. положительное число, максимальное значение 45, по умолчанию 45", "type": "int", "default": "45"}}
            def __call__(self, peer_id, media_type : str = None, start_from : str = None, count : int = None, photo_sizes : bool = None, fields : str = None, group_id : int = None, preserve_order : bool = None, max_forwards_level : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getHistoryAttachments", peer_id = peer_id, media_type = media_type, start_from = start_from, count = count, photo_sizes = photo_sizes, fields = fields, group_id = group_id, preserve_order = preserve_order, max_forwards_level = max_forwards_level, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getImportantMessages:
            '''Возвращает список важных сообщений пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "максимальное число результатов, которые нужно получить. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества результатов. положительное число", "type": "int", "default": "None"}, "start_message_id": {"desc": "идентификатор сообщения, начиная с которого нужно возвращать список. положительное число", "type": "int", "default": "None"}, "preview_length": {"desc": "положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей для пользователей и сообществ. список слов, разделенных через запятую", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительные поля для пользователей и сообществ. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, count : int = None, offset : int = None, start_message_id : int = None, preview_length : int = None, fields : str = None, extended : bool = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getImportantMessages", count = count, offset = offset, start_message_id = start_message_id, preview_length = preview_length, fields = fields, extended = extended, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getInviteLink:
            '''Получает ссылку для приглашения пользователя в беседу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. \nДля групповой беседы: \n2000000000 + id беседы. \n положительное число, обязательный параметр", "type": "int", "default": "None"}, "reset": {"desc": "1 — сгенерировать новую ссылку, сбросив предыдущую. 0 — получить предыдущую ссылку. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "group_id": {"desc": "положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, reset : bool = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getInviteLink", peer_id = peer_id, reset = reset, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLastActivity:
            '''Возвращает текущий статус и дату последней активности указанного пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, информацию о последней активности которого требуется получить. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, user_id, v : str = None, access_token : str = None):
                self.exec_func("messages.getLastActivity", user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLongPollHistory:
            '''Возвращает обновления в личных сообщениях пользователя.
'''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"ts": {"desc": "последнее значение параметра ts, полученное от Long Poll сервера или с помощью метода messages.getLongPollServer положительное число", "type": "int", "default": "None"}, "pts": {"desc": "последнее значение параметра new_pts, полученное от Long Poll сервера, используется для получения действий, которые хранятся всегда. положительное число", "type": "int", "default": "None"}, "preview_length": {"desc": "количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы не хотите обрезать сообщение. (по умолчанию сообщения не обрезаются). положительное число", "type": "int", "default": "None"}, "onlines": {"desc": "1 — возвращать в числе прочих события 8 и 9 (пользователь стал онлайн/оффлайн). Учитывается только при использовании ts. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, photo_id, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation, activities, interests, music, movies, tv, books, games, about, quotes, personal, friend_status, military, career список слов, разделенных через запятую, по умолчанию photo,photo_medium_rec,sex,online,screen_name", "type": "str", "default": "photo"}, "events_limit": {"desc": "лимит по количеству всех событий в истории. Обратите внимание, параметры events_limit и msgs_limit применяются совместно. Число результатов в ответе ограничивается первым достигнутым лимитом. положительное число, по умолчанию 1000, минимальное значение 1000", "type": "int", "default": "1000"}, "msgs_limit": {"desc": "лимит по количеству событий с сообщениями в истории. Обратите внимание, параметры events_limit и msgs_limit применяются совместно. Число результатов в ответе ограничивается первым достигнутым лимитом. положительное число, по умолчанию 200, минимальное значение 200", "type": "int", "default": "200"}, "max_msg_id": {"desc": "максимальный идентификатор сообщения среди уже имеющихся в локальной копии. Необходимо учитывать как сообщения, полученные через методы API (например messages.getDialogs, messages.getHistory), так и данные, полученные из Long Poll сервера (события с кодом 4). положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "lp_version": {"desc": "версия Long Poll. положительное число", "type": "int", "default": "None"}, "last_n": {"desc": "положительное число, по умолчанию 0, максимальное значение 2000", "type": "int", "default": "0"}, "credentials": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, ts : int = None, pts : int = None, preview_length : int = None, onlines : bool = None, fields : str = None, events_limit : int = None, msgs_limit : int = None, max_msg_id : int = None, group_id : int = None, lp_version : int = None, last_n : int = None, credentials : bool = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getLongPollHistory", ts = ts, pts = pts, preview_length = preview_length, onlines = onlines, fields = fields, events_limit = events_limit, msgs_limit = msgs_limit, max_msg_id = max_msg_id, group_id = group_id, lp_version = lp_version, last_n = last_n, credentials = credentials, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLongPollServer:
            '''Возвращает данные, необходимые для подключения к Long Poll серверу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"need_pts": {"desc": "1 — возвращать поле pts, необходимое для работы метода messages.getLongPollHistory флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "lp_version": {"desc": "версия для подключения к Long Poll. Актуальная версия: 3. \nПодробную информацию об изменениях в версиях Вы найдёте на этой странице. положительное число, по умолчанию 0, доступен начиная с версии 5.65", "type": "int", "default": "0"}}
            def __call__(self, need_pts : bool = None, group_id : int = None, lp_version : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.getLongPollServer", need_pts = need_pts, group_id = group_id, lp_version = lp_version, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class isMessagesFromGroupAllowed:
            '''Возвращает информацию о том, разрешена ли отправка сообщений от сообщества пользователю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, user_id, v : str = None, access_token : str = None):
                self.exec_func("messages.isMessagesFromGroupAllowed", group_id = group_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class joinChatByInviteLink:
            '''Позволяет присоединиться к чату по ссылке-приглашению. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"link": {"desc": "ссылка-приглашение. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, link, v : str = None, access_token : str = None):
                self.exec_func("messages.joinChatByInviteLink", link = link, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markAsAnsweredConversation:
            '''Помечает беседу как отвеченную либо снимает отметку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор беседы целое число, обязательный параметр", "type": "int", "default": "None"}, "answered": {"desc": "1 - беседа отмечена отвеченной, 0 - неотвеченной флаг, может принимать значения 1 или 0, по умолчанию 1", "type": "bool", "default": "1"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, answered : bool = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.markAsAnsweredConversation", peer_id = peer_id, answered = answered, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markAsImportant:
            '''Помечает сообщения как важные либо снимает отметку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"message_ids": {"desc": "список идентификаторов сообщений, которые необходимо пометить. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "important": {"desc": "1, если сообщения необходимо пометить, как важные; \n0, если необходимо снять пометку. положительное число", "type": "int", "default": "None"}}
            def __call__(self, message_ids : str = None, important : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.markAsImportant", message_ids = message_ids, important = important, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markAsImportantConversation:
            '''Помечает беседу как важную либо снимает отметку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор беседы целое число, обязательный параметр", "type": "int", "default": "None"}, "important": {"desc": "1, если сообщения необходимо пометить, как важные; \n0, если необходимо снять пометку. флаг, может принимать значения 1 или 0, по умолчанию 1", "type": "bool", "default": "1"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, important : bool = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.markAsImportantConversation", peer_id = peer_id, important = important, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markAsRead:
            '''Помечает сообщения как прочитанные. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"message_ids": {"desc": "идентификаторы сообщений. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n строка", "type": "str", "default": "None"}, "start_message_id": {"desc": "при передаче этого параметра будут помечены как прочитанные все сообщения, начиная с данного. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "mark_conversation_as_read": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, message_ids : str = None, peer_id : str = None, start_message_id : int = None, group_id : int = None, mark_conversation_as_read : bool = None, v : str = None, access_token : str = None):
                self.exec_func("messages.markAsRead", message_ids = message_ids, peer_id = peer_id, start_message_id = start_message_id, group_id = group_id, mark_conversation_as_read = mark_conversation_as_read, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class pin:
            '''Закрепляет сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, обязательный параметр", "type": "int", "default": "None"}, "message_id": {"desc": "идентификатор сообщения, которое нужно закрепить. положительное число", "type": "int", "default": "None"}, "conversation_message_id": {"desc": "идентификатор сообщения беседы, которое нужно закрепить. \nПараметр предназначен для закрепления исходящего сообщения бота в беседах. положительное число, доступен начиная с версии 5.124", "type": "int", "default": "None"}}
            def __call__(self, peer_id, message_id : int = None, conversation_message_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.pin", peer_id = peer_id, message_id = message_id, conversation_message_id = conversation_message_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeChatUser:
            '''Исключает из мультидиалога пользователя, если текущий пользователь или сообщество является администратором беседы либо текущий пользователь пригласил исключаемого пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы. положительное число, обязательный параметр, максимальное значение 100000000", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, которого необходимо исключить из беседы. ", "type": "not defined", "default": "None"}, "member_id": {"desc": "идентификатор участника, которого необходимо исключить из беседы. Для сообществ — идентификатор сообщества со знаком «минус». доступен начиная с версии 5.81", "type": "not defined", "default": "None"}}
            def __call__(self, chat_id, user_id = None, member_id = None, v : str = None, access_token : str = None):
                self.exec_func("messages.removeChatUser", chat_id = chat_id, user_id = user_id, member_id = member_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Восстанавливает удаленное сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"message_id": {"desc": "идентификатор сообщения, которое нужно восстановить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, message_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.restore", message_id = message_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает список найденных личных сообщений текущего пользователя по введенной строке поиска. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "подстрока, по которой будет производиться поиск. строка", "type": "str", "default": "None"}, "peer_id": {"desc": "фильтр по идентификатору назначения для поиска по отдельному диалогу. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число", "type": "int", "default": "None"}, "date": {"desc": "дата в формате DDMMYYYY — если параметр задан, в ответе будут только сообщения, отправленные до указанной даты. положительное число", "type": "int", "default": "None"}, "preview_length": {"desc": "количество символов, по которому нужно обрезать сообщение. Укажите 0, если Вы не хотите обрезать сообщение. (по умолчанию сообщения не обрезаются). положительное число, по умолчанию 0", "type": "int", "default": "0"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества сообщений из списка найденных. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество сообщений, которое необходимо получить. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "extended": {"desc": "1 — возвращать дополнительные поля для пользователей и сообществ. В ответе будет содержаться массив объектов бесед. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для пользователей и сообществ. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, q : str = None, peer_id : int = None, date : int = None, preview_length : int = None, offset : int = None, count : int = None, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.search", q = q, peer_id = peer_id, date = date, preview_length = preview_length, offset = offset, count = count, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class searchConversations:
            '''Позволяет искать диалоги. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "поисковой запрос. строка", "type": "str", "default": "None"}, "count": {"desc": "максимальное число результатов для получения. положительное число, по умолчанию 20, минимальное значение 1, максимальное значение 255", "type": "int", "default": "20"}, "extended": {"desc": "1 — возвращать дополнительные поля. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "дополнительные поля пользователей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, q : str = None, count : int = None, extended : bool = None, fields : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.searchConversations", q = q, count = count, extended = extended, fields = fields, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class send:
            '''Отправляет сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, которому отправляется сообщение. целое число", "type": "int", "default": "None"}, "random_id": {"desc": "уникальный (в привязке к API_ID и ID отправителя) идентификатор, предназначенный для предотвращения повторной отправки одинакового сообщения. Сохраняется вместе с сообщением и доступен в истории сообщений. \nЗаданный random_id используется для проверки уникальности за всю историю сообщений, поэтому используйте большой диапазон (до int32). целое число, доступен начиная с версии 5.45", "type": "int", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, доступен начиная с версии 5.38", "type": "int", "default": "None"}, "peer_ids": {"desc": "идентификаторы получателей сообщения (при необходимости отправить сообщение сразу нескольким пользователям). Доступно только для ключа доступа сообщества. Максимальное количество идентификаторов: 100. список целых чисел, разделенных запятыми, доступен начиная с версии 5.81", "type": "str", "default": "None"}, "domain": {"desc": "короткий адрес пользователя (например, illarionov). строка", "type": "str", "default": "None"}, "chat_id": {"desc": "идентификатор беседы, к которой будет относиться сообщение. положительное число, максимальное значение 100000000", "type": "int", "default": "None"}, "message": {"desc": "текст личного сообщения. Обязательный параметр, если не задан параметр attachment. строка", "type": "str", "default": "None"}, "lat": {"desc": "географическая широта (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота (от -180 до 180). дробное число", "type": "int", "default": "None"}, "attachment": {"desc": "медиавложения к личному сообщению, перечисленные через запятую. Каждое прикрепление представлено в формате:\n<type><owner_id>_<media_id>\n\n<type> — тип медиавложения: \n\nphoto — фотография; \nvideo — видеозапись; \naudio — аудиозапись; \ndoc — документ; \nwall — запись на стене; \nmarket — товар. \npoll — опрос. \n\n\n\n<owner_id> — идентификатор владельца медиавложения (обратите внимание, если объект находится в сообществе, этот параметр должен быть отрицательным).\n<media_id> — идентификатор медиавложения.\n\nНапример:\nphoto100172_166443618\n\nПараметр является обязательным, если не задан параметр message. \nВ случае, если прикрепляется объект, принадлежащий другому пользователю следует добавлять к вложению его access_key в формате <type><owner_id>_<media_id>_<access_key>, Например: video85635407_165186811_69dff3de4372ae9b6e строка", "type": "str", "default": "None"}, "reply_to": {"desc": "идентификатор сообщения, на которое требуется ответить. целое число, доступен начиная с версии 5.92", "type": "int", "default": "None"}, "forward_messages": {"desc": "идентификаторы пересылаемых сообщений, перечисленные через запятую. Перечисленные сообщения отправителя будут отображаться в теле письма у получателя. Не более 100 значений на верхнем уровне, максимальный уровень вложенности: 45, максимальное количество пересылаемых сообщений 500\n\nНапример:\n123,431,544 список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "forward": {"desc": "JSON-объект со следующими полями: \n\nowner_id —  владелец сообщений. Стоит передавать, если вы хотите переслать сообщения из сообщества в диалог; \npeer_id —  идентификатор места, из которого необходимо переслать сообщения; \nconversation_message_ids  — массив conversation_message_id сообщений, которые необходимо переслать. В массив conversation_message_ids можно передать сообщения: \n\nнаходящиеся в личном диалоге с ботом; \nявляющиеся исходящими сообщениями бота; \nнаписанными после того, как бот вступил в беседу и появился доступ к сообщениям. \n\nmessage_ids — массив id сообщений; \nis_reply —  ответ на сообщения. Стоит передавать, если вы хотите ответить на сообщения в том чате, в котором находятся сообщения.  При этом в conversation_message_ids/message_ids должен находиться только один элемент. \n", "type": "str", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "keyboard": {"desc": "объект, описывающий клавиатуру бота. ", "type": "not defined", "default": "None"}, "template": {"desc": "объект, описывающий шаблон сообщения. ", "type": "not defined", "default": "None"}, "payload": {"desc": "полезная нагрузка. максимальная длина 1000", "type": "not defined", "default": "None"}, "content_source": {"desc": "объект, описывающий источник пользовательского контента для чат-ботов. ", "type": "not defined", "default": "None"}, "dont_parse_links": {"desc": "1 — не создавать сниппет ссылки из сообщения. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "disable_mentions": {"desc": "1 - отключить уведомление об упоминании в сообщении. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "intent": {"desc": "строка, описывающая интенты. строка, по умолчанию default", "type": "str", "default": "default"}, "subscribe_id": {"desc": "число, которое в будущем будет предназначено для работы с интентами. положительное число, максимальное значение 100", "type": "int", "default": "None"}, "user_ids": {"desc": "идентификаторы получателей сообщения (при необходимости отправить сообщение сразу нескольким пользователям). Доступно только для ключа доступа сообщества. Максимальное количество идентификаторов: 100. список целых чисел, разделенных запятыми, устаревший параметр, доступен только для версий меньше 5.138", "type": "str", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового сообщения. целое число, устаревший параметр, доступен только для версий меньше 5.46", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, random_id : int = None, peer_id : int = None, peer_ids : str = None, domain : str = None, chat_id : int = None, message : str = None, lat : int = None, long : int = None, attachment : str = None, reply_to : int = None, forward_messages : str = None, forward : str = None, sticker_id : int = None, group_id : int = None, keyboard = None, template = None, payload = None, content_source = None, dont_parse_links : bool = None, disable_mentions : bool = None, intent : str = None, subscribe_id : int = None, user_ids : str = None, guid : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.send", user_id = user_id, random_id = random_id, peer_id = peer_id, peer_ids = peer_ids, domain = domain, chat_id = chat_id, message = message, lat = lat, long = long, attachment = attachment, reply_to = reply_to, forward_messages = forward_messages, forward = forward, sticker_id = sticker_id, group_id = group_id, keyboard = keyboard, template = template, payload = payload, content_source = content_source, dont_parse_links = dont_parse_links, disable_mentions = disable_mentions, intent = intent, subscribe_id = subscribe_id, user_ids = user_ids, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class sendMessageEventAnswer:
            '''Отправляет событие с действием, которое произойдет при нажатии на callback-кнопку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"event_id": {"desc": "случайная строка, которая возвращается в событии message_event строка, обязательный параметр", "type": "str", "default": "None"}, "user_id": {"desc": "идентификатор пользователя. целое число, обязательный параметр", "type": "int", "default": "None"}, "peer_id": {"desc": "идентификатор диалога со стороны сообщества. целое число, обязательный параметр", "type": "int", "default": "None"}, "event_data": {"desc": "объект действия, которое должно произойти после нажатия на кнопку. максимальная длина 1000", "type": "not defined", "default": "None"}}
            def __call__(self, event_id, user_id, peer_id, event_data = None, v : str = None, access_token : str = None):
                self.exec_func("messages.sendMessageEventAnswer", event_id = event_id, user_id = user_id, peer_id = peer_id, event_data = event_data, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setActivity:
            '''Изменяет статус набора текста пользователем в диалоге. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. строка", "type": "str", "default": "None"}, "type": {"desc": "typing — пользователь начал набирать текст, \naudiomessage — пользователь записывает голосовое сообщение строка", "type": "str", "default": "None"}, "peer_id": {"desc": "идентификатор назначения. \nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, доступен начиная с версии 5.38", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : str = None, type : str = None, peer_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.setActivity", user_id = user_id, type = type, peer_id = peer_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setChatPhoto:
            '''Позволяет установить фотографию мультидиалога, загруженную с помощью метода photos.getChatUploadServer. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"file": {"desc": "Содержимое поля response из ответа специального upload сервера, полученного в результате загрузки изображения на адрес, полученный методом photos.getChatUploadServer. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, file, v : str = None, access_token : str = None):
                self.exec_func("messages.setChatPhoto", file = file, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unpin:
            '''Открепляет сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения. \nДля пользователя: \nid  пользователя. \n\nДля групповой беседы: \n2000000000 + id беседы. \n\nДля сообщества: \n-id сообщества. \n целое число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества (для сообщений сообщества с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}}
            def __call__(self, peer_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("messages.unpin", peer_id = peer_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class newsfeed:
        def  __init__(self, exec_func):
            self.addBan = self.addBan(exec_func)
            self.deleteBan = self.deleteBan(exec_func)
            self.deleteList = self.deleteList(exec_func)
            self.get = self.get(exec_func)
            self.getBanned = self.getBanned(exec_func)
            self.getComments = self.getComments(exec_func)
            self.getLists = self.getLists(exec_func)
            self.getMentions = self.getMentions(exec_func)
            self.getRecommended = self.getRecommended(exec_func)
            self.getSuggestedSources = self.getSuggestedSources(exec_func)
            self.ignoreItem = self.ignoreItem(exec_func)
            self.saveList = self.saveList(exec_func)
            self.search = self.search(exec_func)
            self.unignoreItem = self.unignoreItem(exec_func)
            self.unsubscribe = self.unsubscribe(exec_func)
        class addBan:
            '''Запрещает показывать новости от заданных пользователей и групп в ленте новостей текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "перечисленные через запятую идентификаторы друзей пользователя, новости от которых необходимо скрыть из ленты новостей текущего пользователя. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "group_ids": {"desc": "перечисленные через запятую идентификаторы групп пользователя, новости от которых необходимо скрыть из ленты новостей текущего пользователя. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, user_ids : str = None, group_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.addBan", user_ids = user_ids, group_ids = group_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteBan:
            '''Разрешает показывать новости от заданных пользователей и групп в ленте новостей текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "идентификаторы пользователей, новости от которых необходимо вернуть в ленту. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "group_ids": {"desc": "идентификаторы сообществ, новости от которых необходимо вернуть в ленту. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}}
            def __call__(self, user_ids : str = None, group_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.deleteBan", user_ids = user_ids, group_ids = group_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteList:
            '''Метод позволяет удалить пользовательский список новостей '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"list_id": {"desc": "числовой идентификатор списка положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, list_id, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.deleteList", list_id = list_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает данные, необходимые для показа списка новостей для текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"filters": {"desc": "перечисленные через запятую названия списков новостей, которые необходимо получить. В данный момент поддерживаются следующие списки новостей: \n\npost — новые записи со стен; \nphoto — новые фотографии; \nphoto_tag — новые отметки на фотографиях; \nwall_photo — новые фотографии на стенах; \nfriend — новые друзья; \nnote — новые заметки; \naudio — записи сообществ и друзей, содержащие аудиозаписи, а также новые аудиозаписи, добавленные ими; \nvideo — новые видеозаписи. \n\nЕсли параметр не задан, то будут получены все возможные списки новостей. список слов, разделенных через запятую", "type": "str", "default": "None"}, "return_banned": {"desc": "1 - включить в выдачу также скрытых из новостей пользователей. 0 - не возвращать скрытых пользователей. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_time": {"desc": "время в формате unixtime, начиная с которого следует получить новости для текущего пользователя. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате unixtime, до которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным текущему времени. положительное число", "type": "int", "default": "None"}, "max_photos": {"desc": "Максимальное количество фотографий, информацию о которых необходимо вернуть. По умолчанию: 5, максимальное значение: 100. положительное число", "type": "int", "default": "None"}, "source_ids": {"desc": "перечисленные через запятую иcточники новостей, новости от которых необходимо получить.\n\nИдентификаторы пользователей можно указывать в форматах\n<uid> или u<uid>\nгде <uid> — идентификатор друга пользователя.\n\nИдентификаторы сообществ можно указывать в форматах\n-<gid> или g<gid>\nгде <gid> — идентификатор сообщества. \nПомимо этого параметр может принимать строковые значения: \n\nfriends - список друзей пользователя \ngroups - список групп, на которые подписан текущий пользователь \npages - список публичных страниц, на который подписан тeкущий пользователь \nfollowing - список пользователей, на которых подписан текущий пользователь \nlist{идентификатор списка новостей} - список новостей. Вы можете найти все списки новостей пользователя используя метод newsfeed.getLists \n\nЕсли параметр не задан, то считается, что он включает список всех друзей и групп пользователя, за исключением скрытых источников, которые можно получить методом newsfeed.getBanned. \nМаксимальное число символов — 5000. строка", "type": "str", "default": "None"}, "start_from": {"desc": "Идентификатор, необходимый для получения следующей страницы результатов. Значение, необходимое для передачи в этом параметре, возвращается в поле ответа next_from. строка, доступен начиная с версии 5.13", "type": "str", "default": "None"}, "count": {"desc": "указывает, какое максимальное число новостей следует возвращать, но не более 100. По умолчанию 50. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и  групп, которые необходимо вернуть. См. описание полей объекта user и описание полей объекта group. список слов, разделенных через запятую", "type": "str", "default": "None"}, "section": {"desc": "строка", "type": "str", "default": "None"}, "from_": {"desc": "значение, полученное в поле new_from при последней загрузке новостей. Помогает избавляться от дубликатов при реализации автоподгрузки. строка, устаревший параметр, доступен только для версий меньше 5.13", "type": "str", "default": "None"}, "offset": {"desc": "указывает, начиная с какого элемента в данном промежутке времени необходимо получить новости. По умолчанию 0. Для автоподгрузки Вы можете использовать возвращаемый данным методом параметр new_offset. целое число, устаревший параметр, доступен только для версий меньше 5.13", "type": "int", "default": "None"}}
            def __call__(self, filters : str = None, return_banned : bool = None, start_time : int = None, end_time : int = None, max_photos : int = None, source_ids : str = None, start_from : str = None, count : int = None, fields : str = None, section : str = None, from_ : str = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.get", filters = filters, return_banned = return_banned, start_time = start_time, end_time = end_time, max_photos = max_photos, source_ids = source_ids, start_from = start_from, count = count, fields = fields, section = section, from_ = from_, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getBanned:
            '''Возвращает список пользователей и групп, которые текущий пользователь скрыл из ленты новостей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"extended": {"desc": "если этот параметр равен 1, возвращается дополнительная информация о пользователях и группах флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, extended : bool = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getBanned", extended = extended, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает данные, необходимые для показа раздела комментариев в новостях пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "указывает, какое максимальное число новостей следует возвращать, но не более 100. По умолчанию 30. Для автоподгрузки Вы можете использовать возвращаемый данным методом параметр new_offset. положительное число, по умолчанию 30, максимальное значение 100", "type": "int", "default": "30"}, "filters": {"desc": "перечисленные через запятую типы объектов, изменения комментариев к которым нужно вернуть. В данный момент поддерживаются следующие списки новостей:\n\n\npost — новые комментарии к записям со стен; \nphoto — новые комментарии к фотографиям; \nvideo — новые комментарии к видеозаписям; \ntopic — новые сообщения в обсуждениях; \nmarket — новые комментарии к товарам; \nnote — новые комментарии к заметкам.\nЕсли параметр не задан, то будут получены все возможные списки новостей. список слов, разделенных через запятую", "type": "str", "default": "None"}, "reposts": {"desc": "Идентификатор объекта, комментарии к репостам которого необходимо вернуть, например wall1_45486. Если указан данный параметр, параметр filters указывать необязательно. строка", "type": "str", "default": "None"}, "start_time": {"desc": "время в формате unixtime, начиная с которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным значению времени, которое было сутки назад. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате unixtime, до которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным текущему времени. положительное число", "type": "int", "default": "None"}, "last_comments_count": {"desc": "количество комментариев к записям, которые нужно получить. положительное число, доступен начиная с версии 5.23, по умолчанию 0, максимальное значение 10", "type": "int", "default": "0"}, "start_from": {"desc": "Идентификатор, необходимый для получения следующей страницы результатов. Значение, необходимое для передачи в этом параметре, возвращается в поле ответа next_from. строка, доступен начиная с версии 5.13", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_": {"desc": "значение, полученное в поле new_from при последней загрузке новостей. Помогает избавляться от дубликатов при реализации автоподгрузки. строка, устаревший параметр, доступен только для версий меньше 5.13", "type": "str", "default": "None"}, "last_comments": {"desc": "1 - возвращать последние комментарии к записям. 0 - не возвращать последние комментарии. флаг, может принимать значения 1 или 0, устаревший параметр, доступен только для версий меньше 5.23", "type": "bool", "default": "None"}}
            def __call__(self, count : int = None, filters : str = None, reposts : str = None, start_time : int = None, end_time : int = None, last_comments_count : int = None, start_from : str = None, fields : str = None, from_ : str = None, last_comments : bool = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getComments", count = count, filters = filters, reposts = reposts, start_time = start_time, end_time = end_time, last_comments_count = last_comments_count, start_from = start_from, fields = fields, from_ = from_, last_comments = last_comments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLists:
            '''Возвращает пользовательские списки новостей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"list_ids": {"desc": "идентификаторы списков. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "extended": {"desc": "1 — вернуть дополнительную информацию о списке (значения source_ids и no_reposts). флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, list_ids : str = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getLists", list_ids = list_ids, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMentions:
            '''Возвращает список записей пользователей на своих стенах, в которых упоминается указанный пользователь. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "start_time": {"desc": "время в формате unixtime начиная с которого следует получать упоминания о пользователе. \nЕсли параметр не задан, то будут возвращены все упоминания о пользователе, если не задан параметр end_time, в противном случае упоминания с учетом параметра end_time. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время, в формате unixtime, до которого следует получать упоминания о пользователе. \nЕсли параметр не задан, то будут возвращены все упоминания о пользователе, если не задан параметр start_time, в противном случае упоминания с учетом параметра start_time. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества новостей. По умолчанию 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых записей. Если параметр не задан, то считается, что он равен 20. Максимальное значение параметра 50. положительное число, по умолчанию 20, максимальное значение 50", "type": "int", "default": "20"}}
            def __call__(self, owner_id : int = None, start_time : int = None, end_time : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getMentions", owner_id = owner_id, start_time = start_time, end_time = end_time, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getRecommended:
            '''Получает список новостей, рекомендованных пользователю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"start_time": {"desc": "время в формате unixtime, начиная с которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным значению времени, которое было сутки назад. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате unixtime, до которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным текущему времени. положительное число", "type": "int", "default": "None"}, "max_photos": {"desc": "Максимальное количество фотографий, информацию о которых необходимо вернуть. По умолчанию 5. положительное число", "type": "int", "default": "None"}, "start_from": {"desc": "Идентификатор, необходимый для получения следующей страницы результатов. Значение, необходимое для передачи в этом параметре, возвращается в поле ответа next_from. строка, доступен начиная с версии 5.13", "type": "str", "default": "None"}, "count": {"desc": "указывает, какое максимальное число новостей следует возвращать, но не более 100. По умолчанию 50. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_": {"desc": "значение, полученное в поле new_from при последней загрузке новостей. Помогает избавляться от дубликатов при реализации автоподгрузки. строка, устаревший параметр, доступен только для версий меньше 5.13", "type": "str", "default": "None"}, "offset": {"desc": "указывает, начиная с какого элемента в данном промежутке времени необходимо получить новости. По умолчанию 0. Для автоподгрузки Вы можете использовать возвращаемый данным методом параметр new_offset. целое число, устаревший параметр, доступен только для версий меньше 5.13", "type": "int", "default": "None"}}
            def __call__(self, start_time : int = None, end_time : int = None, max_photos : int = None, start_from : str = None, count : int = None, fields : str = None, from_ : str = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getRecommended", start_time = start_time, end_time = end_time, max_photos = max_photos, start_from = start_from, count = count, fields = fields, from_ = from_, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSuggestedSources:
            '''Возвращает сообщества и пользователей, на которые текущему пользователю рекомендуется подписаться. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "отступ, необходимый для выборки определенного подмножества сообществ или пользователей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество сообществ или пользователей, которое необходимо вернуть. положительное число, максимальное значение 1000, по умолчанию 20", "type": "int", "default": "20"}, "shuffle": {"desc": "перемешивать ли возвращаемый список. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей, которые необходимо вернуть. См. возможные поля для пользователей и сообществ. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, offset : int = None, count : int = None, shuffle : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.getSuggestedSources", offset = offset, count = count, shuffle = shuffle, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class ignoreItem:
            '''Позволяет скрыть объект из ленты новостей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "Тип объекта. Возможные значения: \n\nwall — запись на стене; \ntag — отметка на фотографии; \nprofilephoto — фотография профиля; \nvideo — видеозапись; \nphoto — фотография; \naudio — аудиозапись. \nстрока, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "Идентификатор владельца объекта (пользователь или сообщество). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию 0", "type": "int", "default": "0"}, "item_id": {"desc": "Идентификатор объекта. положительное число, по умолчанию 0", "type": "int", "default": "0"}}
            def __call__(self, type, owner_id : int = None, item_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.ignoreItem", type = type, owner_id = owner_id, item_id = item_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveList:
            '''Метод позволяет создавать или редактировать пользовательские списки для просмотра новостей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"list_id": {"desc": "числовой идентификатор списка (если не передан, будет назначен автоматически). положительное число", "type": "int", "default": "None"}, "title": {"desc": "название списка. строка, обязательный параметр", "type": "str", "default": "None"}, "source_ids": {"desc": "идентификаторы пользователей и сообществ, которые должны быть включены в список. Идентификаторы сообществ нужно указывать со знаком «минус». список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "no_reposts": {"desc": "нужно ли отображать копии постов в списке (1 — не нужно). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, title, list_id : int = None, source_ids : str = None, no_reposts : bool = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.saveList", list_id = list_id, title = title, source_ids = source_ids, no_reposts = no_reposts, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает результаты поиска по статусам. Новости возвращаются в порядке от более новых к более старым. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "поисковой запрос, например, \"New Year\". строка", "type": "str", "default": "None"}, "extended": {"desc": "1, если необходимо получить информацию о пользователе или сообществе, разместившем запись. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "count": {"desc": "указывает, какое максимальное число записей следует возвращать. Обратите внимание — даже при использовании параметра offset для получения информации доступны только первые 1000 результатов. \n положительное число, по умолчанию 30, максимальное значение 200", "type": "int", "default": "30"}, "latitude": {"desc": "географическая широта точки, в радиусе от которой необходимо производить поиск, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота точки, в радиусе от которой необходимо производить поиск, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "start_time": {"desc": "время в формате unixtime, начиная с которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным значению времени, которое было сутки назад. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате unixtime, до которого следует получить новости для текущего пользователя. Если параметр не задан, то он считается равным текущему времени. положительное число", "type": "int", "default": "None"}, "start_from": {"desc": "Идентификатор, необходимый для получения следующей страницы результатов. Значение, необходимое для передачи в этом параметре, возвращается в поле ответа next_from. строка, доступен начиная с версии 5.13", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и  групп, которые необходимо вернуть. См. описание полей объекта user и описание полей объекта group. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}, "start_id": {"desc": "строковый идентификатор последней полученной записи. (Возвращается в результатах запроса (new_from) для того, чтобы исключить из выборки нового запроса уже полученные записи). строка, устаревший параметр, доступен только для версий меньше 5.13", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества результатов поиска. положительное число, устаревший параметр, доступен только для версий меньше 5.13", "type": "int", "default": "None"}}
            def __call__(self, q : str = None, extended : bool = None, count : int = None, latitude : int = None, longitude : int = None, start_time : int = None, end_time : int = None, start_from : str = None, fields : str = None, start_id : str = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.search", q = q, extended = extended, count = count, latitude = latitude, longitude = longitude, start_time = start_time, end_time = end_time, start_from = start_from, fields = fields, start_id = start_id, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unignoreItem:
            '''Позволяет вернуть ранее скрытый объект в ленту новостей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "Тип объекта. Возможные значения: \n\nwall — запись на стене; \ntag — отметка на фотографии; \nprofilephoto — фотография профиля; \nvideo — видеозапись; \nphoto — фотография; \naudio — аудиозапись. \nстрока, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "Идентификатор владельца объекта (пользователь или сообщество). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "item_id": {"desc": "Идентификатор объекта. положительное число, обязательный параметр", "type": "int", "default": "None"}, "track_code": {"desc": "строка", "type": "str", "default": "None"}}
            def __call__(self, type, owner_id, item_id, track_code : str = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.unignoreItem", type = type, owner_id = owner_id, item_id = item_id, track_code = track_code, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unsubscribe:
            '''Отписывает текущего пользователя от комментариев к заданному объекту. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип объекта, от комментариев к которому необходимо отписаться. \nВозможные типы:\npost — запись на стене пользователя или группы;\nphoto — фотография;\nvideo — видеозапись;\ntopic — обсуждение;\nnote — заметка;\nmarket — товар. строка, обязательный параметр", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца объекта. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "item_id": {"desc": "идентификатор объекта. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, type, item_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("newsfeed.unsubscribe", type = type, owner_id = owner_id, item_id = item_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class notes:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.createComment = self.createComment(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.edit = self.edit(exec_func)
            self.editComment = self.editComment(exec_func)
            self.get = self.get(exec_func)
            self.getById = self.getById(exec_func)
            self.getComments = self.getComments(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
        class add:
            '''Создает новую заметку у текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"title": {"desc": "заголовок заметки. строка, обязательный параметр", "type": "str", "default": "None"}, "text": {"desc": "текст заметки. строка, обязательный параметр", "type": "str", "default": "None"}, "privacy_view": {"desc": "настройки приватности просмотра заметки в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "privacy_comment": {"desc": "настройки приватности комментирования заметки в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "privacy": {"desc": "уровень доступа к заметке. Возможные значения: \n0 — все пользователи, 1 — только друзья, 2 — друзья и друзья друзей, 3 — только пользователь. целое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}, "comment_privacy": {"desc": "уровень доступа к комментированию заметки. Возможные значения: \n0 — все пользователи, 1 — только друзья, 2 — друзья и друзья друзей, 3 — только пользователь. целое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}}
            def __call__(self, title, text, privacy_view : str = None, privacy_comment : str = None, privacy : int = None, comment_privacy : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.add", title = title, text = text, privacy_view = privacy_view, privacy_comment = privacy_comment, privacy = privacy, comment_privacy = comment_privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Добавляет новый комментарий к заметке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_id": {"desc": "идентификатор заметки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "reply_to": {"desc": "идентификатор пользователя, ответом на комментарий которого является добавляемый комментарий (не передаётся, если комментарий не является ответом). положительное число", "type": "int", "default": "None"}, "message": {"desc": "текст комментария. строка, обязательный параметр", "type": "str", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, note_id, message, owner_id : int = None, reply_to : int = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("notes.createComment", note_id = note_id, owner_id = owner_id, reply_to = reply_to, message = message, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет заметку текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_id": {"desc": "идентификатор заметки. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, note_id, v : str = None, access_token : str = None):
                self.exec_func("notes.delete", note_id = note_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет комментарий к заметке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.deleteComment", comment_id = comment_id, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует заметку текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_id": {"desc": "идентификатор заметки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "заголовок заметки. строка, обязательный параметр", "type": "str", "default": "None"}, "text": {"desc": "текст заметки. строка, обязательный параметр", "type": "str", "default": "None"}, "privacy_view": {"desc": "настройки приватности просмотра заметки в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "privacy_comment": {"desc": "настройки приватности комментирования заметки в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "privacy": {"desc": "уровень доступа к заметке. Возможные значения: \n0 — все пользователи, 1 — только друзья, 2 — друзья и друзья друзей, 3 — только пользователь. целое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}, "comment_privacy": {"desc": "уровень доступа к комментированию заметки. Возможные значения: \n0 — все пользователи, 1 — только друзья, 2 — друзья и друзья друзей, 3 — только пользователь. целое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}}
            def __call__(self, note_id, title, text, privacy_view : str = None, privacy_comment : str = None, privacy : int = None, comment_privacy : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.edit", note_id = note_id, title = title, text = text, privacy_view = privacy_view, privacy_comment = privacy_comment, privacy = privacy, comment_privacy = comment_privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Редактирует указанный комментарий у заметки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "message": {"desc": "новый текст комментария. строка, минимальная длина 2", "type": "str", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, message : str = None, v : str = None, access_token : str = None):
                self.exec_func("notes.editComment", comment_id = comment_id, owner_id = owner_id, message = message, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список заметок, созданных пользователем. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_ids": {"desc": "идентификаторы заметок, информацию о которых необходимо получить. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, информацию о заметках которого требуется получить. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества заметок. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество заметок, информацию о которых необходимо получить. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "sort": {"desc": "сортировка результатов (0 — по дате создания в порядке убывания, 1 - по дате создания в порядке возрастания). положительное число, по умолчанию 0", "type": "int", "default": "0"}}
            def __call__(self, note_ids : str = None, user_id : int = None, offset : int = None, count : int = None, sort : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.get", note_ids = note_ids, user_id = user_id, offset = offset, count = count, sort = sort, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает заметку по её id. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_id": {"desc": "идентификатор заметки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "need_wiki": {"desc": "определяет, требуется ли в ответе wiki-представление заметки (работает, только если запрашиваются заметки текущего пользователя). флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, note_id, owner_id : int = None, need_wiki : bool = None, v : str = None, access_token : str = None):
                self.exec_func("notes.getById", note_id = note_id, owner_id = owner_id, need_wiki = need_wiki, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список комментариев к заметке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"note_id": {"desc": "идентификатор заметки. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "sort": {"desc": "сортировка результатов (0 — по дате добавления в порядке возрастания, 1 — по дате добавления в порядке убывания). положительное число, по умолчанию 0", "type": "int", "default": "0"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества комментариев. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество комментариев, которое необходимо получить. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}}
            def __call__(self, note_id, owner_id : int = None, sort : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.getComments", note_id = note_id, owner_id = owner_id, sort = sort, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удалённый комментарий. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"comment_id": {"desc": "идентификатор удаленного комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца заметки. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("notes.restoreComment", comment_id = comment_id, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class notifications:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
            self.markAsViewed = self.markAsViewed(exec_func)
            self.sendMessage = self.sendMessage(exec_func)
        class get:
            '''Возвращает список оповещений об ответах других пользователей на записи текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "указывает, какое максимальное число оповещений следует возвращать. положительное число, по умолчанию 30, максимальное значение 100, минимальное значение 1", "type": "int", "default": "30"}, "start_from": {"desc": "строковый идентификатор оповещения, полученного последним в предыдущем вызове (см. описание поля next_from в результате). строка, доступен начиная с версии 5.27", "type": "str", "default": "None"}, "filters": {"desc": "перечисленные через запятую типы оповещений, которые необходимо получить. Возможные значения: \n\nwall — записи на стене пользователя; \nmentions — упоминания в записях на стене, в комментариях или в обсуждениях; \ncomments — комментарии к записям на стене, фотографиям и видеозаписям; \nlikes — отметки «Мне нравится»; \nreposts — скопированные у текущего пользователя записи на стене, фотографии и видеозаписи; \nfollowers — новые подписчики; \nfriends — принятые заявки в друзья. \nЕсли параметр не задан, то будут получены все возможные типы оповещений. список слов, разделенных через запятую", "type": "str", "default": "None"}, "start_time": {"desc": "время в формате Unixtime, начиная с которого следует получить оповещения для текущего пользователя. Если параметр не задан, то он считается равным значению времени, которое было сутки назад. целое число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате Unixtime, до которого следует получить оповещения для текущего пользователя. Если параметр не задан, то он считается равным текущему времени. целое число", "type": "int", "default": "None"}, "from_": {"desc": "строковый идентификатор последнего полученного предыдущим вызовом метода оповещения (см. описание поля new_from в результате). строка, устаревший параметр, доступен только для версий меньше 5.27", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для получения определенного подмножества оповещений. положительное число, устаревший параметр, доступен только для версий меньше 5.27", "type": "int", "default": "None"}}
            def __call__(self, count : int = None, start_from : str = None, filters : str = None, start_time : int = None, end_time : int = None, from_ : str = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("notifications.get", count = count, start_from = start_from, filters = filters, start_time = start_time, end_time = end_time, from_ = from_, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class markAsViewed:
            '''Сбрасывает счетчик непросмотренных оповещений об ответах других пользователей на записи текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("notifications.markAsViewed", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class sendMessage:
            '''Отправляет уведомление пользователю приложения VK Apps. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "список идентификаторов пользователей, которым нужно отправить уведомление (максимум 100 идентификаторов). список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "message": {"desc": "текст уведомления. строка, обязательный параметр, максимальная длина 254", "type": "str", "default": "None"}, "fragment": {"desc": "содержимое хэша (часть URL в ссылке на приложение вида https://vk.com/app123456#fragment). строка, максимальная длина 2047", "type": "str", "default": "None"}, "group_id": {"desc": "положительное число", "type": "int", "default": "None"}, "random_id": {"desc": "уникальный (в привязке к API_ID и ID отправителя) идентификатор, предназначенный для предотвращения повторной отправки одинакового сообщения. \nЗаданный random_id используется для проверки уникальности уведомления в течение часа после отправки. целое число, доступен начиная с версии 5.107", "type": "int", "default": "None"}}
            def __call__(self, user_ids, message, fragment : str = None, group_id : int = None, random_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("notifications.sendMessage", user_ids = user_ids, message = message, fragment = fragment, group_id = group_id, random_id = random_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class pages:
        def  __init__(self, exec_func):
            self.clearCache = self.clearCache(exec_func)
            self.get = self.get(exec_func)
            self.getHistory = self.getHistory(exec_func)
            self.getTitles = self.getTitles(exec_func)
            self.getVersion = self.getVersion(exec_func)
            self.parseWiki = self.parseWiki(exec_func)
            self.save = self.save(exec_func)
            self.saveAccess = self.saveAccess(exec_func)
        class clearCache:
            '''Позволяет очистить кеш отдельных внешних страниц, которые могут быть прикреплены к записям ВКонтакте. После очистки кеша при последующем прикреплении ссылки к записи, данные о странице будут обновлены. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"url": {"desc": "Адрес страницы, закешированную версию которой необходимо очистить строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, url, v : str = None, access_token : str = None):
                self.exec_func("pages.clearCache", url = url, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает информацию о вики-странице. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца вики-страницы. целое число", "type": "int", "default": "None"}, "page_id": {"desc": "идентификатор вики-страницы. целое число", "type": "int", "default": "None"}, "global_": {"desc": "1 — требуется получить информацию о глобальной вики-странице. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "site_preview": {"desc": "1 — получаемая wiki страница является предпросмотром для прикрепленной ссылки. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "title": {"desc": "название страницы. строка", "type": "str", "default": "None"}, "need_source": {"desc": "1 —  требуется вернуть содержимое страницы в вики-формате. флаг, может принимать значения 1 или 0, доступен начиная с версии 5.20", "type": "bool", "default": "None"}, "need_html": {"desc": "1 —  требуется вернуть html-представление страницы. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id : int = None, page_id : int = None, global_ : bool = None, site_preview : bool = None, title : str = None, need_source : bool = None, need_html : bool = None, v : str = None, access_token : str = None):
                self.exec_func("pages.get", owner_id = owner_id, page_id = page_id, global_ = global_, site_preview = site_preview, title = title, need_source = need_source, need_html = need_html, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getHistory:
            '''Возвращает список всех старых версий вики-страницы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"page_id": {"desc": "идентификатор вики-страницы. целое число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому принадлежит вики-страница. целое число", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, создавшего вики-страницу. целое число", "type": "int", "default": "None"}}
            def __call__(self, page_id, group_id : int = None, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("pages.getHistory", page_id = page_id, group_id = group_id, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTitles:
            '''Возвращает список вики-страниц в группе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, которому принадлежит вики-страница. целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("pages.getTitles", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getVersion:
            '''Возвращает текст одной из старых версий страницы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"version_id": {"desc": "идентификатор версии. целое число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому принадлежит вики-страница. целое число", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, который создал страницу. целое число", "type": "int", "default": "None"}, "need_html": {"desc": "определяет, требуется ли в ответе html-представление вики-страницы. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, version_id, group_id : int = None, user_id : int = None, need_html : bool = None, v : str = None, access_token : str = None):
                self.exec_func("pages.getVersion", version_id = version_id, group_id = group_id, user_id = user_id, need_html = need_html, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class parseWiki:
            '''Возвращает html-представление вики-разметки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"text": {"desc": "текст в вики-формате. строка, обязательный параметр", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор группы, в контексте которой интерпретируется данная страница. положительное число", "type": "int", "default": "None"}}
            def __call__(self, text, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("pages.parseWiki", text = text, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class save:
            '''Сохраняет текст вики-страницы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"text": {"desc": "новый текст страницы в вики-формате. строка", "type": "str", "default": "None"}, "page_id": {"desc": "идентификатор вики-страницы. Вместо page_id может быть передан параметр title. целое число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому принадлежит вики-страница. целое число", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, создавшего вики-страницу. целое число", "type": "int", "default": "None"}, "title": {"desc": "название вики-страницы. строка", "type": "str", "default": "None"}}
            def __call__(self, text : str = None, page_id : int = None, group_id : int = None, user_id : int = None, title : str = None, v : str = None, access_token : str = None):
                self.exec_func("pages.save", text = text, page_id = page_id, group_id = group_id, user_id = user_id, title = title, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveAccess:
            '''Сохраняет новые настройки доступа на чтение и редактирование вики-страницы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"page_id": {"desc": "идентификатор вики-страницы. целое число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому принадлежит вики-страница. целое число", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, создавшего вики-страницу. целое число", "type": "int", "default": "None"}, "view": {"desc": "значение настройки доступа на чтение. Возможные значения: \n\n2 — просматривать страницу могут все; \n1 — только участники сообщества; \n0 — только руководители сообщества. \nцелое число", "type": "int", "default": "None"}, "edit": {"desc": "значение настройки доступа на редактирование. Возможные значения: \n\n2 — редактировать страницу могут все; \n1 — только участники сообщества; \n0 — только руководители сообщества. \nцелое число", "type": "int", "default": "None"}}
            def __call__(self, page_id, group_id : int = None, user_id : int = None, view : int = None, edit : int = None, v : str = None, access_token : str = None):
                self.exec_func("pages.saveAccess", page_id = page_id, group_id = group_id, user_id = user_id, view = view, edit = edit, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class photos:
        def  __init__(self, exec_func):
            self.confirmTag = self.confirmTag(exec_func)
            self.copy = self.copy(exec_func)
            self.createAlbum = self.createAlbum(exec_func)
            self.createComment = self.createComment(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteAlbum = self.deleteAlbum(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.edit = self.edit(exec_func)
            self.editAlbum = self.editAlbum(exec_func)
            self.editComment = self.editComment(exec_func)
            self.get = self.get(exec_func)
            self.getAlbums = self.getAlbums(exec_func)
            self.getAlbumsCount = self.getAlbumsCount(exec_func)
            self.getAll = self.getAll(exec_func)
            self.getAllComments = self.getAllComments(exec_func)
            self.getById = self.getById(exec_func)
            self.getChatUploadServer = self.getChatUploadServer(exec_func)
            self.getComments = self.getComments(exec_func)
            self.getMarketAlbumUploadServer = self.getMarketAlbumUploadServer(exec_func)
            self.getMarketUploadServer = self.getMarketUploadServer(exec_func)
            self.getMessagesUploadServer = self.getMessagesUploadServer(exec_func)
            self.getNewTags = self.getNewTags(exec_func)
            self.getOwnerCoverPhotoUploadServer = self.getOwnerCoverPhotoUploadServer(exec_func)
            self.getOwnerPhotoUploadServer = self.getOwnerPhotoUploadServer(exec_func)
            self.getTags = self.getTags(exec_func)
            self.getUploadServer = self.getUploadServer(exec_func)
            self.getUserPhotos = self.getUserPhotos(exec_func)
            self.getWallUploadServer = self.getWallUploadServer(exec_func)
            self.makeCover = self.makeCover(exec_func)
            self.move = self.move(exec_func)
            self.putTag = self.putTag(exec_func)
            self.removeTag = self.removeTag(exec_func)
            self.reorderAlbums = self.reorderAlbums(exec_func)
            self.reorderPhotos = self.reorderPhotos(exec_func)
            self.report = self.report(exec_func)
            self.reportComment = self.reportComment(exec_func)
            self.restore = self.restore(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
            self.save = self.save(exec_func)
            self.saveMarketAlbumPhoto = self.saveMarketAlbumPhoto(exec_func)
            self.saveMarketPhoto = self.saveMarketPhoto(exec_func)
            self.saveMessagesPhoto = self.saveMessagesPhoto(exec_func)
            self.saveOwnerCoverPhoto = self.saveOwnerCoverPhoto(exec_func)
            self.saveOwnerPhoto = self.saveOwnerPhoto(exec_func)
            self.saveWallPhoto = self.saveWallPhoto(exec_func)
            self.search = self.search(exec_func)
        class confirmTag:
            '''Подтверждает отметку на фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. обязательный параметр", "type": "not defined", "default": "None"}, "tag_id": {"desc": "идентификатор отметки на фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, photo_id, tag_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.confirmTag", owner_id = owner_id, photo_id = photo_id, tag_id = tag_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class copy:
            '''Позволяет скопировать фотографию в альбом "Сохраненные фотографии" '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца фотографии целое число, обязательный параметр", "type": "int", "default": "None"}, "photo_id": {"desc": "индентификатор фотографии положительное число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "специальный код доступа для приватных фотографий строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, photo_id, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.copy", owner_id = owner_id, photo_id = photo_id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createAlbum:
            '''Создает пустой альбом для фотографий. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"title": {"desc": "название альбома. строка, обязательный параметр, минимальная длина 2", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в котором создаётся альбом. целое число", "type": "int", "default": "None"}, "description": {"desc": "текст описания альбома. строка", "type": "str", "default": "None"}, "privacy_view": {"desc": "настройки приватности просмотра альбома в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "privacy_comment": {"desc": "настройки приватности комментирования альбома в специальном формате. список слов, разделенных через запятую, по умолчанию all, доступен начиная с версии 5.30", "type": "str", "default": "all"}, "upload_by_admins_only": {"desc": "кто может загружать фотографии в альбом (только для альбома сообщества). \nВозможные значения: \n\n0 — фотографии могут добавлять все пользователи; \n1 — фотографии могут добавлять только редакторы и администраторы. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "comments_disabled": {"desc": "отключено ли комментирование альбома (только для альбома сообщества). \nВозможные значения: \n\n0 — комментирование включено; \n1 — комментирование отключено. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "privacy": {"desc": "уровень доступа к альбому (только для альбома пользователя). \nВозможные значения: \n\n0 — все пользователи, \n1 — только друзья, \n2 — друзья и друзья друзей, \n3 — только я. \nцелое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}, "comment_privacy": {"desc": "уровень доступа к комментированию альбома (только для альбома пользователя). \nВозможные значения: \n\n0 — все пользователи, \n1 — только друзья, \n2 — друзья и друзья друзей, \n3 — только я. \nцелое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}}
            def __call__(self, title, group_id : int = None, description : str = None, privacy_view : str = None, privacy_comment : str = None, upload_by_admins_only : bool = None, comments_disabled : bool = None, privacy : int = None, comment_privacy : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.createAlbum", title = title, group_id = group_id, description = description, privacy_view = privacy_view, privacy_comment = privacy_comment, upload_by_admins_only = upload_by_admins_only, comments_disabled = comments_disabled, privacy = privacy, comment_privacy = comment_privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Создает новый комментарий к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст комментария (является обязательным, если не задан параметр attachments). \nМаксимальное количество символов: 2048. строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_group": {"desc": "Данный параметр учитывается, если owner_id < 0 (комментарий к фотографии группы). Возможные значения: \n\n1 — комментарий будет опубликован от имени группы; \n0 — комментарий будет опубликован от имени пользователя. \nПо умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "reply_to_comment": {"desc": "идентификатор комментария, в ответ на который нужно оставить текущий. целое число", "type": "int", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера, который нужно прикрепить к комментарию. положительное число", "type": "int", "default": "None"}, "access_key": {"desc": "ключ доступа. строка", "type": "str", "default": "None"}, "guid": {"desc": "уникальное значение для предотвращения повторной отправки одного и того же комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, message : str = None, attachments : str = None, from_group : bool = None, reply_to_comment : int = None, sticker_id : int = None, access_key : str = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.createComment", owner_id = owner_id, photo_id = photo_id, message = message, attachments = attachments, from_group = from_group, reply_to_comment = reply_to_comment, sticker_id = sticker_id, access_key = access_key, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаление фотографии на сайте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.delete", owner_id = owner_id, photo_id = photo_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteAlbum:
            '''Удаляет указанный альбом для фотографий у текущего пользователя '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"album_id": {"desc": "идентификатор альбома. положительное число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в котором размещен альбом. положительное число", "type": "int", "default": "None"}}
            def __call__(self, album_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.deleteAlbum", album_id = album_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет комментарий к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.deleteComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует описание или геометку у фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. положительное число, обязательный параметр", "type": "int", "default": "None"}, "caption": {"desc": "новый текст описания к фотографии. Если параметр не задан, то считается, что он равен пустой строке. строка", "type": "str", "default": "None"}, "latitude": {"desc": "географическая широта. дробное число", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота. дробное число", "type": "int", "default": "None"}, "place_str": {"desc": "название места. строка", "type": "str", "default": "None"}, "foursquare_id": {"desc": "id в Foursquare. строка", "type": "str", "default": "None"}, "delete_place": {"desc": "удалить место (0 — не удалять, 1 — удалить). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, caption : str = None, latitude : int = None, longitude : int = None, place_str : str = None, foursquare_id : str = None, delete_place : bool = None, v : str = None, access_token : str = None):
                self.exec_func("photos.edit", owner_id = owner_id, photo_id = photo_id, caption = caption, latitude = latitude, longitude = longitude, place_str = place_str, foursquare_id = foursquare_id, delete_place = delete_place, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editAlbum:
            '''Редактирует данные альбома для фотографий. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"album_id": {"desc": "идентификатор альбома. целое число, положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "новое название альбома. строка", "type": "str", "default": "None"}, "description": {"desc": "новый текст описания альбома. строка", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца альбома (пользователь или сообщество). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "privacy_view": {"desc": "настройки приватности просмотра альбома в специальном формате. список слов, разделенных через запятую, доступен начиная с версии 5.30", "type": "str", "default": "None"}, "privacy_comment": {"desc": "настройки приватности комментирования альбома в специальном формате. список слов, разделенных через запятую, доступен начиная с версии 5.30", "type": "str", "default": "None"}, "upload_by_admins_only": {"desc": "кто может загружать фотографии в альбом (только для альбома сообщества). \nВозможные значения: \n\n0 — фотографии могут добавлять все пользователи; \n1 — фотографии могут добавлять только редакторы и администраторы. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "comments_disabled": {"desc": "отключено ли комментирование альбома (только для альбома сообщества). \nВозможные значения: \n\n0 — комментирование включено; \n1 — комментирование отключено. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "privacy": {"desc": "новый уровень доступа к альбому (только для альбома пользователя). \nВозможные значения: \n\n0 — все пользователи, \n1 — только друзья, \n2 — друзья и друзья друзей, \n3 — только я. \nцелое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}, "comment_privacy": {"desc": "новый уровень доступа к комментированию альбома (только для альбома пользователя). \nВозможные значения: \n\n0 — все пользователи, \n1 — только друзья, \n2 — друзья и друзья друзей, \n3 — только я. \nцелое число, устаревший параметр, доступен только для версий меньше 5.30", "type": "int", "default": "None"}}
            def __call__(self, album_id, title : str = None, description : str = None, owner_id : int = None, privacy_view : str = None, privacy_comment : str = None, upload_by_admins_only : bool = None, comments_disabled : bool = None, privacy : int = None, comment_privacy : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.editAlbum", album_id = album_id, title = title, description = description, owner_id = owner_id, privacy_view = privacy_view, privacy_comment = privacy_comment, upload_by_admins_only = upload_by_admins_only, comments_disabled = comments_disabled, privacy = privacy, comment_privacy = comment_privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Изменяет текст комментария к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "новый текст комментария. Обязательный параметр, если не задан параметр attachments. \nМаксимальное количество символов: 2048. строка", "type": "str", "default": "None"}, "attachments": {"desc": "новый список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, message : str = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.editComment", owner_id = owner_id, comment_id = comment_id, message = message, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список фотографий в альбоме. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца альбома. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома. Для служебных альбомов используются следующие идентификаторы: \n\nwall — фотографии со стены; \nprofile — фотографии профиля; \nsaved — сохраненные фотографии. Возвращается только с ключом доступа пользователя. \nстрока", "type": "str", "default": "None"}, "photo_ids": {"desc": "идентификаторы фотографий, информацию о которых необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}, "rev": {"desc": "порядок сортировки фотографий. Возможные значения: \n\n1 — антихронологический; \n0 — хронологический. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, comments, tags, can_comment, reposts. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "feed_type": {"desc": "тип новости, получаемый в поле type метода newsfeed.get, для получения только загруженных пользователем фотографий, либо только фотографий, на которых он был отмечен. Может принимать значения photo, photo_tag. строка", "type": "str", "default": "None"}, "feed": {"desc": "время в формате, который может быть получен методом newsfeed.get в поле date, для получения всех фотографий загруженных пользователем в определённый день либо на которых пользователь был отмечен. Также нужно указать параметр uid пользователя, с которым произошло событие. \nЗначение должно отличаться от текущего времени не более, чем на месяц. целое число", "type": "int", "default": "None"}, "photo_sizes": {"desc": "1 — возвращать доступные размеры фотографии в специальном формате. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "отступ, необходимый для получения определенного подмножества записей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество записей, которое будет получено. положительное число, по умолчанию 50, максимальное значение 1000", "type": "int", "default": "50"}}
            def __call__(self, owner_id : int = None, album_id : str = None, photo_ids : str = None, rev : bool = None, extended : bool = None, feed_type : str = None, feed : int = None, photo_sizes : bool = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.get", owner_id = owner_id, album_id = album_id, photo_ids = photo_ids, rev = rev, extended = extended, feed_type = feed_type, feed = feed, photo_sizes = photo_sizes, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbums:
            '''Возвращает список фотоальбомов пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежат альбомы. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_ids": {"desc": "перечисленные через запятую идентификаторы альбомов. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества альбомов. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество альбомов, которое нужно вернуть. (по умолчанию возвращаются все альбомы) положительное число", "type": "int", "default": "None"}, "need_system": {"desc": "1 — будут возвращены системные альбомы, имеющие отрицательные идентификаторы. \nОбратите внимание, что информация о системных альбомах возвращается даже в том случае, если они не содержат фотографий. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "need_covers": {"desc": "1 — будет возвращено дополнительное поле thumb_src с адресом изображения-обложки. По умолчанию поле thumb_src не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_sizes": {"desc": "1 — размеры фотографий будут возвращены  в специальном формате. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id : int = None, album_ids : str = None, offset : int = None, count : int = None, need_system : bool = None, need_covers : bool = None, photo_sizes : bool = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getAlbums", owner_id = owner_id, album_ids = album_ids, offset = offset, count = count, need_system = need_system, need_covers = need_covers, photo_sizes = photo_sizes, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbumsCount:
            '''Возвращает количество доступных альбомов пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, количество альбомов которого необходимо получить. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "group_id": {"desc": "идентификатор сообщества, количество альбомов которого необходимо получить. целое число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getAlbumsCount", user_id = user_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAll:
            '''Возвращает все фотографии пользователя или сообщества в антихронологическом порядке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, фотографии которого нужно получить. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "extended": {"desc": "1 — возвращать расширенную информацию о фотографиях. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества фотографий. По умолчанию — 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "число фотографий, информацию о которых необходимо получить. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "photo_sizes": {"desc": "1 — будут возвращены размеры фотографий в специальном формате. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "no_service_albums": {"desc": "0 — вернуть все фотографии, включая находящиеся в сервисных альбомах, таких как \"Фотографии на моей стене\" (по умолчанию); \n1 — вернуть фотографии только из стандартных альбомов пользователя или сообщества. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "need_hidden": {"desc": "1 — возвращает информацию от том, скрыта ли фотография из блока над стеной пользователя. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "skip_hidden": {"desc": "1 — не возвращать фотографии, скрытые из блока над стеной пользователя (параметр учитывается только при owner_id > 0, параметр no_service_albums игнорируется). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id : int = None, extended : bool = None, offset : int = None, count : int = None, photo_sizes : bool = None, no_service_albums : bool = None, need_hidden : bool = None, skip_hidden : bool = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getAll", owner_id = owner_id, extended = extended, offset = offset, count = count, photo_sizes = photo_sizes, no_service_albums = no_service_albums, need_hidden = need_hidden, skip_hidden = skip_hidden, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAllComments:
            '''Возвращает отсортированный в антихронологическом порядке список всех комментариев к конкретному альбому или ко всем альбомам пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежат фотографии. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома. Если параметр не задан, то считается, что необходимо получить комментарии ко всем альбомам пользователя или сообщества. положительное число", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — будет возвращено дополнительное поле likes. По умолчанию поле likes не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества комментариев. Если параметр не задан, то считается, что он равен 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество комментариев, которое необходимо получить. Если параметр не задан, то считается что он равен 20. Максимальное значение параметра 100. \nОбратите внимание, даже при использовании параметра offset для получения доступны только первые 10000 комментариев. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id : int = None, album_id : int = None, need_likes : bool = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getAllComments", owner_id = owner_id, album_id = album_id, need_likes = need_likes, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию о фотографиях по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"photos": {"desc": "перечисленные через запятую идентификаторы, которые представляют собой идущие через знак подчеркивания id пользователей, разместивших фотографии, и id самих фотографий. Чтобы получить информацию о фотографии в альбоме группы, вместо id пользователя следует указать -id группы.\nПример значения photos: 1_263219656,6492_456239863, \n-1_456239099 \nНекоторые фотографии, идентификаторы которых могут быть получены через API, закрыты приватностью, и не будут получены. В этом случае следует использовать ключ доступа фотографии (access_key) в её идентификаторе. Пример значения photos: 1_129207899_220df2876123d3542f, 6492_135055734_e0a9bcc31144f67fbd \nПоле access_key будет возвращено вместе с остальными данными фотографии в методах, которые возвращают фотографии, закрытые приватностью но доступные в данном контексте. Например данное поле имеют фотографии, возвращаемые методом newsfeed.get. список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, comments, tags, can_comment, can_repost. Поля comments и tags содержат только количество объектов. По умолчанию данные поля не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "photo_sizes": {"desc": "возвращать ли доступные размеры фотографии в специальном формате. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, photos, extended : bool = None, photo_sizes : bool = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getById", photos = photos, extended = extended, photo_sizes = photo_sizes, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getChatUploadServer:
            '''Позволяет получить адрес для загрузки обложки чата. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"chat_id": {"desc": "идентификатор беседы, для которой нужно загрузить фотографию. положительное число, обязательный параметр", "type": "int", "default": "None"}, "crop_x": {"desc": "координата x для обрезки фотографии (верхний правый угол). положительное число", "type": "int", "default": "None"}, "crop_y": {"desc": "координата y для обрезки фотографии (верхний правый угол). положительное число", "type": "int", "default": "None"}, "crop_width": {"desc": "ширина фотографии после обрезки в px. положительное число, минимальное значение 200", "type": "int", "default": "None"}}
            def __call__(self, chat_id, crop_x : int = None, crop_y : int = None, crop_width : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getChatUploadServer", chat_id = chat_id, crop_x = crop_x, crop_y = crop_y, crop_width = crop_width, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список комментариев к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — будет возвращено дополнительное поле likes. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_comment_id": {"desc": "идентификатор комментария, начиная с которого нужно вернуть список (подробности см. ниже). положительное число, доступен начиная с версии 5.33", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества комментариев. По умолчанию: 0. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество комментариев, которое необходимо получить. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "sort": {"desc": "порядок сортировки комментариев. Возможные значения: \n\nasc — от старых к новым; \ndesc — от новых к старым. \nстрока", "type": "str", "default": "None"}, "access_key": {"desc": "ключ доступа к фотографии. строка", "type": "str", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me. список слов, разделенных через запятую", "type": "str", "default": "None"}, "skip_before_id": {"desc": "идентификатор последнего полученного комментания, при подгрузке более новых комментариев. (этот и более старые комментарии получены не будут) положительное число, устаревший параметр, доступен только для версий меньше 5.33", "type": "int", "default": "None"}, "skip_after_id": {"desc": "идентификатор последнего полученного комментания, при подгрузке более старых комментариев. (этот и более новые комментарии получены не будут) положительное число, устаревший параметр, доступен только для версий меньше 5.33", "type": "int", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, need_likes : bool = None, start_comment_id : int = None, offset : int = None, count : int = None, sort : str = None, access_key : str = None, extended : bool = None, fields : str = None, skip_before_id : int = None, skip_after_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getComments", owner_id = owner_id, photo_id = photo_id, need_likes = need_likes, start_comment_id = start_comment_id, offset = offset, count = count, sort = sort, access_key = access_key, extended = extended, fields = fields, skip_before_id = skip_before_id, skip_after_id = skip_after_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMarketAlbumUploadServer:
            '''Возвращает адрес сервера для загрузки фотографии подборки товаров в сообществе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, для которого необходимо загрузить фотографию подборки товаров. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, group_id, v : str = None, access_token : str = None):
                self.exec_func("photos.getMarketAlbumUploadServer", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMarketUploadServer:
            '''Возвращает адрес сервера для загрузки фотографии товара. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, для которого необходимо загрузить фотографию товара. положительное число, обязательный параметр", "type": "int", "default": "None"}, "main_photo": {"desc": "является ли фотография обложкой товара  (1 — фотография для обложки, 0 — дополнительная фотография) флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "crop_x": {"desc": "координата x для обрезки фотографии (верхний правый угол). положительное число", "type": "int", "default": "None"}, "crop_y": {"desc": "координата y для обрезки фотографии (верхний правый угол). положительное число", "type": "int", "default": "None"}, "crop_width": {"desc": "ширина фотографии после обрезки в px. положительное число, минимальное значение 400", "type": "int", "default": "None"}}
            def __call__(self, group_id, main_photo : bool = None, crop_x : int = None, crop_y : int = None, crop_width : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getMarketUploadServer", group_id = group_id, main_photo = main_photo, crop_x = crop_x, crop_y = crop_y, crop_width = crop_width, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getMessagesUploadServer:
            '''Возвращает адрес сервера для загрузки фотографии в личное сообщение. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"peer_id": {"desc": "идентификатор назначения (для загрузки фотографии в сообщениях сообществ). \nДля ботов/массовых рассылок с токеном сообщества можно указать peer_id=0. Изображение будет загружено в скрытый альбом группы. целое число", "type": "int", "default": "None"}}
            def __call__(self, peer_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getMessagesUploadServer", peer_id = peer_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getNewTags:
            '''Возвращает список фотографий, на которых есть непросмотренные отметки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"offset": {"desc": "смещение, необходимое для получения определённого подмножества фотографий. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество фотографий, которые необходимо вернуть. положительное число, максимальное значение 100, по умолчанию 20", "type": "int", "default": "20"}}
            def __call__(self, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getNewTags", offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOwnerCoverPhotoUploadServer:
            '''Получает адрес для загрузки обложки сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число, обязательный параметр", "type": "int", "default": "None"}, "crop_x": {"desc": "координата X верхнего левого угла для обрезки изображения. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "crop_y": {"desc": "координата Y верхнего левого угла для обрезки изображения. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "crop_x2": {"desc": "координата X нижнего правого угла для обрезки изображения. положительное число, по умолчанию 795", "type": "int", "default": "795"}, "crop_y2": {"desc": "координата Y нижнего правого угла для обрезки изображения. положительное число, по умолчанию 200", "type": "int", "default": "200"}}
            def __call__(self, group_id, crop_x : int = None, crop_y : int = None, crop_x2 : int = None, crop_y2 : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getOwnerCoverPhotoUploadServer", group_id = group_id, crop_x = crop_x, crop_y = crop_y, crop_x2 = crop_x2, crop_y2 = crop_y2, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getOwnerPhotoUploadServer:
            '''Возвращает адрес сервера для загрузки главной фотографии на страницу пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества или текущего пользователя. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getOwnerPhotoUploadServer", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getTags:
            '''Возвращает список отметок на фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "строковой ключ доступа, который может быть получен при получении объекта фотографии. строка", "type": "str", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, access_key : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getTags", owner_id = owner_id, photo_id = photo_id, access_key = access_key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUploadServer:
            '''Возвращает адрес сервера для загрузки фотографий. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"album_id": {"desc": "идентификатор альбома. целое число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, которому принадлежит альбом (если необходимо загрузить фотографию в альбом сообщества). \nЕсли group_id не указан, возвращается адрес для загрузки на стену текущего пользователя. целое число", "type": "int", "default": "None"}}
            def __call__(self, album_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getUploadServer", album_id = album_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUserPhotos:
            '''Возвращает список фотографий, на которых отмечен пользователь '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, список фотографий для которого нужно получить. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества фотографий. По умолчанию — 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество фотографий, которое необходимо получить. положительное число, по умолчанию 20, максимальное значение 1000", "type": "int", "default": "20"}, "extended": {"desc": "1 — будут возвращены дополнительные поля likes, comments, tags, can_comment. Поля comments и tags содержат только количество объектов. По умолчанию данные поля не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "sort": {"desc": "сортировка результатов (0 — по дате добавления отметки в порядке убывания, 1 — по дате добавления отметки в порядке возрастания). строка", "type": "str", "default": "None"}}
            def __call__(self, user_id : int = None, offset : int = None, count : int = None, extended : bool = None, sort : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getUserPhotos", user_id = user_id, offset = offset, count = count, extended = extended, sort = sort, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getWallUploadServer:
            '''Возвращает адрес сервера для загрузки фотографии на стену пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества, на стену которого нужно загрузить фото (без знака «минус»). целое число", "type": "int", "default": "None"}}
            def __call__(self, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.getWallUploadServer", group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class makeCover:
            '''Делает фотографию обложкой альбома. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. Фотография должна находиться в альбоме album_id. целое число, обязательный параметр", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор альбома. целое число", "type": "int", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, album_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.makeCover", owner_id = owner_id, photo_id = photo_id, album_id = album_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class move:
            '''Переносит фотографию из одного альбома в другой. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "target_album_id": {"desc": "идентификатор альбома, в который нужно переместить фотографию. целое число, обязательный параметр", "type": "int", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии, которую нужно перенести. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, target_album_id, photo_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.move", owner_id = owner_id, target_album_id = target_album_id, photo_id = photo_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class putTag:
            '''Добавляет отметку на фотографию. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя, которому принадлежит фотография. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. положительное число, обязательный параметр", "type": "int", "default": "None"}, "user_id": {"desc": "идентификатор пользователя, которого нужно отметить на фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "x": {"desc": "координата верхнего левого угла области с отметкой в % от ширины фотографии. дробное число", "type": "int", "default": "None"}, "y": {"desc": "координата верхнего левого угла области с отметкой в % от высоты фотографии. дробное число", "type": "int", "default": "None"}, "x2": {"desc": "координата правого нижнего угла области с отметкой в % от ширины фотографии. дробное число", "type": "int", "default": "None"}, "y2": {"desc": "координата правого нижнего угла области с отметкой в % от высоты фотографии. дробное число", "type": "int", "default": "None"}}
            def __call__(self, photo_id, user_id, owner_id : int = None, x : int = None, y : int = None, x2 : int = None, y2 : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.putTag", owner_id = owner_id, photo_id = photo_id, user_id = user_id, x = x, y = y, x2 = x2, y2 = y2, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeTag:
            '''Удаляет отметку с фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "tag_id": {"desc": "идентификатор отметки. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, photo_id, tag_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.removeTag", owner_id = owner_id, photo_id = photo_id, tag_id = tag_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderAlbums:
            '''Меняет порядок альбома в списке альбомов пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит альбом. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома. целое число, обязательный параметр", "type": "int", "default": "None"}, "before": {"desc": "идентификатор альбома, перед которым следует поместить альбом. целое число", "type": "int", "default": "None"}, "after": {"desc": "идентификатор альбома, после которого следует поместить альбом. целое число", "type": "int", "default": "None"}}
            def __call__(self, album_id, owner_id : int = None, before : int = None, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.reorderAlbums", owner_id = owner_id, album_id = album_id, before = before, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderPhotos:
            '''Меняет порядок фотографии в списке фотографий альбома пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. целое число, обязательный параметр", "type": "int", "default": "None"}, "before": {"desc": "идентификатор фотографии, перед которой следует поместить фотографию. Если параметр не указан, фотография будет помещена последней. целое число", "type": "int", "default": "None"}, "after": {"desc": "идентификатор фотографии, после которой следует поместить фотографию. Если параметр не указан, фотография будет помещена первой. целое число", "type": "int", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, before : int = None, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.reorderPhotos", owner_id = owner_id, photo_id = photo_id, before = before, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class report:
            '''Позволяет пожаловаться на фотографию. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. целое число, обязательный параметр", "type": "int", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, photo_id, reason : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.report", owner_id = owner_id, photo_id = photo_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reportComment:
            '''Позволяет пожаловаться на комментарий к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца фотографии к которой оставлен комментарий. целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, reason : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.reportComment", owner_id = owner_id, comment_id = comment_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Восстанавливает удаленную фотографию. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "photo_id": {"desc": "идентификатор фотографии. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, photo_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.restore", owner_id = owner_id, photo_id = photo_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удаленный комментарий к фотографии. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит фотография. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор удаленного комментария. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.restoreComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class save:
            '''Сохраняет фотографии после успешной загрузки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"album_id": {"desc": "идентификатор альбома, в который необходимо сохранить фотографии. целое число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в которое необходимо сохранить фотографии. целое число", "type": "int", "default": "None"}, "server": {"desc": "параметр, возвращаемый в результате загрузки фотографий на сервер. целое число", "type": "int", "default": "None"}, "photos_list": {"desc": "параметр, возвращаемый в результате загрузки фотографий на сервер. строка", "type": "str", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографий на сервер. строка", "type": "str", "default": "None"}, "latitude": {"desc": "географическая широта, заданная в градусах (от -90 до 90); дробное число", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота, заданная в градусах (от -180 до 180); дробное число", "type": "int", "default": "None"}, "caption": {"desc": "текст описания фотографии (максимум 2048 символов). строка", "type": "str", "default": "None"}}
            def __call__(self, album_id : int = None, group_id : int = None, server : int = None, photos_list : str = None, hash : str = None, latitude : int = None, longitude : int = None, caption : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.save", album_id = album_id, group_id = group_id, server = server, photos_list = photos_list, hash = hash, latitude = latitude, longitude = longitude, caption = caption, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveMarketAlbumPhoto:
            '''Сохраняет фотографии после успешной загрузки на URI, полученный методом photos.getMarketAlbumUploadServer. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, для которой нужно загрузить фотографию. положительное число, обязательный параметр", "type": "int", "default": "None"}, "photo": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. \nМинимальный размер фотографии — 1280x720 пикселей. строка, обязательный параметр", "type": "str", "default": "None"}, "server": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. положительное число, обязательный параметр", "type": "int", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, group_id, photo, server, hash, v : str = None, access_token : str = None):
                self.exec_func("photos.saveMarketAlbumPhoto", group_id = group_id, photo = photo, server = server, hash = hash, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveMarketPhoto:
            '''Сохраняет фотографии после успешной загрузки на URI, полученный методом photos.getMarketUploadServer. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор группы, для которой нужно загрузить фотографию. положительное число", "type": "int", "default": "None"}, "photo": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "server": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. целое число, обязательный параметр", "type": "int", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "crop_data": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. \nОбязательный параметр, если на этапе загрузки фото был передан main_photo=1 строка", "type": "str", "default": "None"}, "crop_hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. \nОбязательный параметр, если на этапе загрузки фото был передан main_photo=1 строка", "type": "str", "default": "None"}}
            def __call__(self, photo, server, hash, group_id : int = None, crop_data : str = None, crop_hash : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.saveMarketPhoto", group_id = group_id, photo = photo, server = server, hash = hash, crop_data = crop_data, crop_hash = crop_hash, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveMessagesPhoto:
            '''Сохраняет фотографию после успешной загрузки на URI, полученный методом photos.getMessagesUploadServer. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"photo": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "server": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. целое число", "type": "int", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка", "type": "str", "default": "None"}}
            def __call__(self, photo, server : int = None, hash : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.saveMessagesPhoto", photo = photo, server = server, hash = hash, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveOwnerCoverPhoto:
            '''Сохраняет изображение для обложки сообщества после успешной загрузки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"hash": {"desc": "параметр hash, полученный в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "photo": {"desc": "параметр photo, полученный в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, hash, photo, v : str = None, access_token : str = None):
                self.exec_func("photos.saveOwnerCoverPhoto", hash = hash, photo = photo, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveOwnerPhoto:
            '''Позволяет сохранить главную фотографию пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"server": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка", "type": "str", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка", "type": "str", "default": "None"}, "photo": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка", "type": "str", "default": "None"}}
            def __call__(self, server : str = None, hash : str = None, photo : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.saveOwnerPhoto", server = server, hash = hash, photo = photo, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class saveWallPhoto:
            '''Сохраняет фотографии после успешной загрузки на URI, полученный методом photos.getWallUploadServer. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, на стену которого нужно сохранить фотографию. положительное число", "type": "int", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, на стену которого нужно сохранить фотографию. положительное число", "type": "int", "default": "None"}, "photo": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка, обязательный параметр", "type": "str", "default": "None"}, "server": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. целое число", "type": "int", "default": "None"}, "hash": {"desc": "параметр, возвращаемый в результате загрузки фотографии на сервер. строка", "type": "str", "default": "None"}, "latitude": {"desc": "географическая широта, заданная в градусах (от -90 до 90); дробное число", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота, заданная в градусах (от -180 до 180); дробное число", "type": "int", "default": "None"}, "caption": {"desc": "текст описания фотографии (максимум 2048 символов). строка", "type": "str", "default": "None"}}
            def __call__(self, photo, user_id : int = None, group_id : int = None, server : int = None, hash : str = None, latitude : int = None, longitude : int = None, caption : str = None, v : str = None, access_token : str = None):
                self.exec_func("photos.saveWallPhoto", user_id = user_id, group_id = group_id, photo = photo, server = server, hash = hash, latitude = latitude, longitude = longitude, caption = caption, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Осуществляет поиск изображений по местоположению или описанию. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса, например, Nature. строка", "type": "str", "default": "None"}, "lat": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "start_time": {"desc": "время в формате unixtime, не раньше которого должны были быть загружены найденные фотографии. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время в формате unixtime, не позже которого должны были быть загружены найденные фотографии. положительное число", "type": "int", "default": "None"}, "sort": {"desc": "сортировка результатов. Возможные значения: \n\n1 — по количеству отметок «Мне нравится»; \n0 — по дате добавления фотографии. \nположительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первой найденной фотографии для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых фотографий. \nОбратите внимание — даже при использовании параметра offset для получения информации доступны не больше 3000 результатов. \n положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}, "radius": {"desc": "радиус поиска в метрах. (работает очень приближенно, поэтому реальное расстояние до цели может отличаться от заданного). Может принимать значения: 10, 100, 800, 6000, 50000 положительное число, по умолчанию 5000", "type": "int", "default": "5000"}}
            def __call__(self, q : str = None, lat : int = None, long : int = None, start_time : int = None, end_time : int = None, sort : int = None, offset : int = None, count : int = None, radius : int = None, v : str = None, access_token : str = None):
                self.exec_func("photos.search", q = q, lat = lat, long = long, start_time = start_time, end_time = end_time, sort = sort, offset = offset, count = count, radius = radius, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class polls:
        def  __init__(self, exec_func):
            self.addVote = self.addVote(exec_func)
            self.create = self.create(exec_func)
            self.deleteVote = self.deleteVote(exec_func)
            self.edit = self.edit(exec_func)
            self.getBackgrounds = self.getBackgrounds(exec_func)
            self.getById = self.getById(exec_func)
            self.getPhotoUploadServer = self.getPhotoUploadServer(exec_func)
            self.getVoters = self.getVoters(exec_func)
            self.savePhoto = self.savePhoto(exec_func)
        class addVote:
            '''Отдает голос текущего пользователя за выбранный вариант ответа в указанном опросе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит опрос. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "poll_id": {"desc": "идентификатор опроса. положительное число, обязательный параметр", "type": "int", "default": "None"}, "answer_ids": {"desc": "список идентификаторов ответа (для опроса с мультивыбором). список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "is_board": {"desc": "1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, poll_id, answer_ids, owner_id : int = None, is_board : bool = None, v : str = None, access_token : str = None):
                self.exec_func("polls.addVote", owner_id = owner_id, poll_id = poll_id, answer_ids = answer_ids, is_board = is_board, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class create:
            '''Позволяет создавать опросы, которые впоследствии можно прикреплять к записям на странице пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"question": {"desc": "текст вопроса строка", "type": "str", "default": "None"}, "is_anonymous": {"desc": "1 – анонимный опрос, список проголосовавших недоступен; \n0 – опрос публичный, список проголосовавших доступен; \nПо умолчанию – 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "is_multiple": {"desc": "1 — для создания опроса с мультивыбором. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "end_date": {"desc": "дата завершения опроса в Unixtime. положительное число, минимальное значение 1603706835", "type": "int", "default": "None"}, "owner_id": {"desc": "Если опрос будет добавлен в группу, необходимо передать отрицательный идентификатор группы. По умолчанию текущий пользователь. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "add_answers": {"desc": "список вариантов ответов, например: [\"yes\", \"no\", \"maybe\"] \nМожет быть не менее 1 и не более 10 вариантов ответа. данные в формате JSON", "type": "not defined", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии для использования в качестве фона сниппета. положительное число", "type": "int", "default": "None"}, "background_id": {"desc": "идентификатор стандартного фона для сниппета. ", "type": "not defined", "default": "None"}, "disable_unvote": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, question : str = None, is_anonymous : bool = None, is_multiple : bool = None, end_date : int = None, owner_id : int = None, add_answers = None, photo_id : int = None, background_id = None, disable_unvote : bool = None, v : str = None, access_token : str = None):
                self.exec_func("polls.create", question = question, is_anonymous = is_anonymous, is_multiple = is_multiple, end_date = end_date, owner_id = owner_id, add_answers = add_answers, photo_id = photo_id, background_id = background_id, disable_unvote = disable_unvote, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteVote:
            '''Снимает голос текущего пользователя с выбранного варианта ответа в указанном опросе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит опрос. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "poll_id": {"desc": "идентификатор опроса. положительное число, обязательный параметр", "type": "int", "default": "None"}, "answer_id": {"desc": "идентификатор варианта ответа. положительное число, обязательный параметр", "type": "int", "default": "None"}, "is_board": {"desc": "1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, poll_id, answer_id, owner_id : int = None, is_board : bool = None, v : str = None, access_token : str = None):
                self.exec_func("polls.deleteVote", owner_id = owner_id, poll_id = poll_id, answer_id = answer_id, is_board = is_board, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Позволяет редактировать созданные опросы. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца опроса целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "poll_id": {"desc": "идентификатор редактируемого опроса положительное число, обязательный параметр", "type": "int", "default": "None"}, "question": {"desc": "новый текст редактируемого опроса строка", "type": "str", "default": "None"}, "add_answers": {"desc": "список вариантов ответов, например: [\"yes\", \"no\", \"maybe\"] данные в формате JSON", "type": "not defined", "default": "None"}, "edit_answers": {"desc": "объект, содержащий варианты ответов, которые необходимо отредактировать; \nключ – идентификатор ответа, значение – новый текст ответа \nПример: {\"382967099\":\"option1\", \"382967103\":\"option2\"} данные в формате JSON", "type": "not defined", "default": "None"}, "delete_answers": {"desc": "список идентификаторов ответов, которые необходимо удалить, например: [382967099, 382967103] данные в формате JSON", "type": "not defined", "default": "None"}, "end_date": {"desc": "дата завершения опроса в Unixtime. положительное число", "type": "int", "default": "None"}, "photo_id": {"desc": "идентификатор фотографии для сниппета. положительное число", "type": "int", "default": "None"}, "background_id": {"desc": "идентификатор стандартного фона для сниппета. ", "type": "not defined", "default": "None"}}
            def __call__(self, poll_id, owner_id : int = None, question : str = None, add_answers = None, edit_answers = None, delete_answers = None, end_date : int = None, photo_id : int = None, background_id = None, v : str = None, access_token : str = None):
                self.exec_func("polls.edit", owner_id = owner_id, poll_id = poll_id, question = question, add_answers = add_answers, edit_answers = edit_answers, delete_answers = delete_answers, end_date = end_date, photo_id = photo_id, background_id = background_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getBackgrounds:
            '''Возвращает варианты фонового изображения для опросов. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("polls.getBackgrounds", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает детальную информацию об опросе по его идентификатору. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит опрос. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "is_board": {"desc": "1 — опрос находится в обсуждении, 0 — опрос прикреплен к стене. \nПо умолчанию — 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "poll_id": {"desc": "идентификатор опроса. положительное число, обязательный параметр", "type": "int", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительную информацию о профилях пользователей. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "friends_count": {"desc": "число идентификаторов проголосовавших друзей, которые необходимо вернуть в ответе. положительное число, по умолчанию 3, максимальное значение 100", "type": "int", "default": "3"}, "fields": {"desc": "список дополнительных полей профилей. См. список возможных значений список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. по умолчанию nom", "type": "not defined", "default": "nom"}}
            def __call__(self, poll_id, owner_id : int = None, is_board : bool = None, extended : bool = None, friends_count : int = None, fields : str = None, name_case = None, v : str = None, access_token : str = None):
                self.exec_func("polls.getById", owner_id = owner_id, is_board = is_board, poll_id = poll_id, extended = extended, friends_count = friends_count, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPhotoUploadServer:
            '''Возвращает адрес сервера для загрузки фоновой фотографии в опрос. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца опроса. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("polls.getPhotoUploadServer", owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getVoters:
            '''Получает список идентификаторов пользователей, которые выбрали определенные варианты ответа в опросе. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит опрос. целое число", "type": "int", "default": "None"}, "poll_id": {"desc": "идентификатор опроса. положительное число, обязательный параметр", "type": "int", "default": "None"}, "answer_ids": {"desc": "идентификаторы вариантов ответа. список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}, "is_board": {"desc": "1 – опрос находится в обсуждении, 0 – опрос прикреплен к стене. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "friends_only": {"desc": "указывает, необходимо ли возвращать только пользователей, которые являются друзьями текущего пользователя. Параметр может принимать следующие значения:\n0 — возвращать всех пользователей в порядке убывания времени голосования;\n1 — возвращать только друзей текущего пользователя в порядке убывания времени голосования. \nЕсли параметр не был задан, то считается, что он равен 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение относительно начала списка, для выборки определенного подмножества. Если параметр не задан, то считается, что он равен 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых идентификаторов пользователей.\nЕсли параметр не задан, то считается, что он равен 100, если не задан параметр friends_only, в противном случае 10.\nМаксимальное значение параметра 1000, если не задан параметр friends_only, в противном случае 100. положительное число", "type": "int", "default": "None"}, "fields": {"desc": "перечисленные через запятую поля анкет, необходимые для получения. Доступные значения: nickname, screen_name, sex, bdate (birthdate), city, country, timezone, photo, photo_medium, photo_big, has_mobile, rate, contacts, education, online, counters. список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, poll_id, answer_ids, owner_id : int = None, is_board : bool = None, friends_only : bool = None, offset : int = None, count : int = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("polls.getVoters", owner_id = owner_id, poll_id = poll_id, answer_ids = answer_ids, is_board = is_board, friends_only = friends_only, offset = offset, count = count, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class savePhoto:
            '''Сохраняет фотографию, загруженную в опрос. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"photo": {"desc": "параметр, полученный в результате загрузки фотографии. обязательный параметр, строка", "type": "str", "default": "None"}, "hash": {"desc": "параметр, полученный в результате загрузки фотографии. обязательный параметр, строка", "type": "str", "default": "None"}}
            def __call__(self, photo, hash, v : str = None, access_token : str = None):
                self.exec_func("polls.savePhoto", photo = photo, hash = hash, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class prettyCards:
        def  __init__(self, exec_func):
            self.create = self.create(exec_func)
            self.delete = self.delete(exec_func)
            self.edit = self.edit(exec_func)
            self.get = self.get(exec_func)
            self.getById = self.getById(exec_func)
            self.getUploadURL = self.getUploadURL(exec_func)
        class create:
            '''Создаёт карточку карусели. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "Идентификатор владельца карточки. Необходимо указать идентификатор сообщества, взятый со знаком минус. Пример: -19542789. обязательный параметр, целое число", "type": "int", "default": "None"}, "photo": {"desc": "Фотография карточки. \nИспользуйте значение, полученное после загрузки фотографии на сервер. См. метод prettyCards.getUploadURL. \nТакже можно переиспользовать существующую фотографию из другой карточки. Используйте значение поля photo, которое возвращает метод prettyCards.get или prettyCards.getById. обязательный параметр, строка", "type": "str", "default": "None"}, "title": {"desc": "Заголовок обязательный параметр, строка", "type": "str", "default": "None"}, "link": {"desc": "Ссылка. Кроме http(s)-ссылок также допускается указание телефонных номеров в виде tel:+79111234567 обязательный параметр, строка, максимальная длина 2000", "type": "str", "default": "None"}, "price": {"desc": "Цена. «0» будет отображён как «Бесплатно». Не передавайте этот параметр, чтобы не указывать цену. строка, максимальная длина 20", "type": "str", "default": "None"}, "price_old": {"desc": "Старая цена. Отображается зачёркнутой. «0» будет отображён как «Бесплатно». Не передавайте этот параметр, чтобы не указывать старую цену. строка, максимальная длина 20", "type": "str", "default": "None"}, "button": {"desc": "Кнопка. Не передавайте этот параметр, чтобы не использовать кнопку. \nbutton Текст Действие Тип ссылок app_join Запустить Переход по ссылке Приложения и игры app_game_join Играть Переход по ссылке Игры open_url Перейти Переход по ссылке Внешние сайты, сообщества, приложения open Открыть Переход по ссылке Внешние сайты more Подробнее Переход по ссылке Сообщества call Позвонить Набор номера Телефонные номера book Забронировать Набор номера Телефонные номера enroll Записаться Переход по ссылке или набор номера Внешние сайты, телефонные номера register Зарегистрироваться Набор номера Телефонные номера buy Купить Переход по ссылке Внешние сайты buy_ticket Купить билет Переход по ссылке Внешние сайты to_shop В магазин Переход по ссылке Внешние сайты order Заказать Переход по ссылке Внешние сайты create Создать Переход по ссылке Внешние сайты install Установить Переход по ссылке Внешние сайты contact Связаться Переход по ссылке Внешние сайты fill Заполнить Переход по ссылке Внешние сайты choose Выбрать Переход по ссылке Внешние сайты try Попробовать Переход по ссылке Внешние сайты join_public Подписаться Подписка на публичную страницу Публичные страницы join_event Я пойду Участие в мероприятии События join_group Вступить Вступление в сообщество Сообщества im_group Связаться Переход к диалогу с сообществом Сообщества, публичные страницы, события im_group2 Написать Переход к диалогу с сообществом Сообщества, публичные страницы, события begin Начать Переход по ссылке Внешние сайты get Получить Переход по ссылке Внешние сайты  строка, максимальная длина 255", "type": "str", "default": "None"}}
            def __call__(self, owner_id, photo, title, link, price : str = None, price_old : str = None, button : str = None, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.create", owner_id = owner_id, photo = photo, title = title, link = link, price = price, price_old = price_old, button = button, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет карточку. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "Идентификатор владельца карточки. обязательный параметр, целое число", "type": "int", "default": "None"}, "card_id": {"desc": "Идентификатор карточки. обязательный параметр, строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, card_id, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.delete", owner_id = owner_id, card_id = card_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует карточку карусели. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "Идентификатор владельца карточки. обязательный параметр, целое число", "type": "int", "default": "None"}, "card_id": {"desc": "Идентификатор карточки. обязательный параметр, строка", "type": "str", "default": "None"}, "photo": {"desc": "Новая фотография. Подробнее см. метод prettyCards.create. строка", "type": "str", "default": "None"}, "title": {"desc": "Новый заголовок. строка", "type": "str", "default": "None"}, "link": {"desc": "Новая ссылка. Подробнее см. метод prettyCards.create. строка, максимальная длина 2000", "type": "str", "default": "None"}, "price": {"desc": "Новая цена. Подробнее см. метод prettyCards.create. строка, максимальная длина 20", "type": "str", "default": "None"}, "price_old": {"desc": "Обновлённая старая цена. Подробнее см. метод prettyCards.create. строка, максимальная длина 20", "type": "str", "default": "None"}, "button": {"desc": "Новая кнопка. Подробнее см. метод prettyCards.create. строка, максимальная длина 255", "type": "str", "default": "None"}}
            def __call__(self, owner_id, card_id, photo : str = None, title : str = None, link : str = None, price : str = None, price_old : str = None, button : str = None, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.edit", owner_id = owner_id, card_id = card_id, photo = photo, title = title, link = link, price = price, price_old = price_old, button = button, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает неиспользованные карточки владельца. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "Идентификатор владельца. обязательный параметр, целое число", "type": "int", "default": "None"}, "offset": {"desc": "Смещение относительно начала списка карточек. целое число, минимальное значение 0, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "Количество возвращаемых карточек. целое число, минимальное значение 0, по умолчанию 10, максимальное значение 100", "type": "int", "default": "10"}}
            def __call__(self, owner_id, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.get", owner_id = owner_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию о карточке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "Идентификатор владельца карточки. обязательный параметр, целое число", "type": "int", "default": "None"}, "card_ids": {"desc": "Список идентификаторов карточек, которые необходимо вернуть. Строка с числами, разделёнными запятой. обязательный параметр", "type": "not defined", "default": "None"}}
            def __call__(self, owner_id, card_ids, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.getById", owner_id = owner_id, card_ids = card_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getUploadURL:
            '''Возвращает URL для загрузки фотографии для карточки. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("prettyCards.getUploadURL", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class search:
        def  __init__(self, exec_func):
            self.getHints = self.getHints(exec_func)
        class getHints:
            '''Метод позволяет получить результаты быстрого поиска по произвольной подстроке '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "текст запроса, результаты которого нужно получить строка", "type": "str", "default": "None"}, "offset": {"desc": "смещение для выборки определённого подмножества результатов. положительное число, максимальное значение 200", "type": "int", "default": "None"}, "limit": {"desc": "ограничение на количество возвращаемых результатов. положительное число, по умолчанию 9, максимальное значение 200", "type": "int", "default": "9"}, "filters": {"desc": "Перечисленные через запятую типы данных, которые необходимо вернуть. Возможные значения: \n\nfriends – друзья пользователя; \nidols – подписки пользователя; \npublics – публичные страницы, на которые подписан пользователь; \ngroups – группы пользователя; \nevents – встречи пользователя; \ncorrespondents – люди, с которыми пользователь имеет переписку; \nmutual_friends – люди, у которых  есть общие друзья с текущим пользователем (этот фильтр позволяет получить не всех пользователей, имеющих общих друзей). \n \nПо умолчанию возвращаются все. список слов, разделенных через запятую", "type": "str", "default": "None"}, "fields": {"desc": "дополнительные поля профилей и сообществ для получения. список слов, разделенных через запятую", "type": "str", "default": "None"}, "search_global": {"desc": "1 — к результатам поиска добавляются результаты глобального поиска по всем пользователям и группам. флаг, может принимать значения 1 или 0, по умолчанию 1", "type": "bool", "default": "1"}}
            def __call__(self, q : str = None, offset : int = None, limit : int = None, filters : str = None, fields : str = None, search_global : bool = None, v : str = None, access_token : str = None):
                self.exec_func("search.getHints", q = q, offset = offset, limit = limit, filters = filters, fields = fields, search_global = search_global, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class stats:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
            self.getPostReach = self.getPostReach(exec_func)
            self.trackVisitor = self.trackVisitor(exec_func)
        class get:
            '''Возвращает статистику сообщества или приложения. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества. положительное число", "type": "int", "default": "None"}, "app_id": {"desc": "идентификатор приложения. положительное число", "type": "int", "default": "None"}, "timestamp_from": {"desc": "начало периода статистики в Unixtime. положительное число, доступен начиная с версии 5.86", "type": "int", "default": "None"}, "timestamp_to": {"desc": "окончание периода статистики в Unixtime. положительное число, доступен начиная с версии 5.86", "type": "int", "default": "None"}, "interval": {"desc": "временные интервалы. Возможные значения: day, week, month, year, all. По умолчанию: day. строка, по умолчанию day", "type": "str", "default": "day"}, "intervals_count": {"desc": "количество интервалов времени. положительное число", "type": "int", "default": "None"}, "filters": {"desc": "список слов, разделенных через запятую", "type": "str", "default": "None"}, "stats_groups": {"desc": "фильтр для получения данных по конкретному блоку статистики сообщества. Возможные значения: visitors, reach, activity. список слов, разделенных через запятую", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительно агрегированные данные в результатах. флаг, может принимать значения 1 или 0, по умолчанию 1", "type": "bool", "default": "1"}, "date_from": {"desc": "Начальная дата выводимой статистики в формате YYYY-MM-DD. строка, устаревший параметр, доступен только для версий меньше 5.86", "type": "str", "default": "None"}, "date_to": {"desc": "Конечная дата выводимой статистики в формате YYYY-MM-DD. строка, устаревший параметр, доступен только для версий меньше 5.86", "type": "str", "default": "None"}}
            def __call__(self, group_id : int = None, app_id : int = None, timestamp_from : int = None, timestamp_to : int = None, interval : str = None, intervals_count : int = None, filters : str = None, stats_groups : str = None, extended : bool = None, date_from : str = None, date_to : str = None, v : str = None, access_token : str = None):
                self.exec_func("stats.get", group_id = group_id, app_id = app_id, timestamp_from = timestamp_from, timestamp_to = timestamp_to, interval = interval, intervals_count = intervals_count, filters = filters, stats_groups = stats_groups, extended = extended, date_from = date_from, date_to = date_to, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPostReach:
            '''Возвращает статистику для записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор сообщества — владельца записи. Указывается со знаком «минус». целое число, обязательный параметр", "type": "int", "default": "None"}, "post_ids": {"desc": "список положительных чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owner_id, post_ids, v : str = None, access_token : str = None):
                self.exec_func("stats.getPostReach", owner_id = owner_id, post_ids = post_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class trackVisitor:
            '''Добавляет данные о текущем сеансе в статистику посещаемости приложения. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("stats.trackVisitor", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class status:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
            self.set = self.set(exec_func)
        class get:
            '''Получает текст статуса пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя или сообщества, информацию о статусе которого нужно получить. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "group_id": {"desc": "идентификатор сообщества, статус которого необходимо получить. положительное число", "type": "int", "default": "None"}}
            def __call__(self, user_id : int = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("status.get", user_id = user_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class set:
            '''Устанавливает новый статус текущему пользователю или сообществу. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"text": {"desc": "текст нового статуса. строка", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в котором будет установлен статус. По умолчанию статус устанавливается текущему пользователю. положительное число", "type": "int", "default": "None"}}
            def __call__(self, text : str = None, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("status.set", text = text, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class storage:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
            self.getKeys = self.getKeys(exec_func)
            self.set = self.set(exec_func)
        class get:
            '''Возвращает значение переменной, название которой передано в параметре key. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"key": {"desc": "название переменной. строка, максимальная длина 100", "type": "str", "default": "None"}, "keys": {"desc": "список названий переменных, разделённых запятыми. Если указан этот параметр, то параметр key не учитывается. список слов, разделенных через запятую, количество элементов должно составлять не более 1000", "type": "str", "default": "None"}, "user_id": {"desc": "id пользователя, переменная которого устанавливается, в случае если данные запрашиваются серверным методом. положительное число", "type": "int", "default": "None"}}
            def __call__(self, key : str = None, keys : str = None, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("storage.get", key = key, keys = keys, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getKeys:
            '''Возвращает названия всех переменных. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "id пользователя, названия переменных которого получаются, в случае если данные запрашиваются серверным методом. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества названий переменных. По умолчанию 0. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество названий переменных, информацию о которых необходимо получить. положительное число, максимальное значение 1000, по умолчанию 100", "type": "int", "default": "100"}}
            def __call__(self, user_id : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("storage.getKeys", user_id = user_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class set:
            '''Сохраняет значение переменной, название которой передано в параметре key. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"key": {"desc": "название переменной. Может содержать символы латинского алфавита, цифры, знак тире, нижнее подчёркивание [a-zA-Z_\\-0-9]. строка, максимальная длина 100, обязательный параметр", "type": "str", "default": "None"}, "value": {"desc": "значение переменной, сохраняются только первые 4096 байта. строка", "type": "str", "default": "None"}, "user_id": {"desc": "id пользователя, переменная которого устанавливается, в случае если данные запрашиваются серверным методом. положительное число", "type": "int", "default": "None"}}
            def __call__(self, key, value : str = None, user_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("storage.set", key = key, value = value, user_id = user_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class stories:
        def  __init__(self, exec_func):
            self.banOwner = self.banOwner(exec_func)
            self.delete = self.delete(exec_func)
            self.get = self.get(exec_func)
            self.getBanned = self.getBanned(exec_func)
            self.getById = self.getById(exec_func)
            self.getPhotoUploadServer = self.getPhotoUploadServer(exec_func)
            self.getReplies = self.getReplies(exec_func)
            self.getStats = self.getStats(exec_func)
            self.getVideoUploadServer = self.getVideoUploadServer(exec_func)
            self.getViewers = self.getViewers(exec_func)
            self.hideAllReplies = self.hideAllReplies(exec_func)
            self.hideReply = self.hideReply(exec_func)
            self.save = self.save(exec_func)
            self.search = self.search(exec_func)
            self.sendInteraction = self.sendInteraction(exec_func)
            self.unbanOwner = self.unbanOwner(exec_func)
        class banOwner:
            '''Позволяет скрыть из ленты новостей истории от выбранных источников. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owners_ids": {"desc": "список идентификаторов источников. список целых чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owners_ids, v : str = None, access_token : str = None):
                self.exec_func("stories.banOwner", owners_ids = owners_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца истории. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "story_id": {"desc": "идентификатор истории. положительное число", "type": "int", "default": "None"}, "stories": {"desc": "список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id : int = None, story_id : int = None, stories : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.delete", owner_id = owner_id, story_id = story_id, stories = stories, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает истории, доступные для текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя, истории которого необходимо получить. целое число", "type": "int", "default": "None"}, "extended": {"desc": "1 — возвращать в ответе дополнительную информацию о профилях пользователей. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "fields": {"desc": "список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id : int = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.get", owner_id = owner_id, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getBanned:
            '''Возвращает список источников историй, скрытых из ленты текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"extended": {"desc": "1 — возвращать расширенную информацию о пользователях и сообществах. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "дополнительные поля пользователей и сообществ, которые необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getBanned", extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает информацию об истории по её идентификатору. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"stories": {"desc": "перечисленные через запятую идентификаторы, которые представляют собой идущие через знак подчеркивания идентификаторы владельцев историй и идентификаторы самих историй. \n\nПример значения stories:\n93388_21539,93388_20904 список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать в ответе дополнительную информацию о пользователях. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "fields": {"desc": "дополнительные поля профилей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, stories, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getById", stories = stories, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPhotoUploadServer:
            '''Позволяет получить адрес для загрузки истории с фотографией. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"add_to_news": {"desc": "1 — разместить историю в новостях. Обязательно, если не указан user_ids флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_ids": {"desc": "идентификаторы пользователей, которые будут видеть историю (для отправки в личном сообщении). Обязательно, если add_to_news не передан. список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "reply_to_story": {"desc": "идентификатор истории, в ответ на которую создается новая. строка", "type": "str", "default": "None"}, "link_text": {"desc": "текст ссылки для перехода из истории (только для историй сообществ). Возможные значения: \n\nto_store — «В магазин»; \nvote — «Голосовать»; \nmore — «Ещё»; \nbook — «Забронировать»; \norder — «Заказать»; \nenroll — «Записаться»; \nfill — «Заполнить»; \nsignup — «Зарегистрироваться»; \nbuy — «Купить»; \nticket — «Купить билет»; \nwrite — «Написать»; \nopen — «Открыть»; \nlearn_more — «Подробнее» (по умолчанию); \nview — «Посмотреть»; \ngo_to — «Перейти»; \ncontact — «Связаться»; \nwatch — «Смотреть»; \nplay — «Слушать»; \ninstall — «Установить»; \nread — «Читать». \nстрока", "type": "str", "default": "None"}, "link_url": {"desc": "адрес ссылки для перехода из истории. Допустимы только внутренние ссылки https://vk.com. строка, максимальная длина 2048", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в которое должна быть загружена история (при работе с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "clickable_stickers": {"desc": "объект кликабельного стикера. данные в формате JSON", "type": "not defined", "default": "None"}}
            def __call__(self, add_to_news : bool = None, user_ids : str = None, reply_to_story : str = None, link_text : str = None, link_url : str = None, group_id : int = None, clickable_stickers = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getPhotoUploadServer", add_to_news = add_to_news, user_ids = user_ids, reply_to_story = reply_to_story, link_text = link_text, link_url = link_url, group_id = group_id, clickable_stickers = clickable_stickers, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getReplies:
            '''Позволяет получить ответы на историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца истории. целое число, обязательный параметр", "type": "int", "default": "None"}, "story_id": {"desc": "идентификатор истории. положительное число, обязательный параметр", "type": "int", "default": "None"}, "access_key": {"desc": "ключ доступа для приватного объекта. строка", "type": "str", "default": "None"}, "extended": {"desc": "1 — возвращать дополнительную информацию о профилях и сообществах. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "fields": {"desc": "дополнительные поля профилей и сообществ, которые необходимо вернуть в ответе. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id, story_id, access_key : str = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getReplies", owner_id = owner_id, story_id = story_id, access_key = access_key, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getStats:
            '''Возвращает статистику истории. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца истории. целое число, обязательный параметр", "type": "int", "default": "None"}, "story_id": {"desc": "идентификатор истории. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, story_id, v : str = None, access_token : str = None):
                self.exec_func("stories.getStats", owner_id = owner_id, story_id = story_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getVideoUploadServer:
            '''Позволяет получить адрес для загрузки видеозаписи в историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"add_to_news": {"desc": "1 — разместить историю в новостях. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "user_ids": {"desc": "идентификаторы пользователей, которые будут видеть историю (для отправки в личном сообщении). список положительных чисел, разделенных запятыми", "type": "str", "default": "None"}, "reply_to_story": {"desc": "идентификатор истории, в ответ на которую создается новая. строка", "type": "str", "default": "None"}, "link_text": {"desc": "текст ссылки для перехода из истории (только для историй сообществ). Возможные значения: \n\nto_store — «В магазин»; \nvote — «Голосовать»; \nmore — «Ещё»; \nbook — «Забронировать»; \norder — «Заказать»; \nenroll — «Записаться»; \nfill — «Заполнить»; \nsignup — «Зарегистрироваться»; \nbuy — «Купить»; \nticket — «Купить билет»; \nwrite — «Написать»; \nopen — «Открыть»; \nlearn_more — «Подробнее» (по умолчанию); \nview — «Посмотреть»; \ngo_to — «Перейти»; \ncontact — «Связаться»; \nwatch — «Смотреть»; \nplay — «Слушать»; \ninstall — «Установить»; \nread — «Читать»; \ngame — «Играть». \nстрока", "type": "str", "default": "None"}, "link_url": {"desc": "адрес ссылки для перехода из истории. строка, максимальная длина 2048", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в которое должна быть загружена история (при работе с ключом доступа пользователя). положительное число", "type": "int", "default": "None"}, "clickable_stickers": {"desc": "объект кликабельного стикера. данные в формате JSON", "type": "not defined", "default": "None"}}
            def __call__(self, add_to_news : bool = None, user_ids : str = None, reply_to_story : str = None, link_text : str = None, link_url : str = None, group_id : int = None, clickable_stickers = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getVideoUploadServer", add_to_news = add_to_news, user_ids = user_ids, reply_to_story = reply_to_story, link_text = link_text, link_url = link_url, group_id = group_id, clickable_stickers = clickable_stickers, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getViewers:
            '''Возвращает список пользователей, просмотревших историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца истории. целое число, по умолчанию идентификатор текущего пользователя, обязательный параметр", "type": "int", "default": "идентификатор текущего пользователя"}, "story_id": {"desc": "идентификатор истории. положительное число, обязательный параметр", "type": "int", "default": "None"}, "count": {"desc": "максимальное число результатов в ответе. положительное число, по умолчанию 100", "type": "int", "default": "100"}, "offset": {"desc": "сдвиг для получения определённого подмножества результатов. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "extended": {"desc": "1 — возвращать в ответе расширенную информацию о пользователях. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, owner_id, story_id, count : int = None, offset : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("stories.getViewers", owner_id = owner_id, story_id = story_id, count = count, offset = offset, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class hideAllReplies:
            '''Скрывает все ответы автора за последние сутки на истории текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя, ответы от которого нужно скрыть. целое число, обязательный параметр", "type": "int", "default": "None"}, "group_id": {"desc": "положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("stories.hideAllReplies", owner_id = owner_id, group_id = group_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class hideReply:
            '''Скрывает ответ на историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца истории (ответной). целое число, обязательный параметр", "type": "int", "default": "None"}, "story_id": {"desc": "идентификатор истории (ответной). положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, story_id, v : str = None, access_token : str = None):
                self.exec_func("stories.hideReply", owner_id = owner_id, story_id = story_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class save:
            '''Сохраняет историю. В upload_results нужно передать строку, которую возвращает stories.getPhotoUploadServer или stories.getVideoUploadServer '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"upload_results": {"desc": "список строк, которые возвращает stories.getPhotoUploadServer или stories.getVideoUploadServer. список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, upload_results, v : str = None, access_token : str = None):
                self.exec_func("stories.save", upload_results = upload_results, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает результаты поиска по историям. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "поисковый запрос. строка, максимальная длина 255", "type": "str", "default": "None"}, "place_id": {"desc": "идентификатор места. положительное число", "type": "int", "default": "None"}, "latitude": {"desc": "географическая широта точки, в радиусе которой необходимо производить поиск, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "longitude": {"desc": "географическая долгота точки, в радиусе которой необходимо производить поиск, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "radius": {"desc": "радиус зоны поиска в метрах. положительное число", "type": "int", "default": "None"}, "mentioned_id": {"desc": "идентификатор упомянутого в истории пользователя или сообщества. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество историй, информацию о которых необходимо вернуть. целое число, по умолчанию 20, минимальное значение 1, максимальное значение 1000", "type": "int", "default": "20"}, "extended": {"desc": "параметр, определяющий необходимость возвращать расширенную информацию о владельце истории. Возможные значения: \n\n0 — возвращаются только идентификаторы; \n1 — будут дополнительно возвращены имя и фамилия. \n\nПо умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, q : str = None, place_id : int = None, latitude : int = None, longitude : int = None, radius : int = None, mentioned_id : int = None, count : int = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("stories.search", q = q, place_id = place_id, latitude = latitude, longitude = longitude, radius = radius, mentioned_id = mentioned_id, count = count, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class sendInteraction:
            '''Отправляет фидбек на историю. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"access_key": {"desc": "ключ доступа пользователя, полученный при подписке. Возвращает событие VKWebAppSubscribeStoryApp. строка, обязательный параметр", "type": "str", "default": "None"}, "message": {"desc": "текст фидбека. строка, максимальная длина 1000", "type": "str", "default": "None"}, "is_broadcast": {"desc": "Возможные значения: \n\n0 —  фидбек виден только отправителю и автору истории; \n1 —  фидбек виден всем зрителям истории и автору. \nфлаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "is_anonymous": {"desc": "Возможные значения: \n\n0 — автор фидбека не  анонимный; \n1 —  автор фидбека  анонимный. \nфлаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "unseen_marker": {"desc": "флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, access_key, message : str = None, is_broadcast : bool = None, is_anonymous : bool = None, unseen_marker : bool = None, v : str = None, access_token : str = None):
                self.exec_func("stories.sendInteraction", access_key = access_key, message = message, is_broadcast = is_broadcast, is_anonymous = is_anonymous, unseen_marker = unseen_marker, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unbanOwner:
            '''Позволяет вернуть пользователя или сообщество в список отображаемых историй в ленте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owners_ids": {"desc": "список идентификаторов владельцев историй, разделённых запятой. список целых чисел, разделенных запятыми, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, owners_ids, v : str = None, access_token : str = None):
                self.exec_func("stories.unbanOwner", owners_ids = owners_ids, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class streaming:
        def  __init__(self, exec_func):
            self.getServerUrl = self.getServerUrl(exec_func)
            self.getSettings = self.getSettings(exec_func)
            self.getStats = self.getStats(exec_func)
            self.getStem = self.getStem(exec_func)
            self.setSettings = self.setSettings(exec_func)
        class getServerUrl:
            '''Позволяет получить данные для подключения к Streaming API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("streaming.getServerUrl", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSettings:
            '''Позволяет получить значение порога для Streaming API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("streaming.getSettings", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getStats:
            '''Позволяет получить статистику для подготовленных и доставленных событий Streaming API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"type": {"desc": "тип статистики. Возможные значения: \n\nreceived — события, полученные приложением; \nprepared — события, сгенерированные со стороны ВКонтакте. \nстрока", "type": "str", "default": "None"}, "interval": {"desc": "интервалы статистики. Возможные значения: \n\n5m — пять минут. Максимальный период — 3 дня между start_time и end_time; \n1h — один час. Максимальный период — 7 дней между start_time и end_time; \n24h — сутки. Максимальный период — 31 день между start_time и end_time. \nстрока, по умолчанию 5m", "type": "str", "default": "5m"}, "start_time": {"desc": "время начала отсчёта в Unixtime. По умолчанию: end_time минус сутки. положительное число", "type": "int", "default": "None"}, "end_time": {"desc": "время окончания отсчёта в Unixtime. По умолчанию: текущее время. положительное число", "type": "int", "default": "None"}}
            def __call__(self, type : str = None, interval : str = None, start_time : int = None, end_time : int = None, v : str = None, access_token : str = None):
                self.exec_func("streaming.getStats", type = type, interval = interval, start_time = start_time, end_time = end_time, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getStem:
            '''Позволяет получить основу слова. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"word": {"desc": "слово, основу которого мы собираемся получить строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, word, v : str = None, access_token : str = None):
                self.exec_func("streaming.getStem", word = word, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class setSettings:
            '''Позволяет задать значение порога для Streaming API. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"monthly_tier": {"desc": "значение порога в месяц. Возможные значения: \n\ntier_1; \ntier_2; \ntier_3; \ntier_4; \ntier_5; \ntier_6; \nunlimited. \nстрока", "type": "str", "default": "None"}}
            def __call__(self, monthly_tier : str = None, v : str = None, access_token : str = None):
                self.exec_func("streaming.setSettings", monthly_tier = monthly_tier, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class users:
        def  __init__(self, exec_func):
            self.get = self.get(exec_func)
            self.getFollowers = self.getFollowers(exec_func)
            self.getSubscriptions = self.getSubscriptions(exec_func)
            self.report = self.report(exec_func)
            self.search = self.search(exec_func)
        class get:
            '''Возвращает расширенную информацию о пользователях. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_ids": {"desc": "перечисленные через запятую идентификаторы пользователей или их короткие имена (screen_name). По умолчанию — идентификатор текущего пользователя. список слов, разделенных через запятую, количество элементов должно составлять не более 1000", "type": "str", "default": "None"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group. список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, user_ids : str = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("users.get", user_ids = user_ids, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getFollowers:
            '''Возвращает список идентификаторов пользователей, которые являются подписчиками пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества подписчиков. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество подписчиков, информацию о которых нужно получить. положительное число, по умолчанию 100, максимальное значение 1000", "type": "int", "default": "100"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me. список слов, разделенных через запятую", "type": "str", "default": "None"}, "name_case": {"desc": "падеж для склонения имени и фамилии пользователя. Возможные значения: именительный – nom, родительный – gen, дательный – dat, винительный – acc, творительный – ins, предложный – abl. По умолчанию nom. строка", "type": "str", "default": "None"}}
            def __call__(self, user_id : int = None, offset : int = None, count : int = None, fields : str = None, name_case : str = None, v : str = None, access_token : str = None):
                self.exec_func("users.getFollowers", user_id = user_id, offset = offset, count = count, fields = fields, name_case = name_case, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getSubscriptions:
            '''Возвращает список идентификаторов пользователей и публичных страниц, которые входят в список подписок пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, подписки которого необходимо получить. положительное число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "extended": {"desc": "1 – возвращает объединенный список, содержащий объекты group и user вместе. 0 – возвращает список идентификаторов групп и пользователей отдельно. (по умолчанию) флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение необходимое для выборки определенного подмножества подписок. Этот параметр используется только если передан extended=1. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество подписок, которые необходимо вернуть. Этот параметр используется только если передан extended=1. положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "fields": {"desc": "список дополнительных полей для объектов user и group, которые необходимо вернуть. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, user_id : int = None, extended : bool = None, offset : int = None, count : int = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("users.getSubscriptions", user_id = user_id, extended = extended, offset = offset, count = count, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class report:
            '''Позволяет пожаловаться на пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"user_id": {"desc": "идентификатор пользователя, на которого нужно подать жалобу. положительное число, обязательный параметр", "type": "int", "default": "None"}, "type": {"desc": "тип жалобы, может принимать следующие значения: \n\nporn — порнография; \nspam — рассылка спама; \ninsult — оскорбительное поведение; \nadvertisеment — рекламная страница, засоряющая поиск. \nстрока, обязательный параметр", "type": "str", "default": "None"}, "comment": {"desc": "комментарий к жалобе на пользователя. строка", "type": "str", "default": "None"}}
            def __call__(self, user_id, type, comment : str = None, v : str = None, access_token : str = None):
                self.exec_func("users.report", user_id = user_id, type = type, comment = comment, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает список пользователей в соответствии с заданным критерием поиска. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса. Например, Вася Бабич. строка", "type": "str", "default": "None"}, "sort": {"desc": "сортировка результатов. Возможные значения: \n\n1 — по дате регистрации; \n0 — по популярности. \nцелое число", "type": "int", "default": "None"}, "offset": {"desc": "смещение относительно первого найденного пользователя для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых пользователей. Обратите внимание — даже при использовании параметра offset для получения информации доступны только первые 1000 результатов. \n положительное число, по умолчанию 20, максимальное значение 1000", "type": "int", "default": "20"}, "fields": {"desc": "список дополнительных полей профилей, которые необходимо вернуть. См. подробное описание. \nДоступные значения: photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, wall_comments, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me список слов, разделенных через запятую", "type": "str", "default": "None"}, "city": {"desc": "идентификатор города. положительное число", "type": "int", "default": "None"}, "country": {"desc": "идентификатор страны. положительное число", "type": "int", "default": "None"}, "hometown": {"desc": "название города строкой. строка", "type": "str", "default": "None"}, "university_country": {"desc": "идентификатор страны, в которой пользователи закончили ВУЗ. положительное число", "type": "int", "default": "None"}, "university": {"desc": "идентификатор ВУЗа. положительное число", "type": "int", "default": "None"}, "university_year": {"desc": "год окончания ВУЗа. положительное число", "type": "int", "default": "None"}, "university_faculty": {"desc": "идентификатор факультета. положительное число", "type": "int", "default": "None"}, "university_chair": {"desc": "идентификатор кафедры. положительное число", "type": "int", "default": "None"}, "sex": {"desc": "пол. Возможные значения: \n\n1 —  женщина; \n2 — мужчина; \n0 — любой (по умолчанию). \nположительное число", "type": "int", "default": "None"}, "status": {"desc": "семейное положение. Возможные значения: \n\n1 — не женат (не замужем); \n2 — встречается; \n3 — помолвлен(-а); \n4 — женат (замужем); \n5 — всё сложно; \n6 — в активном поиске; \n7 — влюблен(-а); \n8 — в гражданском браке. \nположительное число", "type": "int", "default": "None"}, "age_from": {"desc": "возраст, от. положительное число", "type": "int", "default": "None"}, "age_to": {"desc": "возраст, до. положительное число", "type": "int", "default": "None"}, "birth_day": {"desc": "день рождения. положительное число", "type": "int", "default": "None"}, "birth_month": {"desc": "месяц рождения. положительное число", "type": "int", "default": "None"}, "birth_year": {"desc": "год рождения. положительное число, минимальное значение 1900, максимальное значение 2100", "type": "int", "default": "None"}, "online": {"desc": "учитывать ли статус «онлайн». Возможные значения: \n\n1 — искать только пользователей онлайн; \n0 — искать по всем пользователям. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "has_photo": {"desc": "учитывать ли наличие фото. Возможные значения: \n\n1 — искать только пользователей с фотографией; \n0 — искать по всем пользователям. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "school_country": {"desc": "идентификатор страны, в которой пользователи закончили школу. положительное число", "type": "int", "default": "None"}, "school_city": {"desc": "идентификатор города, в котором пользователи закончили школу. положительное число", "type": "int", "default": "None"}, "school_class": {"desc": "буква класса. положительное число", "type": "int", "default": "None"}, "school": {"desc": "идентификатор школы, которую закончили пользователи. положительное число", "type": "int", "default": "None"}, "school_year": {"desc": "год окончания школы. положительное число", "type": "int", "default": "None"}, "religion": {"desc": "религиозные взгляды. строка", "type": "str", "default": "None"}, "company": {"desc": "название компании, в которой работают пользователи. строка", "type": "str", "default": "None"}, "position": {"desc": "название должности. строка", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор группы, среди пользователей которой необходимо проводить поиск. положительное число", "type": "int", "default": "None"}, "from_list": {"desc": "Разделы среди которых нужно осуществить поиск, перечисленные через запятую. Возможные значения: \n\nfriends — искать среди друзей; \nsubscriptions — искать среди друзей и подписок пользователя. \nсписок слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, q : str = None, sort : int = None, offset : int = None, count : int = None, fields : str = None, city : int = None, country : int = None, hometown : str = None, university_country : int = None, university : int = None, university_year : int = None, university_faculty : int = None, university_chair : int = None, sex : int = None, status : int = None, age_from : int = None, age_to : int = None, birth_day : int = None, birth_month : int = None, birth_year : int = None, online : bool = None, has_photo : bool = None, school_country : int = None, school_city : int = None, school_class : int = None, school : int = None, school_year : int = None, religion : str = None, company : str = None, position : str = None, group_id : int = None, from_list : str = None, v : str = None, access_token : str = None):
                self.exec_func("users.search", q = q, sort = sort, offset = offset, count = count, fields = fields, city = city, country = country, hometown = hometown, university_country = university_country, university = university, university_year = university_year, university_faculty = university_faculty, university_chair = university_chair, sex = sex, status = status, age_from = age_from, age_to = age_to, birth_day = birth_day, birth_month = birth_month, birth_year = birth_year, online = online, has_photo = has_photo, school_country = school_country, school_city = school_city, school_class = school_class, school = school, school_year = school_year, religion = religion, company = company, position = position, group_id = group_id, from_list = from_list, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class utils:
        def  __init__(self, exec_func):
            self.checkLink = self.checkLink(exec_func)
            self.deleteFromLastShortened = self.deleteFromLastShortened(exec_func)
            self.getLastShortenedLinks = self.getLastShortenedLinks(exec_func)
            self.getLinkStats = self.getLinkStats(exec_func)
            self.getServerTime = self.getServerTime(exec_func)
            self.getShortLink = self.getShortLink(exec_func)
            self.resolveScreenName = self.resolveScreenName(exec_func)
        class checkLink:
            '''Возвращает информацию о том, является ли внешняя ссылка заблокированной на сайте ВКонтакте. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"url": {"desc": "внешняя ссылка, которую необходимо проверить. \nНапример, http://google.com строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, url, v : str = None, access_token : str = None):
                self.exec_func("utils.checkLink", url = url, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteFromLastShortened:
            '''Удаляет сокращенную ссылку из списка пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"key": {"desc": "сокращенная ссылка (часть URL после \"vk.cc/\"). строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, key, v : str = None, access_token : str = None):
                self.exec_func("utils.deleteFromLastShortened", key = key, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLastShortenedLinks:
            '''Получает список сокращенных ссылок для текущего пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"count": {"desc": "количество ссылок, которые необходимо получить. положительное число, по умолчанию 10", "type": "int", "default": "10"}, "offset": {"desc": "сдвиг для получения определенного подмножества ссылок. положительное число, по умолчанию 0", "type": "int", "default": "0"}}
            def __call__(self, count : int = None, offset : int = None, v : str = None, access_token : str = None):
                self.exec_func("utils.getLastShortenedLinks", count = count, offset = offset, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getLinkStats:
            '''Возвращает статистику переходов по сокращенной ссылке. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"key": {"desc": "сокращенная ссылка (часть URL после \"vk.cc/\"). строка, обязательный параметр", "type": "str", "default": "None"}, "source": {"desc": "строка, по умолчанию vk_cc", "type": "str", "default": "vk_cc"}, "access_key": {"desc": "ключ доступа к приватной статистике ссылки. строка", "type": "str", "default": "None"}, "interval": {"desc": "единица времени для подсчета статистики. Возможные значения: \n\nhour — час; \nday — день; \nweek — неделя; \nmonth — месяц; \nforever — все время с момента создания ссылки. \nстрока, по умолчанию day", "type": "str", "default": "day"}, "intervals_count": {"desc": "длительность периода для получения статистики в выбранных единицах (из параметра interval). положительное число, по умолчанию 1, максимальное значение 100", "type": "int", "default": "1"}, "extended": {"desc": "1 — возвращать расширенную статистику (пол/возраст/страна/город), 0 — возвращать только количество переходов. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, key, source : str = None, access_key : str = None, interval : str = None, intervals_count : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("utils.getLinkStats", key = key, source = source, access_key = access_key, interval = interval, intervals_count = intervals_count, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getServerTime:
            '''Возвращает текущее время на сервере ВКонтакте в unixtime. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {}
            def __call__(self, v : str = None, access_token : str = None):
                self.exec_func("utils.getServerTime", v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getShortLink:
            '''Позволяет получить URL, сокращенный с помощью vk.cc. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"url": {"desc": "URL, для которого необходимо получить сокращенный вариант. строка, обязательный параметр", "type": "str", "default": "None"}, "private": {"desc": "1 — статистика ссылки приватная. 0 — статистика ссылки общедоступная. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}}
            def __call__(self, url, private : bool = None, v : str = None, access_token : str = None):
                self.exec_func("utils.getShortLink", url = url, private = private, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class resolveScreenName:
            '''Определяет тип объекта (пользователь, сообщество, приложение) и его идентификатор по короткому имени screen_name. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"screen_name": {"desc": "короткое имя пользователя, группы или приложения. Например, apiclub, andrew или rules_of_war. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, screen_name, v : str = None, access_token : str = None):
                self.exec_func("utils.resolveScreenName", screen_name = screen_name, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class video:
        def  __init__(self, exec_func):
            self.add = self.add(exec_func)
            self.addAlbum = self.addAlbum(exec_func)
            self.addToAlbum = self.addToAlbum(exec_func)
            self.createComment = self.createComment(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteAlbum = self.deleteAlbum(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.edit = self.edit(exec_func)
            self.editAlbum = self.editAlbum(exec_func)
            self.editComment = self.editComment(exec_func)
            self.get = self.get(exec_func)
            self.getAlbumById = self.getAlbumById(exec_func)
            self.getAlbums = self.getAlbums(exec_func)
            self.getAlbumsByVideo = self.getAlbumsByVideo(exec_func)
            self.getComments = self.getComments(exec_func)
            self.removeFromAlbum = self.removeFromAlbum(exec_func)
            self.reorderAlbums = self.reorderAlbums(exec_func)
            self.reorderVideos = self.reorderVideos(exec_func)
            self.report = self.report(exec_func)
            self.reportComment = self.reportComment(exec_func)
            self.restore = self.restore(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
            self.save = self.save(exec_func)
            self.search = self.search(exec_func)
        class add:
            '''Добавляет видеозапись в список пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"target_id": {"desc": "идентификатор пользователя или сообщества, в которое нужно добавить видео. \nОбратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком \"-\" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, video_id, owner_id, target_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.add", target_id = target_id, video_id = video_id, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addAlbum:
            '''Создает пустой альбом видеозаписей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (если необходимо создать альбом в сообществе). положительное число", "type": "int", "default": "None"}, "title": {"desc": "название альбома. строка", "type": "str", "default": "None"}, "privacy": {"desc": "настройки доступа к альбому в специальном формате. \nПриватность доступна для альбомов с видео в профиле пользователя. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, group_id : int = None, title : str = None, privacy : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.addAlbum", group_id = group_id, title = title, privacy = privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class addToAlbum:
            '''Позволяет добавить видеозапись в альбом. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"target_id": {"desc": "идентификатор владельца альбома, в который нужно добавить видео. \nОбратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком \"-\" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома, в который нужно добавить видео. \nДля добавления видео в общий альбом «Добавленные» передавайте -2. целое число", "type": "int", "default": "None"}, "album_ids": {"desc": "идентификаторы альбомов, в которые нужно добавить видео. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца видеозаписи. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, video_id, target_id : int = None, album_id : int = None, album_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.addToAlbum", target_id = target_id, album_id = album_id, album_ids = album_ids, owner_id = owner_id, video_id = video_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Cоздает новый комментарий к видеозаписи '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "video_id": {"desc": "идентификатор видеозаписи. целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст комментария. Обязательный параметр, если не задан параметр attachments. строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "from_group": {"desc": "этот параметр учитывается, если owner_id < 0 (комментарий к видеозаписи группы). 1 — комментарий будет опубликован от имени группы, 0 — комментарий будет опубликован от имени пользователя. по умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "reply_to_comment": {"desc": "идентификатор комментария, в ответ на который должен быть добавлен новый комментарий. положительное число", "type": "int", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, video_id, owner_id : int = None, message : str = None, attachments : str = None, from_group : bool = None, reply_to_comment : int = None, sticker_id : int = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.createComment", owner_id = owner_id, video_id = video_id, message = message, attachments = attachments, from_group = from_group, reply_to_comment = reply_to_comment, sticker_id = sticker_id, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет видеозапись со страницы пользователя. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "target_id": {"desc": "идентификатор пользователя или сообщества, для которого нужно удалить видеозапись. \nОбратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком \"-\" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}}
            def __call__(self, video_id, owner_id : int = None, target_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.delete", video_id = video_id, owner_id = owner_id, target_id = target_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteAlbum:
            '''Удаляет альбом видеозаписей. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (если альбом, который необходимо удалить, принадлежит сообществу). положительное число", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор альбома. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, album_id, group_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.deleteAlbum", group_id = group_id, album_id = album_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет комментарий к видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.deleteComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует данные видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "video_id": {"desc": "идентификатор видеозаписи. целое число, обязательный параметр", "type": "int", "default": "None"}, "name": {"desc": "новое название для видеозаписи. строка", "type": "str", "default": "None"}, "desc": {"desc": "новое описание для видеозаписи. строка", "type": "str", "default": "None"}, "privacy_view": {"desc": "настройки приватности просмотра видеозаписи в специальном формате. Приватность доступна для видеозаписей, которые пользователь загрузил в профиль. список слов, разделенных через запятую", "type": "str", "default": "None"}, "privacy_comment": {"desc": "настройки приватности комментирования видеозаписи в специальном формате. \nПриватность доступна для видеозаписей, которые пользователь загрузил в профиль. список слов, разделенных через запятую", "type": "str", "default": "None"}, "no_comments": {"desc": "закрыть комментарии (для видео из сообществ). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "repeat": {"desc": "зацикливание воспроизведения видеозаписи. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, video_id, owner_id : int = None, name : str = None, desc : str = None, privacy_view : str = None, privacy_comment : str = None, no_comments : bool = None, repeat : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.edit", owner_id = owner_id, video_id = video_id, name = name, desc = desc, privacy_view = privacy_view, privacy_comment = privacy_comment, no_comments = no_comments, repeat = repeat, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editAlbum:
            '''Редактирует альбом с видео. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"group_id": {"desc": "идентификатор сообщества (если нужно отредактировать альбом, принадлежащий сообществу). положительное число", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор альбома. положительное число, обязательный параметр", "type": "int", "default": "None"}, "title": {"desc": "новое название для альбома. строка, обязательный параметр", "type": "str", "default": "None"}, "privacy": {"desc": "уровень доступа к альбому в специальном формате. \nПриватность доступна для альбомов с видео в профиле пользователя. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, album_id, title, group_id : int = None, privacy : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.editAlbum", group_id = group_id, album_id = album_id, title = title, privacy = privacy, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Изменяет текст комментария к видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "новый текст комментария. Обязательный параметр, если не задан параметр attachments. строка", "type": "str", "default": "None"}, "attachments": {"desc": "новый список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nОбязательный параметр, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, message : str = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.editComment", owner_id = owner_id, comment_id = comment_id, message = message, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает информацию о видеозаписях. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежат видеозаписи. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "videos": {"desc": "перечисленные через запятую идентификаторы — идущие через знак подчеркивания id пользователей, которым принадлежат видеозаписи, и id самих видеозаписей. Если видеозапись принадлежит сообществу, то в качестве первого параметра используется -id сообщества.\nПример значения videos: \n-4363_136089719,13245770_137352259 \nНекоторые видеозаписи, идентификаторы которых могут быть получены через API, закрыты приватностью, и не будут получены. В этом случае следует использовать ключ доступа access_key в её идентификаторе. Пример значения videos: \n\n1_129207899_220df2876123d3542f, 6492_135055734_e0a9bcc31144f67fbd \nПоле access_key будет возвращено вместе с остальными данными видеозаписи в методах, которые возвращают видеозаписи, закрытые приватностью, но доступные в данном контексте. Например, данное поле имеют видеозаписи, возвращаемые методом messages.get. список слов, разделенных через запятую", "type": "str", "default": "None"}, "album_id": {"desc": "идентификатор альбома, видеозаписи из которого нужно вернуть. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых видеозаписей. положительное число, максимальное значение 200, по умолчанию 100", "type": "int", "default": "100"}, "offset": {"desc": "смещение относительно первой найденной видеозаписи для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "extended": {"desc": "определяет, возвращать ли информацию о настройках приватности видео для текущего пользователя. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, owner_id : int = None, videos : str = None, album_id : int = None, count : int = None, offset : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.get", owner_id = owner_id, videos = videos, album_id = album_id, count = count, offset = offset, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbumById:
            '''Позволяет получить информацию об альбоме с видео. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит альбом. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, album_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.getAlbumById", owner_id = owner_id, album_id = album_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbums:
            '''Возвращает список альбомов видеозаписей пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца альбомов (пользователь или сообщество). По умолчанию — идентификатор текущего пользователя. целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества альбомов. По умолчанию: 0. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество альбомов, информацию о которых нужно вернуть. По умолчанию: не больше 50, максимальное значение: 100. положительное число, по умолчанию 50, максимальное значение 100", "type": "int", "default": "50"}, "extended": {"desc": "1— возвращать дополнительные поля count, updated_time и массив объектов image для каждого альбома. Если альбом пустой, то массив объектов image для него возвращен не будет. По умолчанию: 0. \nПоля объекта image: \n\n\"height\" (integer) — Высота изображения.\n\n\"url\" (string) — Ссылка на изображение \n\n\"width\" (integer) — Ширина изображение \n\n\"with_padding\" (integer) — Поле возвращается, если изображение с отбивкой, всегда содержит 1.\n\nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "need_system": {"desc": "1 — возвращать системные альбомы. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, owner_id : int = None, offset : int = None, count : int = None, extended : bool = None, need_system : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.getAlbums", owner_id = owner_id, offset = offset, count = count, extended = extended, need_system = need_system, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getAlbumsByVideo:
            '''Возвращает список альбомов, в которых находится видеозапись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"target_id": {"desc": "идентификатор пользователя или сообщества, для которого нужно получить список альбомов, содержащих видеозапись. \nОбратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком \"-\" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "owner_id": {"desc": "идентификатор владельца видеозаписи. \nОбратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "extended": {"desc": "1 — возвращать расширенную информацию об альбомах. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, owner_id, video_id, target_id : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.getAlbumsByVideo", target_id = target_id, owner_id = owner_id, video_id = video_id, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список комментариев к видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — будет возвращено дополнительное поле likes. По умолчанию поле likes не возвращается. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_comment_id": {"desc": "идентификатор комментария, начиная с которого нужно вернуть список (подробности см. ниже). положительное число, доступен начиная с версии 5.33", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества комментариев. По умолчанию: 0. целое число", "type": "int", "default": "None"}, "count": {"desc": "количество комментариев, информацию о которых необходимо вернуть. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "sort": {"desc": "порядок сортировки комментариев. Возможные значения: \n\nasc — от старых к новым; \ndesc — от новых к старым. \nстрока", "type": "str", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, video_id, owner_id : int = None, need_likes : bool = None, start_comment_id : int = None, offset : int = None, count : int = None, sort : str = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.getComments", owner_id = owner_id, video_id = video_id, need_likes = need_likes, start_comment_id = start_comment_id, offset = offset, count = count, sort = sort, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class removeFromAlbum:
            '''Позволяет убрать видеозапись из альбома. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"target_id": {"desc": "идентификатор владельца альбома. Обратите внимание, идентификатор сообщества в параметре target_id необходимо указывать со знаком \"-\" — например, target_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома, из которого нужно убрать видео. целое число", "type": "int", "default": "None"}, "album_ids": {"desc": "идентификаторы альбомов, из которых нужно убрать видео. список целых чисел, разделенных запятыми", "type": "str", "default": "None"}, "owner_id": {"desc": "идентификатор владельца видеозаписи. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, обязательный параметр", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, video_id, target_id : int = None, album_id : int = None, album_ids : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.removeFromAlbum", target_id = target_id, album_id = album_id, album_ids = album_ids, owner_id = owner_id, video_id = video_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderAlbums:
            '''Позволяет изменить порядок альбомов с видео. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит альбом. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома, который нужно переместить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "before": {"desc": "идентификатор альбома, перед которым нужно поместить текущий. положительное число", "type": "int", "default": "None"}, "after": {"desc": "идентификатор альбома, после которого нужно поместить текущий. положительное число", "type": "int", "default": "None"}}
            def __call__(self, album_id, owner_id : int = None, before : int = None, after : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.reorderAlbums", owner_id = owner_id, album_id = album_id, before = before, after = after, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reorderVideos:
            '''Позволяет переместить видеозапись в альбоме. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"target_id": {"desc": "идентификатор пользователя или сообщества, в чьем альбоме нужно переместить видео. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "album_id": {"desc": "идентификатор альбома с видеозаписью, которую нужно переместить. целое число", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца видеозаписи, которую нужно переместить (пользователь или сообщество). целое число, обязательный параметр", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи, которую нужно переместить. положительное число, обязательный параметр", "type": "int", "default": "None"}, "before_owner_id": {"desc": "идентификатор владельца видеозаписи, перед которой следует поместить текущую (пользователь или сообщество). целое число", "type": "int", "default": "None"}, "before_video_id": {"desc": "идентификатор видеозаписи, перед которой следует поместить текущую. положительное число", "type": "int", "default": "None"}, "after_owner_id": {"desc": "идентификатор владельца видеозаписи, после которой следует поместить текущую (пользователь или сообщество). целое число", "type": "int", "default": "None"}, "after_video_id": {"desc": "идентификатор видеозаписи, после которой следует поместить текущую. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, video_id, target_id : int = None, album_id : int = None, before_owner_id : int = None, before_video_id : int = None, after_owner_id : int = None, after_video_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.reorderVideos", target_id = target_id, album_id = album_id, owner_id = owner_id, video_id = video_id, before_owner_id = before_owner_id, before_video_id = before_video_id, after_owner_id = after_owner_id, after_video_id = after_video_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class report:
            '''Позволяет пожаловаться на видеозапись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. целое число, обязательный параметр", "type": "int", "default": "None"}, "video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "тип жалобы. Возможные значения: \n\n0 — это спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число", "type": "int", "default": "None"}, "comment": {"desc": "комментарий для жалобы. строка", "type": "str", "default": "None"}, "search_query": {"desc": "поисковой запрос, если видеозапись была найдена через поиск. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, video_id, reason : int = None, comment : str = None, search_query : str = None, v : str = None, access_token : str = None):
                self.exec_func("video.report", owner_id = owner_id, video_id = video_id, reason = reason, comment = comment, search_query = search_query, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reportComment:
            '''Позволяет пожаловаться на комментарий к видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца видеозаписи, к которой оставлен комментарий. целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "тип жалобы. Возможные значения: \n\n0 — это спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, reason : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.reportComment", owner_id = owner_id, comment_id = comment_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Восстанавливает удаленную видеозапись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"video_id": {"desc": "идентификатор видеозаписи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "owner_id": {"desc": "идентификатор владельца видеозаписи (пользователь или сообщество). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}}
            def __call__(self, video_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.restore", video_id = video_id, owner_id = owner_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удаленный комментарий к видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит видеозапись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор удаленного комментария. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("video.restoreComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class save:
            '''Возвращает адрес сервера, необходимый для загрузки, и данные видеозаписи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"name": {"desc": "название видеофайла. строка", "type": "str", "default": "None"}, "description": {"desc": "описание видеофайла. строка", "type": "str", "default": "None"}, "is_private": {"desc": "указывается 1, если видео загружается для отправки личным сообщением. После загрузки с этим параметром видеозапись не будет отображаться в списке видеозаписей пользователя и не будет доступна другим пользователям по ее идентификатору. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "wallpost": {"desc": "требуется ли после сохранения опубликовать запись с видео на стене (1 — требуется, 0 — не требуется). \nОбратите внимание, для публикации записи на стене приложение должно иметь права wall. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "link": {"desc": "url для встраивания видео с внешнего сайта, например, с Youtube. В этом случае нужно вызвать полученный upload_url, не прикрепляя файл, достаточно просто обратиться по этому адресу. строка", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, в которое будет сохранен видеофайл. По умолчанию файл сохраняется на страницу текущего пользователя. положительное число", "type": "int", "default": "None"}, "album_id": {"desc": "идентификатор альбома, в который будет загружен видео файл. положительное число", "type": "int", "default": "None"}, "privacy_view": {"desc": "настройки приватности просмотра видеозаписи в специальном формате. Приватность доступна для видеозаписей, которые пользователь загрузил в профиль. список слов, разделенных через запятую", "type": "str", "default": "None"}, "privacy_comment": {"desc": "настройки приватности комментирования видеозаписи в специальном формате. \nПриватность доступна для видеозаписей, которые пользователь загрузил в профиль. список слов, разделенных через запятую", "type": "str", "default": "None"}, "no_comments": {"desc": "1 — закрыть комментарии (для видео из сообществ). По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "repeat": {"desc": "зацикливание воспроизведения видеозаписи. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "compression": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, name : str = None, description : str = None, is_private : bool = None, wallpost : bool = None, link : str = None, group_id : int = None, album_id : int = None, privacy_view : str = None, privacy_comment : str = None, no_comments : bool = None, repeat : bool = None, compression : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.save", name = name, description = description, is_private = is_private, wallpost = wallpost, link = link, group_id = group_id, album_id = album_id, privacy_view = privacy_view, privacy_comment = privacy_comment, no_comments = no_comments, repeat = repeat, compression = compression, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Возвращает список видеозаписей в соответствии с заданным критерием поиска. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"q": {"desc": "строка поискового запроса. Например, The Beatles. строка, обязательный параметр", "type": "str", "default": "None"}, "sort": {"desc": "сортировка результатов. Возможные значения: \n\n0 — по дате добавления видеозаписи; \n1 — по длительности; \n2 — по релевантности. \nцелое число", "type": "int", "default": "None"}, "hd": {"desc": "если не равен нулю, то поиск производится только по видеозаписям высокого качества. целое число", "type": "int", "default": "None"}, "adult": {"desc": "фильтр «Безопасный поиск». Возможные значения: \n\n1 — выключен; \n0 — включен. \nфлаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "filters": {"desc": "список критериев, по которым требуется отфильтровать видео: \n\nmp4 — искать только видео в формате mp4 (воспроизводимое на iOS); \nyoutube — возвращать только youtube видео; \nvimeo — возвращать только vimeo видео; \nshort — возвращать только короткие видеозаписи; \nlong — возвращать только длинные видеозаписи. \nсписок слов, разделенных через запятую", "type": "str", "default": "None"}, "search_own": {"desc": "1 — искать по видеозаписям пользователя, 0 — не искать по видеозаписям пользователя. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "offset": {"desc": "смещение относительно первой найденной видеозаписи для выборки определенного подмножества. положительное число", "type": "int", "default": "None"}, "longer": {"desc": "количество секунд, видеозаписи длиннее которого необходимо вернуть. положительное число", "type": "int", "default": "None"}, "shorter": {"desc": "количество секунд, видеозаписи короче которого необходимо вернуть. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество возвращаемых видеозаписей. Обратите внимание — даже при использовании параметра offset для получения информации доступны только первые 1000 результатов. \n положительное число, по умолчанию 20, максимальное значение 200", "type": "int", "default": "20"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0, по умолчанию 0", "type": "bool", "default": "0"}}
            def __call__(self, q, sort : int = None, hd : int = None, adult : bool = None, filters : str = None, search_own : bool = None, offset : int = None, longer : int = None, shorter : int = None, count : int = None, extended : bool = None, v : str = None, access_token : str = None):
                self.exec_func("video.search", q = q, sort = sort, hd = hd, adult = adult, filters = filters, search_own = search_own, offset = offset, longer = longer, shorter = shorter, count = count, extended = extended, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class wall:
        def  __init__(self, exec_func):
            self.checkCopyrightLink = self.checkCopyrightLink(exec_func)
            self.closeComments = self.closeComments(exec_func)
            self.createComment = self.createComment(exec_func)
            self.delete = self.delete(exec_func)
            self.deleteComment = self.deleteComment(exec_func)
            self.edit = self.edit(exec_func)
            self.editAdsStealth = self.editAdsStealth(exec_func)
            self.editComment = self.editComment(exec_func)
            self.get = self.get(exec_func)
            self.getById = self.getById(exec_func)
            self.getComment = self.getComment(exec_func)
            self.getComments = self.getComments(exec_func)
            self.getReposts = self.getReposts(exec_func)
            self.openComments = self.openComments(exec_func)
            self.pin = self.pin(exec_func)
            self.post = self.post(exec_func)
            self.postAdsStealth = self.postAdsStealth(exec_func)
            self.reportComment = self.reportComment(exec_func)
            self.reportPost = self.reportPost(exec_func)
            self.repost = self.repost(exec_func)
            self.restore = self.restore(exec_func)
            self.restoreComment = self.restoreComment(exec_func)
            self.search = self.search(exec_func)
            self.unpin = self.unpin(exec_func)
        class checkCopyrightLink:
            '''Проверяет ссылку для указания источника. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"link": {"desc": "ссылка на источник. Поддерживаются внешние и внутренние ссылки. строка, обязательный параметр", "type": "str", "default": "None"}}
            def __call__(self, link, v : str = None, access_token : str = None):
                self.exec_func("wall.checkCopyrightLink", link = link, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class closeComments:
            '''Выключает комментирование записи '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "целое число, обязательный параметр", "type": "int", "default": "None"}, "post_id": {"desc": "положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, post_id, v : str = None, access_token : str = None):
                self.exec_func("wall.closeComments", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class createComment:
            '''Добавляет комментарий к записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на чьей стене находится запись, к которой необходимо добавить комментарий. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число, обязательный параметр", "type": "int", "default": "None"}, "from_group": {"desc": "идентификатор сообщества, от имени которого публикуется комментарий. По умолчанию: 0. положительное число", "type": "int", "default": "None"}, "message": {"desc": "текст комментария. Обязательный параметр, если не передан параметр attachments. строка, строка", "type": "str", "default": "None"}, "reply_to_comment": {"desc": "идентификатор комментария, в ответ на который должен быть добавлен новый комментарий. целое число", "type": "int", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "sticker_id": {"desc": "идентификатор стикера. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинакового комментария. строка", "type": "str", "default": "None"}}
            def __call__(self, post_id, owner_id : int = None, from_group : int = None, message : str = None, reply_to_comment : int = None, attachments : str = None, sticker_id : int = None, guid : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.createComment", owner_id = owner_id, post_id = post_id, from_group = from_group, message = message, reply_to_comment = reply_to_comment, attachments = attachments, sticker_id = sticker_id, guid = guid, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class delete:
            '''Удаляет запись со стены. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id : int = None, post_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.delete", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class deleteComment:
            '''Удаляет комментарий к записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя, на чьей стене находится комментарий к записи. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.deleteComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class edit:
            '''Редактирует запись на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число, обязательный параметр", "type": "int", "default": "None"}, "friends_only": {"desc": "1 — запись будет доступна только друзьям, 0 — всем пользователям. \nПараметр учитывается только при редактировании отложенной записи. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message": {"desc": "текст сообщения (является обязательным, если не задан параметр attachments) строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к записи и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-приложения:\n\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ \ngraffiti — граффити \npage — wiki-страница \nnote — заметка \npoll — опрос \nalbum — альбом. \n\n<owner_id> — идентификатор владельца медиа-приложения;\n<media_id> — идентификатор медиа-приложения.\n\nНапример:\nphoto100172_166443618,photo66748_265827614\n\nТакже в поле attachments может быть указана ссылка на внешнюю страницу, которую Вы хотите разместить в статусе, например:\nphoto66748_265827614,http://habrahabr.ru\n\nПри попытке приложить больше одной ссылки будет возвращена ошибка. \n\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "services": {"desc": "список сервисов или сайтов, на которые необходимо экспортировать запись, в случае если пользователь настроил соответствующую опцию. Например, twitter, facebook. \nПараметр учитывается только при редактировании отложенной записи. строка", "type": "str", "default": "None"}, "signed": {"desc": "1 — у записи, размещенной от имени сообщества будет добавлена подпись (имя пользователя, разместившего запись), 0 — подписи добавлено не будет. \nПараметр учитывается только при редактировании записи на стене сообщества, опубликованной от имени группы. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "publish_date": {"desc": "дата публикации записи в формате unixtime. Если параметр не указан, отложенная запись будет опубликована. \nПараметр учитывается только при редактировании отложенной записи. положительное число", "type": "int", "default": "None"}, "lat": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "place_id": {"desc": "идентификатор места, в котором отмечен пользователь. положительное число", "type": "int", "default": "None"}, "mark_as_ads": {"desc": "1 — у записи, размещенной от имени сообщества, будет добавлена метка \"это реклама\", 0 — метки добавлено не будет/снять установленную метку. Метка может быть снята в течение пяти минут после её установки. В сутки может быть опубликовано не более пяти рекламных записей, из которых не более трёх — вне Биржи ВКонтакте. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "close_comments": {"desc": "1 — комментарии к записи отключены. \n0 — комментарии к записи включены. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "donut_paid_duration": {"desc": "период времени в течение которого запись будет доступна для донов — платных подписчиков VK Donut. Возможные значения: \n\n-1 —  исключительно для донов; \n86400 — на 1 день; \n172800 — на 2 дня; \n172800 — на 3 дня; \n345600 — на 4 дня; \n432000 — на 5 дней; \n518400 — на 6 дней; \n604800 — на 7 дней. \nцелое число, доступен начиная с версии 5.125", "type": "int", "default": "None"}, "poster_bkg_id": {"desc": "положительное число", "type": "int", "default": "None"}, "poster_bkg_owner_id": {"desc": "целое число", "type": "int", "default": "None"}, "poster_bkg_access_hash": {"desc": "строка", "type": "str", "default": "None"}, "copyright": {"desc": "источник материала. Поддерживаются внешние и внутренние ссылки. строка", "type": "str", "default": "None"}}
            def __call__(self, post_id, owner_id : int = None, friends_only : bool = None, message : str = None, attachments : str = None, services : str = None, signed : bool = None, publish_date : int = None, lat : int = None, long : int = None, place_id : int = None, mark_as_ads : bool = None, close_comments : bool = None, donut_paid_duration : int = None, poster_bkg_id : int = None, poster_bkg_owner_id : int = None, poster_bkg_access_hash : str = None, copyright : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.edit", owner_id = owner_id, post_id = post_id, friends_only = friends_only, message = message, attachments = attachments, services = services, signed = signed, publish_date = publish_date, lat = lat, long = long, place_id = place_id, mark_as_ads = mark_as_ads, close_comments = close_comments, donut_paid_duration = donut_paid_duration, poster_bkg_id = poster_bkg_id, poster_bkg_owner_id = poster_bkg_owner_id, poster_bkg_access_hash = poster_bkg_access_hash, copyright = copyright, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editAdsStealth:
            '''Позволяет отредактировать скрытую запись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца стены (идентификатор сообщества нужно указывать со знаком «минус»). целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст записи. строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к записи и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-приложения: \n\nphoto — фотография; \nvideo — видеозапись ; \naudio — аудиозапись; \ndoc — документ; \npage — wiki-страница; \nnote — заметка; \npoll — опрос; \nalbum — альбом; \nmarket — товар; \nmarket_album — подборка товаров. \n\n<owner_id> — идентификатор владельца медиа-приложения (обратите внимание, если объект находится в сообществе, этот параметр должен быть отрицательным). \n<media_id> — идентификатор медиа-приложения. \n\nНапример:\nphoto100172_166443618,photo-1_265827614\n\nТакже в поле attachments может быть указана ссылка на внешнюю страницу, которую Вы хотите разместить в записи, например:\nphoto66748_265827614,http://habrahabr.ru\n\nВ качестве ссылки может быть использован телефонный номер  в формате tel:+71234567890\n\nПри попытке приложить больше одной ссылки будет возвращена ошибка. \n\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "signed": {"desc": "1 — у записи, размещенной от имени сообщества, будет добавлена подпись (имя пользователя, разместившего запись), 0 — без подписи. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "lat": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "place_id": {"desc": "идентификатор места. положительное число", "type": "int", "default": "None"}, "link_button": {"desc": "идентификатор кнопки, которую необходимо добавить к сниппету для ссылки. Подробнее см. документацию метода wall.postAdsStealth. строка", "type": "str", "default": "None"}, "link_title": {"desc": "заголовок, который должен быть использован для сниппета. Если не указан, будет автоматически получен с целевой ссылки. Обязательно указывать в случае, если ссылка является номером телефона. строка", "type": "str", "default": "None"}, "link_image": {"desc": "ссылка на изображение, которое должно быть использовано для сниппета. Минимальное разрешение: 537x240. Если не указана, будет автоматически загружена с целевой ссылки. Обязательно указывать в случае, если ссылка является номером телефона. Одновременно может быть указан либо параметр link_image, либо параметр link_video. строка", "type": "str", "default": "None"}, "link_video": {"desc": "идентификатор видео в формате \"<owner_id>_<media_id>\". Одновременно может быть указан либо параметр link_image, либо параметр link_video. Кроме того, параметр link_video может быть указан только вместе с параметрами  link_button, link_title. строка", "type": "str", "default": "None"}}
            def __call__(self, post_id, owner_id : int = None, message : str = None, attachments : str = None, signed : bool = None, lat : int = None, long : int = None, place_id : int = None, link_button : str = None, link_title : str = None, link_image : str = None, link_video : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.editAdsStealth", owner_id = owner_id, post_id = post_id, message = message, attachments = attachments, signed = signed, lat = lat, long = long, place_id = place_id, link_button = link_button, link_title = link_title, link_image = link_image, link_video = link_video, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class editComment:
            '''Редактирует комментарий на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца стены. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария, который необходимо отредактировать. положительное число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "новый текст комментария. Обязательный параметр, если не передан параметр attachments. строка", "type": "str", "default": "None"}, "attachments": {"desc": "новые вложения к комментарию. Список объектов, приложенных к комментарию и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n<type> — тип медиа-вложения:\nphoto — фотография \nvideo — видеозапись \naudio — аудиозапись \ndoc — документ\n<owner_id> — идентификатор владельца медиа-вложения \n<media_id> — идентификатор медиа-вложения. \n\nНапример:\nphoto100172_166443618,photo66748_265827614\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, message : str = None, attachments : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.editComment", owner_id = owner_id, comment_id = comment_id, message = message, attachments = attachments, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class get:
            '''Возвращает список записей со стены пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, со стены которого необходимо получить записи (по умолчанию — текущий пользователь). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}, "domain": {"desc": "короткий адрес пользователя или сообщества. строка", "type": "str", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества записей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество записей, которое необходимо получить. Максимальное значение: 100. положительное число", "type": "int", "default": "None"}, "filter": {"desc": "определяет, какие типы записей на стене необходимо получить. Возможные значения: \n\nsuggests — предложенные записи на стене сообщества (доступно только при вызове с передачей access_token); \npostponed — отложенные записи (доступно только при вызове с передачей access_token); \nowner — записи владельца стены; \nothers — записи не от владельца стены; \nall — все записи на стене (owner + others). \nПо умолчанию: all. строка", "type": "str", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и сообществ, которые необходимо вернуть. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id : int = None, domain : str = None, offset : int = None, count : int = None, filter : str = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.get", owner_id = owner_id, domain = domain, offset = offset, count = count, filter = filter, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getById:
            '''Возвращает список записей со стен пользователей или сообществ по их идентификаторам. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"posts": {"desc": "перечисленные через запятую идентификаторы, которые представляют собой идущие через знак подчеркивания id владельцев стен и id самих записей на стене. Максимум 100 идентификаторов.\nПример значения posts:\n93388_21539,93388_20904,-1_340364 список слов, разделенных через запятую, обязательный параметр", "type": "str", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "copy_history_depth": {"desc": "определяет размер массива copy_history, возвращаемого в ответе, если запись является репостом записи с другой стены. \nНапример, copy_history_depth=1 — copy_history будет содержать один элемент с информацией о записи, прямым репостом которой является текущая. \ncopy_history_depth=2 — copy_history будет содержать два элемента, добавляется информация о записи, репостом которой является первый элемент, и так далее (при условии, что иерархия репостов требуемой глубины для текущей записи существует). целое число, по умолчанию 2", "type": "int", "default": "2"}, "fields": {"desc": "список дополнительных полей для профилей и  групп, которые необходимо вернуть. См. описание полей объекта user и описание полей объекта group. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, posts, extended : bool = None, copy_history_depth : int = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.getById", posts = posts, extended = extended, copy_history_depth = copy_history_depth, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComment:
            '''Получает информацию о комментарии на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца стены (для сообществ — со знаком «минус»). целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и сообществ, которые необходимо вернуть. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.getComment", owner_id = owner_id, comment_id = comment_id, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getComments:
            '''Возвращает список комментариев к записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца страницы (пользователь или сообщество). Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число", "type": "int", "default": "None"}, "need_likes": {"desc": "1 — возвращать информацию о лайках. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "start_comment_id": {"desc": "идентификатор комментария, начиная с которого нужно вернуть список (подробности см. ниже). положительное число, доступен начиная с версии 5.33", "type": "int", "default": "None"}, "offset": {"desc": "сдвиг, необходимый для получения конкретной выборки результатов. целое число", "type": "int", "default": "None"}, "count": {"desc": "число комментариев, которые необходимо получить. По умолчанию: 10, максимальное значение: 100. положительное число", "type": "int", "default": "None"}, "sort": {"desc": "порядок сортировки комментариев. Возможные значения: \n\nasc — от старых к новым; \ndesc — от новых к старым. \nстрока", "type": "str", "default": "None"}, "preview_length": {"desc": "количество символов, по которому нужно обрезать текст комментария. Укажите 0, если Вы не хотите обрезать текст. положительное число", "type": "int", "default": "None"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и сообществ, которые необходимо вернуть. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}, "comment_id": {"desc": "идентификатор комментария, ветку которого нужно получить. положительное число, доступен начиная с версии 5.91", "type": "int", "default": "None"}, "thread_items_count": {"desc": "максимальное число элементов в поле thread. целое число, максимальное значение 10, минимальное значение 0, по умолчанию 0, доступен начиная с версии 5.91", "type": "int", "default": "0"}}
            def __call__(self, owner_id : int = None, post_id : int = None, need_likes : bool = None, start_comment_id : int = None, offset : int = None, count : int = None, sort : str = None, preview_length : int = None, extended : bool = None, fields : str = None, comment_id : int = None, thread_items_count : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.getComments", owner_id = owner_id, post_id = post_id, need_likes = need_likes, start_comment_id = start_comment_id, offset = offset, count = count, sort = sort, preview_length = preview_length, extended = extended, fields = fields, comment_id = comment_id, thread_items_count = thread_items_count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getReposts:
            '''Позволяет получать список репостов заданной записи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится запись. Если параметр не задан, то он считается равным идентификатору текущего пользователя. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число", "type": "int", "default": "None"}, "offset": {"desc": "смещение, необходимое для выборки определенного подмножества записей. положительное число", "type": "int", "default": "None"}, "count": {"desc": "количество записей, которое необходимо получить. положительное число, по умолчанию 20, максимальное значение 1000", "type": "int", "default": "20"}}
            def __call__(self, owner_id : int = None, post_id : int = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.getReposts", owner_id = owner_id, post_id = post_id, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class openComments:
            '''Включает комментирование записи '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "целое число, обязательный параметр", "type": "int", "default": "None"}, "post_id": {"desc": "положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, owner_id, post_id, v : str = None, access_token : str = None):
                self.exec_func("wall.openComments", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class pin:
            '''Закрепляет запись на стене (запись будет отображаться выше остальных). '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, post_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.pin", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class post:
            '''Позволяет создать запись на стене, предложить запись на стене публичной страницы, опубликовать существующую отложенную запись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого должна быть опубликована запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "friends_only": {"desc": "1 — запись будет доступна только друзьям, 0 — всем пользователям. По умолчанию публикуемые записи доступны всем пользователям. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "from_group": {"desc": "данный параметр учитывается, если owner_id < 0 (запись публикуется на стене группы). 1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя (по умолчанию). флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "message": {"desc": "текст сообщения (является обязательным, если не задан параметр attachments) строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к записи и разделённых символом \",\". Поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-приложения: \n\nphoto — фотография; \nvideo — видеозапись ; \naudio — аудиозапись; \ndoc — документ; \npage — wiki-страница; \nnote — заметка; \npoll — опрос; \nalbum — альбом; \nmarket — товар; \nmarket_album — подборка товаров; \naudio_playlist — плейлист с аудио. \n\n<owner_id> — идентификатор владельца медиа-приложения (обратите внимание, если объект находится в сообществе, этот параметр должен быть отрицательным). \n<media_id> — идентификатор медиа-приложения. \n\nНапример:\nphoto100172_166443618,photo-1_265827614\n\nТакже в поле attachments может быть указана ссылка на внешнюю страницу, которую Вы хотите разместить в записи, например:\nphoto66748_265827614,http://habrahabr.ru\n\nПри попытке приложить больше одной ссылки будет возвращена ошибка. \n\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "services": {"desc": "список сервисов или сайтов, на которые необходимо экспортировать запись, в случае если пользователь настроил соответствующую опцию. Например, twitter, facebook. строка", "type": "str", "default": "None"}, "signed": {"desc": "1 — у записи, размещенной от имени сообщества, будет добавлена подпись (имя пользователя, разместившего запись), 0 — подписи добавлено не будет. Параметр учитывается только при публикации на стене сообщества и указании параметра from_group. По умолчанию подпись не добавляется. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "publish_date": {"desc": "дата публикации записи в формате unixtime. Если параметр указан, публикация записи будет отложена до указанного времени. положительное число", "type": "int", "default": "None"}, "lat": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "place_id": {"desc": "идентификатор места, в котором отмечен пользователь. положительное число", "type": "int", "default": "None"}, "post_id": {"desc": "идентификатор записи, которую необходимо опубликовать. Данный параметр используется для публикации отложенных записей и предложенных новостей. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинаковой записи. Действует в течение одного часа. строка", "type": "str", "default": "None"}, "mark_as_ads": {"desc": "1 — у записи, размещенной от имени сообщества, будет добавлена метка \"это реклама\", 0 — метки добавлено не будет. В сутки может быть опубликовано не более пяти рекламных записей, из которых не более трёх — вне Биржи ВКонтакте. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "close_comments": {"desc": "1 — комментарии к записи отключены. \n0 — комментарии к записи включены. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "donut_paid_duration": {"desc": "период времени в течение которого запись будет доступна для донов — платных подписчиков VK Donut. Возможные значения: \n\n-1 —  исключительно для донов; \n86400 — на 1 день; \n172800 — на 2 дня; \n172800 — на 3 дня; \n345600 — на 4 дня; \n432000 — на 5 дней; \n518400 — на 6 дней; \n604800 — на 7 дней. \nцелое число, доступен начиная с версии 5.125", "type": "int", "default": "None"}, "mute_notifications": {"desc": "1 — уведомления к записи  отключены. \n0 — уведомления к записи включены. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "copyright": {"desc": "источник материала. Поддерживаются внешние и внутренние ссылки. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id : int = None, friends_only : bool = None, from_group : bool = None, message : str = None, attachments : str = None, services : str = None, signed : bool = None, publish_date : int = None, lat : int = None, long : int = None, place_id : int = None, post_id : int = None, guid : str = None, mark_as_ads : bool = None, close_comments : bool = None, donut_paid_duration : int = None, mute_notifications : bool = None, copyright : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.post", owner_id = owner_id, friends_only = friends_only, from_group = from_group, message = message, attachments = attachments, services = services, signed = signed, publish_date = publish_date, lat = lat, long = long, place_id = place_id, post_id = post_id, guid = guid, mark_as_ads = mark_as_ads, close_comments = close_comments, donut_paid_duration = donut_paid_duration, mute_notifications = mute_notifications, copyright = copyright, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class postAdsStealth:
            '''Позволяет создать скрытую запись, которая не попадает на стену сообщества и в дальнейшем может быть использована  для создания рекламного объявления типа "Запись в сообществе". '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор владельца стены (идентификатор сообщества нужно указывать со знаком «минус»). целое число, обязательный параметр", "type": "int", "default": "None"}, "message": {"desc": "текст записи. строка", "type": "str", "default": "None"}, "attachments": {"desc": "список объектов, приложенных к записи и разделённых символом \",\".\n\nВ поле может быть указана ссылка на страницу, которую Вы хотите разместить в записи, например:\nphoto66748_265827614,http://habrahabr.ru\n\nЛибо поле attachments представляется в формате:\n<type><owner_id>_<media_id>,<type><owner_id>_<media_id>\n\n<type> — тип медиа-приложения: \n\nphoto — фотография; \nvideo — видеозапись; \naudio — аудиозапись; \ndoc — документ; \npage — wiki-страница; \nnote — заметка; \npoll — опрос; \nalbum — альбом; \nmarket — товар; \nmarket_album — подборка товаров, \npretty_card — карточка карусели. \n\n<owner_id> — идентификатор владельца медиа-приложения (обратите внимание, если объект находится в сообществе, этот параметр должен быть отрицательным). \n<media_id> — идентификатор медиа-приложения. \n\nНапример:\nphoto100172_166443618,photo-1_265827614\n\nВ качестве ссылки может быть использован телефонный номер  в формате tel:+71234567890\n\nПри попытке приложить больше одной ссылки будет возвращена ошибка. \n\nПараметр является обязательным, если не задан параметр message. список слов, разделенных через запятую", "type": "str", "default": "None"}, "signed": {"desc": "1 — у записи, размещенной от имени сообщества, будет добавлена подпись (имя пользователя, разместившего запись), 0 — без подписи. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "lat": {"desc": "географическая широта отметки, заданная в градусах (от -90 до 90). дробное число", "type": "int", "default": "None"}, "long": {"desc": "географическая долгота отметки, заданная в градусах (от -180 до 180). дробное число", "type": "int", "default": "None"}, "place_id": {"desc": "идентификатор места. положительное число", "type": "int", "default": "None"}, "guid": {"desc": "уникальный идентификатор, предназначенный для предотвращения повторной отправки одинаковой записи. строка", "type": "str", "default": "None"}, "link_button": {"desc": "идентификатор кнопки, которую необходимо добавить к сниппету для ссылки. \nlink_button Текст Действие Тип ссылок auto (автовыбор) (автовыбор) Все app_join Запустить Переход по ссылке Приложения и игры app_game_join Играть Переход по ссылке Игры open_url Перейти Переход по ссылке Внешние сайты, сообщества, приложения open Открыть Переход по ссылке Внешние сайты more Подробнее Переход по ссылке Сообщества call Позвонить Набор номера Телефонные номера book Забронировать Набор номера Телефонные номера enroll Записаться Переход по ссылке или набор номера Внешние сайты, телефонные номера register Зарегистрироваться Набор номера Телефонные номера buy Купить Переход по ссылке Внешние сайты buy_ticket Купить билет Переход по ссылке Внешние сайты order Заказать Переход по ссылке Внешние сайты create Создать Переход по ссылке Внешние сайты install Установить Переход по ссылке Внешние сайты contact Связаться Переход по ссылке Внешние сайты fill Заполнить Переход по ссылке Внешние сайты join_public Подписаться Подписка на публичную страницу Публичные страницы join_event Я пойду Участие в мероприятии События join Вступить Вступление в сообщество Сообщества im Связаться Переход к диалогу с сообществом Сообщества, публичные страницы, события im2 Написать Переход к диалогу с сообществом Сообщества, публичные страницы, события begin Начать Переход по ссылке Внешние сайты get Получить Переход по ссылке Внешние сайты watch Смотреть Переход по ссылке Внешние сайты download Скачать Переход по ссылке Внешние сайты participate Участвовать Переход по ссылке Внешние сайты play Играть Переход по ссылке Внешние сайты apply Подать заявку Переход по ссылке Внешние сайты get_an_offer Получить предложение Переход по ссылке Внешние сайты to_write Написать Переход по ссылке Внешние сайты reply Откликнуться Переход по ссылке Внешние сайты  строка", "type": "str", "default": "None"}, "link_title": {"desc": "заголовок, который должен быть использован для сниппета. Если не указан, будет автоматически получен с целевой ссылки. Обязательно указывать в случае, если ссылка является номером телефона. строка", "type": "str", "default": "None"}, "link_image": {"desc": "ссылка на изображение, которое должно быть использовано для сниппета. Минимальное разрешение: 537x240. Если не указана, будет автоматически загружена с целевой ссылки. Обязательно указывать в случае, если ссылка является номером телефона. Одновременно может быть указан либо параметр link_image, либо параметр link_video. строка", "type": "str", "default": "None"}, "link_video": {"desc": "идентификатор видео в формате \"<owner_id>_<media_id>\". Одновременно может быть указан либо параметр link_image, либо параметр link_video. Кроме того, параметр link_video может быть указан только вместе с параметрами  link_button, link_title. строка", "type": "str", "default": "None"}}
            def __call__(self, owner_id, message : str = None, attachments : str = None, signed : bool = None, lat : int = None, long : int = None, place_id : int = None, guid : str = None, link_button : str = None, link_title : str = None, link_image : str = None, link_video : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.postAdsStealth", owner_id = owner_id, message = message, attachments = attachments, signed = signed, lat = lat, long = long, place_id = place_id, guid = guid, link_button = link_button, link_title = link_title, link_image = link_image, link_video = link_video, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reportComment:
            '''Позволяет пожаловаться на комментарий к записи. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит комментарий. целое число, обязательный параметр", "type": "int", "default": "None"}, "comment_id": {"desc": "идентификатор комментария. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление; \n8 — призывы к суициду. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, comment_id, reason : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.reportComment", owner_id = owner_id, comment_id = comment_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class reportPost:
            '''Позволяет пожаловаться на запись. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, которому принадлежит запись. целое число, обязательный параметр", "type": "int", "default": "None"}, "post_id": {"desc": "идентификатор записи. положительное число, обязательный параметр", "type": "int", "default": "None"}, "reason": {"desc": "причина жалобы: \n\n0 — спам; \n1 — детская порнография; \n2 — экстремизм; \n3 — насилие; \n4 — пропаганда наркотиков; \n5 — материал для взрослых; \n6 — оскорбление; \n8 — призывы к суициду. \nположительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id, post_id, reason : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.reportPost", owner_id = owner_id, post_id = post_id, reason = reason, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class repost:
            '''Копирует объект на стену пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"object": {"desc": "строковый идентификатор объекта, который необходимо разместить на стене, например, wall66748_3675 или wall-1_340364. \nФормируется из типа объекта (wall, photo, video и т.п.), идентификатора владельца объекта и идентификатора самого объекта. строка, обязательный параметр", "type": "str", "default": "None"}, "message": {"desc": "сопроводительный текст, который будет добавлен к записи с объектом. строка", "type": "str", "default": "None"}, "group_id": {"desc": "идентификатор сообщества, на стене которого будет размещена запись с объектом. Если не указан, запись будет размещена на стене текущего пользователя. положительное число", "type": "int", "default": "None"}, "mark_as_ads": {"desc": "1 — пометить запись как рекламную. флаг, может принимать значения 1 или 0, по умолчанию ", "type": "bool", "default": ""}, "mute_notifications": {"desc": "флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}}
            def __call__(self, object, message : str = None, group_id : int = None, mark_as_ads : bool = None, mute_notifications : bool = None, v : str = None, access_token : str = None):
                self.exec_func("wall.repost", object = object, message = message, group_id = group_id, mark_as_ads = mark_as_ads, mute_notifications = mute_notifications, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restore:
            '''Восстанавливает удаленную запись на стене пользователя или сообщества. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находилась удаленная запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число", "type": "int", "default": "None"}}
            def __call__(self, owner_id : int = None, post_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.restore", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class restoreComment:
            '''Восстанавливает удаленный комментарий к записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится комментарий к записи. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "comment_id": {"desc": "идентификатор комментария на стене. целое число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, comment_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.restoreComment", owner_id = owner_id, comment_id = comment_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class search:
            '''Позволяет искать записи на стене в соответствии с заданными критериями. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число", "type": "int", "default": "None"}, "domain": {"desc": "короткий адрес пользователя или сообщества. строка", "type": "str", "default": "None"}, "query": {"desc": "поисковой запрос. Для точного результата запрос необходимо передавать в двойных кавычках. строка", "type": "str", "default": "None"}, "owners_only": {"desc": "1 — возвращать только записи от имени владельца стены. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "count": {"desc": "количество записей, которые необходимо вернуть. положительное число, по умолчанию 20, максимальное значение 100", "type": "int", "default": "20"}, "offset": {"desc": "смещение, необходимо для получения определенного подмножества результатов. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "extended": {"desc": "1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах. По умолчанию: 0. флаг, может принимать значения 1 или 0", "type": "bool", "default": "None"}, "fields": {"desc": "список дополнительных полей для профилей и  групп, которые необходимо вернуть. См. описание полей объекта user и описание полей объекта group. \nОбратите внимание, этот параметр учитывается только при extended=1. список слов, разделенных через запятую", "type": "str", "default": "None"}}
            def __call__(self, owner_id : int = None, domain : str = None, query : str = None, owners_only : bool = None, count : int = None, offset : int = None, extended : bool = None, fields : str = None, v : str = None, access_token : str = None):
                self.exec_func("wall.search", owner_id = owner_id, domain = domain, query = query, owners_only = owners_only, count = count, offset = offset, extended = extended, fields = fields, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class unpin:
            '''Отменяет закрепление записи на стене. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"owner_id": {"desc": "идентификатор пользователя или сообщества, на стене которого находится запись. Обратите внимание, идентификатор сообщества в параметре owner_id необходимо указывать со знаком \"-\" — например, owner_id=-1 соответствует идентификатору сообщества ВКонтакте API (club1)  целое число, по умолчанию идентификатор текущего пользователя", "type": "int", "default": "идентификатор текущего пользователя"}, "post_id": {"desc": "идентификатор записи на стене. положительное число, обязательный параметр", "type": "int", "default": "None"}}
            def __call__(self, post_id, owner_id : int = None, v : str = None, access_token : str = None):
                self.exec_func("wall.unpin", owner_id = owner_id, post_id = post_id, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

    class widgets:
        def  __init__(self, exec_func):
            self.getComments = self.getComments(exec_func)
            self.getPages = self.getPages(exec_func)
        class getComments:
            '''Получает список комментариев к странице, оставленных через Виджет комментариев. '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"widget_api_id": {"desc": "Идентификатор приложения/сайта, с которым инициализируются виджеты. целое число", "type": "int", "default": "None"}, "url": {"desc": "URL-адрес страницы. строка", "type": "str", "default": "None"}, "page_id": {"desc": "внутренний идентификатор страницы в приложении/сайте (в случае, если для инициализации виджетов использовался параметр page_id). строка", "type": "str", "default": "None"}, "order": {"desc": "тип сортировки комментариев. Возможные значения: date, likes, last_comment. Значение по умолчанию - date. строка, по умолчанию date", "type": "str", "default": "date"}, "fields": {"desc": "перечисленные через запятую поля анкет необходимые для получения. Если среди полей присутствует replies, будут возвращены последние комментарии второго уровня для каждого комментария первого уровня. список слов, разделенных через запятую", "type": "str", "default": "None"}, "offset": {"desc": "смещение необходимое для выборки определенного подмножества комментариев. По умолчанию 0. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество возвращаемых записей. положительное число, по умолчанию 10, минимальное значение 10, максимальное значение 200", "type": "int", "default": "10"}}
            def __call__(self, widget_api_id : int = None, url : str = None, page_id : str = None, order : str = None, fields : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("widgets.getComments", widget_api_id = widget_api_id, url = url, page_id = page_id, order = order, fields = fields, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__

        class getPages:
            '''Получает список страниц приложения/сайта, на которых установлен Виджет комментариев или «Мне нравится». '''
            def __init__(self, exec_func):
                self.exec_func = exec_func
                self.args = {"widget_api_id": {"desc": "идентификатор приложения/сайта, с которым инициализируются виджеты. целое число", "type": "int", "default": "None"}, "order": {"desc": "Тип сортировки страниц. Возможные значения: date, comments, likes, friend_likes. строка, по умолчанию friend_likes", "type": "str", "default": "friend_likes"}, "period": {"desc": "Период выборки. Возможные значения: day, week, month, alltime. строка, по умолчанию week", "type": "str", "default": "week"}, "offset": {"desc": "смещение необходимое для выборки определенного подмножества комментариев. По умолчанию 0. положительное число, по умолчанию 0", "type": "int", "default": "0"}, "count": {"desc": "количество возвращаемых записей. положительное число, по умолчанию 10, минимальное значение 10, максимальное значение 200", "type": "int", "default": "10"}}
            def __call__(self, widget_api_id : int = None, order : str = None, period : str = None, offset : int = None, count : int = None, v : str = None, access_token : str = None):
                self.exec_func("widgets.getPages", widget_api_id = widget_api_id, order = order, period = period, offset = offset, count = count, v = v, access_token = access_token)
            def get_args(self):
                res = []
                for arg in self.args:
                    res.append(arg)
                return ", ".join(res)
            def desc(self):
                return self.__doc__



    class execute:
        '''Универсальный метод, который позволяет запускать последовательность других методов, сохраняя и фильтруя промежуточные результаты.'''
        def __init__(self, exec_func):
            self.exec_func = exec_func
            self.args = {"code": {"desc": "код алгоритма в VKScript - формате, похожем на JavaSсript или ActionScript (предполагается совместимость с ECMAScript). Алгоритм должен завершаться командой return %выражение%. Операторы должны быть разделены точкой с запятой.", "type": "str", "default": "None"}, "func_v": {"desc": "целое число", "type": "int", "default": "week"}}
        def __call__(self, code : str = None, func_v : int = None, v : str = None, access_token : str = None):
            self.exec_func("execute", code = code, func_v = func_v, v = v, access_token = access_token)
        def get_args(self):
            res = []
            for arg in self.args:
                res.append(arg)
            return ", ".join(res)
        def desc(self):
            return self.__doc__


    def exec_func(self, method, **kwargs):
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
    print("widget_api_id - " + Vk.widgets.getPages.args["widget_api_id"]["desc"])
