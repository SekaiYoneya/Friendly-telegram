#clown... again :/ by @Sekai_Yoneya

from .. import loader, utils 
import re 
from asyncio import sleep 
 
 
@loader.tds 
class DelTmMod(loader.Module): 
    strings = {"name": "Delete timer"} 
 
    @loader.owner 
    async def deltmcmd(self, m): 
        ".deltm <реплай> <секунды>\ 
        \nУдалить сообщение в реплае через указанное время" 
        reply = await m.get_reply_message() 
        if not reply: 
            return await m.edit("reply to message...") 
        a = re.compile(r"^\d+$") 
        t = utils.get_args_raw(m) 
        if a.match(t): 
            await m.delete() 
            await sleep(int(t)) 
            await reply.delete() 
        else: 
            await m.edit("shit...") 
            return
