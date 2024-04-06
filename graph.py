# each team has a 4 element array: auto amp, auto speaker, tele amp, tele speaker
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
# f = open("test.json", encoding="utf8")
f = open("matchscout.json", encoding="utf8")
data = json.load(f)
teamsJSON = data["data"]
graphObj = {}

def setTeams(teamsJSON, graphObj):
    for team in teamsJSON:
        graphObj[team] = []



def AutoAmp(teamsJSON, graphObj):
    averages = []
    for team in teamsJSON: 
        k = team
        auto = teamsJSON[team]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes =submission["notesScoredInAmp"]
            val+=Notes
            times+=1
        averages.append((k,val/times))
    for i in averages:
        graphObj[i[0]].append(i[1])

def AutoSpeaker(teamsJSON, graphObj):
    averages = []
    for team in teamsJSON: 
        k = team
        auto = teamsJSON[team]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes = submission["notesScoredInSpeaker"]
            val+=Notes
            times+=1
        averages.append((k,val/times))
    for i in averages:
        graphObj[i[0]].append(i[1])

def TeleopAmp(teamsJSON, graphObj):
    averages = []
    for team in teamsJSON: 
        k = team
        tele = teamsJSON[team]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            try:
                Notes = submission["notesScoredInAmpInTeleop"]
                val+=Notes
                times+=1
            except:
                print("database skill issue")
        averages.append((k,val/times))
    for i in averages:
        graphObj[i[0]].append(i[1])

def TeleopSpeaker(teamsJSON, graphObj):
    averages = []
    for team in teamsJSON: 
        k = team
        tele = teamsJSON[team]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            try:
                Notes = submission["notesScoredInSpeakerInTeleop"]
                val+=Notes
                times+=1
            except:
                print("database skill issue")
        averages.append((k,val/times))
    for i in averages:
        graphObj[i[0]].append(i[1])

setTeams(teamsJSON, graphObj)
AutoAmp(teamsJSON, graphObj)
AutoSpeaker(teamsJSON, graphObj)
TeleopAmp(teamsJSON, graphObj)
TeleopSpeaker(teamsJSON, graphObj)

# print(graphObj)
df = pd.DataFrame(data=graphObj)
# df.rename(index={0: "AutoAmp", 1: "AutoSpeaker", 2: "TeleopAmp", 3: "TeleopSpeaker"})
df = df.T
new_labels = ["AutoAmp", "AutoSpeaker", "TeleopAmp", "TeleopSpeaker"]
df.columns = new_labels
# Set the column labels

# Now the DataFrame has columns labeled 'X' and 'Y'

print(df)

# plot data in stack manner of bar type
# df.plot(x='Team', kind='bar', stacked=True,
#         title='Stacked Bar Graph by dataframe')
# plt.show()