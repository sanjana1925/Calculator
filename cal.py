from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
class Calculator(GridLayout):
 def _init_(self, **kwargs):
 super(Calculator, self)._init_(**kwargs)
 self.cols = 4
 self.display = Button(text="0", font_size=40)
 self.add_widget(self.display)
 self.buttons = [
 "7", "8", "9", "/",
 "4", "5", "6", "*",
 "1", "2", "3", "-",
 "C", "0", "=", "+"
 ]
 for button_label in self.buttons:
 button = Button(text=button_label, font_size=40)
 button.bind(on_release=self.on_button_press)
 self.add_widget(button)
 def on_button_press(self, instance):
 current_text = self.display.text
 button_text = instance.text
 if button_text == "C":
 self.display.text = "0"
 elif button_text == "=":
 try:
 self.display.text = str(eval(current_text))
 except:
 self.display.text = "Error"
 else:
 if current_text == "0":
 self.display.text = button_text
 else:
 self.display.text = current_text + button_text
class CalculatorApp(App):
 def build(self):
 return Calculator()
