#dont forget to hover giphy_client and hit install + import.

async def gif(ctx, *, q="Error"):
    api_key = "0Hv8Jh4EbijmQQbTF250BXuu0bKymwvZ"
    api_instance = giphy_client.DefaultApi()

    try:

        api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating="pg")
        lst = list(api_responce.data)
        giff = random.choice(lst)

        emb = discord.Embed(title="Your Gif")
        emb.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")

        await ctx.channel.send(embed=emb)

    except ApiException as e:
        print("")
