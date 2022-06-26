import os
import discord

from dotenv import load_dotenv
# from opensky_api import OpenSkyApi
from discord.ext import tasks

from memy import Memy

# load_dotenv()
# TOKEN = os.getenv('DC_TOKEN')

# TOKEN = ""
client = discord.Client(intents= discord.Intents.all())

@client.event
async def on_ready():
    print("Bot jest gotowy!")

#
#   BOT TO POBIERANIA I WYSYLANIA FILMIKOW W FORMACIE MP4 NA DISCORDZIE
#

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #check if message is "/mem"
    if message.content.startswith('/mem'):
        print("Uzycie komendy '/mem' wykryte")
        # get the message after the command
        message_after_command = message.content.split(' ')[1:]
        # wypisywanie wiadomosci po '/mem'
        await Memy(message_after_command)
        if (os.path.getsize("./mem.mp4") < 8000000):
            await message.channel.send(file=discord.File("./mem.mp4"))
            os.remove("./mem.mp4")
        else:
            await message.channel.send("mem za cienszki, musisz wejsc w link ＞﹏＜")
            os.remove("./mem.mp4")

client.run(TOKEN)

# 
#   BOT DO CIAGLEGO WYKRYWANIA SAMOLOTOW NAD WYBRANYM TERENEM
#

# global poprzednieSamoloty
# global poprzednieSamolotyKraj

# poprzednieSamoloty = []
# poprzednieSamolotyKraj = []

# @client.event
# async def on_ready():
#     mojaPetla.start()
#     WyczyscStatyczne.start()
#     print('Slava Ukraini!!')

# @tasks.loop(minutes=1)
# async def WyczyscStatyczne():
#     global poprzednieSamoloty
#     global poprzednieSamolotyKraj

#     poprzednieSamoloty.clear()
#     poprzednieSamolotyKraj.clear()
#     print("Statyczne zmienne wyczyszczone")

# @tasks.loop(seconds=10)
# async def mojaPetla():
#     global poprzednieSamoloty
#     global poprzednieSamolotyKraj

#     print(poprzednieSamoloty, poprzednieSamolotyKraj)

#     api_c = OpenSkyApi()
#     states = api_c.get_states(bbox=(49.596470, 49.875168, 20.405045, 20.849991))
#     sCallSigns = []
#     sOrigins = []
#     ostatecznaOdp = []
#     odpowiedz = ""

#     for s in states.states:

#         # jesli w wyszukanych samolotach pojawi sie jakis z USA, to doda jego nazwe i kraj do tablic i zwiekszy counter o 1
#         if (str(s.origin_country) == "United States"):

#             if (not poprzednieSamoloty or not poprzednieSamolotyKraj):
#                 sCallSigns.append(str(s.callsign))
#                 sOrigins.append(str(s.origin_country))

#             if (poprzednieSamoloty and poprzednieSamolotyKraj):
#                 if str(s.callsign) in poprzednieSamoloty:
#                     continue
#                 if str(s.callsign) not in poprzednieSamoloty:
#                     sCallSigns.append(str(s.callsign))
#                 if str(s.origin_country) in poprzednieSamolotyKraj:
#                     continue
#                 if str(s.origin_country) not in poprzednieSamolotyKraj:
#                     sOrigins.append(str(s.origin_country))
            


#     for x in range(0, len(sCallSigns)):
#         ostatecznaOdp.append('Prawdopodobny samolot NATO wykryty\n' + 'Samolot: ' + str(sCallSigns[x] + ' ' + 'z kraju: ' + str(sOrigins[x]) + '\n'))

#     odpowiedz = '\n'.join(ostatecznaOdp)

#     # bot nie wysyla wiadomosci gdy nie ma nic wykrytego
#     if odpowiedz:
#         await client.get_channel(949322365005860864).send(odpowiedz)
#     if sCallSigns and sOrigins:
#         poprzednieSamoloty = sCallSigns
#         poprzednieSamolotyKraj = sOrigins

# @client.event
# async def on_message(message):
#     if 'testowa dwadawd' in message.content:
#         await message.channel.send("wtf")
#     if message.author == client.user:
#         return
#     if message.content == '!loty':
#         api_c = OpenSkyApi()
#         states = api_c.get_states(bbox=(49.596470, 49.875168, 20.405045, 20.849991))
#         counter = 0
#         sCallSigns = []
#         sOrigins = []
#         ostatecznaOdp = []

#         for s in states.states:
#             sCallSigns.append(s.callsign)
#             sOrigins.append(s.origin_country)
#             counter += 1

#         if counter == 0:
#             resposne = 'Brak samolotów nad obszarem'
#             await message.channel.send(resposne)
#         else:
#             stringTemp = ""
#             for x in range(0, (len(sCallSigns))):
#                 ostatecznaOdp.append('Samolot: ' + str(sCallSigns[x] + ' ' + 'z kraju: ' + str(sOrigins[x]) + '\n'))
#             stringTemp = '\n'.join(ostatecznaOdp)
#             print(stringTemp)
#             response = stringTemp
#             await message.channel.send(response)

# client.run(TOKEN)