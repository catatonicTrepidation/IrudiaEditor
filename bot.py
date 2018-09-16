import discord
from discord.ext import commands
import json

# my code
from opencv import filters, imgtools, kernelparse
import filter_switchboard
import contextparse


config_data = json.load(open('data/config.json','r',encoding="utf-8_sig"))
TOKEN = config_data['token']

description = '''Apply filters, transform, and combine images with Irudia.

lotta bull'''

bot = commands.Bot(command_prefix=('...','…','---'), description=description)

@bot.command(aliases=['edgelord'], pass_context=True)
async def edge(ctx: commands.Context, url : str = None, kern_dim : int = None, *, args = 'nyan'):
    """Rolls a dice in NdN format."""
    # success = None
    # if url:
    #     success = download.download_image(url, 'data\databases\{}\downloaded\images\input_{}.png'.format(ctx.message.server.id, 'edge'))
    # elif ctx.message.attachments:
    #     success = download.download_image(ctx.message.attachments[0]['url'], 'data\databases\{}\downloaded\images\input_{}.png'.format(
    #         ctx.message.server.id, 'edge'))
    # if success:
    #     # grab image
    #     img = filter_switchboard.read_image('data\databases\{}\downloaded\images\input_{}.png'.format(ctx.message.server.id, 'edge'))
    #
    img = contextparse.get_image(ctx, url, 'edge')
    if img is not None:
        result_img = filters.edge(img, kern_dim)
        imgtools.write_image(result_img, ctx.message.server.id, 'edge')
        await bot.send_file(ctx.message.channel, 'data\databases\{}\output\images\output_edge.png'.format(ctx.message.server.id))
        return True

    await bot.say('Need to supply img! (might make bot check a few images above, dunno)')

@bot.command(aliases=['custom','k'], pass_context=True)
async def kernel(ctx: commands.Context, url : str = None, *, args = 'nyan'):
    """Rolls a dice in NdN format."""

    img = contextparse.get_image(ctx, url, 'customkernel')
    if img is None:
        await bot.say('Had trouble reading! (might make bot check a few images above, dunno)')

    operands = None
    if '-' in args or '+' in args:
        operands = True
    if operands:
        kern = kernelparse.parse_multiple_matrices(args)
    else:
        kern = kernelparse.parse_one_matrix(args)
    result_img = filters.convolve(img, kern)
    imgtools.write_image(result_img, ctx.message.server.id, 'customkernel')

    await bot.send_file(ctx.message.channel, 'data\databases\{}\output\images\output_customkernel.png'.format(ctx.message.server.id))
    return True


bot.run(TOKEN)