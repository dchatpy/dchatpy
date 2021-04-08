import dogehouse
import os

class thisbot(dogehouse.DogeClient):
    @dogehouse.event
    async def on_ready(self):
      print(f"Logged on as {self.user.username}")
      await self.create_room("DogeChatBot Testing Room")
    @dogehouse.event
    async def on_error(self,error):
      await self.send("Hey, that command doesn't exists, try to find the command on "+os.getenv("prefix")+"help")
    @dogehouse.command
    async def test0(self,ctx):
      await self.send("I'm @"+self.user.username)
    @dogehouse.command
    async def help(self,ctx):
      await self.send(f"""DogeChatBot Command list
{os.getenv("prefix")}help | Watch the command list
{os.getenv("prefix")}test0 | Test0""")

thisbot(os.getenv("token"), os.getenv("refresh_token"), prefix=os.getenv("prefix")).run()
