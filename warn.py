import json

a = "paradise#0666"

with open('warns.json', encoding='utf-8') as f:
  try:
    warns = json.load(f)
  except ValueError:
    warns = {}
    warns['users'] = []

@bot.command(pass_context = True)
async def warn(ctx,user:discord.User,*reason:str):
    if ctx.author.guild_permissions.kick_members:
        if not reason:
            embed = discord.Embed(title="Fatal Error!",
                                 description=f"Theres no Reason given.",
                                 color=0x0F77DE)
            embed.set_footer(text="{}".format(a))
            mess = await ctx.channel.send(embed=embed)
            return
        reason = ' '.join(reason)
        for current_user in warns['users']:
            if current_user['name'] == user.name:
                current_user['reasons'].append(reason)
            break
        else:
            warns['users'].append({
            'name':user.name,
            'reasons': [reason,]
            })
        with open('warns.json','w+') as f:
            json.dump(warns,f)
            embed = discord.Embed(title=f"{user} has been warned!",
                                description=f"**Reason** | {reason}",
                                color=0x0F77DE)
            embed.set_footer(text="{}".format(a))
            mess = await ctx.channel.send(embed=embed)

@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User):
    if ctx.author.guild_permissions.kick_members:
        for current_user in warns['users']:
            if user.name == current_user['name']:
                embed = discord.Embed(title=f"{user.name} | Warnings",
                                    description=f"{len(current_user['reasons'])} times",
                                    color=0x0F77DE)
                embed.add_field(name="Reasons", value=(','.join(current_user['reasons'])),
                                    inline=False)
                embed.set_footer(text="{}".format(a))
                mess = await ctx.channel.send(embed=embed)
                break
