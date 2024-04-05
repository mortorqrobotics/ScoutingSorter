import json
from datetime import datetime
f = open("test.json", encoding="utf8")
# f = open("matchscout.json", encoding="utf8")
data = json.load(f)
matches = data["data"]


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
    f = open("sortByAutoScore.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} in auto\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
    f = open("sortByTeleopScore.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} in teleop (not couning amped shots)\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

def sortByTotalScore(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"] 
        auto = matches[match]["autoscout"]
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
        for key in auto:
            submissionKey = list(auto[key].keys())[0]
            submission = auto[key][submissionKey]
            score = submission["notesScoredInSpeaker"]*5  +submission["notesScoredInAmp"]*2
            val+=score
        averages.append((k,val/times))

    sorteds = (sorted(averages, key = lambda x: x[1]))
    f = open("sortByTotalScore.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} in teleop (not couning amped shots)\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
    f = open("sortByAutoNotes.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} notes in auto\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
        f = open("sortByTeleopNotes.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} notes in teleop\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
            try:
                val+=int(score)
            except:
                val+=0
            times+=1
        averages.append((k,val/times))
    sorteds = (sorted(averages, key = lambda x: x[1]))
    f = open("sortByClimb.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} had an average climb rating of {i[1]}\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

def sortByDefense(matches):
    averages = []
    for match in matches: 
        k = match
        tele = matches[match]["teleopscout"]
        val = 0
        times = 0
        for key in tele:
            submissionKey = list(tele[key].keys())[0]
            submission = tele[key][submissionKey]
            score = submission["defenseRating"]
            try:
                val+=int(score)
            except:
                val+=0
            times+=1
        averages.append((k,val/times))
    sorteds = (sorted(averages, key = lambda x: x[1]))
    f = open("sortByDefense.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} had an average defense rating of {i[1]}\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
        f = open("sortByTeleopAmp.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} amp notes in teleop\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
        f = open("sortByTeleopSpeaker.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} speaker notes in teleop\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
        f = open("sortByAutoAmp.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} amp notes in auto\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
        f = open("sortByAutoSpeaker.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} speaker notes in auto\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
            except:
                print("database skill issue")
        averages.append((k,val/times))
        sorteds = (sorted(averages, key = lambda x: x[1]))
        f = open("sortByTotalAmp.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} amp notes in total\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

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
            except:
                print("database skill issue")
        averages.append((k,val/times))
        sorteds = (sorted(averages, key = lambda x: x[1]))
        f = open("sortByTotalSpeaker.txt", "w")
    for i in sorteds:
        f.write(f"team {i[0]} scored on average {i[1]} Speaker notes in total\n")
    f.write(f"\nlast updated at "+str(datetime.now()))

sortByAutoScore(matches)
sortByTeleopScore(matches)
sortByTotalScore(matches) 
sortByAutoNotes(matches)
sortByTeleopNotes(matches)
sortByClimb(matches)
sortByTeleopAmp(matches)
sortByTeleopSpeaker(matches)
sortByAutoAmp(matches)
sortByAutoSpeaker(matches)
sortByTotalAmp(matches)
sortByTotalSpeaker(matches)
sortByDefense(matches)