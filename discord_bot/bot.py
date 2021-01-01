import discord
import re

from discord_bot import (
    database_query as db,
    google_api as google_api
)
from settings import settings as settings


class BotClient(discord.Client):
    """
    Bot client for all bot related methods
    """
    async def on_ready(self):
        # In future we can use logging instead of print statements
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        """
        Method called when a message is created or sent.
        :param message: message
        :return: None
        """
        message_data = message.content.strip()
        splited_message_data = message_data.split()

        # bot replying "Hey" to "Hi" message functionality
        if re.search('^hi$', message_data.lower()):
            await message.channel.send(embed=discord.Embed(title="Hey!", color=0x00ff00))

        # bot returning top 5 google search title and link
        elif len(splited_message_data) > 1 and re.search('^!google$', splited_message_data[0]):
            search_query = ' '.join(splited_message_data[1:])
            google_result, error = google_api.GoogleClient().get_google_search_link(search_query)
            await message.channel.send(
                (
                    google_result if google_result else 'No result found.'
                    if not error else 'Something went wrong. Bot is unable to do a google search for you.'
                )
            )
            # In future we can call this db connection asynchronously
            db.DbConnection().insert_data(message.author.id, search_query)

        # bot returning recent history
        elif len(splited_message_data) > 1 and re.search('^!recent$', splited_message_data[0]):
            search_query = ' '.join(splited_message_data[1:])
            search_result, error = db.DbConnection().get_data(message.author.id, search_query)
            await message.channel.send(
                (
                    search_result if search_result else 'No recent search found.'
                    if not error else 'Something went wrong. Bot is unable to show recent search.'
                )
            )


client = BotClient()
client.run(settings.BOT_TOKEN)
