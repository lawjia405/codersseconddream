# Define a class to represent a user
class User:
    def __init__(self, name, age, gender, height, preferences):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferences = preferences
        self.height = height


def calculate_match_score(user1, user2):
    # Define a dictionary of preference weights
    preference_weights = {
        "not working": 2,
        "working": 1,  
        "morning person": 1,
        "night owl": 1,
        "boba fein": 1,
        "boba hater": 1,
    }

    # Initialize a match score variable
    match_score = 0

    # Increment the match score for each preference that the users have in common, using the preference weights
    for preference in user1.preferences:
        if preference in user2.preferences:
            match_score += preference_weights[preference]

    # Return the match score
    return match_score

# Define a function to find the best match for a given user
def find_best_match(user, users):
    # Initialize variables to keep track of the best match
    best_match = None
    best_match_score = 0

    # Loop through the list of users and calculate the match score for each one
    for potential_match in users:
        # Skip the user themselves
        if potential_match == user:
            continue

        # Calculate the match score for the potential match
        match_score = calculate_match_score(user, potential_match)

        # If the match score is higher than the current best match score, update the best match
        if match_score > best_match_score:
            best_match = potential_match
            best_match_score = match_score

    # Return the best match
    return best_match


# Define some sample users
import random

# List of possible preferences
preferences = ["working", "not working", "morning person", "night owl", "boba fein", "boba hater"]

# Generate 1000 users with random attributes
users = [
    User("Dennis", 25, "female", 60, ["not working", "morning person"]),
    User("Fidel", 32, "male", 72, ["not working", "night owl"]),
    User("Charlie", 29, "male", 48, ["working", "morning person"]),
    User("Diane", 27, "female", 90, ["working", "night owl"]),
    User("Sheila", 22, "female", 50, ["not working", "morning person", "boba fein"]),
    User("Frank", 35, "male", 52, ["working", "night owl", "likes pets"]),
    User("Greta", 31, "female", 54, ["not working", "morning person", "boba hater"]),
    User("Henry", 30, "male", 74, ["working", "night owl", "boba hater"]),
    User("Bob", 45, "male", 30, ["working", "night owl", "boba fein"]),

]

best_match = find_best_match(users[0], users)