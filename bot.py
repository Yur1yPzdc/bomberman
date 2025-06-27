import funcs
import json
import discord


#region functions
def get_w():
    with open('nukes.json', 'r') as f:
        return json.load(f)

#endregion


#region variables
w = get_w()
token = ''
with open('tkn.txt') as f:
    token = f.readline()

#endregion


#region BOT
client = discord.Client()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(msg):
    if '!nuke' in msg:
        lv = msg[6]
        content = msg[7:]

        e = discord.Embed(
            title='The bomb has dropped!',
            color=discord.Colour.green()
        )

        match lv:
            case '1':
                respond = funcs.l1(w, content)
            case '2':
                respond = funcs.l2(w, content)
            case '3':
                respond = funcs.l3(w, content)
            case '4':
                respond = funcs.l4(w, content)
            case '5':
                respond = funcs.l5(w, content)
            case _:
                await msg.channel.send('Иди нахуй!')

        e.add_field(
            name='BOMB'
        )

#endregion


client.run()

