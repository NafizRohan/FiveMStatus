"""
Author: Nafiz Rohan
LICENSE: MIT
Copyright: (c) 2023-present Nafiz
Version: v1.0
Item: Discord Bot Script
Files: client.py, config.py, client.log & README.md
"""
import config
import discord
from discord.ext import tasks
from discord import app_commands as ac
from discord import Color as c
from discord.interactions import Interaction
from discord import Button
from fivem import FiveM
import fivem.player as p
from prettytable import PrettyTable
import psutil
import re
import time

#Client Setup
intents = discord.Intents.all()
client = discord.Client(intents = intents)
ghost = ac.CommandTree(client = client)

#timestap
time_ = time.localtime()
timestamp = f"[{time_.tm_hour}:{time_.tm_min}:{time_.tm_sec}]  "

#definations
def log_write(log: str):
    try:
        with open(config.LOG_PATH, "a+t") as lw:
            lw.write(f"{timestamp}{log}\n")
    except Exception as e:
        raise print(f"{timestamp}{e}")

#Loops
@tasks.loop(seconds= 120)
async def status():
    try:
        try:
            channel_id = config.CHANNEL
            channel = await client.fetch_channel(channel_id)
            await channel.purge(limit= 5)
            fivem = FiveM(ip = config.IP, port = config.PORT)
        except Exception as e:
            channel = await client.fetch_channel(channel_id)
            error = discord.Embed(title= "SVR Name")
            error.add_field(name= "IP Address", value= config.CFX_RE, inline= False)
            error.add_field(name= status,value= "```❌Oflline!```")
            error.add_field(name= "Players", value= "0/64")
            error.add_field(name="Infromation", value= "```diff\n- Cannot Connect With FiveM......:)")
            await channel.send(embed= error)
            log_write(e)
            return
        else:
            list = PrettyTable(['USERNAME   ','  PING'])
            list.align['USERNAME   '] = "l"#[left align]
            list.align['  PING'] = "r"#[right align]
            list1 = PrettyTable(['USERNAME   ','  PING'])
            list1.align['USERNAME   '] = "l"#[left align]
            list1.align['  PING'] = "r"#[right align]
            list2 = PrettyTable(['USERNAME   ','  PING'])
            list2.align['USERNAME   '] = "l"#[left align]
            list2.align['  PING'] = "r"#[right align]
            list3 = PrettyTable(['USERNAME   ','  PING'])
            list3.align['USERNAME   '] = "l"#[left align]
            list3.align['  PING'] = "r"#[right align]
            list4 = PrettyTable(['USERNAME   ','  PING'])
            list4.align['USERNAME   '] = "l"#[left align]
            list4.align['  PING'] = "r"#[right align]
            
            #Server Details
            info = await fivem.get_dynamic_raw()
            host = info.get("hostname")
            online = info.get("clients")
            max_players = info.get("sv_maxclients")
            type_ = info.get("gametype")
            host = re.sub(r"\^\d", "", host)


            #Player Detalis
            data = await fivem.get_players_raw()
            players = [i.name for i in p.parse_players_json(data)]
            ping = [i.ping for i in p.parse_players_json(data)]

            status = discord.Embed(color= c.green())
            status.set_author(name= host, icon_url= config.LOGO)
            status.add_field(name= "IP ADDRESS",value= f"```\n{config.CFX_RE}\n```",inline= False)
            status.add_field(name= "Status", value="```\n✅Online!\n```")
            status.add_field(name= "Players", value=f"```\n{online}/{max_players}\n```")
            status.set_footer(text = f"Status Will Refresh In Every 2 Minutes.\n Last Refreshed At {time_.tm_hour}:{time_.tm_min}:{time_.tm_sec}")
            status.set_thumbnail(url= config.LOGO)
            if online == 0:
                status.add_field(name="City Status", value= "```diff\n- No Players Are Playing:(```", inline= False)
                await channel.send(embed = status)
            if online == 100:
                status.add_field(name= "City Status", value= "```fix\nWe Reached 100 Players In Our Server, Thats Great!```", inline= False)
                await channel.send(embed = status)
            if online > 100:
                status.add_field(name="City Status", value="```fix\nHurrah! We Reached More Then 100 Players.```", inline= False)
                await channel.send(embed = status)
            if online > 0 and online < 100:
                if online < 20:
                    for i in range(online):
                        list.add_row([players[i], ping[i]])
                    value = f"```\n{list}\n```"
                    status.add_field(name= "👥 Current Players", value= value, inline= False)  
                          
                if online > 20 and online < 40:
                    for i in range(0,20):
                        list.add_row([players[i], ping[i]])
                    value0 = f"```\n{list}\n```"
                    status.add_field(name = "👥 Current Players", value= value0, inline= False)
                    for i in range(20, online):
                        list1.add_row([players[i], ping[i]])
                    value1 = f"```\n{list1}\n```"
                    status.add_field(name = "", value= value1, inline= False)    

                if online > 40 and online < 60:
                    for i in range(0,20):
                        list.add_row([players[i], ping[i]])
                    value00 = f"```\n{list}\n```"
                    status.add_field(name = "👥 Current Players", value= value00, inline= False)
                    for i in range(20,40):
                        list1.add_row([players[i], ping[i]])
                    value11 = f"```\n{list1}\n```"
                    status.add_field(name = "", value= value11, inline= False)
                    for i in range(40, online):
                        list2.add_row([players[i], ping[i]])
                    value22 = f"```\n{list2}\n```"
                    status.add_field(name = "", value= value22, inline= False)

                if online > 60 and online < 80:
                    for i in range(online):
                        list.add_row([players[i], ping[i]])
                    value000 = f"```\n{list}\n```"
                    status.add_field(name = "👥 Current Players", value= value000, inline= False)
                    for i in range(20, 40):
                        list1.add_row([players[i], ping[i]])
                    value111 = f"```\n{list1}\n```"
                    status.add_field(name = "", value= value111, inline= False)
                    for i in range(40, 60):
                        list2.add_row([players[i], ping[i]])
                    value222 = f"```\n{list2}\n```"
                    status.add_field(name = "", value= value222, inline= False)
                    for i in range(60, online):
                        list3.add_row([players[i], ping[i]])
                    value333 = f"```\n{list3}\n```"
                    status.add_field(name = "", value= value333, inline= False)
                
                if online > 80 and online < 100:

                    for i in range(0,20):
                        list.add_row([players[i], ping[i]])
                    value0000 = f"```\n{list}\n```"
                    status.add_field(name = "👥 Current Players", value= value0000, inline= False)
                    for i in range(20, 40):
                        list1.add_row([players[i], ping[i]])
                    value1111 = f"```\n{list1}\n```"
                    status.add_field(name = "", value= value1111, inline= False)
                    for i in range(40, 60):
                        list2.add_row([players[i], ping[i]])
                    value2222 = f"```\n{list2}\n```"
                    status.add_field(name = "", value= value2222, inline= False)
                    for i in range(60, 80):
                        list3.add_row([players[i], ping[i]])
                    value3333 = f"```\n{list3}\n```"
                    status.add_field(name = "", value= value3333, inline= False)
                    for i in range(80, online):
                        list4.add_row([players[i], ping[i]])
                    value4444 = f"```\n{list4}\n```"
                    status.add_field(name = "", value= value4444, inline= False)
                await channel.send(embed= status )
            return
    except Exception as e:
        print(e)
        log_write(e)
        return

#events
@client.event
async def on_ready():
    print(f"{timestamp}In Search Of Diamond We Got {client.user.name}.")
    status.start()
    try:
        synced = await ghost.sync()
        print(f"{timestamp}{client.user.name} has synced {len(synced)} command(s)")
    except Exception as e:
        print(f"{timestamp}I Cannot sync any command(s) because of {e}")
        log_write(e)
    log_write(f"{client.user.name} is activated. {client.user.name} has synced {len(synced)} command(s)")
    return

#Commands
@ghost.command(name = "client", description="Bot Information")
async def Client(intraction:Interaction):
    try:
        BOT = discord.Embed(title=f"{client.user.name} Information",color= c.green(),)
        BOT.set_author(name= f"{client.user.name}", icon_url=f"{client.user.avatar}")
        BOT.add_field(name="Creator & Developer", value="> [Nafiz Rohan](https://github.com/RohanZhid)",inline= True)
        BOT.add_field(name= "Bot Prefix", value="> `/`**Slash**", inline= True)
        BOT.set_thumbnail(url=f"{client.user.avatar}")
        BOT.add_field(name= "UI Language", value="> English", inline= True)
        BOT.add_field(name="Ping", value=f"> {round(client.latency * 1000)}ms", inline= True)
        BOT.add_field(name="CPU Usage", value=f"> {psutil.cpu_percent()}%", inline= True)
        ram_usage = psutil.virtual_memory().used / (1024 * 1024)
        BOT.add_field(name="Ram Usage", value=f"> {ram_usage: .2f} MB")
        BOT.add_field(name="Version", value=f"> v1.0", inline= True)
        cmd = ghost.get_commands()
        BOT.add_field(name="Total Commands", value=f"> {len(cmd)} Command(s)", inline= True)  
        BOT.add_field(name="Watching Servers", value=f"> {str(len(client.guilds))} Servers", inline= True)
        BOT.add_field(name= "Description:", value="The Script of this bot is fully written on `Python` with Discord.py[`2.1.0`] and written by [Nafiz Rohan](https://github.com/RohanZhid)", inline= False)
        BOT.set_footer(text= "If you want to buy this kind of bot feel free to contact with me. My discord id Nafiz Rohan#2097")
        await intraction.response.send_message(embed = BOT)
    except Exception as e:
        print(e)
        log_write(e)
    return#end

@ghost.command(name= "server", description= "Show Server related info(FiveM).")
async def server(interaction: Interaction):
    try:
        fivem = FiveM(ip = config.IP, port = config.PORT)
        info = await fivem.get_dynamic_raw()
        online = info.get("clients")
        max_players = info.get("sv_maxclients")
        type_ = info.get("gametype")
        server = discord.Embed(title= "SVR Name")
        server.add_field(name= "Owner & Developer", value= "> Nafiz Rohan")
        server.add_field(name= "server", value= "> FiveM")
        server.add_field(name= "Type", value= f"> {type_}")
        server.add_field(name= "Players", value= f"> {online}/{max_players}")
        server.add_field(name= "IP Address", value= "> connect cfx.re/join/dp56ed")
        server.add_field(name= "Language", value= "> English/Bangla")
        server.set_thumbnail(url= config.LOGO)
        await interaction.response.send_message(embed= server)
    except Exception as e:
        log_write(e)
        print(e)
    return

#Client Activation
try:
    client.run(token= config.TOKEN, log_handler= None)
except Exception as e:
    print(e)
    log_write(e)