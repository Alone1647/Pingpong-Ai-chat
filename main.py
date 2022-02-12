import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix="!") 

@client.event
async def on_ready():
    print('We have logged in as {}'.format(client.user))
    print('Bot name: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=disnake.Game(name="!help"))
    
url = "Pingpngurl"
pingpongauth = "Pingpingauth"

@client.command(name="디스크야")
async def _pingpong(ctx,*,message=None):
    if message == None:
      await ctx.reply("안녕하세요! 디스크에요! `?도움`으로 명령어를 확인하세요!")
      return
    
    header = {
      'Authorization': pingpongauth,
      'Content-Type': 'application/json'
    }
    param = {
      'request': {
        'query': message
      }
    }
    async with aiohttp.ClientSession(headers=header) as session:
      async with session.post(pingpongurl+f'/{ctx.message.author.id}', json=param) as res:
        data = await res.json()
        assert 'response' in data
        assert 'replies' in data['response']
        for send in data['response']['replies']:
          await ctx.send(f"{ctx.author.mention}님, " + send['text'])
 
client.run("Bot_token")
