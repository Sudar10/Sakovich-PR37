import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget

kivy.require('1.9.1')

class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super(DrawingWidget, self).__init__(**kwargs)
        self.line_color = (1, 0, 0)
        self.line_width = 2
        self.bind(size=self._update_canvas, pos=self._update_canvas)

    def _update_canvas(self, instance, value):
        self.canvas.clear()

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.line_color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()

    def set_line_color(self, color):
        self.line_color = color

    def set_line_width(self, width):
        self.line_width = width

class DrawingApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        
        # Drawing Widget
        self.drawing_widget = DrawingWidget()
        
        # Control Panel
        control_panel = BoxLayout(size_hint_y=0.2)
        
        # Clear Button
        clear_button = Button(text='Очистить холст')
        clear_button.bind(on_press=self.clear_canvas)
        control_panel.add_widget(clear_button)
        
        # Color Picker
        color_picker = ColorPicker()
        color_picker.bind(color=self.on_color)
        control_panel.add_widget(color_picker)
        
        # Line Width Slider
        line_width_slider = Slider(min=1, max=10, value=2)
        line_width_slider.bind(value=self.on_line_width)
        control_panel.add_widget(line_width_slider)
        
        root.add_widget(control_panel)
        root.add_widget(self.drawing_widget)
        return root

    def clear_canvas(self, instance):
        self.drawing_widget.clear_canvas()

    def on_color(self, instance, value):
        self.drawing_widget.set_line_color(value)

    def on_line_width(self, instance, value):
        self.drawing_widget.set_line_width(value)

if __name__ == '__main__':
    DrawingApp().run()
