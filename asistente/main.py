import sys
sys.path.append('noticias')
sys.path.append('tts')
import noticias as nt
import tts as vs

# text = ['Pronuinciar este texto', 'y este otro texto mas']
# text = '. '.join(text)

result_noticias = nt.buscarNoticias()
text = 'Noticias: ' + '. '.join(result_noticias)
vs.simpleTTS(text, 'play')
# print(result_noticias)
