import PySimpleGUI as sg
import json
from experta import Fact, Rule, KnowledgeEngine

with open('libros.json', 'r') as file:
    datos = json.load(file)



class Book(Fact):
  """Información sobre el videojuego."""
  pass

class BookRecommendationSystem(KnowledgeEngine):    
    @Rule(Book(genre='Fantasia', autor='J.R.R. Tolkien'))
    def recommend_action_Book(self):
        print("Recomendamos el libro 'el señor de los anillos'")
        window['-TEXT-'].update("Recomendamos el libro 'el señor de los anillos'")

    @Rule(Book(genre='Realismo mágico', autor='Gabriel Garcia Marquez'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Cien años de soledad'")

    @Rule(Book(genre='Distopia', autor='George Orwell'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro '1984'")

    @Rule(Book(genre='Ficcion clasica', autor='Harper Lee'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Matar a un ruiseñor'")

    @Rule(Book(genre='Romance', autor='Jane Austen'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Orgullo y prejuicio'")

    @Rule(Book(genre='Novela picaresca', autor='Miguel de Cervantes'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Don Quijote de la Mancha'")

    @Rule(Book(genre='Fantasia', autor='J.K. Rowling'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Harry Potter y la piedra filosofal'")

    @Rule(Book(genre='Epopeya', autor='Homero'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'La Odisea'")
        
    @Rule(Book(genre='Ficcion modernista', autor='Marcel Proust'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'En busca del tiempo perdido'")
        
    @Rule(Book(genre='Novela psicologica', autor='Fiodor Dostoievski'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Crimen y castigo'")

    @Rule(Book(genre='Ficcion modernista', autor='James Joyce'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Ulises'")
        
    @Rule(Book(genre='Tragedia', autor='William Shakespeare'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Romeo y Julieta'")
        
    @Rule(Book(genre='Ficcion abssurda', autor='Franz Kafka'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'La metamorfosis'")
        
    @Rule(Book(genre='Novela Historica', autor='Victor Hugo'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Los miserables'")
        
    @Rule(Book(genre='Ficcion moderna', autor='F. Scott Fitzgerald'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El gran Gatsby'")

    @Rule(Book(genre='Fabula', autor='Antoine de Saint-Exupery'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El principito'")
        
    @Rule(Book(genre='Aventura', autor='Herman Melville'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Moby Dick'")
        
    @Rule(Book(genre='Ficcion gotica', autor='Oscar Wilde'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El retrato de Dorian Gray'")
        
    @Rule(Book(genre='Aventura', autor='Robert Louis Stevenson'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'La isla del tesoro'")
        
    @Rule(Book(genre='Fantasia', autor='J.R.R. Tolkien'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El Hobbit'")
        
    @Rule(Book(genre='Novela realista', autor='Leon Tolkien'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Anna Karenina'")
        
    @Rule(Book(genre='Terror gotico', autor='Bram Stoker'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Drácula'")
        
    @Rule(Book(genre='Novela negra', autor='Camila Lackberg'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Crimen en directo'")
        
    @Rule(Book(genre='Misterio historico', autor='Umberto Eco'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El nombre de la rosa'")
        
    @Rule(Book(genre='Thriller religioso', autor='Dan Brown'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El código Da Vinci'")
        
    @Rule(Book(genre='Novela gotica', autor='Carlos Ruiz Zafon'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'La sombra del viento'")

    @Rule(Book(genre='Ciencia ficcion', autor='Orson Scott Card'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El juego de Ender'")
        
    @Rule(Book(genre='Thriller', autor='Stieg Larsson'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Los hombres que no amaban a las mujeres'")
        
    @Rule(Book(genre='Ficcion espiritual', autor='Paulo Coelho'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El alquimista'")
        
    @Rule(Book(genre='Novela de aventuras', autor='Maark Twain'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Las aventuras de Tom Sawyer'")
        
    @Rule(Book(genre='Historica', autor='Ken Follet'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Los pilares de la Tierra'")

    @Rule(Book(genre='Divulgacion historica', autor='Yuval Noah Harari'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'Sapiens: De animales a dioses'")
        
    @Rule(Book(genre='Historica', autor='Noah Gordon'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El médico'")
        
    @Rule(Book(genre='Historica', autor='Ildefonso Falcones'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'La catedral del mar'")
        
    @Rule(Book(genre='ficcion de supervivencia', autor='William Golding'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El señor de las moscas'")
            
    @Rule(Book(genre='Ciencia ficcion distopica', autor='Margaret Atwood'))
    def recommend_action_Book(self):
        window['-TEXT-'].update("Recomendamos el libro 'El cuento de la criada'")

layout = [
   [sg.Text("Ingrese el género del libro")],
   [sg.Input(key='-GENRE-')],
   [sg.Text("Ingrese el autor del libro")],
   [sg.Input(key='-AUTOR-')],
   [sg.Text('')],
   [sg.Text('', key='-TEXT-', font=('Helvetica', 12), text_color='blue', background_color='white')],
   [sg.Button('Recomendar'), sg.Button('Salir')]
]

window = sg.Window('Sistema de recomendación de libros', layout)

while True:
   event, values = window.read()
   if event == sg.WINDOW_CLOSED or event == 'Salir':
       break
   elif event == 'Recomendar':
       window['-TEXT-'].update("no tenemos recomendaciones :(")
       genre = values['-GENRE-']
       autor = values['-AUTOR-']
    #    Book = Book(genre=genre, autor=autor)
       engine = BookRecommendationSystem()
       engine.reset()
       engine.declare(Book(genre=genre, autor=autor))
       engine.run()

window.close()
