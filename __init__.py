from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

class RememberSkill(Skill):
    @match_regex(r'^!remember (?P<key>\w+) (?P<value>.*)$')
    async def put(self, message):
        await self.opsdroid.memory.put(message.regex.group('key'), message.regex.group('value'))
        await message.respond("OK, I'll remember {} as {}".format(message.regex.group('key'), message.regex.group('value')))

    @match_regex(r'^!(?P<key>\w+)$')
    async def get(self, message):
        information = await self.opsdroid.memory.get(message.regex.group('key'))
        if (information == None):
            await message.respond("I don't remember {}".format(message.regex.group('key')))
        else:
            await message.respond(information)

    @match_regex(r'^!forget (?P<key>\w+)$')
    async def delete(self, message):
        await self.opsdroid.memory.delete(message.regex.group('key'))
        await message.respond("Ok I've forgetten {}".format(message.regex.group('key')))
