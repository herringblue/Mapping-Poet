# adjectives.json and nouns.json from: https://github.com/leonardr/olipy
# places.json from personal Moves data.
import json

nouns_file = open("nouns.json").read()
adjectives_file = open("adjectives.json").read()
places_file = open("places.json").read()
nouns = json.loads(nouns_file)
adjectives = json.loads(adjectives_file)
places = json.loads(places_file)
maximum_n = len(nouns)
maximum_a = len(adjectives)

punctuation = [".\n", ",", ".", "?", ".", ",\n", "?\n", "!\n"]
conjunction = ["and", "by", "with", "to", "for", "or", "not", "yet", "so", "nor", "caused", "is", "over"]
pronoun = ["my", "that", "thy", "his", "her", "our", "they", "their", "all", "this", "those"]


final = []
for place in places:
    segments = place["segments"]
    newPara = place.get("lastUpdate")

    for segment in segments:

        activities = segment.get("activities")
        if activities != None:
            for activity in activities:
                keya = activity["distance"]
                anum = int(keya)
                while anum > maximum_a:
                    anum = anum - maximum_a
                final.append(adjectives[anum])

        place = segment.get("place")
        if place != None:
            keyp = place["id"]
            pnum = int(keyp)
            while pnum > maximum_n:
                pnum = pnum - maximum_n
                cnum = pnum
            if cnum % 4 == 0:
                while cnum > (len(conjunction) - 1):
                    cnum = cnum - len(conjunction)
                final.append(conjunction[cnum])
            elif cnum % 3 == 0:
                while cnum > (len(pronoun) - 1):
                    cnum = cnum - len(pronoun)
                final.append(pronoun[cnum])
            final.append(nouns[pnum])

        lastUpdate = segment.get("lastUpdate")
        if lastUpdate != None:
            lnum = int(filter(str.isdigit, str(lastUpdate)))
            lnum = lnum % len(punctuation)
            final.append(punctuation[lnum]+"\n")

    if newPara != None:
        final.append("---\n\n")

joined = " ".join(final)
joined = joined.replace(" ?", "?").replace(" .", ".").replace(" !", "!").replace(" ,", ",").replace("\n ", "\n")

with open('locationpoetry.txt', 'a') as f:
    f.write(joined)
