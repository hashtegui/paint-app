from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button


class PaintWidget(Widget):
    def on_touch_down(self, touch):
        print('Clicando o mouse')
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        return super().on_touch_move(touch)


class PaintApp(App):
    def build(self):
        parent = Widget()
        self.paint = PaintWidget()
        btnLimpa = Button(text='Limpar')
        btnLimpa.bind(on_release=self.limpa_canvas)
        parent.add_widget(self.paint)
        parent.add_widget(btnLimpa)

        return parent

    def limpa_canvas(self, obj):
        print('Limpou a tela')
        self.paint.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()
