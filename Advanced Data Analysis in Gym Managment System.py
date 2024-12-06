'''
As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data.
Your task is to develop Python functions that execute advanced SQL queries for distinct department identification,
employee count in each department, and age-based employee filtering. '''


from gym_db_connect import connect_database                                                                                                                               
from mysql.connector import Error

gym_connection = connect_database()                                                                                                                                         #connecting to the database and setting it to a variable


# Task 1: Retrieve the details of members whose ages fall between 25 and 30.

def get_members_in_age_range():                                                                                                                                             #defining a function to get members in a certain age range
    try:
        if gym_connection is not None:                                                                                                                                      #checking the connection to the database
            cursor = gym_connection.cursor()                                                                                                                                #creating a cursor 

            age1 = int(input("Enter the lower bound for your age range: "))                                                                                                 #user input getting the lower limit to the age range they wish to search
            age2 = int(input("Enter the upper bound for your age range: "))                                                                                                 #user input getting the upper limit to the age range they wish to search

            query = 'SELECT * FROM Members WHERE age BETWEEN %s AND %s'                                                                                                     #query where we're selecting all from the members table but setting a stipulation where the age of the member must fall between two place holder values

            cursor.execute(query, (age1,age2))                                                                                                                              #calling the cursor to execute the query

            for row in cursor.fetchall():                                                                                                                                   #for loop to cycle through the rows in cursor obtained using fetchall 
                print(row)                                                                                                                                                  #printing the rows                                                                                                                                        
                 
    except ValueError:                                                                                                                                                      #except block for a ValueError
        print("\nAges must be integers")                                                                                                                                      #print statement telling the user the age inputs must be integers

    except Error as e:                                                                                                                                                      #print statement printing off the error for the user
        print(f"\nError: {e}")                                                                                                                                                #print statement telling the user the error
    
    finally:                                                                                                                                                                #finally block
        cursor.close()                                                                                                                                                      #closing down the cursor
        gym_connection.close()                                                                                                                                              #closing the conenction to the database





get_members_in_age_range()                                                                                                                                                  #calling the function get_memebers_in_age_range