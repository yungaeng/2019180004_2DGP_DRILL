from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_PLUS:
                    play_state.team += 1
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    play_state.team -= 1
                    game_framework.pop_state()
