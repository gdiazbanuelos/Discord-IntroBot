#!/usr/bin/env python
import discord,random,json
from asyncio import sleep

# Bot ID = #
intents = discord.Intents.all()
client = discord.Client(intents=intents)


def get_users_json():
    users_json = open('users.json')
    users = json.load(users_json)
    users_json.close()
    return users


def get_sound_bank(id, users):
    for key in users:
        if id in users[key]['id']:
            return users[key]['sounds']
    return None


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
        if message.content == ('?bot greet'):
            await message.reply('Hello!', mention_author=True)


@client.event
async def on_voice_state_update(member, before, after):
    # Wait a moment after a user joins
    await sleep(1)
    # Exclude the bot joining itself
    if not before.channel and after.channel and member.id != "BOT_ID_HERE":
        users = get_users_json()
        bank = get_sound_bank(member.id, users)
        if(bank != None):
            channel = client.get_channel(after.channel.id)
            vc = await channel.connect()
            rand = random.randint(0,len(bank)-1)
            sound = bank[rand]
            vc.play(discord.FFmpegPCMAudio(source="./audio/"+sound))
            while vc.is_playing():
                await sleep(1)
            await vc.disconnect()
        else:
            print('User: {} with ID: {} not found in users.json file!'.format(str(member), str(member.id)))


client.run('DISCORD_KEY_HERE')
