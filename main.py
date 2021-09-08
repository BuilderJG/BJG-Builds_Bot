import asyncio
import json
import random

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")

p = bot.command_prefix


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(f'{p}help money | Money Update! | Bot by BuilderJG#4088'))
    print("Ready to rumble!")
    print("Bot by BuilderJG#4088\n")
    print("Bot running with:")
    print(f"Username: {bot.user.name}")
    print(f"User ID: {bot.user.id}")
    print(f"Command Prefix: {p}")
    print(f"Invite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8")


@bot.command(aliases=['commands'])
@commands.bot_has_permissions(send_messages=True)
async def help(ctx, message=None):
    if message is None:
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
        await ctx.send(embed=em)
    elif message == "mod":
        em = discord.Embed(title=f"{bot.user.name} Moderations Befehle Hilfe-Seite", description="", color=0x00a8ff)
        em.add_field(name=f"`{p}ban <member> <reason>`", value="Dieser Command bannt ein Mitglied.")
        em.add_field(name=f"`{p}unban <user>`",
                     value="Dieser Command entbannt ein ehemaliges Mitglied. !Achtung! Gib hier bitte Name#Tag an, da sonst der Command nicht funktioniert!")
        em.add_field(name=f"`{p}clear <amount>`", value="Dieser Command löscht die angegebene Menge an Nachrichten.")
        em.add_field(name=f"`{p}warn <member> <reason>`", value="Dieser Command verwarnt ein Mitglied.")
        em.add_field(name=f"`{p}addmodlog <channel>`", value="Dieser Command setzt einen Modlog.")
        em.add_field(name=f"`{p}delmodlog <channel>`", value="Dieser Command entfernt einen Modlog.")
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        await ctx.send(embed=em)
    elif message == "info":
        em = discord.Embed(title=f"{bot.user.name} Info Hilfe-Seite", description="", color=0x00a8ff)
        em.add_field(name=f"`{p}getpp <member>`", value="Dieser Command sendet das Profilbild eines Mitglieds.")
        em.add_field(name=f"`{p}geticon`", value="Dieser Command sendet das Icon des Servers.")
        em.add_field(name=f"`{p}botinfo`", value="Dieser Command zeigt Informationen zum Bot an.")
        em.add_field(name=f"`{p}serverinfo`", value="Dieser Command zeigt Informationen zum Server an.")
        em.add_field(name=f"`{p}roleinfo <role>`", value="Dieser Command zeigt Informationen zu einer Rolle an.")
        em.add_field(name=f"`{p}userinfo <member>`", value="Dieser Command zeigt Informationen zu einem Mitglied an.")
        em.add_field(name=f"`{p}credits`", value="Dieser Command zeigt die Credits zu diesem Bot an.")
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        await ctx.send(embed=em)
    elif message == "text":
        em = discord.Embed(title=f"{bot.user.name} Embed Hilfe-Seite", description="", color=0x00a8ff)
        em.add_field(name=f"`{p}embed <color> <title> <text>`",
                     value="Dieser Command erzeugt ein Embed, dessen Farbe man als erstes mit den Parametern `red`, `yellow`, `green`, `blue` & `black`bestimmen kann, der Titel wird als nächstes festgelegt und kann mehrere Worte umfassen, indem man diese in Anführungszeichen schreibt und der Rest wird unter der Überschrift als Text angezeigt.")
        em.add_field(name=f"`{p}echo <text>`",
                     value="Dieser Command wiederholt den angegebenen Text und löscht die Ursprungs Nachricht")
        await ctx.send(embed=em)
    elif message == "bot":
        em = discord.Embed(title=bot.user.name + " Bot spezifische Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}botnick`",
                     value="Dieser Command ändert den Nickname von diesem Bot.", inline=True)
        em.add_field(name=f"`{p}botinfo`",
                     value="Dieser Command zeigt Informationen zu diesem Bot an.", inline=True)
        em.add_field(name=f"`{p}credits`",
                     value="Dieser Command zeigt die Credits von diesem Bot an.", inline=True)
        em.add_field(name=f"`{p}invite`",
                     value="Dieser Command sendet einen Link zum Einladen von diesem Bot.", inline=True)
        em.add_field(name=f"`{p}ping`",
                     value="Dieser Command zeigt den Ping (in ms) von diesem Bot an.", inline=True)
        em.set_footer(text=bot.user.name + " by BuilderJG")
        await ctx.send(embed=em)
    elif message == "fun":
        em = discord.Embed(title=bot.user.name + " Spaß Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}ask <question>`",
                     value="Dieser Command gibt eine zufällige lustige Antwort aus (!NICHT ERNST NEHMEN!).")
        em.add_field(name=f"`{p}dice`", value="Dieser Command würfelt eine Zahl zwischen 1 & 6", inline=True)
        em.add_field(name=f"`{p}coinflip`",
                     value="Dieser Command wirft eine Münze, die entweder auf Kopf, oder auf Zahl landet.",
                     inline=True)
        em.add_field(name=f"`{p}poll <arg1> - <arg5>`",
                     value="Dieser Command startet eine Abstimmung mit mindestens 2 und maximal 5 Auswahlmöglichkeiten (Auswahl per Reaktionen).",
                     inline=True)
        em.set_footer(text=bot.user.name + " by BuilderJG")
        await ctx.send(embed=em)
    elif message == "money":
        em = discord.Embed(title=bot.user.name + " Money Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}balance <user>`",
                     value="Dieser Command zeigt dir den Kontostand der markierten Person an.", inline=True)
        em.add_field(name=f"`{p}work`",
                     value="Dieser Command zahlt dir ein zufälliges Gehalt zwischen 1€ & 100€ aus.",
                     inline=True)
        em.add_field(name=f"`{p}daily`", value="Dieser Command zahlt dir täglich 100€ aus.")
        em.add_field(name=f"`{p}pay <user> <amount>`",
                     value="Dieser Command zahlt der markierten Person die angegebene Menge an Geld.")
        em.add_field(name=f"`{p}beg`", value="Dieser Command gibt dir zwischen 0€ und 5€.")
        em.set_footer(text=bot.user.name + " by BuilderJG")
        await ctx.send(embed=em)
    elif message == "verify":
        em = discord.Embed(title=bot.user.name + " Verify Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}verify`",
                     value="Dieser Command verifiziert dich auf einem Server wo Verify aktiviert ist (Standard: deaktiviert).",
                     inline=True)
        em.add_field(name=f"`{p}enableverify`",
                     value="Dieser Command aktiviert den Befehl .verify auf dem derzeitigen Server.",
                     inline=True)
        em.add_field(name=f"`{p}disableverify`",
                     value="Dieser Command deaktiviert den Befehl .verify auf dem derzeitigen Server.",
                     inline=True)
        em.add_field(name=f"`{p}setverifyrole`",
                     value="Dieser Command setzt die Rolle, die man mit dem Befehl .verify erhält.")
        em.set_footer(text=bot.user.name + " by BuilderJG")
        await ctx.send(embed=em)
    elif message == "logging":
        em = discord.Embed(title=bot.user.name + " Logging Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}addjoinlog <channel>`",
                     value="Dieser Command setzt einen Kanal in den eine Begrüßungsnachricht gesendet wird, wenn jemand den Server betritt.")
        em.add_field(name=f"`{p}deljoinlog <channel>`",
                     value="Dieser Command deaktiviert, dass Begrüßungsnachrichten in den Kanal gesendet werden.")
        em.add_field(name=f"`{p}adddeavelog <channel>`",
                     value="Dieser Command setzt einen Kanal in den eine Abschiedsnachricht gesendet wird, wenn jemand den Server verlässt.")
        em.add_field(name=f"`{p}deljoinlog <channel>`",
                     value="Dieser Command deaktiviert, dass Abschiedsnachrichten in den Kanal gesendet werden.")
        await ctx.send(embed=em)
    elif message == "feedback":
        em = discord.Embed(title=bot.user.name + " Feedback und Bug Report Commands Übersichts Seite", description="",
                           color=0x00a8ff)
        em.add_field(name=f"`{p}feedback <message>`",
                     value="Dieser Command sendet dein Feedback an den Botowner (Achtung: Ausnutzung kann zum Ausschluss von dieser Funktion führen).")
        em.add_field(name=f"`{p}report`",
                     value="Dieser Command sagt dir, wie du einen Bug melden kannt.")
        await ctx.send(embed=em)
    elif message == "automod":
        em = discord.Embed(title=bot.user.name + " Automoderator Funktionen Übersicht", description="",
                           color=discord.Color.blue())
        em.add_field(name="`AntiInvite`",
                     value="Es werden automatisch alle Nachrichten, die einen Discord Invitelink beinhalten gelöscht, sofern der Nutzer nicht die Berechtigung Links einbetten hat")
        em.add_field(name="`AntiLink`",
                     value="Es werden automatisch alle Nachrichten die ein https:// oder ein http:// enthalten gelöscht, sofern der Nutzer nicht die Berechtigung Links einbetten hat. (überspringt GIFs)")
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        await ctx.send(embed=em)
    else:
        await help(ctx, None)


# MOD


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    await member.ban(reason=reason)
    em = discord.Embed(title=f"Mitglied gebannt von {ctx.message.author}", description=str(reason),
                       color=discord.Color.red())
    em.set_thumbnail(url=member.avatar_url)
    em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
    await ctx.send(embed=em)
    with open("data.json") as f:
        data = json.load(f)
        em = discord.Embed(title=f"Mitglied gebannt von {ctx.message.author}",
                           description=f"Grund: {reason}\nMitglied: {member.mention} ({member})",
                           color=discord.colour.Color.red())
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        for modlog in data["modlogs"]:
            try:
                channel = discord.utils.get(ctx.guild.channels, id=modlog)
                await channel.send(embed=em)
            except Exception:
                pass
        try:
            em = discord.Embed(
                title=f"Du wurdest von {ctx.message.author} von dem Server {ctx.guild.name} für den Grund `{reason}` gebannt.",
                description="", color=discord.colour.Color.red())
            em.set_thumbnail(url=ctx.message.author.avatar_url)
            em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
            await member.send(embed=em)
        except Exception:
            pass


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(administrator=True)
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    mf = False
    for ban_entry in banned_users:
        f = ban_entry.user
        if (f.name, f.discriminator) == (member_name, member_discriminator):
            mf = True
            await ctx.guild.unban(f)
            await ctx.send(f"Der Nutzer {member} wurde vom Server entbannt.")
            with open("data.json") as f:
                data = json.load(f)
                em = discord.Embed(title=f"Mitglied entbannt von {ctx.message.author}",
                                   description=f"Mitglied: {member}",
                                   color=discord.colour.Color.red())
                em.set_thumbnail(url=member.avatar_url)
                em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
                for modlog in data["modlogs"]:
                    try:
                        channel = discord.utils.get(ctx.guild.channels, id=modlog)
                        await channel.send(embed=em)
                    except Exception:
                        pass
    if not mf:
        await ctx.send("Dieser Nutzer ist bereits entbannt.")


@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(administrator=True)
async def clear(ctx, amount=5):
    if amount == 0:
        await ctx.send("Legende! xD", delete_after=5.0)
        return
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.message.author} hat {amount} Nachricht(en) gelöscht.", delete_after=5.0)
    with open("data.json") as f:
        data = json.load(f)
        em = discord.Embed(title=f"{amount} Nachricht(en) gelöscht von {ctx.message.author}",
                           description=f"Kanal: {ctx.channel.mention}", color=discord.Color.red())
        em.set_thumbnail(url=ctx.message.author.avatar_url)
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        for modlog in data["modlogs"]:
            try:
                channel = discord.utils.get(ctx.guild.channels, id=modlog)
                await channel.send(embed=em)
            except Exception:
                pass


@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    if member.guild_permissions.administrator and ctx.message.author is not ctx.guild.owner:
        await ctx.send(f"{ctx.author} du kannst keinen Admin verwarnen!")
    with open("data.json") as f:
        data = json.load(f)
        em = discord.Embed(title=f"{member} wurde von {ctx.message.author} verwarnt",
                           description=f"Grund: {reason}", color=discord.Color.red())
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        for modlog in data["modlogs"]:
            try:
                channel = discord.utils.get(ctx.guild.channels, id=modlog)
                await channel.send(embed=em)
            except Exception:
                pass
        em = discord.Embed(title=f"{member} wurde von {ctx.message.author} verwarnt",
                           description=f"Grund: {reason}", color=discord.Color.red())
        em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
        await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def addmodlog(ctx, channel: discord.TextChannel):
    if not channel in ctx.guild.channels:
        ctx.send("Bitte gib einen Kanal auf diesem Server an.")
        return
    with open("data.json") as f:
        data = json.load(f)
        if channel.id in data["modlogs"]:
            await ctx.send("Der angegebene Kanal wurde bereits als Modlog registriert.")
        else:
            data["modlogs"].append(channel.id)
            await ctx.send(f"{ctx.author} du hast erfolgreich den Kanal `{channel.mention}` als Modlog registriert.")
            with open("data.json", 'w') as file:
                json.dump(data, file)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def delmodlog(ctx, channel: discord.TextChannel):
    if not channel in ctx.guild.channels:
        ctx.send("Bitte gib einen Kanal auf diesem Server an.")
        return
    with open("data.json") as f:
        data = json.load(f)
        modlogs = data["modlogs"]
        if channel in modlogs:
            index = modlogs.index(channel)
            del modlogs[index]
            data["modlogs"] = modlogs
            with open('data.json', 'w') as f:
                json.dump(data, f)
                await ctx.send(f"{ctx.message.author} der Kanal {channel.mention} ist nun kein Modlog mehr.")
        else:
            await ctx.send("Der angegebene Kanal ist bereits kein Modlog")


# INFO


@bot.command()
async def credits(ctx):
    em = discord.Embed(title=bot.user.name + " Credits",
                       description="Bot Code by BuilderJG#4088\nDiscord(Support-)Server: discord.gg/V3svjsdn47",
                       color=discord.colour.Color.blue())
    em.set_footer(text=bot.user.name + " by BuilderJG#4088")
    await ctx.send(embed=em)


@bot.command()
async def getpp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)


@bot.command()
async def geticon(ctx):
    try:
        await ctx.send(ctx.guild.icon_url)
    except Exception:
        await ctx.send("Leider ist ein Fehler aufgetreten")


@bot.command()
async def botinfo(ctx):
    em = discord.Embed(title=bot.user.name + "-Info:", description="", color=discord.Color.blue())
    em.add_field(name="Bot-Owner:", value="`BuilderJG#4088`\n", inline=True)
    em.add_field(name="Ping:", value="`" + str(round(bot.latency * 1000)) + "ms`", inline=True)
    em.add_field(name="Prefix:", value="`" + bot.command_prefix + "`", inline=True)
    em.add_field(name="Commands:", value="`" + str(len(bot.commands)) + "`")
    em.add_field(name="Server:", value="`" + str(len(bot.guilds)) + " Server`", inline=True)
    em.add_field(name="Nutzername:", value="`" + bot.user.name + "`", inline=True)
    em.add_field(name="NutzerID:", value="`" + str(bot.user.id) + "`", inline=True)
    em.set_footer(text=bot.user.name + " by BuilderJG#4088")
    await ctx.send(embed=em)


@bot.command()
async def serverinfo(ctx):
    em = discord.Embed(title=str(ctx.guild.name) + " Server Infos", description="", color=discord.Color.blue())
    em.set_thumbnail(url=str(ctx.guild.icon_url))
    em.add_field(name="`Owner`", value=str(ctx.guild.owner), inline=True)
    em.add_field(name="`Server ID`", value=str(ctx.guild.id), inline=True)
    em.add_field(name="`Region`", value=str(ctx.guild.region), inline=True)
    em.add_field(name="`Member Count`", value=str(ctx.guild.member_count), inline=True)
    em.set_footer(text=bot.user.name + " by BuilderJG#4088")
    await ctx.send(embed=em)


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    em = discord.Embed(color=member.color)
    em.set_thumbnail(url=member.avatar_url)
    em.add_field(name="Nutzer:", value=f"{member.mention}", inline=True)
    em.add_field(name="Name", value=f"{member}", inline=True)
    em.add_field(name="ID:", value=f"{member.id}", inline=True)
    em.add_field(name="Bot:", value=str(member.bot), inline=True)
    em.add_field(name="Account erstellt:", value=f"{member.created_at}", inline=True)
    em.add_field(name="Beigetreten:", value=f"{member.joined_at}", inline=True)
    em.add_field(name="Nickname:", value=f"{member.nick}", inline=True)
    roles = " ".join([role.mention for role in member.roles if role.name != "@everyone"])
    em.add_field(name="Rollen:", value=f"{roles}", inline=True)
    em.add_field(name="Höchste Rolle", value=f"{member.top_role}", inline=True)
    em.add_field(name="Administrator:", value=f"{member.guild_permissions.administrator}", inline=True)
    em.set_footer(text=bot.user.name + " by BuilderJG")
    await ctx.send(embed=em)


@bot.command()
async def roleinfo(ctx, role: discord.Role):
    em = discord.Embed(title=role.name + " Info", description=role.mention, color=discord.colour.Color.blue())
    em.add_field(name="`Farbe:`", value=str(role.color))
    em.add_field(name="`Erstellt um:`", value=str(role.created_at))
    em.add_field(name="`ID:`", value=str(role.id))
    em.add_field(name="`Anzahl Member:`", value=str(len(role.members)))
    em.add_field(name="`Berechtigungs Intent:`", value=str(role.permissions))
    em.add_field(name="`Position`", value=str(role.position))
    em.set_footer(text=bot.user.name + " by BuilderJG#4088")
    await ctx.send(embed=em)


# TEXT
@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def embed(ctx, color, title, *, text):
    await ctx.message.delete()
    if color == "red":
        embed = discord.Embed(title="{}".format(title), description="{}".format(text),
                              color=discord.colour.Colour.red())
        await ctx.send(embed=embed)
    elif color == "green":
        embed = discord.Embed(title="{}".format(title), description="{}".format(text),
                              color=discord.colour.Colour.green())
        await ctx.send(embed=embed)
    elif color == "blue":
        embed = discord.Embed(title="{}".format(title), description="{}".format(text),
                              color=discord.colour.Colour.blue())
        await ctx.send(embed=embed)
    elif color == "yellow":
        embed = discord.Embed(title="{}".format(title), description="{}".format(text),
                              color=discord.colour.Colour.gold())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="{}".format(title), description="{}".format(text))
        await ctx.send(embed=embed)
        if color != "black":
            await ctx.send("Mögliche Farben sind: `red`, `yellow`, `green`, `blue` & `black`.", delete_after=5.0)


@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def echo(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


# BOT

@bot.command()
async def invite(ctx):
    userid = bot.user.id
    em = discord.Embed(title='[KLICK]',
                       url="https://discord.com/oauth2/authorize?client_id=" + str(userid) + "&scope=bot&permissions=8",
                       description='Klicke auf den Titel um diesen Bot zu deinem Discord-Server hinzuzufügen (Du benötigst die Berechtigung *Manage Server*)',
                       color=discord.Color.blue())
    em.set_footer(text=bot.user.name + " by BuilderJG")
    await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(manage_nicknames=True)
@commands.bot_has_permissions(change_nickname=True)
async def botnick(ctx, *, name=None):
    if name is None:
        await ctx.send(str(ctx.message.author) + ", bitte gib einen neuen Nickname an!")
    else:
        getserror = False
        try:
            await ctx.message.guild.get_member(bot.user.id).edit(nick=name)
        except Exception:
            await ctx.send("Leider ist beim Nickname ändern ein Fehler aufgetreten")
            getserror = True

        if not getserror:
            await ctx.send("Mein Nickname wurde erfolgreich zu `" + str(name) + "` geändert.")


@bot.command()
async def ping(ctx):
    await ctx.send("Mein Ping ist: " + str(round(bot.latency * 1000)) + "ms")


# FUN

@bot.command()
async def ask(ctx):
    answer = random.choice(["Ja", "Nein", "Vieleicht", "Sei nicht so neugierig", "Auf jeden Fall!", "Auf keinen Fall!",
                            "stell nicht so komische Fragen!", "Weiß ich doch nicht!"])
    await ctx.send(answer)


@bot.command()
async def dice(ctx):
    count = random.randint(1, 6)
    await ctx.send(ctx.message.author.name + " du hast eine **" + str(count) + "** gewürfelt.")


@bot.command()
async def coinflip(ctx):
    count = random.randint(1, 2)
    if count == 1:
        await ctx.send(ctx.message.author.name + " du wirfst **Kopf**")
    if count == 2:
        await ctx.send(ctx.message.author.name + " du wirfst **Zahl**")


@bot.command()
@commands.has_permissions(administrator=True)
async def randommember(ctx):
    if ctx.message.author.guild_permissions.manage_guild:
        member = random.choice(ctx.guild.members)
        em = discord.Embed(title="Es wurde der Nutzer " + str(member) + " ausgewählt", description=member.mention,
                           color=discord.colour.Color.blue())
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        await ctx.send(embed=em)
    else:
        await ctx.send(ctx.author.name + " du hast keine Berechtigung dazu, dir fehlt: 'manage_messages'")


@bot.command()
@commands.cooldown(1, 15, type=BucketType.user)
async def poll(ctx, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, *, rest=None):
    # lemojis = "1⃣, 2⃣, 3⃣, 4⃣, 5⃣, 6⃣, 7⃣, 8⃣, 9⃣, 🔟"
    if not arg2:
        await ctx.message.delete()
        await ctx.send(ctx.message.author.name + " bitte gib mindedestens 2 Auswahlmöglichkeiten an!", delete_after=5.0)
    elif not arg3 and arg2:
        em = discord.Embed(title="Abstimmung von " + ctx.message.author.name, description="",
                           color=discord.colour.Color.blue())
        em.add_field(name="1⃣", value=arg1, inline=False)
        em.add_field(name="2⃣", value=arg2, inline=False)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        message = await ctx.send(embed=em)
        emojis = ["1⃣", "2⃣"]
        for emoji in emojis:
            await message.add_reaction(emoji)
    elif arg3 and not arg4:
        em = discord.Embed(title="Abstimmung von " + ctx.message.author.name, description="",
                           color=discord.colour.Color.blue())
        em.add_field(name="1⃣", value=arg1, inline=False)
        em.add_field(name="2⃣", value=arg2, inline=False)
        em.add_field(name="3⃣", value=arg3, inline=False)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        message = await ctx.send(embed=em)
        emojis = ["1⃣", "2⃣", "3⃣"]
        for emoji in emojis:
            await message.add_reaction(emoji)
    elif arg4 and not arg5:
        em = discord.Embed(title="Abstimmung von " + ctx.message.author.name, description="",
                           color=discord.colour.Color.blue())
        em.add_field(name="1⃣", value=arg1, inline=False)
        em.add_field(name="2⃣", value=arg2, inline=False)
        em.add_field(name="3⃣", value=arg3, inline=False)
        em.add_field(name="4⃣", value=arg4, inline=False)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        message = await ctx.send(embed=em)
        emojis = ["1⃣", "2⃣", "3⃣", "4⃣"]
        for emoji in emojis:
            await message.add_reaction(emoji)
    elif arg5 and not rest:
        em = discord.Embed(title="Abstimmung von " + ctx.message.author.name, description="",
                           color=discord.colour.Color.blue())
        em.add_field(name="1⃣", value=arg1, inline=False)
        em.add_field(name="2⃣", value=arg2, inline=False)
        em.add_field(name="3⃣", value=arg3, inline=False)
        em.add_field(name="4⃣", value=arg4, inline=False)
        em.add_field(name="5⃣", value=arg5, inline=False)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        message = await ctx.send(embed=em)
        emojis = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣"]
        for emoji in emojis:
            await message.add_reaction(emoji)
    elif rest:
        em = discord.Embed(title="Abstimmung von " + ctx.message.author.name, description="",
                           color=discord.colour.Color.blue())
        em.add_field(name="1⃣", value=arg1, inline=False)
        em.add_field(name="2⃣", value=arg2, inline=False)
        em.add_field(name="3⃣", value=arg3, inline=False)
        em.add_field(name="4⃣", value=arg4, inline=False)
        em.add_field(name="5⃣", value=arg5, inline=False)
        em.set_footer(text=bot.user.name + " by BuilderJG#4088")
        message = await ctx.send(embed=em)
        emojis = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣"]
        for emoji in emojis:
            await message.add_reaction(emoji)
        await ctx.send(
            ctx.message.author.name + ' derzeit ist es nur möglich bis zu 5 verschiedene Auswahlmöglichkeiten anzugeben. Eine Auswahlmöglichkeit kann aus mehreren Worten bestehen, indem du sie in Anführungszeichen (") setzt.',
            delete_after=10.0)


# VERIFY


@bot.command()
@commands.has_permissions(manage_channels=True)
async def enableverify(ctx):
    with open("data.json") as file:
        data = json.load(file)
        if ctx.message.guild.id in data["verifyserver"]:
            await ctx.send(ctx.message.author.name + " Verify ist bereits auf diesem Server aktiviert.")
        else:
            data["verifyserver"].append(ctx.message.guild.id)
            await ctx.send(ctx.message.author.name + " Verify wurde auf diesem Server aktiviert")
            with open("data.json", 'w') as f:
                json.dump(data, f)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def disableverify(ctx):
    with open("data.json") as f:
        data = json.load(f)
        if not ctx.message.guild.id in data["verifyserver"]:
            await ctx.send(ctx.message.author.name + " Verify ist bereits auf diesem Server deaktiviert.")
        else:
            verifyroles = data["verifyroles"]
            for role in ctx.message.guild.roles:
                try:
                    index = verifyroles.index(role)
                    del verifyroles[index]
                    data[verifyroles] = verifyroles
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                except Exception:
                    pass
            verifyserver = data["verifyserver"]
            index = verifyserver.index(ctx.message.guild.id)

            del verifyserver[index]

            data["verifyserver"] = verifyserver

            with open('data.json', 'w') as f:
                json.dump(data, f)
            await ctx.send(ctx.message.author.name + " Verify wurde auf diesem Server deaktiviert")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def setverifyrole(ctx, role: discord.Role):
    with open("data.json") as f:
        data = json.load(f)
        if not ctx.message.guild.id in data["verifyserver"]:
            await ctx.send(ctx.message.author.name + " Verify ist auf diesem Server deaktiviert.")
        else:
            data["verifyroles"].append(role.id)
            em = discord.Embed(
                title=ctx.message.author.name + " als Verifyrolle wurde " + role.mention + " (ID:`" + str(
                    role.id) + "`) gesetzt.", description="", color=discord.Color.blue())
            em.set_footer(text=f"{bot.user.name} by BuilderJG#4088")
            await ctx.send(embed=em)
            with open("data.json", 'w') as f:
                json.dump(data, f)


@bot.command()
async def verify(ctx):
    with open("data.json") as f:
        data = json.load(f)
        if not ctx.message.guild.id in data["verifyserver"]:
            await ctx.send(ctx.message.author.name + " Verify ist auf diesem Server deaktiviert.")
        else:
            try:
                for roleid in data["verifyroles"]:
                    role = discord.utils.get(ctx.message.guild.roles, id=roleid)
                    await ctx.message.author.add_roles(role)
                await ctx.send(ctx.message.author.name + "  du wurdest erfolgreich verifiziert!")
            except Exception:
                pass


# MONEY


@bot.command(aliases=['bal', 'money'])
async def balance(ctx, person: discord.User = None):
    if not person:
        person = ctx.message.author
    with open("data.json") as f:
        data = json.load(f)
    existingacc = False
    for user in data["balance"]:
        if user["id"] == person.id:
            existingacc = True
    if existingacc is False and not person.bot:
        data["balance"].append({
            "id": person.id,
            "points": 0,
        })
        with open("data.json", "w") as file:
            json.dump(data, file)
    if not person.bot:
        for user in data["balance"]:
            if user["id"] == person.id:
                point_num = user["points"]
                if person.id == ctx.message.author.id:
                    await ctx.send(f"Du hast {point_num}€")
                else:
                    await ctx.send(f"{person.name} hat {point_num}€")
    elif person.id == bot.user.id:
        await ctx.send("Das hier ist **mein** Moneysystem, selbstverständlich ist mein Kontostand ∞!")
    else:
        await ctx.send("Bitte gib einen normalen Benutzer an, der kein Bot ist.")


@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def work(ctx):
    jobs = ["Programmierer", "Putzkraft", "Bürokraft", "Straßenkehrer", "Lehrer", "YouTuber", "Streamer", "Polizist",
            "Feuerwehrmann", "Sanitäter", "Bauarbeiter", "Hausmeister", "Tischler"]
    lohn = random.randint(1, 100)
    job = random.choice(jobs)
    with open("data.json") as f:
        data = json.load(f)
    existingacc = False
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            existingacc = True
    if existingacc is False:
        data["balance"].append({
            "id": ctx.message.author.id,
            "points": 0,
        })
        with open("data.json", "w") as file:
            json.dump(data, file)
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            user["points"] += lohn
    with open("data.json", "w") as file:
        json.dump(data, file)
    await ctx.send("Du hast als " + job + " gerabeitet und " + str(lohn) + "€ bekommen.")


@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def beg(ctx):
    with open("data.json") as f:
        data = json.load(f)
    existingacc = False
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            existingacc = True
    if existingacc is False:
        data["balance"].append({
            "id": ctx.message.author.id,
            "points": 0,
        })
        with open("data.json", "w") as file:
            json.dump(data, file)
    lohn = random.choice([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5])
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            user["points"] += lohn
    with open("data.json", "w") as file:
        json.dump(data, file)
    await ctx.send("Du hast beim Betteln " + str(lohn) + "€ bekommen.")


@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    with open("data.json") as f:
        data = json.load(f)
    existingacc = False
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            existingacc = True
    if existingacc is False:
        data["balance"].append({
            "id": ctx.message.author.id,
            "points": 0,
        })
    with open("data.json", "w") as file:
        json.dump(data, file)
    for user in data["balance"]:
        if user["id"] == ctx.message.author.id:
            user["points"] += 100
    await ctx.send("Du hast deine täglichen 100€ bekommen.")
    with open("data.json", "w") as file:
        json.dump(data, file)


@bot.command()
async def pay(ctx, person: discord.User, amount=None):
    if not person.bot:
        with open("data.json") as f:
            data = json.load(f)
        existingacc = False
        for user in data["balance"]:
            if user["id"] == ctx.message.author.id:
                existingacc = True
        if existingacc is False:
            data["balance"].append({
                "id": ctx.message.author.id,
                "points": 0,
            })
        pexistingacc = False
        for user in data["balance"]:
            if user["id"] == person.id:
                pexistingacc = True
        if pexistingacc is False:
            data["balance"].append({
                "id": person.id,
                "points": 0,
            })
        with open("data.json", "w") as file:
            json.dump(data, file)
        if not amount:
            await ctx.send("Bitte gib an wie viel Geld du zahlen möchtest.")
            return
        try:
            amount = int(amount)
        except Exception:
            await ctx.send("Bitte gib eine gültige Zahl an.")
            return
        for user in data["balance"]:
            if user["id"] == ctx.message.author.id:
                if user["points"] >= amount:
                    user["points"] -= amount
                else:
                    await ctx.send("Du hast nicht genug Geld dafür.")
                    return
        for user in data["balance"]:
            if user["id"] == person.id:
                user["points"] += amount
        with open("data.json", "w") as file:
            json.dump(data, file)
        await ctx.send(f"Du hast {person.name} {amount}€ gezahlt.")
    elif person.id == bot.user.id:
        await ctx.send("Danke, aber ich habe schon ∞ Geld!")
    else:
        await ctx.send("Bitte gib einen normalen Benutzer an, der kein Bot ist.")


# LOGGING


@bot.command()
@commands.has_permissions(manage_channels=True)
async def addjoinlog(ctx, channel: discord.TextChannel):
    with open("data.json") as f:
        data = json.load(f)
        if channel.id in data["joinchannel"]:
            await ctx.send("Der angegebene Kanal wurde bereits als Joinlog registriert.")
        else:
            data["joinchannel"].append(channel.id)
            await ctx.send(
                ctx.author.name + f" du hast erfolgreich den Kanal {channel.mention} als Joinlog registriert.")
            with open("data.json", 'w') as file:
                json.dump(data, file)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def deljoinlog(ctx, channel: discord.TextChannel):
    with open("data.json") as f:
        data = json.load(f)
        joinchannel = data["joinchannel"]

        if channel.id in joinchannel:
            index = joinchannel.index(channel.id)

            del joinchannel[index]

            data["joinchannel"] = joinchannel

            with open('data.json', 'w') as f:
                json.dump(data, f)
                await ctx.send(
                    ctx.author.name + f" der Kanal {channel.mention} ist nun kein Joinlog mehr.")
        else:
            await ctx.send("Der angegebene Kanal ist bereits kein Joinlog.")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def addleavelog(ctx, channel: discord.TextChannel):
    with open("data.json") as f:
        data = json.load(f)
        if channel.id in data["leavechannel"]:
            await ctx.send("Der angegebene Kanal wurde bereits als Leavelog registriert.")
        else:
            data["leavechannel"].append(channel.id)
            await ctx.send(
                ctx.author.name + f" du hast erfolgreich den Kanal {channel.mention} als Leavelog registriert.")
            with open("data.json", 'w') as file:
                json.dump(data, file)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def delleavelog(ctx, channel: discord.TextChannel):
    with open("data.json") as f:
        data = json.load(f)
        joinchannel = data["leavechannel"]

        if channel.id in joinchannel:
            index = joinchannel.index(channel.id)

            del joinchannel[index]

            data["leavechannel"] = joinchannel

            with open('data.json', 'w') as f:
                json.dump(data, f)
                await ctx.send(
                    ctx.author.name + f" der Kanal {channel.mention} ist nun kein Leavelog mehr.")
        else:
            await ctx.send("Der angegebene Kanal ist bereits kein Leavelog.")


# FEEDBACK & BUGS

@bot.command(aliases=['error', 'report'])
async def bug(ctx):
    em = discord.Embed(title="Fehler gefunden?",
                       description=f"Nutze den Command `{p}feedback` oder joine auf unseren Discord-Server und schreibe BuilderJG#4088 an!",
                       colour=discord.Colour.blue())
    em.add_field(name="Unser Discord-Server:",
                 value="`discord.gg/V3svjsdn47`")
    em.set_footer(text=str(bot.user.name) + " by BuilderJG#4088")
    await ctx.send(embed=em)


@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def feedback(ctx, *, text):
    with open("data.json") as f:
        data = json.load(f)
    if not ctx.message.author.id in data["bannedusers"]:
        ownerid = 602546162909708331

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["✅"] and reaction.message == message

        message = await ctx.send(
            "Feedback:\nUm sicherzugehen, dass du dir sicher bist, dass du dein Feedback (`" + text + "`) an den Bot-Owner abschicken möchtest, reagiere bitte innerhalb von 60 Sekunden mit `✅` auf diese Nachricht!")
        await message.add_reaction("✅")
        confirmation = await bot.wait_for("reaction_add", check=check, timeout=60)
        if confirmation:
            em = discord.Embed(title="Feedback von " + str(ctx.message.author) + ":",
                               description=text + "\nUserID: `" + str(ctx.message.author.id) + "`",
                               color=0xff0000)
            await bot.get_user(ownerid).send(embed=em)
            await ctx.send(
                str(ctx.message.author.name) + ", dein Feedback wurde erfolgreich abgesendet, wir werden uns so schnell wie möglich darum kümmern!")
    else:
        await ctx.send(
            ctx.author.name + " du wurdest von der Feedback-Funktion ausgeschlossen und kannst diesen Command nicht nutzen.")


@bot.command()
@commands.is_owner()
async def fbban(ctx, user: discord.User):
    with open("data.json") as f:
        data = json.load(f)
        if user.id in data["bannedusers"]:
            await ctx.send("Der angegebene wurde bereits von der Feedback Funktion ausgeschlossen.")
        else:
            data["bannedusers"].append(user.id)
            await ctx.send(
                ctx.author.name + f" du hast erfolgreich den User {user} von der Feedback Funktion ausgeschlossen.")
            with open("data.json", 'w') as file:
                json.dump(data, file)


# GIVEAWAY
def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except Exception:
        return -2

    return val * time_dict[unit]


@bot.command()
@commands.has_permissions(kick_members=True)
async def giveaway(ctx, channel: discord.TextChannel = None):
    if not channel:
        await ctx.send("Bitte gib einen Kanal an.")
        return
    await ctx.send("Los gehts, bitte beantworte diese Fragen innerhalb von 60 Sekunden.")

    questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)",
                 "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('messsage', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except Exception:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time just be an integer. Please enter an integer next time.")
        return

    prize = answers[2]

    await ctx.send(f"The giveaway will be in {channel.mention} and will last {answers[1]} seconds!")

    embed = discord.Embed(title="Giveaway!", description=f"{prize}", color=ctx.author.color)

    embed.add_field(name="Hosted by:", value=ctx.author.mention)

    embed.set_footer(text=f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won the prize: {prize}!")


@bot.command()
@commands.has_permissions(kick_members=True)
async def reroll(ctx, channel: discord.TextChannel, id_: int):
    try:
        new_msg = await channel.fetch_message(id_)
    except Exception:
        await ctx.send(
            "The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await help(ctx)
    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, und {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' und '.join(missing)
        await ctx.send(f"Ich habe keine Berechtigung dazu, mir fehlt die Berechtigung `{fmt}`.")
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send('Dieser Command wurde deaktiviert.')
        return
    if isinstance(error, commands.CommandOnCooldown):
        seconds = round(error.retry_after)
        minutes = 0
        hours = 0
        if seconds < 60:
            await ctx.send(f"Befehl ist unter Cooldown, versuch es noch mal nach {seconds} Sekunden!")
        else:
            while seconds >= 60:
                seconds -= 60
                minutes += 1
            if minutes < 60:
                await ctx.send(
                    f"Befehl ist unter Cooldown, versuch es noch mal nach {minutes} Minuten und {seconds} Sekunden!")
            else:
                while minutes >= 60:
                    minutes -= 60
                    hours += 1
                await ctx.send(
                    f"Befehl ist unter Cooldown, versuch es noch mal nach {hours} Stunden, {minutes} Minuten und {seconds} Sekunden!")

    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, und {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' und '.join(missing)
        await ctx.send(f"Du hast keine Berechtigung dazu, dir fehlt die Berechtigung `{fmt}`.")
        return

    if isinstance(error, commands.UserInputError):
        await ctx.send("Ungültige Eingabe.")
        return

    if isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send('Dieser Command kann nicht in Direktnachrichten genutzt werden.')
        except discord.Forbidden:
            pass
        return

    if isinstance(error, commands.CheckFailure):
        await ctx.send("Du bist nicht berechtigt diesen Command auszuführen.")
        return
    print(error)


with open("data.json") as f:
    data = json.load(f)
    bot.run(data["token"])
