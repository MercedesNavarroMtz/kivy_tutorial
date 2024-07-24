import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class MainApp(App):
    def build(self):
        self.title = "GUI tutorial"
        self.screen_manager = ScreenManager()

        self.main_screen = Screen(name='main')
        self.data_screen = Screen(name='data')

        main_layout = BoxLayout(orientation='vertical', padding=2, spacing=0, pos_hint={'center_x': 0.75, 'center_y': 0.5})
        horizontal_layout = BoxLayout(orientation='horizontal', spacing=9)
        horizontal_layout.add_widget(self.create_button('¡Empezar  tutorial!', (300, 190), (1, 0, 0, 1), '20sp', self.on_start_button_pressed))
        horizontal_layout.add_widget(self.create_button('¡Finalizar  tutorial!', (300, 190), (1, 0, 0, 1), '20sp', self.on_start_button_pressed2))
        horizontal_layout.add_widget(self.create_button('Comentarios', (350, 190), (1, 1, 1, 1), '20sp', self.on_save_comment_pressed))

        vertical_layout = BoxLayout(orientation='vertical', spacing=5, pos_hint={'center_x': 0.67, 'center_y': 2.5})
        vertical_layout.add_widget(self.create_button('Ver código', (250, 100), (1, 0, 0, 1), '20sp', self.on_start_button_pressed3))
        vertical_layout.add_widget(self.create_button('Sobre Kivy', (250, 100), (1, 0, 0, 1), '20sp', self.on_start_button_pressed4))


        main_layout.add_widget(horizontal_layout)
        main_layout.add_widget(vertical_layout)

        self.main_screen.add_widget(main_layout)
        self.screen_manager.add_widget(self.main_screen)

        self.data_layout = BoxLayout(orientation='vertical')
        self.input_text2 = TextInput(size_hint_y=None, height=110, font_size='18sp')
        save_button = Button(text='Guardar', size_hint_y=None, height=60, font_size='18sp')
        save_button.bind(on_press=self.save_comment)

        self.data_layout.add_widget(self.input_text2)
        self.data_layout.add_widget(save_button)

        self.data_screen.add_widget(self.data_layout)
        self.screen_manager.add_widget(self.data_screen)

        return self.screen_manager

    def create_button(self, text, size, background_color, font_size, callback):
        button = Button(text=text, size_hint=(None, None), size=size, background_color=background_color, font_size=font_size)
        button.bind(on_press=callback)
        return button

    def on_save_comment_pressed(self, instance):
        self.screen_manager.current = 'data'

    def save_comment(self, instance):
        val2 = self.input_text2.text
        with open('comment.txt', 'a') as file:
            now = datetime.datetime.now()
            formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'Comentario: {formatted_time} {val2}\n')

        # Volver a la pantalla principal después de guardar el comentario
        self.screen_manager.current = 'main'

    def on_start_button_pressed(self, instance):
        self.show_input_popup('datos personales','tutorial.txt', ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30'], width= 53)
        now = datetime.datetime.now()
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        with open('tutorial.txt', 'a') as file:
            file.write('Datos personales ' + formatted_time + '\n')
        
    def on_start_button_pressed3(self, instance):
        self.popup_box = BoxLayout(orientation='vertical', padding=25, spacing=10)
        python_code= '''
        def create_button(self, text, size, background_color, font_size, callback):
            button = Button(text=text, size_hint=(None, None), size=size, background_color=background_color, font_size=font_size)
            button.bind(on_press=callback)
            return button

        horizontal_layout = BoxLayout(orientation='horizontal', spacing=9)
        horizontal_layout.add_widget(self.create_button('¡Start the tutorial!', (300, 190), (1, 0, 0, 1), '20sp', self.on_start_button_pressed))
        horizontal_layout.add_widget(self.create_button('¡Finish the tutorial!', (300, 190), (1, 0, 0, 1), '20sp', self.on_start_button_pressed2))
        horizontal_layout.add_widget(self.create_button('Comments', (350, 190), (1, 1, 1, 1), '20sp', self.on_save_comment_pressed))

                    '''
        code_label = Label(text=python_code, size_hint_y=None, height=200, font_size='15sp', halign='left', valign='top')
        code_label.text_size = (650, None)
        code_label.bind(size=code_label.setter('text_size'))
        
        self.popup_box.add_widget(code_label)
        
        self.popup = Popup(title='Code for create a button', content=self.popup_box, size_hint=(None, None), size=(1200, 300), title_size='20sp')
        self.popup.open()

    def on_start_button_pressed4(self, instance):
        self.popup_box = BoxLayout(orientation='vertical', padding=25, spacing=10)
        text= '''
        Kivy es una biblioteca de software de código abierto para el desarrollo rápido de aplicaciones con interfaces de usuario novedosas.
        El objetivo principal del marco Kivy es optimizar la creación de interfaces de usuario (UI). 
        Ofrece una interfaz de usuario (NUI) natural para las operaciones.
        Es una herramienta flexible para desarrollar aplicaciones móviles debido a su amplia colección de configuraciones de interfaz de usuario.
        Para más información: https://kivy.org/doc/stable/

                    '''
        code_label = Label(text=text, size_hint_y=None, height=150, font_size='15sp', halign='left', valign='top')
        code_label.text_size = (650, None)
        code_label.bind(size=code_label.setter('text_size'))
        
        self.popup_box.add_widget(code_label)
        
        self.popup = Popup(title='Que es Kivy?', content=self.popup_box, size_hint=(None, None), size=(1200, 300), title_size='20sp')
        self.popup.open()


    def show_input_popup(self, event_name, reg, feed_speed_ranges, width):
        self.popup_box = BoxLayout(orientation='vertical', padding=25, spacing=40)

        feed_speed_label_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=10, spacing=8)
        feed_speed_label = Label(text='Edad', size_hint_y=None, height=20, font_size='20sp')
        feed_speed_label_layout.add_widget(feed_speed_label)

        self.feed_speed_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=70, spacing=10)
        self.feed_speed_value = ''
        self.feed_speed_buttons = []  

        for range_value in feed_speed_ranges:
            btn = Button(text=range_value, size_hint_x=None, width=width, height=70, font_size='18sp')
            btn.bind(on_press=lambda instance, val=range_value: self.set_feed_speed(val, instance))
            self.feed_speed_layout.add_widget(btn)
            self.feed_speed_buttons.append(btn)

        self.input_text2 = TextInput(hint_text='Nombre', size_hint_y=None, height=70, font_size='18sp')
        self.input_text4 = Spinner(text='Correo electrónico', values=('rosamartinez@ctnaval.com', 'joseantoniogarcia@ctnaval.com', 'jcarlossanz@ctnaval.com'), size_hint_y=None, height=150, font_size='18sp')

        save_button = Button(text='Guardar', size_hint_y=None, height=70, font_size='18sp')
        save_button.bind(on_press=lambda instance: self.on_save_button_pressed(self.feed_speed_value,self.input_text2.text,self.input_text4.text))
        
        self.popup_box.add_widget(self.input_text2)
        self.popup_box.add_widget(feed_speed_label_layout)
        self.popup_box.add_widget(self.feed_speed_layout)
        self.popup_box.add_widget(self.input_text4)
        self.popup_box.add_widget(save_button)

        self.popup = Popup(title='Introducir ' + event_name, content=self.popup_box, size_hint=(None, None), size=(700, 675), title_size='20sp')
        self.popup.open()

    def set_feed_speed(self, value, instance):
        self.feed_speed_value = value
        
        for btn in self.feed_speed_buttons:
            if btn == instance:
                btn.background_color = (1, 1, 0, 1) 
            else:
                btn.background_color = (1, 1, 1, 1) 


    def on_save_button_pressed(self, edad, name, email):
        self.popup.dismiss()

        self.popup_box = BoxLayout(orientation='vertical', padding=25, spacing=40)

        self.input_text2 = TextInput(hint_text='¿En qué ciudad europea está el Atomium?', size_hint_y=None, height=70, font_size='18sp')
        self.input_text4 = Spinner(text='¿Cuánto años duró “La Guerra de los Cien Años”?', values=('102', '100', '116', '97'), size_hint_y=None, height=150, font_size='18sp')
        
        save_button = Button(text='Guardar', size_hint_y=None, height=70, font_size='18sp')
        save_button.bind(on_press=lambda instance: self.on_button_pressed(self.input_text2.text, self.input_text4.text, name, edad,email))

        self.popup_box.add_widget(self.input_text2)
        self.popup_box.add_widget(self.input_text4)
        self.popup_box.add_widget(save_button)

        self.popup = Popup(title='Responde a las siguientes preguntas de cultura general', content=self.popup_box, size_hint=(None, None), size=(700, 500), title_size='20sp')
        self.popup.open()


    def on_button_pressed(self, resp1, resp2, nombre, edad, email, ):
        with open('tutorial.txt', 'a') as file:
            file.write(f'Nombre: {nombre}, edad {edad} con email: {email} ha respondido  {resp1} y {resp2} \n')
        if resp1.lower() == ('bruselas' or 'Bruselas') and resp2 == '116':
            self.show_correct_response_popup()
        else:
            self.show_incorrect_response_popup()

        self.popup.dismiss()  

    def show_correct_response_popup(self):
        popup_box = BoxLayout(orientation='vertical', padding=25, spacing=10)
        message_label = Label(text='Respuesta guardada', size_hint_y=None, height=100, font_size='20sp')
        close_button = Button(text='Cerrar', size_hint_y=None, height=50, font_size='18sp')
        close_button.bind(on_press=lambda instance: self.correct_response_popup.dismiss())

        popup_box.add_widget(message_label)
        popup_box.add_widget(close_button)

        self.correct_response_popup = Popup(title='¡Correcto!', content=popup_box, size_hint=(None, None), size=(300, 270), title_size='20sp')
        self.correct_response_popup.open()

    def show_incorrect_response_popup(self):
        popup_box = BoxLayout(orientation='vertical', padding=25, spacing=10)
        message_label = Label(text='Respuesta guardada', size_hint_y=None, height=100, font_size='20sp')
        close_button = Button(text='Cerrar', size_hint_y=None, height=50, font_size='18sp')
        close_button.bind(on_press=lambda instance: self.correct_response_popup.dismiss())

        popup_box.add_widget(message_label)
        popup_box.add_widget(close_button)

        self.correct_response_popup = Popup(title=' Incorrecto :( ', content=popup_box, size_hint=(None, None), size=(300, 270), title_size='20sp')
        self.correct_response_popup.open()

    def on_save_comment_pressed(self, instance):        
        self.popup_box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.popup_box.size_hint = (None, None)
        self.popup_box.width = 600  
        self.popup_box.height = 300  
        self.input_text2 = TextInput( size_hint_y=None, height=110, font_size = '18sp')

        save_button = Button(text='Guardar', size_hint_y=None, height=60, font_size='18sp')
        save_button.bind(on_press=self.save_comment)
 
        self.popup_box.add_widget(self.input_text2)
        self.popup_box.add_widget(save_button)

        self.popup = Popup(title='Comentarios', content=self.popup_box, size_hint=(None, None), size=(650, 330), title_size = '20sp')
        self.popup.open()


    def save_comment(self, instance):
        val2 = self.input_text2.text
        with open('tutorial.txt', 'a') as file:
            now = datetime.datetime.now()
            formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
            # file.write('Incidencia ' + formatted_time + '\n')
            file.write(f'Comentario: {formatted_time} {val2}\n')

        self.popup.dismiss() 


    def on_start_button_pressed2(self, instance):
        popup_box = BoxLayout(orientation='horizontal', padding=10, spacing=10)
        message_label = Label(text='Enlace GitHub', size_hint_y=None, height=100, font_size='20sp')
        popup_box.add_widget(message_label)

        self.popup = Popup(title='Código disponible en GitHub en el siguiente enlace', content=popup_box, size_hint=(None, None), size=(430, 250), title_size = '20sp')

        self.popup.open()


if __name__ == '__main__':
    MainApp().run()
