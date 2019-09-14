import asyncio
import sys
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform, LicenseType, LocalGameState
from galaxy.api.types import Game, LicenseInfo, Authentication, LocalGame
import subprocess


urls = {
    'pyconpl-2018': 'https://pl.pycon.org/2018/',
    'pyconpl-2019': 'https://pl.pycon.org/2019/',
    'meetpy': 'https://github.com/meetpy/meetpy',
}


class PyconPLPlugin(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.PcEngine,  # Choose platform from available list
            "0.1",  # Version
            reader,
            writer,
            token
        )

    async def get_local_games(self):
        return [
            LocalGame(
                game_id='pyconpl-2019',
                local_game_state=LocalGameState.Installed
            ),
            LocalGame(
                game_id='meetpy',
                local_game_state=LocalGameState.Installed
            ),
        ]

    async def authenticate(self, stored_credentials=None):
        return Authentication('user_unique_id', 'Authenticated Username')

    async def get_owned_games(self):
        return [
            Game(
                game_id='meetpy',
                game_title='MeetPy - a project of common and unified webpage for all polish python meetups',
                dlcs=None,
                license_info=LicenseInfo(LicenseType.SinglePurchase, None)
            ),
            Game(
                game_id='pykonik',
                game_title='Pykonik - Kraków Meetup',
                dlcs=None,
                license_info=LicenseInfo(LicenseType.SinglePurchase, None)
            ),
            Game(
                game_id='pyconpl-2018',
                game_title='PyConPL 2018',
                dlcs=None,
                license_info=LicenseInfo(LicenseType.SinglePurchase, None)
            ),
            Game(
                game_id='pyconpl-2019',
                game_title='PyConPL 2019',
                dlcs=None,
                license_info=LicenseInfo(LicenseType.SinglePurchase, None)
            ),
        ]

    async def launch_game(self, game_id):
        subprocess.Popen(['open', urls[game_id]])


def main():
    create_and_run_plugin(PyconPLPlugin, sys.argv)


# run plugin event loop
if __name__ == "__main__":
    main()
