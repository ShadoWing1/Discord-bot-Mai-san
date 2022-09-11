# This example requires the 'message_content' intent.
from hesap import *
import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.default()
intents.message_content = True

Bot = commands.Bot("!m ", intents=intents)

class social:
    instagram = "https://instagram.com/"
    github = "https://github.com/"

all_social_media = {
"instagram" :"https://instagram.com/mai_san_bot/",
"github":"https://github.com/ShadoWing1"
}    

ROOM = 0

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="opening",url ="https://www.youtube.com/watch?v=K1PCl5D-IpU"))
    print(f'{Bot.user} Mai san güzellik uykusundan uyandı ')

@Bot.command
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amaount)

@Bot.event
async def on_commend_error(ctx, error):
    await ctx.send(error)


@tasks.loop(seconds=10)
async def social_media_push():
         await ROOM.send()

@Bot.command()
async def socialpush(ctx):   
    await ctx.channel.send(f"instagram: {all_social_media['instagram']}")
    await ctx.channel.send(f"github: {all_social_media['github']}")
    #social_media_push.start()
@Bot.command()
async def setSocial(ctx, s, absolute_path): 
     """s must be github or instagram"""
     all_social_media[s] = absolute_path
     print(all_social_media)

def getSocials()-> str:
    return 
    """
    {Social.INSTAGRAM}/{all_social_media.get("instagram")}
    {Social.GITHUB}/{all_social_media.get("github")}
    """

@Bot.command()
@commands.has_role("Admin")
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_role("Admin")
async def kick(ctx, member:discord.member, *args, reason="yok"):
    await member.kick(reason=reason)


@Bot.command()
@commands.has_role("Admin")
async def ban(ctx, member:discord.member, *args, reason="yok"):
    await member.ban(reason=reason)


@Bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for bans in banned_users:
        user = bans.user

        if(user.name, user. discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.sende(f"Unbanned user {user.mention}")
            return






#@Bot.event
#async def on_message(message):
#    if message.author == Bot.user:
#        return
#    if message.content.startswith('En iyi anime ne'):
#        await message.channel.send('danmachi')

@Bot.command()
async def ne_yapiyorsun(msg):
    await msg.send("anime izliyorum")

@Bot.command()
async def ne(msg, *args):
    if(args[0] == "izliyorsun"):
        await msg.send("bunny girl senpai")

@Bot.command()
async def MustafaŞatıroğlu(msg):
    await msg.send("Bana çok yardım etti")        

@Bot.command()
async def selam(msg):
    await msg.send("selam")        

@Bot.command()
async def günaydin(msg):
    await msg.send("sanada günaydın")



@Bot.command()
async def nasilsin(msg):
    await msg.send("iyiyim sen")

@Bot.command()
async def instagram(msg):
    await msg.send(f"{hesap.instagram} 'yi takip edebilirsin")


@Bot.command()
async def ahbe(msg):
    await msg.send("noldu")

  
@Bot.command()
async def iyi(msg, *args):
    if(args[0] == "geceler"):
        await msg.send("sanada iyi geceler")  

@Bot.command()
async def bb(msg):
    await msg.send("bb")
   


@Bot.command()
async def sa(msg, *args):
    print(args)
    if(len(args) > 0):
        if (args[0] == "mai"):
            await msg.send("as")
        else:
            await msg.send(f"{args[0]} o kim")


Bot.run(botid)
