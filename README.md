PROJECT: MOVIE ONLINE TICKET BOOKING SIMULATION PROGRAM PROJECT
PROGRAMMING LANGUAGE: PYTHON
ASSIGNED STUDENTS: GROUP 3
This project simulates the process of booking a movie ticket online. You have been given a database (movies.db) containing movie data for 10 different movies. The movies are categorized based on parental guidance restrictions which apply to different ages of the viewers. Each movie has its own movie code for easy identification. Depending on the number of viewers that want to purchase a movie ticket, you will be required to make successful bookings and output these records. 
WHAT YOUR PROGRAM MUST ACCOMPLISH
Your program must be able to do or accomplish the following: 
1.	Prompt customer support for how many user booking they want to make. This takes care of the number of users they want to book a ticket for.
2.	Accept user's name and day they desire to watch the movie.
3.	Display all movies that are to be shown on that day alone.
4.	Accept user's age. If the age is less than the minimum required for the movie. the booking should be aborted with a message to that effect.
5.	If age requirement is satisfied, generate a movie ticket/booking ID that is a combination of the movie code, minimum age for that movie and the last three letters of the user's name (e.g SW16SAM).
6.	All movies cost NGN2500 on Friday and NGN3000 on Saturday. Generate a random wallet balance for current user to be booked and display it for the user to see his balance.
7.	If balance is not enough to book the movie keep generating a wallet balance for the user to see until the displayed balance is enough to book a movie.
8.	If displayed balance can book the movie, complete the booking and generate a booking.txt file containing the name of movie, booking ID/Ticket, user's name, PG code, day and time of the movie.
9.	All successful booking should have their booking txt files respectively (representing the movie ticket for each user).
