import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Escuchar el microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #Almacenar el recognizer en variable
    r=sr.Recognizer()
    #Configurar el microfono
    with sr.Microphone() as origen:
        #Tiempo de espera de escucha
        r.pause_threshold=0.8
        #Informar que empezo la grabacion
        print("Ya se puede hablar")
        #Guardar lo que se escucha como audio
        audio=r.listen(origen)
        #Manejo de errores
        try:
            #Buscar en google lo que escucho
            pedido=r.recognize_google(audio,language="es-col")
            #Prueba de que pudo transformar la voz en texo
            print("Dijo: "+pedido)
            #Devolver lo que se pidio, para usarlo luego
            return pedido
        #En caso de no comprender el audio
        except sr.UnknownValueError:
            #Prueba de que no comprendio el audio
            print("No se entendio")
            #Devolver error
            return "Sigo esperando"
        #En caso de no resolver el pedido
        except sr.RequestError:
            #Prueba de que no resolvio el pedido
            print("No hay servicio")
            #Devolver error
            return "Sigo esperando"
        #Error inesperado
        except:
            #Prueba de error inesperado
            print("Algo salio mal")
            #Devolver error
            return "Sigo esperando"

#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #Opciones de voz
    id1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
    id2="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    #Encender el motor de pyttsx3
    engine=pyttsx3.init()
    engine.setProperty('voice',id1)
    #Pronunciar mensaje
    engine.say(mensaje)
    #Ejecuta el mensaje y espera
    engine.runAndWait()

#Informar el dia de la semana
def pedir_dia():
    #Crear variable con datos de hoy
    dia=datetime.date.today()
    print(dia)
    #Crear variable para el dia de la semana
    dia_semana=dia.weekday()
    print(dia_semana)
    #Diccionoario con nombres de dias
    dias={0:'Lunes',
                1:'Martes',
                2:'Miércoles',
                3:'Jueves',
                4:'Viernes',
                5:'Sábado',
                6:'Domingo'}
    #Decir el dia de la semana
    hablar(f'Hoy es, {dias[dia_semana]} del {dia}')

#Informar hora del dia
def pedir_hora():
    #Crear variable con datos de la hora
    hora=datetime.datetime.now()
    hora=f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)
    #Decir la hora
    hablar(hora)

#Funcion saludo inicial
def saludo_inicial():
    #Crear variable con datos de hora
    hora=datetime.datetime.now()
    if hora.hour < 6 or hora.hour>20:
        momento='Buenas noches David'
    elif 6<=hora.hour<13:
        momento='Buenos dias David'
    else:
        momento='Buenas tardes David'
    #Decir el saludo
    hablar(f'{momento}, soy Star, su asistente personal. En que cosa lo puedo ayudar')

#Funcion central del asistente
def pedir_cosas():
    #Activar el saludo inicial
    saludo_inicial()
    #Variable de corte
    comenzar=True
    #Loop central
    while comenzar:
        #Activar el microfono y guardar el pedido en un string
        pedido=transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Estoy ejecutando la orden')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Enseguida')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'terminar ejecución' in pedido:
            hablar('Terminando mis labores, que tengas buen día David')
            break
        elif 'buscar en wikipedia' in pedido:
            hablar('Lo estoy buscando')
            pedido=pedido.replace('buscar en wikipedia','')
            wikipedia.set_lang('es')
            resultado=wikipedia.summary(pedido,sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'buscar en internet' in pedido:
            hablar('Lo estoy buscando')
            pedido=pedido.replace('buscar en internet','')
            pywhatkit.search(pedido)
            hablar('Encontre la siguiente información')
            continue
        elif 'reproducir' in pedido:
            hablar('Enseguida reprodusco el vídeo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion=pedido.split('de')[-1].strip()
            cartera={'apple':'APPL',
                     'amazon':'AMZN',
                     'google':'GOOGL'}
            try:
                accion_buscada=cartera[accion]
                accion_buscada=yf.Ticker(accion_buscada)
                precio_actual=accion_buscada.info['regularMarketPrice']
                hablar(f'Encontre la accion, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("No he podido encontrar la acción")

pedir_cosas()