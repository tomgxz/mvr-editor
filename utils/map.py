def gdtfmap():
    with open("./data/gdtfmap.csv") as f:
        read = f.read().split("\n")

        data = []

        for line in list(map(lambda x: x.split(","),read[1:])):
            if len(line) < 5: continue
            data.append({
                "layer":line[0],
                "file":line[1],
                "mode":line[2],
                "channels":int(line[3]),
                "name":line[4]
            })        

    f.close()
    return data