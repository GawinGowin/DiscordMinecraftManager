import datetime
import json
import os

import discord
from discord.ext import commands

file = os.path.join(".devcontainer", "config.json")
with open(file) as f:
    config = json.load(f)["discord"]

TOKEN = config["bot_token"]

class MinecraftBot(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix, intents=intents)
        try:
            self.load_extension("utils.discord_server")
        except discord.ExtensionNotFound as e:
            now = datetime.datetime.now()
            print(F"{now}: {e}")

    async def on_ready(self):
        now = datetime.datetime.now()
        print(F"{now}: Logged in as {self.user} (ID: {self.user.id})")
        await self.change_presence(activity=None)

bot = MinecraftBot(command_prefix='!')
bot.run(TOKEN)