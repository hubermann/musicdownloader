from pytube import YouTube
import ssl

# Desactivar la verificación de certificados SSL
ssl._create_default_https_context = ssl._create_unverified_context

# URL del video de YouTube que quieres descargar
video_url = "https://www.youtube.com/watch?v=7nJRGARveVc"

# Crea un objeto YouTube
yt = YouTube(video_url)

# Selecciona la mejor corriente de audio (en formato MP4)
audio_stream = yt.streams.filter(only_audio=True).last()

# Imprime el título del video
print("Título del video:", yt.title)


audio_stream.download(output_path="music", filename=yt.title+".mp4")