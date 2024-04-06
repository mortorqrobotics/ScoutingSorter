import json
import numpy as np
f = open("test.json", encoding="utf8")
# f = open("matchscout.json", encoding="utf8")
data = json.load(f)
teams = data["data"]



def checkAutoSpeaker(teams):
    means = {}
    stds = {}
    threshold = 3
    for team in teams: 
        k = team
        auto = teams[team]["autoscout"]
        data = []
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            speaker = submission["notesScoredInSpeaker"]
            data.append(speaker)
        means[k] = np.mean(data)
        stds[k] = np.std(data)
    print(means)
    print(stds)
    for team in teams:
        k = team
        auto = teams[team]["autoscout"]
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            speaker = submission["notesScoredInSpeaker"]
            if(stds[k] != 0):
                zscore = (speaker-means[k])/stds[k]
                print(zscore)
            else:
                print("divide by 0")
                continue
            if abs(zscore)>threshold:
                print(f"outlier: team{k} submission{key} name{submissionKey} \nautospeaker: {speaker}, mean: {means[k]}, std: {stds[k]}\n")

checkAutoSpeaker(teams)