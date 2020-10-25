import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock


class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.minutes = 25
        self.seconds = 0
        self.counter = 0

        self.submit = Button(text="Click to Start\n- Pomodoro -", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        self.clear_widgets()
        self.Label1 = self.add_widget(Label(text='%02d:%02d' % (self.minutes, self.seconds),
                                            font_size=250,
                                            pos_hint={'center_x': .5, 'center_y': .5}))
        self.timer = Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        if self.seconds > 0:
            self.seconds = self.seconds - 1
            self.clear_widgets()
            self.Label1 = self.add_widget(Label(text='%02d:%02d' % (self.minutes, self.seconds),
                                                font_size=250,
                                                pos_hint={'center_x': .5, 'center_y': .5}))
        elif self.minutes > 0:
            self.minutes = self.minutes - 1
            self.seconds = 59
            self.clear_widgets()
            self.Label1 = self.add_widget(Label(text='%02d:%02d' % (self.minutes, self.seconds),
                                                font_size=250,
                                                pos_hint={'center_x': .5, 'center_y': .5}))
        else:
            self.counter = self.counter + 1
            self.count()

    def count(self, *args):
        self.minutes = 25
        self.seconds = 0
        self.clear_widgets()
        self.Label1 = self.add_widget(Label(text='COMPLETED',
                                            font_size=40,
                                            pos_hint={'center_x': .5, 'center_y': .5}))
        self.Button2 = Button(text="Pomodoro's Completed:" + str(self.counter))
        self.Button2.bind(on_press=self.pressed)
        self.add_widget(self.Button2)
        self.timer.cancel()


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
