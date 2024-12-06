'''
You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables.
Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.
'''


from gym_db_connect import connect_database                                                                                                                               
from mysql.connector import Error

gym_connection = connect_database()                                                                                                                                         #connecting to the database and setting it to a variable


# Task 1:Write a Python function to add a new member to the 'Members' table in the gym's database.

def add_member():                                                                                                                                                           #defining a function to add a memeber to the database

    if gym_connection is not None:                                                                                                                                          #making sure the databse connection is good
        try:                                                                                                                                                                #try block for error handling
            cursor = gym_connection.cursor()                                                                                                                                #creating a cursor

            name = input("Enter the name of the member you wish to add: ").title()                                                                                          #user input to get the name of the new member
            age = int(input("Enter the age of the member you wish to add: "))                                                                                               #user input to get the age of the new member, set to int becasue that's what the database is expecting

            query = 'INSERT INTO Members (name, age) VALUES (%s, %s)'                                                                                                       #setting up an INSERT query to add the new user to the Members table, and setting palceholders for the VALUES to be added

            cursor.execute(query, (name, age))                                                                                                                              #calling the cursor to execute the query substituting in the user inputs for the place holders
            gym_connection.commit()                                                                                                                                         #commiting the change to the database
            print("New Member added successfully")                                                                                                                          #print statement letting the user know the new member has been added
        
        except ValueError:                                                                                                                                                  #except block for a ValueError
            print("\nERROR: age must be an integer")                                                                                                                        #print statement letting he user know that age must be an integer
        
        except Error as e:                                                                                                                                                  #except block for a general Error
            print(f"Error: {e}")                                                                                                                                            #print statement printing off the error for the user

        finally:                                                                                                                                                            #finally block to close the cursor
            cursor.close()

    else:                                                                                                                                                                   #else block letting the user know a connection to the database couldnt be established
        print("Connection to database not established")        
    


# Task 2: Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.

def add_workout():                                                                                                                                                          #defining a function to add a workout to the database

    if gym_connection is not None:                                                                                                                                          #making sure the databse connection is good
        try:                                                                                                                                                                #try block for error handling
            cursor = gym_connection.cursor()                                                                                                                                #creating a cursor

            member_id = int(input("Enter the id number of the member you wish to add a workout for: "))                                                                     #user input to get member id of the person the workout is for
            session_date = input("Enter the date of the workout (YYYY-MM-DD): ")                                                                                            #user input to get the date of the workout session
            session_time = input("Enter the time of day of the session: ")                                                                                                  #user input to get the time of day for the session
            activity = input("Enter the activity to be performed: ")                                                                                                        #user input to get the activity being performed during the workout

            query = 'INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)'                                                 #INSERT INTO query to add the workout to the database, using place holders for the necessary VALUES

            cursor.execute(query, (member_id, session_date, session_time, activity))                                                                                        #calling the cursor to execute the query, substituting in user inputs for the place holders
            gym_connection.commit()                                                                                                                                         #commiting the changes to the database
            print("New workout added successfully")                                                                                                                         #print statement letting the user know the workout was successfully added
        
        except ValueError:                                                                                                                                                  #except block for a ValueError            
            print("Error: member id must be an integer")                                                                                                                    #print statement telling the user member id must be an integer
        
        except Error as e:                                                                                                                                                  #except block for a general error
            print(f"Error: {e}")                                                                                                                                            #print statement telling the user what error occured

        finally:                                                                                                                                                            #finally block to close the cursor
            cursor.close()

    else:                                                                                                                                                                   #else block letting the user know a connection to the database couldnt be established
        print("Connection to database not established")         


# Task 3: Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.

def update_member_age():                                                                                                                                                    #defining a function to update the age of a member
    if gym_connection is not None:                                                                                                                                          #making sure the databse connection is good
        try:                                                                                                                                                                #try block for error handling
            cursor = gym_connection.cursor()                                                                                                                                #creating a cursor

            id = int(input("Enter the id number of the member whose age you wish to update: "))                                                                             #user input to get member id
            age = int(input("Enter the updated age of the member: "))                                                                                                       #user input to get updated age of user
            
            query = 'UPDATE Members SET age = %s WHERE id = %s'                                                                                                             #query to UPDATE Members database, using SET to change the age and using WHERE to update the proper member. Also using place holders for the actual values.

            cursor.execute(query, (age, id))                                                                                                                                #calling the cursor to execute the query substituting in the user inputs for the place holder values
            gym_connection.commit()                                                                                                                                         #commiting the change to the database
            print("\nMember age updated successfully")                                                                                                                      #print statement letting the user know the age was updated successfully
        
        except ValueError:                                                                                                                                                  #except block for a ValueError
            print("\nError: id and age must be integers")                                                                                                                   #print statement telling the user id and age must be integers 
        
        except Error as e:                                                                                                                                                  #except block for a general error
            print(f"Error: {e}")                                                                                                                                            #print statement telling the user what error occured

        finally:                                                                                                                                                            #finally block to close the cursor
            cursor.close()
   
    else:                                                                                                                                                                   #else block letting the user know a connection to the database couldnt be established
        print("Connection to database not established") 


# Task 4: Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.

def delete_workout():                                                                                                                                                       #defining a function to delete a workout
    if gym_connection is not None:                                                                                                                                          #making sure the databse connection is good
        try:                                                                                                                                                                #try block for error handling
            cursor = gym_connection.cursor()                                                                                                                                #creating a cursor

            session_id = int(input("Enter the session id number of the workout you wish to delete: "))                                                                      #user input to get the session id of the workout to be deleted

            
            query = 'DELETE FROM WorkoutSessions WHERE session_id = %s'                                                                                                     #query deleting a workout from the WorkoutSessions table where the session id is a place holder value

            cursor.execute(query, (session_id, ))                                                                                                                           #calling the cursor to execute the query and substituting in the user input for the place holder value, the value is entered s a tuple because a tuple, list, or dictionary is expected
            gym_connection.commit()                                                                                                                                         #commiting the change to the database
            print("Workout successfully deleted")                                                                                                                           #print statement letting the user know the workout was successfully deleted
        
        except ValueError:                                                                                                                                                  #except block for a ValueError
            print("Error: session id must be an integer")                                                                                                                   #print statement telling the user session id must be an integer   
        
        except Error as e:                                                                                                                                                  #except block for a general error
            print(f"Error: {e}")                                                                                                                                            #print statement telling the user what error occured

        finally:                                                                                                                                                            #finally block to close the cursor
            cursor.close()

    else:                                                                                                                                                                   #else block letting the user know a connection to the database couldnt be established
        print("Connection to database not established") 


def main():                                                                                                                                                                 #main function to run the main program
    print("\nWelcome to the Gym Database Managment App")                                                                                                                    #print statement that welcomes the user to the application
    while True:                                                                                                                                                             #infinite while loop to cycle through all the function of the app
        print("\n1. Add a member\n2. Add a workout\n3. Update member age\n4. Delete workout\n5. Exit")                                                                      #print statement listing the available functions for the user
        user_choice = input("\nEnter the function you'd like to perform (1-5): ")                                                                                           #user input obtaining which function they'd like to use

        if user_choice == "1":                                                                                                                                              #if block for when user input is '1'
            add_member()                                                                                                                                                    #calling the function add_member
        
        elif user_choice == "2":                                                                                                                                            #elif block for when user choice is '2'
            add_workout()                                                                                                                                                   #calling the function add_workout
        
        elif user_choice == "3":                                                                                                                                            #elif block for when user choice is '3'
            update_member_age()                                                                                                                                             #calling the function upate_member_age
        
        elif user_choice == "4":                                                                                                                                            #elif block for when user choice is '4'
            delete_workout()                                                                                                                                                #calling the funciton delete_workout
        
        elif user_choice == "5":                                                                                                                                            #elif block for when user choice is '5'
            gym_connection.close()                                                                                                                                          #close the connection to the database
            print("\nThank you for using the Gym Database Managment App, goobye.")                                                                                          #goodbye statement for the user
            break                                                                                                                                                           #breaking the infinite loop
        
        else:                                                                                                                                                               #else block telling the user their input wasnt recognized
            print("\nInput not recognized please enter a number 1-5.")          

main()                                                                                                                                                                      #calling the main function