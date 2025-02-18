from anime import Anime
# tenfile.class -> import ten File
# dùng thẳng tên class -> from ten file import ten class

class AnimeList:
    def  __init__(self):
        self.anime_list = [] 
    def add_anime(self,anime_dict):
        # self.anime_list.append(item)
        anime_dict["id"] = len(self.anime_list)
        new_item = Anime(id = anime_dict["id"],
                        name =  anime_dict["name"],
                        genre = anime_dict["genre"],
                        episodes = anime_dict["episodes"])
        self.anime_list.append(new_item)
        
    def get_item_by_title(self, anime_title):
        for anime_item in self.anime_list:
            if anime_item.name == anime_title:
                return anime_item # trả giá trị nếu tìm thấy
            return False # trả về nếu không tìm thấy
    def edit_item(self,edit_title,new_dict):
        matched = self.get_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)
    def delete_item(self, detele_title): 
        delete_item = self.get_item_by_title(detele_title) 
        if delete_item:
            self.anime_list.remove(delete_item)
    def search_by_title():
        
    def sort_by_title()


   
