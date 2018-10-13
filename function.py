def show(d):
    for s in training:
        print("{0}: {1}".format(s, d[s]))

if __name__=="__main__":
    training = {"workout": "running",
                "time": 60,
                "quantity": 4,
                "place": "fitnessacademy"}

show(training)
