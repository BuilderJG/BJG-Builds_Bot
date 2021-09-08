import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents,
                   command_prefix=".")

p = bot.command_prefix


@bot.event
async def on_ready():
    print("Ready to rumble!")
    print("Bot by BuilderJG\n")
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
    print("Prefix: ", p)


# ## AUTOMOD ###

# antinvite & antilink


@bot.event
async def on_message(message):
    author = message.author
    if 'discord.gg/' in message.content or "discord.com/invite/" in message.content or "discordapp.com/invite/" in message.content and not author.guild_permissions.embed_links and not author.guild_permissions.administrator:
        await message.delete()
        embed = discord.Embed(title=str(author) + ", Invites sind hier nicht erlaubt!", description="",
                              color=0xff0000)
        await message.channel.send(embed=embed)
        em = discord.Embed(
            title="Invite gepostet von " + str(message.author) + " in " + str(message.channel),
            description=str(message.content), color=discord.colour.Color.gold())
        em.set_thumbnail(url=message.author.avatar_url)
        with open("data.json") as f:
            data = json.load(f)
        for modlog in data["modlogs"]:
            try:
                channel = discord.utils.get(message.guild.channels, id=modlog)
                await channel.send(embed=em)
            except Exception:
                pass
        await bot.process_commands(message)


    if 'https://' in message.content or 'http://' in message.content and not author.guild_permissions.embed_links and not "https://tenor.com/view/" in message.content and not "https://cdn.discordapp.com/attachments/" in message.content and not author.guild_permissions.administrator:
        await message.delete()
        embed = discord.Embed(title=str(author) + ", Links sind hier nicht erlaubt!", description="",
                              color=0xff0000)
        await message.channel.send(embed=embed)
        em = discord.Embed(
            title="Link gepostet von " + str(message.author) + " in " + str(message.channel),
            description=str(message.content), color=discord.colour.Color.gold())
        em.set_thumbnail(url=message.author.avatar_url)
        with open("data.json") as f:
            data = json.load(f)
        for modlog in data["modlogs"]:
            try:
                channel = discord.utils.get(message.guild.channels, id=modlog)
                await channel.send(embed=em)
            except Exception:
                pass
        await bot.process_commands(message)

    if bot.user.mentioned_in(message) and not message.content.startswith(p):
        em = discord.Embed(title=f"{bot.user.name} allgemeine Hilfe-Seite", description="", color=0x00a8ff)
        em.add_field(name=f"`{p}help mod`", value="Dieser Command zeigt alle Moderations-Commands an.")
        em.add_field(name=f"`{p}help info`", value="Dieser Command zeigt alle Info-Commands an.")
        em.add_field(name=f"`{p}help text`", value="Dieser Command zeigt dir alle Embed Befehle an.")
        em.add_field(name=f"`{p}help bot`", value="Dieser Command zeigt alle Commands zu diesem Bot an.")
        em.add_field(name=f"`{p}help fun`", value="Dieser Command zeigt dir alle Spaß Befehle an.")
        em.add_field(name=f"`{p}help money`", value="Dieser Command zeigt dir alle Money Commands an.")
        em.add_field(name=f"`{p}help verify`", value="Dieser Command zeigt dir alle Verify Commands an.")
        em.add_field(name=f"`{p}help logging`", value="Dieser Command zeigt dir alle Logging Commands an.")
        em.add_field(name=f"`{p}help feedback`",
                     value="Dieser Command zeigt dir alle Feedback und Bug-Report Commands an.")
        em.add_field(name=f"`{p}help automod`",
                     value="Dieser Command zeigt dir Hilfe zu unseren automatischen Moderations Funktionen an.")
        em.add_field(name=f"`Probleme?`",
                     value="Wenn du einen Fehler gefunden hast, oder Hilfe brauchst, joine gerne auf unseren Discord-Server: discord.gg/V3svjsdn47.")
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        await message.channels.send(embed=em)
        await bot.process_commands(message)


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hey, danke für's hinzufügen zu diesem Server! Mein Commandprefix ist `.` und meine Hilfeseite bekommt ihr, wenn ihr mich erwähnt, oder `.help` nutzt :D")
        break


@bot.event
async def on_member_join(member):
    with open("data.json") as f:
        data = json.load(f)
        joinlog = data["joinchannel"]
        for modlog in joinlog:
            try:
                channel = discord.utils.get(member.guild.channels, id=modlog)
                em = discord.Embed(title="Herzlich willkommen auf diesem Server " + str(member) + "! :D",
                                   description="", color=discord.colour.Color.blue())
                em.set_thumbnail(url=member.avatar_url)
                em.set_footer(text=bot.user.name + " by BuilderJG#4088")
                await channel.send(embed=em)
            except Exception:
                pass



@bot.event
async def on_member_remove(member):
    with open("data.json") as f:
        data = json.load(f)
        leavelog = data["leavechannel"]
        for modlog in leavelog:
            try:
                channel = discord.utils.get(member.guild.channels, id=modlog)
                em = discord.Embed(title="Schade, dass du diesen Server verlassen hast " + str(member) + ". :c", description="", color=discord.colour.Color.blue())
                em.set_thumbnail(url=member.avatar_url)
                em.set_footer(text=bot.user.name + " by BuilderJG#4088")
                await channel.send(embed=em)
            except Exception:
                pass


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, und {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' und '.join(missing)
        _message = 'Ich benötige die **{}** Berechtigung(en) um diese Command ausführen zu können.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send('Dieser Command wurde deaktiviert.')
        return
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Befehl ist unter Cooldown, versuch es noch mal nach {round(error.retry_after)} Sekunden!")
        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, und {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' und '.join(missing)
            _message = 'Du benötigst die **{}** Berechtigung(en) um diesen Command ausführen zu können.'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("Ungültige Eingabe.")
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send('Dieser Command kann nicht in Direkt nachrichten genutzt werden.')
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("Du bist nicht berechtigt diesen Command auszuführen.")
            return

with open("data.json") as f:
    data = json.load(f)
    bot.run(data["token"])
