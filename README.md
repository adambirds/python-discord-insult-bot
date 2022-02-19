# python-discord-insult-bot

[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy coverage](https://img.shields.io/badge/mypy-100%25-green.svg)](https://github.com/python/mypy)
![GitHub Sponsors](https://img.shields.io/github/sponsors/adambirds)

A Discord Bot Written in Python to Dish Out Insults.

## Support
For support using this bot, please join our [official support server](https://discord.gg/f5veJaa4ZX) on [Discord](https://discord.com).

[![discord](https://img.shields.io/discord/941885906443468880?color=%237289DA&label=Coding%20With%20Adam&logo=discord&logoColor=white)](https://discord.gg/f5veJaa4ZX)

## Source
The source code can be found [here](https://github.com/adambirds/python-discord-insult-bot).

Contributions welcome and gratefully appreciated!

## Requirements
Python 3 (Version 3.6 or later).

## Installation

This has only been tested on Linux, so preferably use Linux or WSL 2 if on Windows.

Navigate to where you will store the bot files, then run:

```
git clone git@github.com:adambirds/python-discord-insult-bot.git
```

Then run:

```
tools/setup/prep-prod-environment
```

Then run:

```
cp example-config.yaml config.yaml
```

You will then need to edit config.yaml to your needs. You shouldn't delete any of the keys, however the `USER_TO_INSULT`, `INSULT_KEYS` and `CHANNEL_FOR_TASK` can be left empty if you don't want to consistently insult a user every hour.

The `ACCESS_TOKEN` key can be generated[here](https://discord.com/developers/applications).

You can setup your bot to run as a service by amending the `./python-discord-insult-bot.service` file with your working directorys and copying it using the following command:

```
cp ./python-discord-insult-bot.service /lib/systemd/system/
```

Then run:

```
systemctl daemon-reload
```

Then run:

```
systemctl start python-discord-insult-bot
```

And then to ensure it starts when your server does run:

```
systemctl enable python-discord-insult-bot
```

## Commands and Events

### Commands

The bot supports the following commands:

| Command | Aliases | Example | Permissions | Purpose |
|-------- | ------- | ------- | ----------- | ------- |
| !insult | | `!insult @nameofuser` | Everyone | The bot will mention the user and then insult them. |

### Taks
If you set the `USER_TO_INSULT` key to a user's ID **AND** set the `CHANNEL_FOR_TASK` to a channel ID, they will be insulted every hour in that channel. For this to work you need at least 1 custom insult in the `INSULT_LIST` key.

## License

This project is released under the [GNU GENERAL PUBLIC LICENSE v3](https://github.com/adambirds/python-discord-insult-bot/blob/main/LICENSE).

## Contributing

Anybody is welcome to contribute to this project. I just ask that you check out our contributing guidelines
[here](https://github.com/adambirds/python-discord-insult-bot/blob/main/docs/contributing/contributing.md) first.
