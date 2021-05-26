import os
import re
import urllib.request

import discord
import youtube_dl
from discord.ext import commands


def scrap_video(query):
    base_url = "https://www.youtube.com/results?search_query="
    query.replace(" ", "+")
    html = urllib.request.urlopen(base_url + query)
    x = re.search(r'watch\?v=(\S{11})', html.read().decode())
    if x != None:
        html = urllib.request.urlopen(base_url + query)
        vid_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
        return f'https://www.youtube.com/watch?v=' + vid_ids[0]
    return False


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Started Music cog.")

    @commands.command()
    async def play(self, ctx, *, arg):
        if_song_exists = os.path.isfile("song.mp3")
        try:
            if if_song_exists:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command.")
            return

        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='test')
        await voice_channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }

        if arg.startswith("https://"):
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([arg])
        else:
            url = scrap_video(arg)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("Mayaa is not connected to a voice channel.")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Mayaa is not playing audio.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Mayaa is playing audio.")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()


def setup(bot):
    bot.add_cog(Music(bot))
