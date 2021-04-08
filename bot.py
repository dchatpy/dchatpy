import dogehouse
import os

class thisbot(dogehouse.DogeClient):
    @dogehouse.event
    async def on_ready(self):
      print(f"Logged on as {self.user.username}")
      await self.create_room("DogeChatBot Testing Room")
    @dogehouse.event
    async def on_error(self,error):
      await self.send("Error")
    @dogehouse.command
    async def test0(self,ctx):
      await self.send("I'm @"+self.user.username)

thisbot(os.getenv("token"), os.getenv("refresh_token"), prefix=os.getenv("prefix")).run()
