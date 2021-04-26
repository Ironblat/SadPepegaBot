import discord
from discord.ext import commands



client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.pepehelp a segítséghez'))
    print("SadPepegaBot is online")

@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping: {round(client.latency * 1000)}ms')

@client.command()
async def opgg(ctx, member: discord.Member):
    if f'{member}' == 'G2 Wakandai#4369':
        await ctx.send('https://eune.op.gg/summoner/userName=Wakandaiharcos')

    if f'{member}' == 'G2 Ironblyat#2488':
        await ctx.send('https://eune.op.gg/summoner/userName=bodorjano05')

    if f'{member}' == 'SzabiTábornokHadnagy#4723':
        await ctx.send('https://eune.op.gg/summoner/userName=SzabiZ')


@client.command()
async def pepehelp(ctx):
    embed = discord.Embed(
        title='Segítség',
        description='Itt vagyok segítek.',
        colour=discord.Colour.green()

    )

    embed.set_footer(text='Nah mentem! A szurdok legyen veletek idézők!')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/779083318871588887/779083399804485632/sadpepe.png?width=427&height=427")
    embed.add_field(name=".pepehelp", value="Ezt olvasod most.", inline=False)
    embed.add_field(name=".ping", value="Megmutatom a pinged hogy rá tud fogni arra, hogy miért feedeltél.",
                    inline=False)
    embed.add_field(name=".opgg @G2 Ironblyat/@G2 Wakandai/@SzabiZ", value="A három alapítótag LoL accountja.",
                    inline=False)
    embed.add_field(name=".pepedance", value="Elkezdek táncolni.",
                    inline=False)
    embed.add_field(name=".test", value="Működök? Tudd meg!",
                    inline=False)
    embed.add_field(name=".mester", value="A mester elérhetőségei.",
                    inline=False)
    embed.add_field(name=".verzio", value="Hanyas verziójú vagyok? Megmondom!",
                    inline=False)
    embed.add_field(name=".win", value="Winner winner chicken dinner!",
                    inline=False)
    embed.add_field(name=".újdonságok", value="Mik az újdonságok? Lesd meg!",
                    inline=False)

    await ctx.send(embed=embed)


@client.command()
async def pepedance(ctx):
    await ctx.send("https://tenor.com/VEsD.gif")

@client.command()
async def test(ctx):
    await ctx.send("Működök!")

@client.command()
async def mester(ctx):
    ak = discord.Embed(
        title='Mester elérhetőségei',
        description='',
        colour=discord.Colour.dark_red()
    )
    ak.add_field(name="Instagram", value="https://www.instagram.com/adamkissak/?hl=hu",
                    inline=False)
    ak.add_field(name="Youtube", value="https://www.youtube.com/channel/UCE6hAWc-vFW1ZzugFA-XggA",
                 inline=False)
    ak.add_field(name="Twitch", value="https://www.twitch.tv/adamkissak",
                 inline=False)
    ak.set_thumbnail(url="https://cdn.discordapp.com/attachments/779673013427765261/779673073401856001/ak.jpg")
    await ctx.send(embed=ak)


@client.command()
async def pcjani(ctx):
        pc = discord.Embed(
            title='PC',
            description='',
            colour=discord.Colour.red()

        )
        pc.add_field(name="Gépház", value="https://www.pcx.hu/zeus-gaming-midi-prodigy-a65-650w-szamitogephaz-00927324",
                     inline=False)
        pc.add_field(name="Alaplap", value="https://www.pcx.hu/gigabyte-b450m-s2h-alaplap-00135138",
                     inline=False)
        pc.add_field(name="Processzor", value="https://hardverapro.hu/apro/elado_amd_ryzen_5_2600_4/hsz_1-50.html",
                     inline=False)
        pc.add_field(name="RAM", value="https://www.pcx.hu/kingston-8gb-ddr4-3200mhz-hyperx-fury-hx432c16fb3-8-memoria-00179803",
                     inline=False)

        await ctx.send(embed=pc)


@client.command()
async def verzió(ctx):
 verzio = discord.Embed(
    title='',
    description='',
    colour=discord.Colour.green()
 )
 verzio.add_field(name="Aktuáis verzió", value="SadPepegaBot v2.5", inline=False)
 await ctx.send(embed=verzio)

@client.command()
async def win(ctx):
    await ctx.send("https://tenor.com/9ETn.gif")

@client.command()
async def újdonságok(ctx):
 ujdonsagok = discord.Embed(
        title='Újdonságok!',
        description='',
        colour=discord.Colour.blue()
    )
 
 ujdonsagok.add_field(name=".report @MODI", value="Jelentsd be ha valaki rosszalkodik. A többit én és a modik elintézzük")
 await ctx.send(embed=ujdonsagok)


@client.command()
async def infó(ctx):
 credit = discord.Embed(
        title='Credits',
        description='',
        colour=discord.Colour.green()
    )
 
 credit.add_field(name="Készítette", value="Bodor János Bence A.K.A. Ironblyat")
 credit.add_field(name="Készült", value="2020.11.18.-án")
 credit.add_field(name="Program nyelv", value="Python")
 await ctx.send(embed=credit)




#That part is not working
@client.command()
async def report(ctx, role: discord.Role, user: discord.Member, *, msg,):
    await ctx.send('Sikeresen bejelentteted ' f'{user}' ' nevű tagot! Vizsgáljuk bejelentésedet')

    if f'{role}' == "@MODI":
    await role.send(f'{ctx.author.name}' ' bejelentette ' f'{user}' ' tagot. A bejelentés oka: ' f'{msg}')






#Token goes here
client.run()
