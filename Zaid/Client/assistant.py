from Zaid.main import *


from config import SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
random_assistant = ["1", "2", "3", "4", "5"]



async def get_assistant_details(assistant: int):
    if SESSION_NAME != "None":
       getme1 = await Test.get_me()
       ASSID1 = getme1.id
       ASSIDS.append(ASSID1)
       ASSNAME1 = (
           f"{getme1.first_name} {getme1.last_name}"
           if getme1.last_name
           else getme1.first_name
       )
       ASSUSERNAME1 = getme1.username
       ASSMENTION1 = getme1.mention
    if SESSION2 != "None":
       getme2 = await user.get_me()
       ASSID2 = getme2.id
       ASSIDS.append(ASSID2)
       ASSNAME2 = (
           f"{getme2.first_name} {getme2.last_name}"
           if getme2.last_name
           else getme2.first_name
       )
       ASSUSERNAME2 = getme2.username
       ASSMENTION2 = getme2.mention
    if SESSION3 != "None":
       getme3 = await user3.get_me()
       ASSID3 = getme3.id
       ASSIDS.append(ASSID3)
       ASSNAME3 = (
           f"{getme3.first_name} {getme3.last_name}"
           if getme3.last_name
           else getme3.first_name
       )
       ASSUSERNAME3 = getme3.username
       ASSMENTION3 = getme3.mention
    if SESSION4 != "None":
       getme4 = await user4.get_me()
       ASSID4 = getme4.id
       ASSIDS.append(ASSID4)
       ASSNAME4 = (
           f"{getme4.first_name} {getme4.last_name}"
           if getme4.last_name
           else getme4.first_name
       )
       ASSUSERNAME4 = getme4.username
       ASSMENTION4 = getme4.mention
    if SESSION5 != "None":
       getme5 = await user5.get_me()
       ASSID5 = getme5.id
       ASSIDS.append(ASSID5)
       ASSNAME5 = (
           f"{getme5.first_name} {getme5.last_name}"
           if getme5.last_name
           else getme5.first_name
       )
       ASSUSERNAME5 = getme5.username
       ASSMENTION5 = getme5.mention
    if int(assistant) == 1:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = Test
    elif int(assistant) == 6:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = Test
    elif int(assistant) == 2:
        x = ASSID2
        y = ASSNAME2
        z = ASSUSERNAME2
        a = user
    elif int(assistant) == 3:
        x = ASSID3
        y = ASSNAME3
        z = ASSUSERNAME3
        a = user3
    elif int(assistant) == 4:
        x = ASSID4
        y = ASSNAME4
        z = ASSUSERNAME4
        a = user4
    elif int(assistant) == 5:
        x = ASSID5
        y = ASSNAME5
        z = ASSUSERNAME5
        a = user5
    return x, y, z, a
