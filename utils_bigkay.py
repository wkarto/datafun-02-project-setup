''' ITERATION 5
FINAL Iteration

Module: Venirr Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:
In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''

#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - 'statistics': This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code. 
# Did you find statistics.mean()?
# Did you find statistics.stdev()?

import statistics

#####################################
# Declare global variables
#####################################
# Boolean variable to indicate if the company has internation clients
has_international_clients: bool = False

# Integer variable for the number of years in operation
years_in_operation: int = 4

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Engineering", "Artificial Intelliegnce", "Machine Learning"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.7, 5.0, 4.5]

Rating: list = [7.7, 5.7, 9.8]

# List of clients
clients = ['ABC', 'XYZ', 'IJK']


# Calculate Basic Statistics 
#   Do this BEFORE we declare the byline
#   so the values have been calculated
#   and are ready for use in the byline.
#####################################

#Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev()
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_rating: float = min(Rating)
max_rating: float = max(Rating)
mean_rating: float = statistics.mean(Rating)
stdev_rating: float = statistics.stdev(Rating)


#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------
Venirr Analytics: Delivering Professional Insights
---------------------------------------------------
Has International Clients:      {has_international_clients}
Years in Operation:             {years_in_operation}
Clients:     {clients}
Skills Offered:                 {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Rating: {Rating}

Minimum Client Satisfaction Scores:               {min_score}
Maximum Client Satisfaction Scores:               {max_score}
Average Client Satisfaction Scores:               {mean_score:.2f}
Standard Deviation of Client Satisfaction Scores: {stdev_score:.2f}

Minimum Rating:               {min_rating}
Maximum Rating:               {max_rating}
Average Rating:               {mean_rating:.2f}
Standard Rating: {stdev_rating:.2f}

"""

#####################################
# Define the get_byline() Function.
#####################################

def get_byline() -> str:
   ''' Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
