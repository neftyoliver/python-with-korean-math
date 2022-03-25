import moderngl as mgl
import moderngl_window

"""
모던 오픈지엘 라이브러리를 이용해 눈에 보이는 오브젝트를 그립니다.

NeftyShapes 클래스를 통해 인스턴스를 만들 수 있고 이 인스턴스를 통해
라이브러리에 들어갈 객체들을 관리할 수 있습니다. 
"""

object_vertex_shader = """
    #version 330
    
    void main(void)
    {
        gl_Position = vec4(0.0, 0.0, 0.5, 1.0);
    }
"""

object_fragment_shader = """
    #version 330
    
    out vec4 color;
    
    void main(void)
    {
        color = vec4(0.0, 0.8, 1.0, 1.0);
    }
"""



class Shape:
    """
        그릴 수 있는 단 하나의 유일한 도형입니다.
    """

    def __init__(self, frec, color: int):
        self.vertex = tuple(frec)
        self.r = color & 0xFF0000
        self.g = color & 0xFF00
        self.b = color & 0xFF

the_shape = None

class GLConfig(moderngl_window.WindowConfig):
    """
        그리기 위한 아주 최소한의 그래픽 시스템을 만듭니다.
    """
    vsync = False
    resizable = False
    gl_version = (3, 3)

    render_shape: callable = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ctx.program(vertex_shader=object_vertex_shader, fragment_shader=object_fragment_shader)
        self.shape = the_shape
        #TODO: Make shape renderable

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.2, 0.2, 0.2)
        self.ctx.enable(mgl.DEPTH_TEST)

        GLConfig.render_shape(self.ctx, )


class NeftyShapes:
    def render_shape(self, ctx: mgl.Context, vao: mgl.VertexArray):
        vao.render()

    def __init__(self):
        self.gl_window = GLConfig

    def run(self):
        moderngl_window.run_window_config(self.gl_window)


if __name__ == '__main__':
    app = NeftyShapes()

    app.run()
