records = {
    ("rick", "sanchez"),
    ("morty", "sanchez"),
    ("nandor", "the relentless"),
    ("Lazlo", "the reletless"),
    ("Beth", "sanchez"),
    ("summer", "smith"),
    ("jerry", "smith")
}

def build_index(records):
    index = {}

    for name, state in records:
        if state in index:
            index[state].append(name)
        else:
            index[state] = []
            index[state].append(name)

    return index

idx = build_index(records)

print(idx["smith"])

        