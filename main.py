import random
from time import sleep
from gtts import gTTS
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Miguel, Arturo, Gael
if __name__ == '__main__':
    loteria = {
        1: 'Artículo 1. Convivencia',
        2: 'Artículo 1. Universidad de Guadalajara',
        3: 'Artículo 1. Valores Éticos',
        4: 'Artículo 2. Constitución Política',
        5: 'Artículo 2. Derechos Humanos',
        6: 'Artículo 2. México',
        7: 'Artículo 3. Comunidad Universitaria',
        8: 'Artículo 4. Capacidades',
        9: 'Artículo 4. Diálogo',
        10: 'Artículo 4. Educación para la Paz',
        11: 'Artículo 4. El Desarrollo Sustentable',
        12: 'Artículo 4. La Democracia',
        13: 'Artículo 4. La Diversidad',
        14: 'Artículo 4. Recursos Naturales',
        15: 'Artículo 4. Comunidad',
        16: 'Artículo 4. Cooperación',
        17: 'Artículo 4. Legalidad',
        18: 'Artículo 4. Libertad',
        19: 'Artículo 4. Pensamiento',
        20: 'Artículo 4. Respeto',
        21: 'Artículo 4. Responsabilidad',
        22: 'Artículo 4. Solidaridad',
        23: 'Artículo 4. Igualdad',
        24: 'Artículo 4. Profesionalismo',
        25: 'Artículo 4. Dignidad',
        26: 'Artículo 4. Ecuanimidad',
        27: 'Artículo 4. Equidad',
        28: 'Artículo 4. Honestidad',
        29: 'Artículo 4. Imparcialidad',
        30: 'Artículo 4. Justicia',
        31: 'Artículo 4. Rectitud',
        31: 'Artículo 5. Conducta',
        32: 'Artículo 5. Contraloria general',
        33: 'Artículo 5. Ética',
        34: 'Artículo 5. Normatividad Universitaria',
        36: 'Artículo 5. Prevención de conflictos',
        37: 'Artículo Transitorio. Aplicación código de ética',
        38: 'Artículo Transitorio. Código de ética', 
        39: 'Artículo Transitorio. Ley orgánica',
        40: 'Artículo Transitorio. Gaceta Universitaria', 
        41: 'Artículo Transitorio. Consejo Universitario',
        42: 'Artículo Transitorio. Códigos de conducta'
    }
    claves = list(loteria.keys())

    """imagenes = []
    for numero in loteria:
        imagenes.append(f'{numero}. {loteria.get(numero)}.png')
    """

    while loteria:
        key = random.choice(claves)
        img = loteria.get(key)
        carta = loteria.pop(key)
        claves.remove(key)

        image = f'{img}.png'
        print(carta)

        tts = gTTS(carta, lang='es')
        tts.save('sound.mp3')

        os.system('sound.mp3')

        img = mpimg.imread(f'cartas/{image}')
        imgplot = plt.imshow(img)
        
        plt.show(block=False)
        plt.pause(4)
        plt.close()

