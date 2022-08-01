import sqlite3

def acceptViewers():
    while True:
        users=input('Enter number of Customers: ').strip()
        try:
            int(users)
            break
        except ValueError:
            print('Please input a valid integer')
        
    return int(users)

        

# def usersname():
#     while True:
#         try:
#             name = input('\nEnter your Full name: ')
#             if name.isalpha():
#                 # return name
#                 break
#         except:
#             pass
#         print('name cannot be in number')
#     while len(name)<3:
#         print('name cannot be less than 3 characters')
#         name =input('Enter your full name: ').strip()
#     return name 

def acceptUserName():
    user = input("Enter customer's name: ").strip()
    num=[i for i in user if i in '1234567890,\./<>?;":\'=+)(!@#$%^&*-_}[]{']

    while user =='' or len(num)>0 or len(user) <3:
        if user =='':
            print(f'Customer\'s name cannot be empty.')
        # user = input("Enter user's name: ").strip()
        elif len(num)>0:
            print('Non-alphabet not allowed in viewer\'s name')
        else:
            print(f'Customer name cannot be less than 3 characters.')
        user = input("Please!, Enter customer's name: ").strip()
        num=[i for i in user if i in '1234567890,\./<>?;":\'=+)(!@#$%^&*-_}[]{']
    # while len(user) <3:
    #     print(f'Customer name cannot be less than 3 characters.')
    #     user = input("Enter customer's name: ").strip()
    # # validate user name!!!!!!!!!!!!!!!!
    # num=[i for i in user if i in '1234567890,\./<>?;":\'=+)(!@#$%^&*-_}[]{']
    # while len(num)>0:
    #     print('Invalid name')
    #     acceptUserName()
    return user


def acceptDay():
    while True:
        day = input('Enter booking day, e.g (Friday): ').strip().title()
        if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:
            break
        print('Please! Enter a valid weekday') 
    return day


def acceptAge():
    while True:
        age=input('Enter Customer\'s age: ').strip()
        if age=='':
            age='a'
        alp=[]
        for i in age:
            if i not in '0123456789':
                alp.append(i)
        if len(alp) ==0:
            break
        else:
            print("Kindly enter valid age: ")
    return int(age)


    # while True:
    #     try:
    #         age = input('user age: ')
    #         int(age)
    #     except ValueError:
    #         print("Kindly enter valid age: ")
    #     finally:

    # if isinstance(age,int):
    #     return age

def queryMovies(d):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM moviesData WHERE DayOfWeek = '{d}'")
    data = cur.fetchall()
    conn.close()
    return data


class Movie:
    def __init__(self,name,moviecode,dayofweek,pg,age,time):
        self.name=name
        self.moviecode=moviecode
        self.dayofweek=dayofweek
        self.pg=pg
        self.age=age
        self.time=time
    def cost(self):
        if self.dayofweek=='Friday':
            return 2500
        elif self.dayofweek=='Saturday':
            return 3000
        else:
            return 0



def noMovies(day):
    print(f'There are no movies showing on {day}. Check other weekdays')
    day = acceptDay()
    query=queryMovies(day)
    #no movie code


def listMovies(movies):
    # go ahead and proceed
    movieList=[]
    for movie in movies:
        name,moviecode,dayofweek,pg,age,time =movie
        m = Movie(name.lower(),moviecode,dayofweek,pg,age,time)
        movieList.append(m)
        
    print(f'These are the available movies on {dayofweek}:')
    n=1
    for movie in movieList:
        print(f'        {n}.  {movie.name.title()}  ({movie.pg})  {movie.time}')
        n+=1
    return movieList


def selectMovie(name,movies):
    # movie:Movie
    for i in movies:
        if i.name == name:
            movie=i
    return movie
