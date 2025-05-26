from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.core.window import Window
import random

class JuegoAdivinaNumero(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(20)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Fondo gris claro
        
        self.numero_secreto = random.randint(1, 50)
        self.intentos = 0
        
        # Título
        self.titulo = Label(
            text="¡Adivina el Número!",
            font_size=dp(32),
            size_hint_y=None,
            height=dp(70),
            color=(0.2, 0.2, 0.8, 1)  # Azul oscuro
        )
        
        # Instrucciones
        self.instrucciones = Label(
            text="Pensé un número entre 1 y 50.\n¿Podés adivinarlo?",
            font_size=dp(24),
            size_hint_y=None,
            height=dp(100),
            color=(0.3, 0.3, 0.3, 1)  # Gris oscuro
        )
        
        # Campo de entrada
        self.input_numero = TextInput(
            hint_text='Ingresa tu intento',
            multiline=False,
            font_size=dp(24),
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={'center_x': 0.5},
            input_filter='int',
            background_color=(1, 1, 1, 1),  # Blanco
            cursor_color=(0.2, 0.2, 0.8, 1),  # Azul oscuro
            padding=[dp(10), dp(10), dp(10), dp(10)]
        )
        self.input_numero.bind(on_text_validate=self.verificar_intento)
        
        # Botón Adivinar
        self.boton_adivinar = Button(
            text='¡ADIVINAR!',
            size_hint=(0.8, None),
            height=dp(60),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.2, 0.8, 1),  # Azul oscuro
            font_size=dp(24)
        )
        self.boton_adivinar.bind(on_press=self.verificar_intento)
        
        # Mensaje de resultado
        self.mensaje = Label(
            text="",
            font_size=dp(24),
            size_hint_y=None,
            height=dp(100),
            color=(0.3, 0.3, 0.3, 1)  # Gris oscuro
        )
        
        # Botón Reiniciar
        self.boton_reiniciar = Button(
            text='JUGAR DE NUEVO',
            size_hint=(0.8, None),
            height=dp(60),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 0.2, 1),  # Verde
            font_size=dp(24),
            opacity=0,
            disabled=True
        )
        self.boton_reiniciar.bind(on_press=self.reiniciar_juego)
        
        # Agregar widgets
        self.add_widget(self.titulo)
        self.add_widget(self.instrucciones)
        self.add_widget(self.input_numero)
        self.add_widget(self.boton_adivinar)
        self.add_widget(self.mensaje)
        self.add_widget(self.boton_reiniciar)
    
    def verificar_intento(self, instance):
        try:
            intento = int(self.input_numero.text)
            
            if intento < 1 or intento > 50:
                self.mensaje.text = "Por favor, ingresa un número entre 1 y 50"
                self.mensaje.color = (0.8, 0.2, 0.2, 1)  # Rojo
                self.input_numero.text = ""
                return
                
            self.intentos += 1
            
            if intento == self.numero_secreto:
                self.mensaje.text = f"¡Felicitaciones!\n¡Adivinaste el número en {self.intentos} intentos!"
                self.mensaje.color = (0.2, 0.6, 0.2, 1)  # Verde
                self.boton_adivinar.disabled = True
                self.boton_reiniciar.opacity = 1
                self.boton_reiniciar.disabled = False
            elif intento < self.numero_secreto:
                self.mensaje.text = "El número es más alto.\n¡Intenta de nuevo!"
                self.mensaje.color = (0.8, 0.2, 0.2, 1)  # Rojo
            else:
                self.mensaje.text = "El número es más bajo.\n¡Intenta de nuevo!"
                self.mensaje.color = (0.8, 0.2, 0.2, 1)  # Rojo
            
            self.input_numero.text = ""
        except ValueError:
            self.mensaje.text = "Por favor, ingresa un número válido"
            self.mensaje.color = (0.8, 0.2, 0.2, 1)  # Rojo
    
    def reiniciar_juego(self, instance):
        self.numero_secreto = random.randint(1, 50)
        self.intentos = 0
        self.mensaje.text = ""
        self.boton_adivinar.disabled = False
        self.boton_reiniciar.opacity = 0
        self.boton_reiniciar.disabled = True

class AdivinaNumeroApp(App):
    def build(self):
        return JuegoAdivinaNumero()

if __name__ == '__main__':
    AdivinaNumeroApp().run() 