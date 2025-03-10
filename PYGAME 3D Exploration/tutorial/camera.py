import glm

FOV = 50
NEAR = 0.1
FAR = 100

class Camera:  
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        #view matrix
        self.m_view = self.get_veiw_matrix()
        #projection matrix
        self.m_proj = self.get_projecion_matrix()

    def get_veiw_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0, 0, 0), self.up)

    def get_projecion_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)