def layers():
    with open("./data/gdtfmap.csv") as f:
        read = f.read().split("\n")

        data = []

        for line in list(map(lambda x: x.split(","),read[1:])):
            print(line)
            if len(line) < 5: continue
            if line[0] not in data: data.append(line[0])

    f.close()
    return data

def files():
    with open("./data/gdtfmap.csv") as f:
        read = f.read().split("\n")

        data = []

        for line in list(map(lambda x: x.split(","),read[1:])):
            if len(line) < 5: continue
            if line[1] not in data: data.append(line[1])

    f.close()
    return data

def names():
    with open("./data/gdtfmap.csv") as f:
        read = f.read().split("\n")

        data = []

        for line in list(map(lambda x: x.split(","),read[1:])):
            if len(line) < 5: continue
            if line[4] not in data: data.append(line[4])

    f.close()
    return data