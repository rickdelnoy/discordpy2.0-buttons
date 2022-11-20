import discord
from discord.ui import Button, View
from discord.ext import commands


class Buttons(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=5)
        self.ctx = ctx

    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.edit_message(content=f"This is an edited button response!")
    
    @discord.ui.button(label="Clear",style=discord.ButtonStyle.red)
    async def red_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.clear_items()
        await interaction.response.edit_message(view=self)
    
    async def on_timeout(self):
        await self.message.edit(view=None)


@bot.command()
async def button(ctx):
    view = Buttons(ctx)
    msg = await ctx.send("This message has buttons!", view=view)
    view.message = msg
