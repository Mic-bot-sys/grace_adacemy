from datetime import datetime


def DateTime():
    result = datetime.now().strftime(("%d-%m-%Y %H:%M:%S.%f"))
    return result


# dateCreated = datetime.now()
# d = datetime.strptime(dateCreated, "%Y-%m-%d %H:%M:%S")
# final = d.strftime("%d-%m-%Y %H:%M:%S")