import json
f = open("matchscout.json", encoding="utf8")
data = json.load(f)
matches = data["data"]
teams = []
for key in matches: 
    teams.append(key)
# print(teams)


def sortByAutoScore(matches):
    averages = []
    for match in matches: 
        k = match
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            score = submission["notesScoredInSpeaker"]*5  +submission["notesScoredInAmp"]*2
            val+=score
            times+=1
        averages.append((k,val/times))

    sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} in auto")

def sortByTeleopScore(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            try:
                score = submission["notesScoredInSpeakerInTeleop"]*2  +submission["notesScoredInAmpInTeleop"]*1
                val+=score
                times+=1
            except:
                print("database skill issue")
        averages.append((k,val/times))

    sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} in teleop (not couning amped shots)")

def sortByAutoNotes(matches):
    averages = []
    for match in matches: 
        k = match
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes = submission["notesScoredInSpeaker"] +submission["notesScoredInAmp"]
            val+=Notes
            times+=1
        averages.append((k,val/times))

    sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} notes in auto")

def sortByTeleopNotes(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            try:
                Notes = submission["notesScoredInSpeakerInTeleop"]  +submission["notesScoredInAmpInTeleop"]
                val+=Notes
                times+=1
            except:
                print("database skill issue")
        averages.append((k,val/times))
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} notes in teleop")

def sortByClimb(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            score = submission["climbRating"]
            if score == "No Climb" or score == "-":
                val+=0
            else:
                val+=int(score)
            times+=1
        averages.append((k,val/times))
    sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} had an average climb rating of {i[1]}")

def sortByTeleopAmp(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
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
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} amp notes in teleop")

def sortByTeleopSpeaker(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
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
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} speaker notes in teleop")

def sortByAutoAmp(matches):
    averages = []
    for match in matches: 
        k = match
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes =submission["notesScoredInAmp"]
            val+=Notes
            times+=1
        averages.append((k,val/times))
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} amp notes in auto")

def sortByAutoSpeaker(matches):
    averages = []
    for match in matches: 
        k = match
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes = submission["notesScoredInSpeaker"]
            val+=Notes
            times+=1
        averages.append((k,val/times))
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} speaker notes in auto")

def sortByTotalAmp(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes = submission["notesScoredInAmp"]
            val+=Notes
            times+=1
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
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} amp notes in total")

def sortByTotalSpeaker(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        auto = matches[match]["autoscout"]
        val = 0
        times = 0
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            Notes = submission["notesScoredInSpeaker"]
            val+=Notes
            times+=1
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
        sorteds = (sorted(averages, key = lambda x: x[1]))
    for i in sorteds:
        print(f"team {i[0]} scored on average {i[1]} Speaker notes in total")

# sortByAutoScore(matches)
# sortByTeleopScore(matches)
# sortByAutoNotes(matches)
# sortByTeleopNotes(matches)
# sortByClimb(matches)
# sortByTeleopAmp(matches)
# sortByTeleopSpeaker(matches)
# sortByAutoAmp(matches)
# sortByAutoSpeaker(matches)
# sortByTotalAmp(matches)
# sortByTotalSpeaker(matches)

