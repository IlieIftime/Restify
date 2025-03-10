from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class GradientBackgroundWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            # Criando gradiente dividido em várias camadas para dar efeito suave
            # Cores do gradiente azul
            color_top = Color(0.4, 0.8, 1, 1)  # Azul claro
            color_bottom = Color(0, 0, 1, 1)  # Azul escuro

            # Retângulo de cor azul claro
            self.top_rect = Rectangle(size=self.size, pos=self.pos)
            color_top
            self.top_rect.size = (self.width, self.height / 2)

            # Retângulo de cor azul escuro
            self.bottom_rect = Rectangle(size=self.size, pos=self.pos)
            color_bottom
            self.bottom_rect.pos = (0, self.height / 2)
            self.bottom_rect.size = (self.width, self.height / 2)

    def on_size(self, *args):
        # Atualiza os tamanhos e posições dos retângulos para acompanhar o redimensionamento
        self.top_rect.size = (self.width, self.height / 2)
        self.bottom_rect.pos = (0, self.height / 2)
        self.bottom_rect.size = (self.width, self.height / 2)


class MyApp(App):
    def build(self):
        return GradientBackgroundWidget()


if __name__ == '__main__':
    MyApp().run()
