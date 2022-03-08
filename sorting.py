import data
import sorting
import CompareAttractions

desired = ["","","","","",""]
chosenAttractions = []
sortedAttractions = []

def showRecommendedAttractions():
    print("Desired List=",desired[1])
    print("Chosen List=",chosenAttractions[0][1])
    for i in (chosenAttractions):
        for j, item in enumerate(i):
            for k, test in enumerate(i):
                if ((desired[1] == item) and (desired[2] == test)):
                    print("Location and type matched")
                    sortedAttractions.append(i)
                    print("sort attractions = ",sortedAttractions)


# desiredVisitorsAttribute = input("On a scale of 0-10, how many visitors are you comfortable with, "
#                                  "with 0 being no visitors and 10 being many visitors?\nEnter any other value"
#                                  " if you have preference: ")
#
# if desiredVisitorsAttribute.isnumeric():
#     desiredVisitorsAttribute = int(desiredVisitorsAttribute)
#     if desiredVisitorsAttribute >= 0 & desiredVisitorsAttribute <= 10:
#         desired[1] = desiredVisitorsAttribute
#
# desiredRatingAttribute = input("\nOn a scale of 0-10, how highly rated would you like your attraction "
#                                "to be, with 0 being the lowest rated, and 10 the highest rated?\n"
#                                "Enter any other value if you have no preference: ")
#
# if desiredRatingAttribute.isnumeric():
#     desiredRatingAttribute = int(desiredRatingAttribute)
#     if desiredRatingAttribute >= 0 & desiredRatingAttribute <= 10:
#         desired[2] = desiredRatingAttribute
#
# desiredPriceAttribute = input("\nOn a scale of 0-10, how pricey would you like your attraction "
#                                "to be, with 0 being the cheapest, and 10 the most expensive?\n"
#                                "Enter any other value if you have no preference: ")
#
# if desiredPriceAttribute.isnumeric():
#     desiredPriceAttribute = int(desiredPriceAttribute)
#     if desiredPriceAttribute >= 0 & desiredPriceAttribute <= 10:
#         desired[4] = desiredPriceAttribute
#
# desiredTypeAttribute = input("\nFrom the following list of types of attractions: "
#                              "\n1 = Man-made / purpose-built"
#                              "\n2 = Food"
#                              "\n3 = Natural / outdoor"
#                              "\n4 = Sports"
#                              "\n5 = Political / religious / cultural / heritage"
#                              "\nPlease input your desired type of attraction, or enter any other"
#                              "value for no preference: ")
#
# if desiredTypeAttribute.isnumeric():
#     desiredTypeAttribute = int(desiredTypeAttribute)
#     if desiredTypeAttribute >= 1 & desiredTypeAttribute <= 5:
#         desired[3] = desiredTypeAttribute
#
#
# desiredSafeAttribute = input("\nOn a True or False scale, do you want to be safe, "
#                                "with False being not safe and True being safe?\n"
#                                "Enter any other value if you have no preference: ")
#
# if desiredSafeAttribute.isalpha():
#     if desiredSafeAttribute == "True":
#         desired[5] = True
#     elif desiredSafeAttribute == "False":
#         desired[5] = False

count = 0
currentIndex = 0
length = len(data.allAttractions)
while count < length:
    if CompareAttractions.compareToDesired(desired, data.allAttractions[currentIndex]) < 0:
        data.allAttractions.pop(currentIndex)
        count += 1
    else:
        currentIndex += 1
        count += 1





def sortingCriteria(data):

    return CompareAttractions.compareToDesired(desired, data)

data.allAttractions.sort(key=sortingCriteria)

print(data.allAttractions)

#print(data.allAttractions)