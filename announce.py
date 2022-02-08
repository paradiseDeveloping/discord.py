a = "paradise#0666"

@bot.command()
async def announce(ctx,*,arg):
    if ctx.author.guild_permissions.administrator:
        member = ctx.author
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="Announcement",
                              colour=0xDC6BC4,
                              description=f"{arg}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="{}".format(a))
        mess = await ctx.channel.send(embed=embed)
