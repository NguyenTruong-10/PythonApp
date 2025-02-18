class Movie(): # tạo ra lớp cho đối tượng
    def __init__(self,id_movie, title,type, release_date, rating, link_movie):
        self.id_movie = id_movie
        self.type = type
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link_movie = link_movie
    def MovieUpdate(self,id_movie, title,type, release_date, rating, link_movie):
        self.id_movie = id_movie
        self.type = type
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link_movie = link_movie

class MovieManagement(): #tạo ra lớp quản lý danh sách
    def __init__(self):
        self.movies = []  # danh sach chứa các bộ phim
    def AddMovie(self,movie):
        self.movies.append(movie)
    def Display_Movie(self):  # Hien thi cac bo phim
        for movie in self.movies:
            print(f"ID: {movie.id_movie}, Title: {movie.title}, Rating: {movie.rating}")
    def Delete_Movie(self,id_movie):
        for deleteMovie in self.movies:
            if deleteMovie.id_movie == id_movie:
                self.movies.remove(deleteMovie)
                break
    def Filter_Movie(self,title):
        filter_movie = []
        for filterMovie in self.movies:
            if title in filterMovie.title:
                filter_movie.append(filterMovie)
        return filter_movie
#     def Sort_Movie():
list_movie = MovieManagement()
movie1 = Movie(1,"Fast and Furious","Action","01/01/2005",9.5, "https/") 
movie2 = Movie(2,"Fast and Furious 2","Action","01/01/2006",8.5, "https/")
movie3 = Movie(3,"Fast and Furious 3","Action","01/01/2007",7.5, "https/")
movie4 = Movie(4,"Spiderman","Action","01/02/2007",10, "https/")
list_movie.AddMovie(movie1) #thêm 1 đối tượng vào danh sách(thêm bộ phim vào danh sách)
list_movie.AddMovie(movie2)
list_movie.AddMovie(movie3)
list_movie.AddMovie(movie4)
print("Danh sách trước khi xóa")
list_movie.Display_Movie() 
print("Danh sách sau khi xóa")
list_movie.Delete_Movie(3)
list_movie.Display_Movie()
print("Danh sach tim kiem:")
FilterMovie = list_movie.Filter_Movie("Spiderman")
for filter in FilterMovie:
        print(filter.title)
