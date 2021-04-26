def MTC(time):
    times = time.split(":")
    hours = int(times[0])
    minutes = int(times[1])
    total = hours*60
    total = total + minutes
    return total

def toMTC(time):
    minutes = time%60
    hours = (time-minutes)/60
    hours = int(hours)
    hours = str(hours)
    minutes = int(minutes)
    minutes = str(minutes)
    if len(minutes) < 2:
        minutes = "0"+minutes
    list = [hours, minutes]
    string = ":"
    result = string.join(list)
    return result


def calendarAlgorithm(list1, list2, meetingLength):
    list1Avaliable = []
    list2Avaliable = []
    totalAvaliable = []
    finalList = []
    result = []
    for i in range(0, len(list1)):
        if i == len(list1)-1:
            timeSlotList = list1[i].split('-')
            boundEnd = list1[0].split('-')
            if (MTC(boundEnd[1])-MTC(timeSlotList[1])) >= meetingLength:
                avaliable = []
                avaliable.append(timeSlotList[1])
                avaliable.append(boundEnd[1])
                str='-'
                avaliable = str.join(avaliable)
                list1Avaliable.append(avaliable)
        if i == 0:
            timeSlotList = list1[0].split('-')
            timeSlotList2 = list1[1].split('-')
            if (MTC(timeSlotList2[0])-MTC(timeSlotList[0]) >= meetingLength):
                avaliable = []
                avaliable.append(timeSlotList[0])
                avaliable.append(timeSlotList2[0])
                str = '-'
                avaliable = str.join(avaliable)
                list1Avaliable.append(avaliable)
        elif i != 0 and i != len(list1)-1:
            timeSlotList = list1[i].split('-')
            timeSlotList2 = list1[i + 1].split('-')
            if (MTC(timeSlotList2[0]) - MTC(timeSlotList[1])) >= meetingLength:
                avaliable = []
                avaliable.append(timeSlotList[1])
                avaliable.append(timeSlotList2[0])
                str = '-'
                avaliable = str.join(avaliable)
                list1Avaliable.append(avaliable)
    for i in range(0, len(list2)):
        if i == len(list2)-1:
            timeSlotList = list2[i].split('-')
            boundEnd = list2[0].split('-')
            if (MTC(boundEnd[1])-MTC(timeSlotList[1])) >= meetingLength:
                avaliable = []
                avaliable.append(timeSlotList[1])
                avaliable.append(boundEnd[1])
                str='-'
                avaliable = str.join(avaliable)
                list2Avaliable.append(avaliable)
        if i == 0:
            timeSlotList = list2[0].split('-')
            timeSlotList2 = list2[1].split('-')
            if (MTC(timeSlotList2[0])-MTC(timeSlotList[0]) >= meetingLength):
                avaliable = []
                avaliable.append(timeSlotList[0])
                avaliable.append(timeSlotList2[0])
                str = '-'
                avaliable = str.join(avaliable)
                list2Avaliable.append(avaliable)
        elif i != 0 and i != len(list2)-1:
            timeSlotList = list2[i].split('-')
            timeSlotList2 = list2[i + 1].split('-')
            if (MTC(timeSlotList2[0]) - MTC(timeSlotList[1])) >= meetingLength:
                avaliable = []
                avaliable.append(timeSlotList[1])
                avaliable.append(timeSlotList2[0])
                str = '-'
                avaliable = str.join(avaliable)
                list2Avaliable.append(avaliable)
    for timeSlot in list1Avaliable:
        timeSlot = timeSlot.split("-")
        startTime= MTC(timeSlot[0])
        endTime= MTC(timeSlot[1])
        timeSlot[0] = startTime
        timeSlot[1] = endTime
        totalAvaliable.append(timeSlot)
    for timeSlot in list2Avaliable:
        timeSlot = timeSlot.split("-")
        startTime = MTC(timeSlot[0])
        endTime = MTC(timeSlot[1])
        timeSlot[0] = startTime
        timeSlot[1] = endTime
        totalAvaliable.append(timeSlot)
    totalAvaliable = sorted(totalAvaliable)
    for i in range(0, len(totalAvaliable)):
        if i == len(totalAvaliable)-1:
            timeSlot = totalAvaliable[i]
            earlySlot = totalAvaliable[i-1]
            if (earlySlot[1]-timeSlot[0]) >= meetingLength:
                temp = [timeSlot[0], earlySlot[1]]
                finalList.append(temp)
        else:
            timeSlot = totalAvaliable[i]
            lateSlot = totalAvaliable[i+1]
            if (timeSlot[1]-lateSlot[0]) >= meetingLength:
                temp = [lateSlot[0], timeSlot[1]]
                finalList.append(temp)
    list1Entry = list1[0]
    list1Entry = list1Entry.split("-")
    list2Entry = list2[0]
    list2Entry = list2Entry.split("-")
    bound1 = MTC(list1Entry[1])
    bound2 = MTC(list2Entry[1])
    for timeSlot in finalList:
        if timeSlot[1] > bound1:
            timeSlot[1] = bound1
        if timeSlot[1] > bound2:
            timeSlot[1] = bound2
    for timeSlot in finalList:
        startTime = toMTC(timeSlot[0])
        endTime = toMTC(timeSlot[1])
        temp = [startTime, endTime]
        str = "-"
        time = str.join(temp)
        result.append(time)
    for i in range(0, len(result)-1):
        if result[i] == result [i+1]:
            result.pop(i+1)
    if len(result) >= 1:
        print(result)
    else:
        print("There are no compatible times.")

calendarAlgorithm(["8:00-18:00", "9:00-10:00", "10:00-10:10", "11:00-13:00"], ["7:00-16:00", "9:00-10:00", "11:00-13:00", "14:00-14:30"], 30)