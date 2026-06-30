from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder

# Diseño de la interfaz en lenguaje KV integrado
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'
    md_bg_color: 0.1, 0.1, 0.1, 1  # Fondo oscuro elegante

    # Pantalla de visualización de resultados
    MDLabel:
        id: pantalla
        text: "0"
        halign: "right"
        valign: "center"
        font_style: "H3"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        size_hint_y: 0.25

    # Rejilla de botones (4 columnas)
    MDGridLayout:
        cols: 4
        spacing: '10dp'
        size_hint_y: 0.75

        # Fila 1
        MDRoundFlatButton:
            text: "C"
            text_color: 1, 0.3, 0.3, 1
            line_color: 1, 0.3, 0.3, 1
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.limpiar()
        MDRoundFlatButton:
            text: "("
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('(')
        MDRoundFlatButton:
            text: ")"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar(')')
        MDRoundFlatButton:
            text: "/"
            text_color: 0.2, 0.6, 1, 1
            line_color: 0.2, 0.6, 1, 1
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('/')

        # Fila 2
        MDRoundFlatButton:
            text: "7"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('7')
        MDRoundFlatButton:
            text: "8"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('8')
        MDRoundFlatButton:
            text: "9"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('9')
        MDRoundFlatButton:
            text: "*"
            text_color: 0.2, 0.6, 1, 1
            line_color: 0.2, 0.6, 1, 1
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('*')

        # Fila 3
        MDRoundFlatButton:
            text: "4"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('4')
        MDRoundFlatButton:
            text: "5"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('5')
        MDRoundFlatButton:
            text: "6"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('6')
        MDRoundFlatButton:
            text: "-"
            text_color: 0.2, 0.6, 1, 1
            line_color: 0.2, 0.6, 1, 1
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('-')

        # Fila 4
        MDRoundFlatButton:
            text: "1"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('1')
        MDRoundFlatButton:
            text: "2"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('2')
        MDRoundFlatButton:
            text: "3"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('3')
        MDRoundFlatButton:
            text: "+"
            text_color: 0.2, 0.6, 1, 1
            line_color: 0.2, 0.6, 1, 1
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('+')

        # Fila 5
        MDRoundFlatButton:
            text: "0"
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('0')
        MDRoundFlatButton:
            text: "."
            font_size: '24sp'
            size_hint: 1, 1
            on_press: app.presionar('.')
        MDRoundFlatButton:
            text: "="
            md_bg_color: 0.2, 0.6, 1, 1
            text_color: 1, 1, 1, 1
            font_size: '24sp'
            size_hint: 2, 1  # Ocupa el espacio restante en la fila
            on_press: app.calcular()
'''

class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def presionar(self, boton):
        pantalla = self.root.ids.pantalla
        if pantalla.text == "0" or pantalla.text == "Error":
            pantalla.text = str(boton)
        else:
            pantalla.text += str(boton)

    def limpiar(self):
        self.root.ids.pantalla.text = "0"

    def calcular(self):
        pantalla = self.root.ids.pantalla
        try:
            # Evalúa matemáticamente la cadena de texto de forma segura
            resultado = str(eval(pantalla.text))
            # Si el resultado termina en .0 lo dejamos como entero visualmente
            if resultado.endswith('.0'):
                resultado = resultado[:-2]
            pantalla.text = resultado
        except Exception:
            pantalla.text = "Error"

if __name__ == '__main__':
    CalculadoraApp().run()