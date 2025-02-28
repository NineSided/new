import pygame as pg
import moderngl as mgl
import sys

from model import Triangle, Cube
from camera import Camera

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        #initialize pygame
        pg.init()
        #window size
        self.WIN_SIZE = win_size
        #set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) #opengl 3.x
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3) #opengl x.3
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) #opengl core profile e.g: 3.3 core
        #create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.DOUBLEBUF | pg.OPENGL) #create window OPENGL: opengl-type window, DOUBLEBUF: double buffer
        #detect and use existing opengl context
        self.ctx = mgl.create_context()
        #create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        #camera
        self.camera = Camera(self)
        #scene
        self.scene = Cube(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def get_time(self):
        self.time = pg.time.get_ticks() / 1000

    def render(self):
        #clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #render scene
        self.scene.render()
        #swap buffers
        pg.display.flip()

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()