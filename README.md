# opsdroid skill remember

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to remember things.

## Requirements

Opsdroid has a memory class which can be used to persist data between different connectors (which run in different process forks) and across restarts of the bot.
You need to have a database configured or it won't work past a restart.

## Configuration

None

## Usage

### Remember:

> user: !remember faq https://poshcode.gitbook.io/powershell-faq/
> opsdroid: OK, I'll remember faq as https://poshcode.gitbook.io/powershell-faq/

### Recall:

> user: !faq
> opsdroid: https://poshcode.gitbook.io/powershell-faq/

### Forget:

> user: !forget faq
> opsdroid: Ok I've forgetten faq

