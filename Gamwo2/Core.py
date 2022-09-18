import pyglet.window
import sys
from pyglet import app

class GamwoForExtend:
    def __init__(self, title: str = "Gamwo2 Game", width: int = 800, height: int = 600, fullscreen: bool = False, vsync: bool = False) -> None:
        self.title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.vsync = vsync

        try:
            self.win = pyglet.window.Window(
                caption = self.title,
                width = self.width,
                height = self.height,
                fullscreen = self.fullscreen,
                vsync = self.vsync,
            )

            print("---- GAMWO 2 NOTIFICATION --> Window created succesfuly.")
        except Exception as e:
            print(f"---- GAMWO ERROR NOTIFICATION --> Window couldn't be created. ")
            print("Error:")
            print(str(e))
            sys.exit(1)


    def run(self):
        try:
            app.run()
            print("---- GAMWO NOTIFICATION ---> Running game...")
        except Exception as e:
            print("---- GAMWO ERROR NOTIFICATION ---> Couldn't run game.")
            print("Error:")
            print(str(e))
            sys.exit(1)
            

##### 2D CLASS

class Gamwo2D(GamwoForExtend):
    def __init__(self) -> None:
        super().__init__()