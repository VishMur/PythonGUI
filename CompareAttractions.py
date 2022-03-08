


def compareToDesired(desired, data):
    difference = 0

    # Different location and types are already eliminated, just need difference
    # if desired[1] != "":
    #     attractionType = desired[1]
    #     if attractionType != data[1]:
    #         return -1


    # if desired[2] != "":
    #     attractionType = desired[2]
    #     if attractionType != data[2]:
    #         return -1

    if desired[3] != "":
        difference += abs(desired[3] - data[3])
    if desired[4] != "":
        difference += abs(desired[4] - data[4])
    if desired[5] != "":
        difference += abs(desired[5] - data[5])

    return difference

