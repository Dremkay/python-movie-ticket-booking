from projectComponents import *
from random import randint


print("\n\t\t\tWelcome to The Movie Booking Portal\n".upper())

try:

    viewers=acceptViewers()
    booked=0

    for i in range(viewers): 
        print(' ')   
        userName = acceptUserName() # validate user name!!!!!!!!!!!!!!!!
        # userName = usersname()
        print()
        day = acceptDay()      
        # print()
        query=queryMovies(day)

        while True:
            if query !=[]:
                movies =listMovies(query)
                break
            else:
                print(' ')
                print(f'\t\t\tThere are no movies showing on {day}. Check other weekdays')
                print(' ')
                day = acceptDay()
                query=queryMovies(day)

        # selecting movie
        proceed=0
        print(' ')
        while proceed==0:
            movieName = input("Select movie: ").strip().lower()
            while True:
                if movieName in [movie.name for movie in movies]:
                    movie=selectMovie(movieName,movies)
                    userAge=acceptAge()        
                    break
                else:
                    print('Please, type in the available movie name\n')
                    movieName = input("Select movie (e.g squid game): ").strip().lower()
            if userAge < movie.age:
                print(f"Sorry you are too young to watch the selected movie!\n")
                print('Select another movie: \n')
            else:
                proceed=1

        ticket=movie.moviecode+str(movie.age)+userName[-3:].upper()
        # print('go ahead..',ticket)
        balance = randint(500,4000)
        while balance< movie.cost():
            print(f'Your wallet balance is N{balance} and the ticket is N{movie.cost()}. Not enough to book your movie at the moment.\n')
            print('Click Enter to generate a new balance \n')
            input()
            print('Generating a new balance...\n')
            balance = randint(500,4000)

        print(f'your Wallet Balance is now N{balance}, enough to book your movie...')
        print('Click Enter to book your movie')
        input()
        # generate a booking.txt file containing the name of movie, 
        # booking ID/Ticket, user's name, PG code, day and time of the movie.
        f=open('allbookings.txt','a')
        f.write(f'{movie.name},{ticket},{userName},{movie.pg},{movie.dayofweek},{movie.time}\n')
        f.close()
                            

        body =f'''****************************************************************
        *                         MOVIE TICKET                         *
        *       Ticket ID: {ticket}                                     *
        *           Movie Name: {movie.name.title()}                        
        *           Day:        {movie.dayofweek}                   
        *           Time:       {movie.time}
                    PG:         {movie.pg}           
        *           User:       {userName.upper()}                             
        *                                                              *
        *       NB:This is non refundable. Thanks for patronizing      *
        ****************************************************************'''
        f = open(f'BookingTickets/{userName.upper()}ticket.txt', 'w')
        print(body, file=f)
        f.close()
        print("Movie booked successfully...")
        booked+=1
        if booked < viewers:
            print(' ')
            print("Press enter to Book the next viewer...")
            input()
        else:
            print('All users booked successfully!')
            print("Check booking tickets directory for the ticket(s)...")
            print(' ')
            print('THANK YOU FOR BOOKING'.center(50))
            print(' ')
            print(' ')
except KeyboardInterrupt:
    print()

