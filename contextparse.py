from data import download
import filter_switchboard




def get_image(ctx, url, funct_name):
    success = None
    if url:
        success = download.download_image(url, 'data\databases\{}\downloaded\images\input_{}.png'.format(ctx.message.server.id, funct_name))
    if not success and ctx.message.attachments:
        success = download.download_image(ctx.message.attachments[0]['url'], 'data\databases\{}\downloaded\images\input_{}.png'.format(
            ctx.message.server.id, funct_name))
    if success:
        # grab image
        img = filter_switchboard.read_image('data\databases\{}\downloaded\images\input_{}.png'.format(ctx.message.server.id, funct_name))
        return img
    return False, None