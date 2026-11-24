# === Stage 8: Текстовый поиск ===
# Project: VinylCrate
def search_tracks(tracks, query):
    query = query.strip().lower()
    results = []
    for track in tracks:
        haystack = " ".join(
            [
                track.get("title", "").lower(),
                track.get("artist", "").lower(),
                track.get("year", "").lower(),
                track.get("condition", "").lower(),
            ]
        )
        if query in haystack:
            results.append(haystack)
    return results


def search_tracks_with_marks(tracks, query):
    query = query.strip().lower()
    results = []
    for track in tracks:
        haystack = " ".join(
            [
                track.get("title", "").lower(),
                track.get("artist", "").lower(),
                track.get("year", "").lower(),
                track.get("condition", "").lower(),
            ]
        )
        if query in haystack:
            matches = 0
            for word in re.split(r"\s+", query):
                if word and word in haystack:
                    matches += 1
            mark = ""
            if matches == len([w for w in query.split() if w]):
                mark = " " + query
            results.append(haystack + mark)
    return results


if __name__ == "__main__":
    sample = [
        {
            "title": "Abbey Road",
            "artist": "The Beatles",
            "year": "1969",
            "condition": "mint",
        },
        {
            "title": "Nevermind",
            "artist": "Nirvana",
            "year": "1991",
            "condition": "good",
        },
        {
            "title": "Dark Side of the Moon",
            "artist": "Pink Floyd",
            "year": "1973",
            "condition": "very good",
        },
    ]
    print("Search for 'beatles':")
    for line in search_tracks_with_marks(sample, "beatles"):
        print(line)
    print("Search for 'MINT':")
    for line in search_tracks_with_marks(sample, "MINT"):
        print(line)
    print("Search for '1991':")
    for line in search_tracks_with_marks(sample, "1991"):
        print(line)
