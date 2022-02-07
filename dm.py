# sends a custom DM to @user

@bot.command()
async def dm(ctx, user: discord.User, *, msg):
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        try:
            embed = discord.Embed(title="**{}**".format(user.name),
                                description="{}".format(msg),
                                color=0xD70000)
            embed.set_footer(text="{}".format(lower))
            mess = await user.send(embed=embed)
            mess = await ctx.send(embed=embed)
        except:
            errorembed = discord.Embed(title="**Warning**",
                                       description="Couldnt send the message.",
                                       color=0xD70000)
            mess = await ctx.channel.send(embed=errorembed)
