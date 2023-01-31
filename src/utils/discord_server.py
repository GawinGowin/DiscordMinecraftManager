import asyncio
import json
import os

import discord
from discord.ext import commands

from utils.aws_server import instances_switch

file = os.path.join(".devcontainer", "config.json")
with open(file) as f:
    config = json.load(f)["discord"]

CHANNEL_ID = int(config["channel_id"])

class SwitchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_in_channel(channel_id):
        async def predicate(ctx):
            return ctx.channel_id == channel_id
        return commands.check(predicate)

    @commands.slash_command(description="Server controle")
    @is_in_channel(CHANNEL_ID)
    async def server(self, ctx, action: str):
        await ctx.defer()
        action = action.upper()
        if action =="ON":
            await ctx.respond(F"Server {action} processing...")
            task = asyncio.create_task(instances_switch(action))
            message, public_ip = await task
            await ctx.respond(F"Server {message} !\nPlease Access: {public_ip}")
            await self.bot.change_presence(activity=discord.Activity(
                type = discord.ActivityType.playing, name="MinecraftServer"))

        elif action =="OFF":
            await ctx.respond(F"Server {action} processing...")
            task = asyncio.create_task(instances_switch(action))
            message = await task
            await ctx.respond(F"Server {message} !")
            await self.bot.change_presence(activity=None)

        else:
            await ctx.respond("format: `/server [ON|OFF]`")

    @server.error
    async def server_error(self, ctx, error):
        name = self.bot.get_channel(CHANNEL_ID)
        await ctx.respond(F"`{error}`\nPlease use commands at [{name}] CHANNEL")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello!')

def setup(bot):
    bot.add_cog(SwitchCog(bot))

# Refer
## https://qiita.com/Lazialize/items/81f1430d9cd57fbd82fb
## https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f
## https://github.com/Pycord-Development/pycord/blob/30e0de45c2685070bd66d495a7acbdc05f0f7804/examples/app_commands/slash_cog.py
## https://github.com/Pycord-Development/pycord/blob/315082ff9e7ae868965b2d3eb2f75ba3c9fba378/examples/views/counter.py