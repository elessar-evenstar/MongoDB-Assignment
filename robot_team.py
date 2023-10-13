import json
import pymongo

myclient = pymongo.MongoClient("localhost", 1678)
mydb = myclient["training"]
mycol = mydb["team-data"]
with open("example_tim_data.json") as f:
    data = json.load(f)
for i in data:
    mycol.insert_one(i)
class Team:
    def __init__(self, number):
        self.number = number
    def average_balls_scored(self):
        numbers = []
        iterable = 0
        for team in data:
            if team["team_num"] == self.number:
                numbers.append(team["num_balls"])
                iterable += 1
        sum2 = sum(numbers)
        average = sum2/iterable
        return average
    def least_balls_scored(self):
        numbers = []
        for team in data:
            if team["team_num"] == self.number:
                numbers.append(team["num_balls"])
        min2 = min(numbers)
        return min2
    def most_balls_scored(self):
        numbers = []
        for team in data:
            if team["team_num"] == self.number:
                numbers.append(team["num_balls"])
        max2 = max(numbers)
        return max2
    def num_matches_played(self):
        iterable = 0
        for team in data:
            if team["team_num"] == self.number:
                iterable += 1
        return iterable
    def percent_climb_success(self):
        numbers = []
        total = 0
        for team in data:
            if team["team_num"] == self.number:
                if team["climbed"] == True:
                    numbers.append(1)
                    total += 1
                if team["climbed"] == False:
                    total += 1
        sum2 = sum(numbers)
        percentfake = sum2/total
        percent = percentfake * 100
        return percent

answer = int(input("What is your team number? "))
team = Team(answer)
print("Average balls scored: " + str(team.average_balls_scored())) 
print("Least balls scored: " + str(team.least_balls_scored()))  
print("Most balls scored: " + str(team.most_balls_scored())) 
print("Number of matches played: " + str(team.num_matches_played()))  
print("Percent of climb success: " + str(team.percent_climb_success()) + "%")    
mycol.insert_one(team.average_balls_scored())
mycol.insert_one(team.least_balls_scored())
mycol.insert_one(team.most_balls_scored())
mycol.insert_one(team.num_matches_played())
mycol.insert_one(team.percent_climb_success())