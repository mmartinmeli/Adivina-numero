from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
import random

class JuegoAdivinaNumero(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.numero_secreto = random.randint(1, 50)
        self.intentos = 0
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear el layout principal con más espacio entre elementos
        layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(30),
            padding=dp(20)
        )

        # Título del juego - más grande y llamativo
        self.titulo = MDLabel(
            text="¡Adivina el Número!",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=dp(70),
            bold=True
        )

        # Instrucciones - texto más grande
        self.instrucciones = MDLabel(
            text="Pensé un número entre 1 y 50.\n¿Podés adivinarlo?",
            halign="center",
            font_style="H6",
            size_hint_y=None,
            height=dp(100)
        )

        # Campo para ingresar el número - más grande y fácil de tocar
        self.input_numero = MDTextField(
            hint_text="Ingresa tu intento",
            helper_text="Escribe un número entre 1 y 50",
            helper_text_mode="on_error",
            input_filter="int",
            size_hint_x=0.8,
            pos_hint={'center_x': 0.5},
            font_size=dp(24),
            on_text_validate=self.verificar_intento
        )

        # Botón para adivinar - más grande y visible
        self.boton_adivinar = MDRaisedButton(
            text="¡ADIVINAR!",
            pos_hint={'center_x': 0.5},
            size_hint=(0.8, None),
            height=dp(60),
            font_size=dp(24),
            on_release=self.verificar_intento
        )

        # Mensaje de resultado - más grande y visible
        self.mensaje = MDLabel(
            text="",
            halign="center",
            font_style="H6",
            size_hint_y=None,
            height=dp(100)
        )

        # Botón para reiniciar - más grande
        self.boton_reiniciar = MDRaisedButton(
            text="JUGAR DE NUEVO",
            pos_hint={'center_x': 0.5},
            size_hint=(0.8, None),
            height=dp(60),
            font_size=dp(24),
            opacity=0,
            disabled=True,
            on_release=self.reiniciar_juego
        )

        # Agregar widgets al layout
        layout.add_widget(self.titulo)
        layout.add_widget(self.instrucciones)
        layout.add_widget(self.input_numero)
        layout.add_widget(self.boton_adivinar)
        layout.add_widget(self.mensaje)
        layout.add_widget(self.boton_reiniciar)

        self.add_widget(layout)

    def verificar_intento(self, *args):
        try:
            intento = int(self.input_numero.text)
            
            # Validar que el número esté en el rango correcto
            if intento < 1 or intento > 50:
                self.mensaje.text = "Por favor, ingresa un número entre 1 y 50"
                self.input_numero.text = ""
                return
                
            self.intentos += 1

            if intento == self.numero_secreto:
                self.mensaje.text = f"¡Felicitaciones!\n¡Adivinaste el número en {self.intentos} intentos!"
                self.boton_adivinar.disabled = True
                self.boton_reiniciar.opacity = 1
                self.boton_reiniciar.disabled = False
            elif intento < self.numero_secreto:
                self.mensaje.text = "El número es más alto.\n¡Intenta de nuevo!"
            else:
                self.mensaje.text = "El número es más bajo.\n¡Intenta de nuevo!"

            self.input_numero.text = ""
        except ValueError:
            self.mensaje.text = "Por favor, ingresa un número válido"

    def reiniciar_juego(self, *args):
        self.numero_secreto = random.randint(1, 50)
        self.intentos = 0
        self.mensaje.text = ""
        self.boton_adivinar.disabled = False
        self.boton_reiniciar.opacity = 0
        self.boton_reiniciar.disabled = True

class AdivinaNumeroApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.accent_palette = "Purple"
        return JuegoAdivinaNumero()

if __name__ == '__main__':
    AdivinaNumeroApp().run() 