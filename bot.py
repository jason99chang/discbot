import discord
import random
import asyncio
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = ".")

class animal:
    def __init__(self, species, name, image):
        self.species = species
        self.name = name
        self.image = image
        self.owner = "None"

    def catch(self, catcher):
        if self.owner == "None":
            self.owner = catcher
            return True
        return False

    def getSpecies(self):
        return self.species

    def getName(self):
        return self.name

    def getPic(self):
        return self.image

    def changeName(self, newName):
        self.name = newName

    def getOwner(self):
        return self.owner

cat1 = animal("Cat", "Plip & Plop", "cat/cat1.png")
bunny1 = animal("Bunny", "Cotton", "bunny/bunny1.png")
dog1 = animal("Dog", "Daisy", "dog/dog1.png")
cat2 = animal("Cat", "Breadcat", "cat/cat2.png")
bunny2 = animal("Bunny", "Earl Grey", "bunny/bunny2.png")
dog2 = animal("Dog", "Cloud", "dog/dog2.png")
cat3 = animal("Cat", "Flowercat", "cat/cat3.png")
bunny3 = animal("Bunny", "Sweepy", "bunny/bunny3.png")
dog3 = animal("Dog", "Gambino", "dog/dog3.png")

animals = [cat1, bunny1, dog1, cat2, bunny2, dog2, cat3, bunny3, dog3]
caughtAnimals = []
global WildAnimal
WildAnimal = animals[1]
WildAnimal1 = True

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("i love jason"))
    client.loop.create_task(found())
    WildAnimal = animals[1]
    #found.start()
    print("Bot is ready.")


#@tasks.loop(seconds=3)
async def found():
    WildAnimal = random.choice(animals)
    await asyncio.sleep(3)

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")

@client.event
async def on_member_join(member):
    print(f"{member} has left the server.")

@client.command()
async def hi(ctx):
    await ctx.send("hi")

@client.command()
async def is_jason_dumb(ctx):
    await ctx.send("yes")

@client.command()
async def cat(ctx):
    await ctx.send("cat")

@client.command()
async def catch(ctx):
    person = str(ctx.author.name)
    if WildAnimal.catch(person):
        await ctx.send(f"{person} has caught {WildAnimal.getName()}!")
        await ctx.send(file=discord.File(WildAnimal.getPic()))
        animals.remove(WildAnimal)
        caughtAnimals.append(WildAnimal)
    else:
        await ctx.send(f"{WildAnimal.getOwner()} has already caught {WildAnimal.getName()}!")

@client.command()
async def players(ctx):
    await ctx.send(players)

@client.command()
async def allcats(ctx):
    for a in animals:
        if a.getSpecies() is "Cat":
            await ctx.send(a.getName())

@client.command()
async def alldogs(ctx):
    for a in animals:
        if a.getSpecies() is "Dog":
            await ctx.send(a.getName())

@client.command()
async def allbunnies(ctx):
    for a in animals:
        if a.getSpecies() is "Bunny":
            await ctx.send(a.getName())

@client.command()
async def lookup(ctx, *, name):
    for a in animals:
        if a.getName() == name.capitalize():
            await ctx.send(f"Name: " + a.getName())
            await ctx.send(f"Owner: " + a.getOwner())
            await ctx.send(file=discord.File(a.getPic()))

@client.command()
async def mypets(ctx):
    count = 0
    name = str(ctx.author.name)
    for a in animals:
        if a.getOwner() == name:
            count = count + 1
            await ctx.send(f"Name: " + a.getName())
            await ctx.send(f"Owner: " + a.getOwner())
            await ctx.send(file=discord.File(a.getPic()))
    if count == 0:
        await ctx.send("You have no pets yet!")

@client.command()
async def check(ctx):
    await ctx.send(WildAnimal.getName())

@client.command()
async def next(ctx):
    WildAnimal = random.choice(animals)
    await ctx.send(f"A wild {WildAnimal.getName()} has appeared!")

@client.command()
async def test(ctx, *, name):
    await ctx.send(f"name: {name}")
    await ctx.send(file=discord.File('bunny/bunny1.png'))

@client.command()
async def test2(ctx):
    await ctx.send(file=discord.File('bunny/bunny1.png'))

@client.command()
async def jason(ctx):
    await ctx.send("I love jason")


client.run("NjE2NDc4NjI4NzgzMzI1MTg0.XWdKmQ.p-PKtOuBpXGnbN2llDNfn0bvaYE")
