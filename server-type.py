import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import urllib.request

pygame.mixer.music.load("song.mp3") #Eric Matyas
pygame.mixer.music.play(-1)

level=-2
message=""
target="http://localhost"

def get_server_type(url):
    global message
    try:
        request = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(request) as response:
            headers = response.info()
            server = headers.get("Server")
            if server:
                message=f"Server type for {url}: {server}"
            else:
                message=f"Server type for {url}: (not disclosed)"
    except Exception as e:
        message=f"Error fetching {url}: {e}"

def draw():
    global level, target, message
    screen.clear()
    if level==-2:
        screen.blit("disclaimer",(0,0))
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Website to find out the server-type:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
        get_server_type(target)
    elif level == 2:
        screen.blit("back",(0,0))
        screen.draw.text(message, center=(400, 130), fontsize=24, color=(25, 0, 55))
 
def on_key_down(key, unicode=None):
    global level, target
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        target = ""
    elif key == keys.RETURN and level == 1:
        if not target.strip():
            target = "127.0.0.1"
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode

def update():
    global level
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==2 and keyboard.space:
        level=0

pgzrun.go()
