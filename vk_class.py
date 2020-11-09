class Vk:
    def __init__(self, event):
        self.event = event
        try:
            vk_class_dict_file = open("vk_classes.json", encoding="utf-8", mode="r")
            self.vk_class_dict = json.loads(vk_class_dict_file.read())
            vk_class_dict_file.close()
        except:
            self.vk_class_dict = None
        self.account = self.account(event)
        self.appWidgets = self.appWidgets(event)
        self.apps = self.apps(event)
        self.auth = self.auth(event)
        self.board = self.board(event)
        self.database = self.database(event)
        self.docs = self.docs(event)
        self.donut = self.donut(event)
        self.downloadedGames = self.downloadedGames(event)
        self.fave = self.fave(event)
        self.friends = self.friends(event)
        self.gifts = self.gifts(event)
        self.groups = self.groups(event)
        self.leadForms = self.leadForms(event)
        self.likes = self.likes(event)
        self.market = self.market(event)
        self.messages = self.messages(event)
        self.newsfeed = self.newsfeed(event)
        self.notes = self.notes(event)
        self.notifications = self.notifications(event)
        self.pages = self.pages(event)
        self.photos = self.photos(event)
        self.polls = self.polls(event)
        self.prettyCards = self.prettyCards(event)
        self.search = self.search(event)
        self.stats = self.stats(event)
        self.status = self.status(event)
        self.storage = self.storage(event)
        self.stories = self.stories(event)
        self.streaming = self.streaming(event)
        self.users = self.users(event)
        self.utils = self.utils(event)
        self.video = self.video(event)
        self.wall = self.wall(event)
        self.widgets = self.widgets(event)


    class account:
        def  __init__(self, event):
            self.event = event
        def ban(v = None, access_token = None, owner_id = None):
            pass
        def changePassword(v = None, access_token = None, restore_sid = None, change_password_hash = None, old_password = None, new_password = None):
            pass
        def getActiveOffers(v = None, access_token = None, offset = None, count = None):
            pass
        def getAppPermissions(v = None, access_token = None, user_id = None):
            pass
        def getBanned(v = None, access_token = None, offset = None, count = None):
            pass
        def getCounters(v = None, access_token = None, filter = None):
            pass
        def getInfo(v = None, access_token = None, fields = None):
            pass
        def getProfileInfo(v = None, access_token = None):
            pass
        def getPushSettings(v = None, access_token = None, device_id = None, token = None):
            pass
        def registerDevice(v = None, access_token = None, token = None, device_model = None, device_year = None, device_id = None, system_version = None, settings = None, sandbox = None, no_text = None, subscribe = None):
            pass
        def saveProfileInfo(v = None, access_token = None, first_name = None, last_name = None, maiden_name = None, screen_name = None, cancel_request_id = None, sex = None, relation = None, relation_partner_id = None, bdate = None, bdate_visibility = None, home_town = None, country_id = None, city_id = None, status = None):
            pass
        def setInfo(v = None, access_token = None, name = None, value = None, intro = None, own_posts_default = None, no_wall_replies = None):
            pass
        def setNameInMenu(v = None, access_token = None, user_id = None, name = None):
            pass
        def setOffline(v = None, access_token = None):
            pass
        def setOnline(v = None, access_token = None, voip = None):
            pass
        def setPushSettings(v = None, access_token = None, device_id = None, settings = None, key = None, value = None):
            pass
        def setSilenceMode(v = None, access_token = None, device_id = None, time = None, peer_id = None, sound = None, token = None, chat_id = None, user_id = None):
            pass
        def unban(v = None, access_token = None, owner_id = None):
            pass
        def unregisterDevice(v = None, access_token = None, device_id = None, sandbox = None, token = None):
            pass


    class appWidgets:
        def  __init__(self, event):
            self.event = event
        def getAppImageUploadServer(v = None, access_token = None, image_type = None):
            pass
        def getAppImages(v = None, access_token = None):
            pass
        def getGroupImageUploadServer(v = None, access_token = None):
            pass
        def getGroupImages(v = None, access_token = None):
            pass
        def getImagesById(v = None, access_token = None):
            pass
        def saveAppImage(v = None, access_token = None, hash = None, image = None):
            pass
        def saveGroupImage(v = None, access_token = None):
            pass
        def update(v = None, access_token = None):
            pass


    class apps:
        def  __init__(self, event):
            self.event = event
        def deleteAppRequests(v = None, access_token = None):
            pass
        def get(v = None, access_token = None, app_id = None, app_ids = None, platform = None, extended = None, return_friends = None, fields = None, name_case = None):
            pass
        def getCatalog(v = None, access_token = None, sort = None, offset = None, count = None, platform = None, extended = None, return_friends = None, fields = None, name_case = None, q = None, genre_id = None, filter = None):
            pass
        def getFriendsList(v = None, access_token = None, extended = None, count = None, offset = None, type = None, fields = None):
            pass
        def getLeaderboard(v = None, access_token = None, type = None, global_ = None, extended = None):
            pass
        def getScopes(v = None, access_token = None, type = None):
            pass
        def getScore(v = None, access_token = None, user_id = None):
            pass
        def promoHasActiveGift(v = None, access_token = None, promo_id = None, user_id = None):
            pass
        def promoUseGift(v = None, access_token = None, promo_id = None, user_id = None):
            pass
        def sendRequest(v = None, access_token = None, user_id = None, text = None, type = None, name = None, key = None, separate = None):
            pass


    class auth:
        def  __init__(self, event):
            self.event = event
        def checkPhone(v = None, access_token = None, phone = None, client_id = None, client_secret = None, auth_by_phone = None):
            pass
        def restore(v = None, access_token = None, phone = None, last_name = None):
            pass


    class board:
        def  __init__(self, event):
            self.event = event
        def addTopic(v = None, access_token = None, group_id = None, title = None, text = None, from_group = None, attachments = None):
            pass
        def closeTopic(v = None, access_token = None, group_id = None, topic_id = None):
            pass
        def createComment(v = None, access_token = None, group_id = None, topic_id = None, message = None, attachments = None, from_group = None, sticker_id = None, guid = None):
            pass
        def deleteComment(v = None, access_token = None, group_id = None, topic_id = None, comment_id = None):
            pass
        def deleteTopic(v = None, access_token = None, group_id = None, topic_id = None):
            pass
        def editComment(v = None, access_token = None, group_id = None, topic_id = None, comment_id = None, message = None, attachments = None):
            pass
        def editTopic(v = None, access_token = None, group_id = None, topic_id = None, title = None):
            pass
        def fixTopic(v = None, access_token = None, group_id = None, topic_id = None):
            pass
        def getComments(v = None, access_token = None, group_id = None, topic_id = None, need_likes = None, start_comment_id = None, offset = None, count = None, extended = None, sort = None):
            pass
        def getTopics(v = None, access_token = None, group_id = None, topic_ids = None, order = None, offset = None, count = None, extended = None, preview = None, preview_length = None):
            pass
        def openTopic(v = None, access_token = None, group_id = None, topic_id = None):
            pass
        def restoreComment(v = None, access_token = None, group_id = None, topic_id = None, comment_id = None):
            pass
        def unfixTopic(v = None, access_token = None, group_id = None, topic_id = None):
            pass


    class database:
        def  __init__(self, event):
            self.event = event
        def getChairs(v = None, access_token = None, faculty_id = None, offset = None, count = None):
            pass
        def getCities(v = None, access_token = None, country_id = None, region_id = None, q = None, need_all = None, offset = None, count = None):
            pass
        def getCitiesById(v = None, access_token = None, city_ids = None):
            pass
        def getCountries(v = None, access_token = None, need_all = None, code = None, offset = None, count = None):
            pass
        def getCountriesById(v = None, access_token = None, country_ids = None):
            pass
        def getFaculties(v = None, access_token = None, university_id = None, offset = None, count = None):
            pass
        def getMetroStations(v = None, access_token = None, city_id = None, offset = None, count = None, extended = None):
            pass
        def getMetroStationsById(v = None, access_token = None, station_ids = None):
            pass
        def getRegions(v = None, access_token = None, country_id = None, q = None, offset = None, count = None):
            pass
        def getSchoolClasses(v = None, access_token = None, country_id = None):
            pass
        def getSchools(v = None, access_token = None, q = None, city_id = None, offset = None, count = None):
            pass
        def getUniversities(v = None, access_token = None, q = None, country_id = None, city_id = None, offset = None, count = None):
            pass


    class docs:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, owner_id = None, doc_id = None, access_key = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, doc_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, doc_id = None, title = None, tags = None):
            pass
        def get(v = None, access_token = None, count = None, offset = None, type = None, owner_id = None, return_tags = None):
            pass
        def getById(v = None, access_token = None, docs = None, return_tags = None):
            pass
        def getMessagesUploadServer(v = None, access_token = None, type = None, peer_id = None):
            pass
        def getTypes(v = None, access_token = None, owner_id = None):
            pass
        def getUploadServer(v = None, access_token = None, group_id = None):
            pass
        def getWallUploadServer(v = None, access_token = None, group_id = None):
            pass
        def save(v = None, access_token = None, file = None, title = None, tags = None, return_tags = None):
            pass
        def search(v = None, access_token = None, q = None, search_own = None, count = None, offset = None, return_tags = None):
            pass


    class donut:
        def  __init__(self, event):
            self.event = event
        def getFriends(v = None, access_token = None, owner_id = None, offset = None, count = None, fields = None):
            pass
        def getSubscription(v = None, access_token = None, owner_id = None):
            pass
        def getSubscriptions(v = None, access_token = None, fields = None, offset = None, count = None):
            pass
        def isDon(v = None, access_token = None, owner_id = None):
            pass


    class downloadedGames:
        def  __init__(self, event):
            self.event = event
        def getPaidStatus(v = None, access_token = None, user_id = None):
            pass


    class fave:
        def  __init__(self, event):
            self.event = event
        def addArticle(v = None, access_token = None, url = None):
            pass
        def addLink(v = None, access_token = None, link = None):
            pass
        def addPage(v = None, access_token = None, user_id = None, group_id = None):
            pass
        def addPost(v = None, access_token = None, owner_id = None, id = None, access_key = None, ref = None, track_code = None, source = None):
            pass
        def addProduct(v = None, access_token = None, owner_id = None, id = None, access_key = None):
            pass
        def addTag(v = None, access_token = None, name = None, position = None):
            pass
        def addVideo(v = None, access_token = None, owner_id = None, id = None, access_key = None):
            pass
        def editTag(v = None, access_token = None, id = None, name = None):
            pass
        def get(v = None, access_token = None, extended = None, item_type = None, tag_id = None, offset = None, count = None, fields = None, is_from_snackbar = None):
            pass
        def getPages(v = None, access_token = None, offset = None, count = None, type = None, fields = None, tag_id = None):
            pass
        def getTags(v = None, access_token = None):
            pass
        def markSeen(v = None, access_token = None):
            pass
        def removeArticle(v = None, access_token = None, owner_id = None, article_id = None, ref = None):
            pass
        def removeLink(v = None, access_token = None, link_id = None):
            pass
        def removePage(v = None, access_token = None, user_id = None, group_id = None):
            pass
        def removePost(v = None, access_token = None, owner_id = None, id = None):
            pass
        def removeProduct(v = None, access_token = None, owner_id = None, id = None):
            pass
        def removeTag(v = None, access_token = None, id = None):
            pass
        def removeVideo(v = None, access_token = None, owner_id = None, id = None):
            pass
        def reorderTags(v = None, access_token = None, ids = None):
            pass
        def setPageTags(v = None, access_token = None, user_id = None, group_id = None, tag_ids = None):
            pass
        def setTags(v = None, access_token = None, item_type = None, item_owner_id = None, item_id = None, tag_ids = None, link_id = None, link_url = None):
            pass
        def trackPageInteraction(v = None, access_token = None, user_id = None, group_id = None):
            pass


    class friends:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, user_id = None, text = None, follow = None):
            pass
        def addList(v = None, access_token = None, name = None, user_ids = None):
            pass
        def areFriends(v = None, access_token = None, user_ids = None, need_sign = None, extended = None):
            pass
        def delete(v = None, access_token = None, user_id = None):
            pass
        def deleteAllRequests(v = None, access_token = None):
            pass
        def deleteList(v = None, access_token = None, list_id = None):
            pass
        def edit(v = None, access_token = None, user_id = None, list_ids = None):
            pass
        def editList(v = None, access_token = None, name = None, list_id = None, user_ids = None, add_user_ids = None, delete_user_ids = None):
            pass
        def get(v = None, access_token = None, user_id = None, order = None, list_id = None, count = None, offset = None, fields = None, name_case = None, ref = None):
            pass
        def getAppUsers(v = None, access_token = None):
            pass
        def getByPhones(v = None, access_token = None, phones = None, fields = None):
            pass
        def getLists(v = None, access_token = None, user_id = None, return_system = None):
            pass
        def getMutual(v = None, access_token = None, source_uid = None, target_uid = None, target_uids = None, order = None, count = None, offset = None):
            pass
        def getOnline(v = None, access_token = None, user_id = None, list_id = None, online_mobile = None, order = None, count = None, offset = None):
            pass
        def getRecent(v = None, access_token = None, count = None):
            pass
        def getRequests(v = None, access_token = None, offset = None, count = None, extended = None, need_mutual = None, out = None, sort = None, need_viewed = None, suggested = None, ref = None, fields = None):
            pass
        def getSuggestions(v = None, access_token = None, filter = None, count = None, offset = None, fields = None, name_case = None):
            pass
        def search(v = None, access_token = None, user_id = None, q = None, fields = None, name_case = None, offset = None, count = None):
            pass


    class gifts:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, user_id = None, count = None, offset = None):
            pass


    class groups:
        def  __init__(self, event):
            self.event = event
        def addAddress(v = None, access_token = None, group_id = None, title = None, address = None, additional_address = None, country_id = None, city_id = None, metro_id = None, latitude = None, longitude = None, phone = None, work_info_status = None, timetable = None, is_main_address = None):
            pass
        def addCallbackServer(v = None, access_token = None, group_id = None, url = None, title = None, secret_key = None):
            pass
        def addLink(v = None, access_token = None, group_id = None, link = None, text = None):
            pass
        def approveRequest(v = None, access_token = None, group_id = None, user_id = None):
            pass
        def ban(v = None, access_token = None, group_id = None, owner_id = None, end_date = None, reason = None, comment = None, comment_visible = None):
            pass
        def create(v = None, access_token = None, title = None, description = None, type = None, public_category = None, subtype = None):
            pass
        def deleteAddress(v = None, access_token = None, group_id = None, address_id = None):
            pass
        def deleteCallbackServer(v = None, access_token = None, group_id = None, server_id = None):
            pass
        def deleteLink(v = None, access_token = None, group_id = None, link_id = None):
            pass
        def disableOnline(v = None, access_token = None, group_id = None):
            pass
        def edit(v = None, access_token = None, group_id = None, title = None, description = None, screen_name = None, access = None, website = None, subject = None, email = None, phone = None, rss = None, event_start_date = None, event_finish_date = None, event_group_id = None, public_category = None, public_subcategory = None, public_date = None, wall = None, topics = None, photos = None, video = None, audio = None, links = None, events = None, places = None, contacts = None, docs = None, wiki = None, messages = None, articles = None, addresses = None, age_limits = None, market = None, market_comments = None, market_country = None, market_city = None, market_currency = None, market_contact = None, market_wiki = None, obscene_filter = None, obscene_stopwords = None, obscene_words = None, main_section = None, secondary_section = None, country = None, city = None):
            pass
        def editAddress(v = None, access_token = None, group_id = None, address_id = None, title = None, address = None, additional_address = None, country_id = None, city_id = None, metro_id = None, latitude = None, longitude = None, phone = None, work_info_status = None, timetable = None, is_main_address = None):
            pass
        def editCallbackServer(v = None, access_token = None, group_id = None, server_id = None, url = None, title = None, secret_key = None):
            pass
        def editLink(v = None, access_token = None, group_id = None, link_id = None, text = None):
            pass
        def editManager(v = None, access_token = None, group_id = None, user_id = None, role = None, is_contact = None, contact_position = None, contact_phone = None, contact_email = None):
            pass
        def enableOnline(v = None, access_token = None, group_id = None):
            pass
        def get(v = None, access_token = None, user_id = None, extended = None, filter = None, fields = None, offset = None, count = None):
            pass
        def getAddresses(v = None, access_token = None, group_id = None, address_ids = None, latitude = None, longitude = None, offset = None, count = None, fields = None):
            pass
        def getBanned(v = None, access_token = None, group_id = None, offset = None, count = None, fields = None, owner_id = None):
            pass
        def getById(v = None, access_token = None, group_ids = None, group_id = None, fields = None):
            pass
        def getCallbackConfirmationCode(v = None, access_token = None, group_id = None):
            pass
        def getCallbackServers(v = None, access_token = None, group_id = None, server_ids = None):
            pass
        def getCallbackSettings(v = None, access_token = None, group_id = None, server_id = None):
            pass
        def getCatalog(v = None, access_token = None, category_id = None, subcategory_id = None):
            pass
        def getCatalogInfo(v = None, access_token = None, extended = None, subcategories = None):
            pass
        def getInvitedUsers(v = None, access_token = None, group_id = None, offset = None, count = None, fields = None, name_case = None):
            pass
        def getInvites(v = None, access_token = None, offset = None, count = None, extended = None):
            pass
        def getLongPollServer(v = None, access_token = None, group_id = None):
            pass
        def getLongPollSettings(v = None, access_token = None, group_id = None):
            pass
        def getMembers(v = None, access_token = None, group_id = None, sort = None, offset = None, count = None, fields = None, filter = None):
            pass
        def getOnlineStatus(v = None, access_token = None, group_id = None):
            pass
        def getRequests(v = None, access_token = None, group_id = None, offset = None, count = None, fields = None):
            pass
        def getSettings(v = None, access_token = None, group_id = None):
            pass
        def getTagList(v = None, access_token = None, group_id = None):
            pass
        def getTokenPermissions(v = None, access_token = None):
            pass
        def invite(v = None, access_token = None, group_id = None, user_id = None):
            pass
        def isMember(v = None, access_token = None, group_id = None, user_id = None, user_ids = None, extended = None):
            pass
        def join(v = None, access_token = None, group_id = None, not_sure = None):
            pass
        def leave(v = None, access_token = None, group_id = None):
            pass
        def removeUser(v = None, access_token = None, group_id = None, user_id = None):
            pass
        def reorderLink(v = None, access_token = None, group_id = None, link_id = None, after = None):
            pass
        def search(v = None, access_token = None, q = None, type = None, country_id = None, city_id = None, future = None, market = None, sort = None, offset = None, count = None):
            pass
        def setCallbackSettings(v = None, access_token = None, group_id = None, server_id = None, api_version = None, message_new = None, message_reply = None, message_allow = None, message_edit = None, message_deny = None, message_typing_state = None, photo_new = None, audio_new = None, video_new = None, wall_reply_new = None, wall_reply_edit = None, wall_reply_delete = None, wall_reply_restore = None, wall_post_new = None, wall_repost = None, board_post_new = None, board_post_edit = None, board_post_restore = None, board_post_delete = None, photo_comment_new = None, photo_comment_edit = None, photo_comment_delete = None, photo_comment_restore = None, video_comment_new = None, video_comment_edit = None, video_comment_delete = None, video_comment_restore = None, market_comment_new = None, market_comment_edit = None, market_comment_delete = None, market_comment_restore = None, market_order_new = None, market_order_edit = None, poll_vote_new = None, group_join = None, group_leave = None, group_change_settings = None, group_change_photo = None, group_officers_edit = None, user_block = None, user_unblock = None, lead_forms_new = None, like_add = None, like_remove = None, message_event = None):
            pass
        def setLongPollSettings(v = None, access_token = None, group_id = None, enabled = None, api_version = None, message_new = None, message_reply = None, message_allow = None, message_deny = None, message_edit = None, message_typing_state = None, photo_new = None, audio_new = None, video_new = None, wall_reply_new = None, wall_reply_edit = None, wall_reply_delete = None, wall_reply_restore = None, wall_post_new = None, wall_repost = None, board_post_new = None, board_post_edit = None, board_post_restore = None, board_post_delete = None, photo_comment_new = None, photo_comment_edit = None, photo_comment_delete = None, photo_comment_restore = None, video_comment_new = None, video_comment_edit = None, video_comment_delete = None, video_comment_restore = None, market_comment_new = None, market_comment_edit = None, market_comment_delete = None, market_comment_restore = None, poll_vote_new = None, group_join = None, group_leave = None, group_change_settings = None, group_change_photo = None, group_officers_edit = None, user_block = None, user_unblock = None, like_add = None, like_remove = None, message_event = None):
            pass
        def setSettings(v = None, access_token = None, group_id = None, messages = None, bots_capabilities = None, bots_start_button = None, bots_add_to_chat = None):
            pass
        def setUserNote(v = None, access_token = None, group_id = None, user_id = None, note = None):
            pass
        def tagAdd(v = None, access_token = None, group_id = None, tag_name = None, tag_color = None):
            pass
        def tagBind(v = None, access_token = None, group_id = None, tag_id = None, user_id = None, act = None):
            pass
        def tagDelete(v = None, access_token = None, group_id = None, tag_id = None):
            pass
        def tagUpdate(v = None, access_token = None, group_id = None, tag_id = None, tag_name = None):
            pass
        def toggleMarket(v = None, access_token = None, group_id = None, state = None):
            pass
        def unban(v = None, access_token = None, group_id = None, owner_id = None):
            pass


    class leadForms:
        def  __init__(self, event):
            self.event = event
        def create(v = None, access_token = None, group_id = None, name = None, title = None, description = None, questions = None, policy_link_url = None, photo = None, confirmation = None, site_link_url = None, active = None, once_per_user = None, pixel_code = None, notify_admins = None, notify_emails = None):
            pass
        def delete(v = None, access_token = None, group_id = None, form_id = None):
            pass
        def get(v = None, access_token = None, group_id = None, form_id = None):
            pass
        def getLeads(v = None, access_token = None, group_id = None, form_id = None, limit = None, next_page_token = None):
            pass
        def getUploadURL(v = None, access_token = None):
            pass
        def list(v = None, access_token = None, group_id = None):
            pass
        def update(v = None, access_token = None, group_id = None, form_id = None, name = None, title = None, description = None, questions = None, policy_link_url = None, photo = None, confirmation = None, site_link_url = None, active = None, once_per_user = None, pixel_code = None, notify_admins = None, notify_emails = None):
            pass


    class likes:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, type = None, owner_id = None, item_id = None, access_key = None):
            pass
        def delete(v = None, access_token = None, type = None, owner_id = None, item_id = None, access_key = None):
            pass
        def getList(v = None, access_token = None, type = None, owner_id = None, item_id = None, page_url = None, filter = None, friends_only = None, extended = None, offset = None, count = None, skip_own = None):
            pass
        def isLiked(v = None, access_token = None, user_id = None, type = None, owner_id = None, item_id = None):
            pass


    class market:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, owner_id = None, name = None, description = None, category_id = None, price = None, old_price = None, deleted = None, main_photo_id = None, photo_ids = None, url = None, dimension_width = None, dimension_height = None, dimension_length = None, weight = None, sku = None):
            pass
        def addAlbum(v = None, access_token = None, owner_id = None, title = None, photo_id = None, main_album = None):
            pass
        def addToAlbum(v = None, access_token = None, owner_id = None, item_id = None, album_ids = None):
            pass
        def createComment(v = None, access_token = None, owner_id = None, item_id = None, message = None, attachments = None, from_group = None, reply_to_comment = None, sticker_id = None, guid = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, item_id = None):
            pass
        def deleteAlbum(v = None, access_token = None, owner_id = None, album_id = None):
            pass
        def deleteComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, item_id = None, name = None, description = None, category_id = None, price = None, old_price = None, deleted = None, main_photo_id = None, photo_ids = None, url = None, dimension_width = None, dimension_height = None, dimension_length = None, weight = None, sku = None):
            pass
        def editAlbum(v = None, access_token = None, owner_id = None, album_id = None, title = None, photo_id = None, main_album = None):
            pass
        def editComment(v = None, access_token = None, owner_id = None, comment_id = None, message = None, attachments = None):
            pass
        def editOrder(v = None, access_token = None, user_id = None, order_id = None, merchant_comment = None, status = None, track_number = None, payment_status = None, delivery_price = None, width = None, length = None, height = None, weight = None):
            pass
        def get(v = None, access_token = None, owner_id = None, album_id = None, count = None, offset = None, extended = None):
            pass
        def getAlbumById(v = None, access_token = None, owner_id = None, album_ids = None):
            pass
        def getAlbums(v = None, access_token = None, owner_id = None, offset = None, count = None):
            pass
        def getById(v = None, access_token = None, item_ids = None, extended = None):
            pass
        def getCategories(v = None, access_token = None):
            pass
        def getComments(v = None, access_token = None, owner_id = None, item_id = None, need_likes = None, start_comment_id = None, offset = None, count = None, sort = None, extended = None, fields = None):
            pass
        def getGroupOrders(v = None, access_token = None, group_id = None, offset = None, count = None):
            pass
        def getOrderById(v = None, access_token = None, user_id = None, order_id = None, extended = None):
            pass
        def getOrderItems(v = None, access_token = None, user_id = None, order_id = None, offset = None, count = None):
            pass
        def getOrders(v = None, access_token = None, offset = None, count = None, extended = None):
            pass
        def removeFromAlbum(v = None, access_token = None, owner_id = None, item_id = None, album_ids = None):
            pass
        def reorderAlbums(v = None, access_token = None, owner_id = None, album_id = None, before = None, after = None):
            pass
        def reorderItems(v = None, access_token = None, owner_id = None, album_id = None, item_id = None, before = None, after = None):
            pass
        def report(v = None, access_token = None, owner_id = None, item_id = None, reason = None):
            pass
        def reportComment(v = None, access_token = None, owner_id = None, comment_id = None, reason = None):
            pass
        def restore(v = None, access_token = None, owner_id = None, item_id = None):
            pass
        def restoreComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def search(v = None, access_token = None, owner_id = None, album_id = None, q = None, price_from = None, price_to = None, sort = None, rev = None, offset = None, count = None, extended = None, status = None):
            pass


    class messages:
        def  __init__(self, event):
            self.event = event
        def addChatUser(v = None, access_token = None, chat_id = None, user_id = None, visible_messages_count = None):
            pass
        def allowMessagesFromGroup(v = None, access_token = None, group_id = None, key = None):
            pass
        def createChat(v = None, access_token = None, user_ids = None, title = None, group_id = None):
            pass
        def delete(v = None, access_token = None, message_ids = None, spam = None, group_id = None, delete_for_all = None):
            pass
        def deleteChatPhoto(v = None, access_token = None, chat_id = None, group_id = None):
            pass
        def deleteConversation(v = None, access_token = None, user_id = None, peer_id = None, group_id = None, offset = None, count = None):
            pass
        def denyMessagesFromGroup(v = None, access_token = None, group_id = None):
            pass
        def edit(v = None, access_token = None, peer_id = None, message = None, lat = None, long = None, attachment = None, keep_forward_messages = None, keep_snippets = None, group_id = None, dont_parse_links = None, message_id = None, conversation_message_id = None, template = None, keyboard = None):
            pass
        def editChat(v = None, access_token = None, chat_id = None, title = None):
            pass
        def getByConversationMessageId(v = None, access_token = None, peer_id = None, conversation_message_ids = None, extended = None, fields = None, group_id = None):
            pass
        def getById(v = None, access_token = None, message_ids = None, preview_length = None, extended = None, fields = None, group_id = None):
            pass
        def getChat(v = None, access_token = None, chat_id = None, chat_ids = None, fields = None, name_case = None):
            pass
        def getChatPreview(v = None, access_token = None, peer_id = None, link = None, fields = None):
            pass
        def getConversationMembers(v = None, access_token = None, peer_id = None, fields = None, group_id = None):
            pass
        def getConversations(v = None, access_token = None, offset = None, count = None, filter = None, extended = None, start_message_id = None, fields = None, group_id = None):
            pass
        def getConversationsById(v = None, access_token = None, peer_ids = None, extended = None, fields = None, group_id = None):
            pass
        def getHistory(v = None, access_token = None, offset = None, count = None, user_id = None, peer_id = None, start_message_id = None, rev = None, extended = None, fields = None, group_id = None):
            pass
        def getHistoryAttachments(v = None, access_token = None, peer_id = None, media_type = None, start_from = None, count = None, photo_sizes = None, fields = None, group_id = None, preserve_order = None, max_forwards_level = None):
            pass
        def getImportantMessages(v = None, access_token = None, count = None, offset = None, start_message_id = None, preview_length = None, fields = None, extended = None, group_id = None):
            pass
        def getInviteLink(v = None, access_token = None, peer_id = None, reset = None, group_id = None):
            pass
        def getLastActivity(v = None, access_token = None, user_id = None):
            pass
        def getLongPollHistory(v = None, access_token = None, ts = None, pts = None, preview_length = None, onlines = None, fields = None, events_limit = None, msgs_limit = None, max_msg_id = None, group_id = None, lp_version = None, last_n = None, credentials = None):
            pass
        def getLongPollServer(v = None, access_token = None, need_pts = None, group_id = None, lp_version = None):
            pass
        def isMessagesFromGroupAllowed(v = None, access_token = None, group_id = None, user_id = None):
            pass
        def joinChatByInviteLink(v = None, access_token = None, link = None):
            pass
        def markAsAnsweredConversation(v = None, access_token = None, peer_id = None, answered = None, group_id = None):
            pass
        def markAsImportant(v = None, access_token = None, message_ids = None, important = None):
            pass
        def markAsImportantConversation(v = None, access_token = None, peer_id = None, important = None, group_id = None):
            pass
        def markAsRead(v = None, access_token = None, message_ids = None, peer_id = None, start_message_id = None, group_id = None, mark_conversation_as_read = None):
            pass
        def pin(v = None, access_token = None, peer_id = None, message_id = None, conversation_message_id = None):
            pass
        def removeChatUser(v = None, access_token = None, chat_id = None, user_id = None, member_id = None):
            pass
        def restore(v = None, access_token = None, message_id = None, group_id = None):
            pass
        def search(v = None, access_token = None, q = None, peer_id = None, date = None, preview_length = None, offset = None, count = None, extended = None, fields = None, group_id = None):
            pass
        def searchConversations(v = None, access_token = None, q = None, count = None, extended = None, fields = None, group_id = None):
            pass
        def send(v = None, access_token = None, user_id = None, random_id = None, peer_id = None, peer_ids = None, domain = None, chat_id = None, message = None, lat = None, long = None, attachment = None, reply_to = None, forward_messages = None, forward = None, sticker_id = None, group_id = None, keyboard = None, template = None, payload = None, content_source = None, dont_parse_links = None, disable_mentions = None, intent = None, subscribe_id = None, user_ids = None, guid = None):
            pass
        def sendMessageEventAnswer(v = None, access_token = None, event_id = None, user_id = None, peer_id = None, event_data = None):
            pass
        def setActivity(v = None, access_token = None, user_id = None, type = None, peer_id = None, group_id = None):
            pass
        def setChatPhoto(v = None, access_token = None, file = None):
            pass
        def unpin(v = None, access_token = None, peer_id = None, group_id = None):
            pass


    class newsfeed:
        def  __init__(self, event):
            self.event = event
        def addBan(v = None, access_token = None, user_ids = None, group_ids = None):
            pass
        def deleteBan(v = None, access_token = None, user_ids = None, group_ids = None):
            pass
        def deleteList(v = None, access_token = None, list_id = None):
            pass
        def get(v = None, access_token = None, filters = None, return_banned = None, start_time = None, end_time = None, max_photos = None, source_ids = None, start_from = None, count = None, fields = None, section = None, from_ = None, offset = None):
            pass
        def getBanned(v = None, access_token = None, extended = None, fields = None, name_case = None):
            pass
        def getComments(v = None, access_token = None, count = None, filters = None, reposts = None, start_time = None, end_time = None, last_comments_count = None, start_from = None, fields = None, from_ = None, last_comments = None):
            pass
        def getLists(v = None, access_token = None, list_ids = None, extended = None):
            pass
        def getMentions(v = None, access_token = None, owner_id = None, start_time = None, end_time = None, offset = None, count = None):
            pass
        def getRecommended(v = None, access_token = None, start_time = None, end_time = None, max_photos = None, start_from = None, count = None, fields = None, from_ = None, offset = None):
            pass
        def getSuggestedSources(v = None, access_token = None, offset = None, count = None, shuffle = None, fields = None):
            pass
        def ignoreItem(v = None, access_token = None, type = None, owner_id = None, item_id = None):
            pass
        def saveList(v = None, access_token = None, list_id = None, title = None, source_ids = None, no_reposts = None):
            pass
        def search(v = None, access_token = None, q = None, extended = None, count = None, latitude = None, longitude = None, start_time = None, end_time = None, start_from = None, fields = None, start_id = None, offset = None):
            pass
        def unignoreItem(v = None, access_token = None, type = None, owner_id = None, item_id = None, track_code = None):
            pass
        def unsubscribe(v = None, access_token = None, type = None, owner_id = None, item_id = None):
            pass


    class notes:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, title = None, text = None, privacy_view = None, privacy_comment = None, privacy = None, comment_privacy = None):
            pass
        def createComment(v = None, access_token = None, note_id = None, owner_id = None, reply_to = None, message = None, guid = None):
            pass
        def delete(v = None, access_token = None, note_id = None):
            pass
        def deleteComment(v = None, access_token = None, comment_id = None, owner_id = None):
            pass
        def edit(v = None, access_token = None, note_id = None, title = None, text = None, privacy_view = None, privacy_comment = None, privacy = None, comment_privacy = None):
            pass
        def editComment(v = None, access_token = None, comment_id = None, owner_id = None, message = None):
            pass
        def get(v = None, access_token = None, note_ids = None, user_id = None, offset = None, count = None, sort = None):
            pass
        def getById(v = None, access_token = None, note_id = None, owner_id = None, need_wiki = None):
            pass
        def getComments(v = None, access_token = None, note_id = None, owner_id = None, sort = None, offset = None, count = None):
            pass
        def restoreComment(v = None, access_token = None, comment_id = None, owner_id = None):
            pass


    class notifications:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, count = None, start_from = None, filters = None, start_time = None, end_time = None, from_ = None, offset = None):
            pass
        def markAsViewed(v = None, access_token = None):
            pass
        def sendMessage(v = None, access_token = None, user_ids = None, message = None, fragment = None, group_id = None, random_id = None):
            pass


    class pages:
        def  __init__(self, event):
            self.event = event
        def clearCache(v = None, access_token = None, url = None):
            pass
        def get(v = None, access_token = None, owner_id = None, page_id = None, global_ = None, site_preview = None, title = None, need_source = None, need_html = None):
            pass
        def getHistory(v = None, access_token = None, page_id = None, group_id = None, user_id = None):
            pass
        def getTitles(v = None, access_token = None, group_id = None):
            pass
        def getVersion(v = None, access_token = None, version_id = None, group_id = None, user_id = None, need_html = None):
            pass
        def parseWiki(v = None, access_token = None, text = None, group_id = None):
            pass
        def save(v = None, access_token = None, text = None, page_id = None, group_id = None, user_id = None, title = None):
            pass
        def saveAccess(v = None, access_token = None, page_id = None, group_id = None, user_id = None, view = None, edit = None):
            pass


    class photos:
        def  __init__(self, event):
            self.event = event
        def confirmTag(v = None, access_token = None, owner_id = None, photo_id = None, tag_id = None):
            pass
        def copy(v = None, access_token = None, owner_id = None, photo_id = None, access_key = None):
            pass
        def createAlbum(v = None, access_token = None, title = None, group_id = None, description = None, privacy_view = None, privacy_comment = None, upload_by_admins_only = None, comments_disabled = None, privacy = None, comment_privacy = None):
            pass
        def createComment(v = None, access_token = None, owner_id = None, photo_id = None, message = None, attachments = None, from_group = None, reply_to_comment = None, sticker_id = None, access_key = None, guid = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, photo_id = None):
            pass
        def deleteAlbum(v = None, access_token = None, album_id = None, group_id = None):
            pass
        def deleteComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, photo_id = None, caption = None, latitude = None, longitude = None, place_str = None, foursquare_id = None, delete_place = None):
            pass
        def editAlbum(v = None, access_token = None, album_id = None, title = None, description = None, owner_id = None, privacy_view = None, privacy_comment = None, upload_by_admins_only = None, comments_disabled = None, privacy = None, comment_privacy = None):
            pass
        def editComment(v = None, access_token = None, owner_id = None, comment_id = None, message = None, attachments = None):
            pass
        def get(v = None, access_token = None, owner_id = None, album_id = None, photo_ids = None, rev = None, extended = None, feed_type = None, feed = None, photo_sizes = None, offset = None, count = None):
            pass
        def getAlbums(v = None, access_token = None, owner_id = None, album_ids = None, offset = None, count = None, need_system = None, need_covers = None, photo_sizes = None):
            pass
        def getAlbumsCount(v = None, access_token = None, user_id = None, group_id = None):
            pass
        def getAll(v = None, access_token = None, owner_id = None, extended = None, offset = None, count = None, photo_sizes = None, no_service_albums = None, need_hidden = None, skip_hidden = None):
            pass
        def getAllComments(v = None, access_token = None, owner_id = None, album_id = None, need_likes = None, offset = None, count = None):
            pass
        def getById(v = None, access_token = None, photos = None, extended = None, photo_sizes = None):
            pass
        def getChatUploadServer(v = None, access_token = None, chat_id = None, crop_x = None, crop_y = None, crop_width = None):
            pass
        def getComments(v = None, access_token = None, owner_id = None, photo_id = None, need_likes = None, start_comment_id = None, offset = None, count = None, sort = None, access_key = None, extended = None, fields = None, skip_before_id = None, skip_after_id = None):
            pass
        def getMarketAlbumUploadServer(v = None, access_token = None, group_id = None):
            pass
        def getMarketUploadServer(v = None, access_token = None, group_id = None, main_photo = None, crop_x = None, crop_y = None, crop_width = None):
            pass
        def getMessagesUploadServer(v = None, access_token = None, peer_id = None):
            pass
        def getNewTags(v = None, access_token = None, offset = None, count = None):
            pass
        def getOwnerCoverPhotoUploadServer(v = None, access_token = None, group_id = None, crop_x = None, crop_y = None, crop_x2 = None, crop_y2 = None):
            pass
        def getOwnerPhotoUploadServer(v = None, access_token = None, owner_id = None):
            pass
        def getTags(v = None, access_token = None, owner_id = None, photo_id = None, access_key = None):
            pass
        def getUploadServer(v = None, access_token = None, album_id = None, group_id = None):
            pass
        def getUserPhotos(v = None, access_token = None, user_id = None, offset = None, count = None, extended = None, sort = None):
            pass
        def getWallUploadServer(v = None, access_token = None, group_id = None):
            pass
        def makeCover(v = None, access_token = None, owner_id = None, photo_id = None, album_id = None):
            pass
        def move(v = None, access_token = None, owner_id = None, target_album_id = None, photo_id = None):
            pass
        def putTag(v = None, access_token = None, owner_id = None, photo_id = None, user_id = None, x = None, y = None, x2 = None, y2 = None):
            pass
        def removeTag(v = None, access_token = None, owner_id = None, photo_id = None, tag_id = None):
            pass
        def reorderAlbums(v = None, access_token = None, owner_id = None, album_id = None, before = None, after = None):
            pass
        def reorderPhotos(v = None, access_token = None, owner_id = None, photo_id = None, before = None, after = None):
            pass
        def report(v = None, access_token = None, owner_id = None, photo_id = None, reason = None):
            pass
        def reportComment(v = None, access_token = None, owner_id = None, comment_id = None, reason = None):
            pass
        def restore(v = None, access_token = None, owner_id = None, photo_id = None):
            pass
        def restoreComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def save(v = None, access_token = None, album_id = None, group_id = None, server = None, photos_list = None, hash = None, latitude = None, longitude = None, caption = None):
            pass
        def saveMarketAlbumPhoto(v = None, access_token = None, group_id = None, photo = None, server = None, hash = None):
            pass
        def saveMarketPhoto(v = None, access_token = None, group_id = None, photo = None, server = None, hash = None, crop_data = None, crop_hash = None):
            pass
        def saveMessagesPhoto(v = None, access_token = None, photo = None, server = None, hash = None):
            pass
        def saveOwnerCoverPhoto(v = None, access_token = None, hash = None, photo = None):
            pass
        def saveOwnerPhoto(v = None, access_token = None, server = None, hash = None, photo = None):
            pass
        def saveWallPhoto(v = None, access_token = None, user_id = None, group_id = None, photo = None, server = None, hash = None, latitude = None, longitude = None, caption = None):
            pass
        def search(v = None, access_token = None, q = None, lat = None, long = None, start_time = None, end_time = None, sort = None, offset = None, count = None, radius = None):
            pass


    class polls:
        def  __init__(self, event):
            self.event = event
        def addVote(v = None, access_token = None, owner_id = None, poll_id = None, answer_ids = None, is_board = None):
            pass
        def create(v = None, access_token = None, question = None, is_anonymous = None, is_multiple = None, end_date = None, owner_id = None, add_answers = None, photo_id = None, background_id = None, disable_unvote = None):
            pass
        def deleteVote(v = None, access_token = None, owner_id = None, poll_id = None, answer_id = None, is_board = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, poll_id = None, question = None, add_answers = None, edit_answers = None, delete_answers = None, end_date = None, photo_id = None, background_id = None):
            pass
        def getBackgrounds(v = None, access_token = None):
            pass
        def getById(v = None, access_token = None, owner_id = None, is_board = None, poll_id = None, extended = None, friends_count = None, fields = None, name_case = None):
            pass
        def getPhotoUploadServer(v = None, access_token = None, owner_id = None):
            pass
        def getVoters(v = None, access_token = None, owner_id = None, poll_id = None, answer_ids = None, is_board = None, friends_only = None, offset = None, count = None, fields = None, name_case = None):
            pass
        def savePhoto(v = None, access_token = None, photo = None, hash = None):
            pass


    class prettyCards:
        def  __init__(self, event):
            self.event = event
        def create(v = None, access_token = None, owner_id = None, photo = None, title = None, link = None, price = None, price_old = None, button = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, card_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, card_id = None, photo = None, title = None, link = None, price = None, price_old = None, button = None):
            pass
        def get(v = None, access_token = None, owner_id = None, offset = None, count = None):
            pass
        def getById(v = None, access_token = None, owner_id = None, card_ids = None):
            pass
        def getUploadURL(v = None, access_token = None):
            pass


    class search:
        def  __init__(self, event):
            self.event = event
        def getHints(v = None, access_token = None, q = None, offset = None, limit = None, filters = None, fields = None, search_global = None):
            pass


    class stats:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, group_id = None, app_id = None, timestamp_from = None, timestamp_to = None, interval = None, intervals_count = None, filters = None, stats_groups = None, extended = None, date_from = None, date_to = None):
            pass
        def getPostReach(v = None, access_token = None, owner_id = None, post_ids = None):
            pass
        def trackVisitor(v = None, access_token = None):
            pass


    class status:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, user_id = None, group_id = None):
            pass
        def set(v = None, access_token = None, text = None, group_id = None):
            pass


    class storage:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, key = None, keys = None, user_id = None):
            pass
        def getKeys(v = None, access_token = None, user_id = None, offset = None, count = None):
            pass
        def set(v = None, access_token = None, key = None, value = None, user_id = None):
            pass


    class stories:
        def  __init__(self, event):
            self.event = event
        def banOwner(v = None, access_token = None, owners_ids = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, story_id = None, stories = None):
            pass
        def get(v = None, access_token = None, owner_id = None, extended = None, fields = None):
            pass
        def getBanned(v = None, access_token = None, extended = None, fields = None):
            pass
        def getById(v = None, access_token = None, stories = None, extended = None, fields = None):
            pass
        def getPhotoUploadServer(v = None, access_token = None, add_to_news = None, user_ids = None, reply_to_story = None, link_text = None, link_url = None, group_id = None, clickable_stickers = None):
            pass
        def getReplies(v = None, access_token = None, owner_id = None, story_id = None, access_key = None, extended = None, fields = None):
            pass
        def getStats(v = None, access_token = None, owner_id = None, story_id = None):
            pass
        def getVideoUploadServer(v = None, access_token = None, add_to_news = None, user_ids = None, reply_to_story = None, link_text = None, link_url = None, group_id = None, clickable_stickers = None):
            pass
        def getViewers(v = None, access_token = None, owner_id = None, story_id = None, count = None, offset = None, extended = None):
            pass
        def hideAllReplies(v = None, access_token = None, owner_id = None, group_id = None):
            pass
        def hideReply(v = None, access_token = None, owner_id = None, story_id = None):
            pass
        def save(v = None, access_token = None, upload_results = None):
            pass
        def search(v = None, access_token = None, q = None, place_id = None, latitude = None, longitude = None, radius = None, mentioned_id = None, count = None, extended = None, fields = None):
            pass
        def sendInteraction(v = None, access_token = None, access_key = None, message = None, is_broadcast = None, is_anonymous = None, unseen_marker = None):
            pass
        def unbanOwner(v = None, access_token = None, owners_ids = None):
            pass


    class streaming:
        def  __init__(self, event):
            self.event = event
        def getServerUrl(v = None, access_token = None):
            pass
        def getSettings(v = None, access_token = None):
            pass
        def getStats(v = None, access_token = None, type = None, interval = None, start_time = None, end_time = None):
            pass
        def getStem(v = None, access_token = None, word = None):
            pass
        def setSettings(v = None, access_token = None, monthly_tier = None):
            pass


    class users:
        def  __init__(self, event):
            self.event = event
        def get(v = None, access_token = None, user_ids = None, fields = None, name_case = None):
            pass
        def getFollowers(v = None, access_token = None, user_id = None, offset = None, count = None, fields = None, name_case = None):
            pass
        def getSubscriptions(v = None, access_token = None, user_id = None, extended = None, offset = None, count = None, fields = None):
            pass
        def report(v = None, access_token = None, user_id = None, type = None, comment = None):
            pass
        def search(v = None, access_token = None, q = None, sort = None, offset = None, count = None, fields = None, city = None, country = None, hometown = None, university_country = None, university = None, university_year = None, university_faculty = None, university_chair = None, sex = None, status = None, age_from = None, age_to = None, birth_day = None, birth_month = None, birth_year = None, online = None, has_photo = None, school_country = None, school_city = None, school_class = None, school = None, school_year = None, religion = None, company = None, position = None, group_id = None, from_list = None):
            pass


    class utils:
        def  __init__(self, event):
            self.event = event
        def checkLink(v = None, access_token = None, url = None):
            pass
        def deleteFromLastShortened(v = None, access_token = None, key = None):
            pass
        def getLastShortenedLinks(v = None, access_token = None, count = None, offset = None):
            pass
        def getLinkStats(v = None, access_token = None, key = None, source = None, access_key = None, interval = None, intervals_count = None, extended = None):
            pass
        def getServerTime(v = None, access_token = None):
            pass
        def getShortLink(v = None, access_token = None, url = None, private = None):
            pass
        def resolveScreenName(v = None, access_token = None, screen_name = None):
            pass


    class video:
        def  __init__(self, event):
            self.event = event
        def add(v = None, access_token = None, target_id = None, video_id = None, owner_id = None):
            pass
        def addAlbum(v = None, access_token = None, group_id = None, title = None, privacy = None):
            pass
        def addToAlbum(v = None, access_token = None, target_id = None, album_id = None, album_ids = None, owner_id = None, video_id = None):
            pass
        def createComment(v = None, access_token = None, owner_id = None, video_id = None, message = None, attachments = None, from_group = None, reply_to_comment = None, sticker_id = None, guid = None):
            pass
        def delete(v = None, access_token = None, video_id = None, owner_id = None, target_id = None):
            pass
        def deleteAlbum(v = None, access_token = None, group_id = None, album_id = None):
            pass
        def deleteComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, video_id = None, name = None, desc = None, privacy_view = None, privacy_comment = None, no_comments = None, repeat = None):
            pass
        def editAlbum(v = None, access_token = None, group_id = None, album_id = None, title = None, privacy = None):
            pass
        def editComment(v = None, access_token = None, owner_id = None, comment_id = None, message = None, attachments = None):
            pass
        def get(v = None, access_token = None, owner_id = None, videos = None, album_id = None, count = None, offset = None, extended = None):
            pass
        def getAlbumById(v = None, access_token = None, owner_id = None, album_id = None):
            pass
        def getAlbums(v = None, access_token = None, owner_id = None, offset = None, count = None, extended = None, need_system = None):
            pass
        def getAlbumsByVideo(v = None, access_token = None, target_id = None, owner_id = None, video_id = None, extended = None):
            pass
        def getComments(v = None, access_token = None, owner_id = None, video_id = None, need_likes = None, start_comment_id = None, offset = None, count = None, sort = None, extended = None, fields = None):
            pass
        def removeFromAlbum(v = None, access_token = None, target_id = None, album_id = None, album_ids = None, owner_id = None, video_id = None):
            pass
        def reorderAlbums(v = None, access_token = None, owner_id = None, album_id = None, before = None, after = None):
            pass
        def reorderVideos(v = None, access_token = None, target_id = None, album_id = None, owner_id = None, video_id = None, before_owner_id = None, before_video_id = None, after_owner_id = None, after_video_id = None):
            pass
        def report(v = None, access_token = None, owner_id = None, video_id = None, reason = None, comment = None, search_query = None):
            pass
        def reportComment(v = None, access_token = None, owner_id = None, comment_id = None, reason = None):
            pass
        def restore(v = None, access_token = None, video_id = None, owner_id = None):
            pass
        def restoreComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def save(v = None, access_token = None, name = None, description = None, is_private = None, wallpost = None, link = None, group_id = None, album_id = None, privacy_view = None, privacy_comment = None, no_comments = None, repeat = None, compression = None):
            pass
        def search(v = None, access_token = None, q = None, sort = None, hd = None, adult = None, filters = None, search_own = None, offset = None, longer = None, shorter = None, count = None, extended = None):
            pass


    class wall:
        def  __init__(self, event):
            self.event = event
        def checkCopyrightLink(v = None, access_token = None, link = None):
            pass
        def closeComments(v = None, access_token = None, owner_id = None, post_id = None):
            pass
        def createComment(v = None, access_token = None, owner_id = None, post_id = None, from_group = None, message = None, reply_to_comment = None, attachments = None, sticker_id = None, guid = None):
            pass
        def delete(v = None, access_token = None, owner_id = None, post_id = None):
            pass
        def deleteComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def edit(v = None, access_token = None, owner_id = None, post_id = None, friends_only = None, message = None, attachments = None, services = None, signed = None, publish_date = None, lat = None, long = None, place_id = None, mark_as_ads = None, close_comments = None, poster_bkg_id = None, poster_bkg_owner_id = None, poster_bkg_access_hash = None, copyright = None):
            pass
        def editAdsStealth(v = None, access_token = None, owner_id = None, post_id = None, message = None, attachments = None, signed = None, lat = None, long = None, place_id = None, link_button = None, link_title = None, link_image = None, link_video = None):
            pass
        def editComment(v = None, access_token = None, owner_id = None, comment_id = None, message = None, attachments = None):
            pass
        def get(v = None, access_token = None, owner_id = None, domain = None, offset = None, count = None, filter = None, extended = None, fields = None):
            pass
        def getById(v = None, access_token = None, posts = None, extended = None, copy_history_depth = None, fields = None):
            pass
        def getComment(v = None, access_token = None, owner_id = None, comment_id = None, extended = None, fields = None):
            pass
        def getComments(v = None, access_token = None, owner_id = None, post_id = None, need_likes = None, start_comment_id = None, offset = None, count = None, sort = None, preview_length = None, extended = None, fields = None, comment_id = None, thread_items_count = None):
            pass
        def getReposts(v = None, access_token = None, owner_id = None, post_id = None, offset = None, count = None):
            pass
        def openComments(v = None, access_token = None, owner_id = None, post_id = None):
            pass
        def pin(v = None, access_token = None, owner_id = None, post_id = None):
            pass
        def post(v = None, access_token = None, owner_id = None, friends_only = None, from_group = None, message = None, attachments = None, services = None, signed = None, publish_date = None, lat = None, long = None, place_id = None, post_id = None, guid = None, mark_as_ads = None, close_comments = None, donut_paid_duration = None, mute_notifications = None, copyright = None):
            pass
        def postAdsStealth(v = None, access_token = None, owner_id = None, message = None, attachments = None, signed = None, lat = None, long = None, place_id = None, guid = None, link_button = None, link_title = None, link_image = None, link_video = None):
            pass
        def reportComment(v = None, access_token = None, owner_id = None, comment_id = None, reason = None):
            pass
        def reportPost(v = None, access_token = None, owner_id = None, post_id = None, reason = None):
            pass
        def repost(v = None, access_token = None, object = None, message = None, group_id = None, mark_as_ads = None, mute_notifications = None):
            pass
        def restore(v = None, access_token = None, owner_id = None, post_id = None):
            pass
        def restoreComment(v = None, access_token = None, owner_id = None, comment_id = None):
            pass
        def search(v = None, access_token = None, owner_id = None, domain = None, query = None, owners_only = None, count = None, offset = None, extended = None, fields = None):
            pass
        def unpin(v = None, access_token = None, owner_id = None, post_id = None):
            pass


    class widgets:
        def  __init__(self, event):
            self.event = event
        def getComments(v = None, access_token = None, widget_api_id = None, url = None, page_id = None, order = None, fields = None, offset = None, count = None):
            pass
        def getPages(v = None, access_token = None, widget_api_id = None, order = None, period = None, offset = None, count = None):
            pass
