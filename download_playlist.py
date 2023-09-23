from pytube import YouTube
from pytube import Playlist
import ssl
import random
import string

# Caracteres permitidos para generar el string aleatorio
caracteres_permitidos = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos

# Desactivar la verificación de certificados SSL
ssl._create_default_https_context = ssl._create_unverified_context

# URL de la playlist de YouTube que deseas descargar
playlist_url = "https://music.youtube.com/playlist?list=RDCLAK5uy_nX21_ZSVbClYkXhcLsVUEbABHn3ZqgCvs"

# Crea un objeto Playlist
playlist = Playlist(playlist_url)

# Itera a través de los videos de la playlist
for video_url in playlist.video_urls:
    # Crea un objeto YouTube para el video actual
    yt = YouTube(video_url)
    
    # Obtiene el título del video
    video_title = yt.title
    
    # Genera un string aleatorio de 3 caracteres para adicionar el nombre y evitar sobreescritura
    random_string = ''.join(random.choice(caracteres_permitidos) for _ in range(3))
    
    #video_stream = yt.streams.get_highest_resolution()
    video_stream = yt.streams.filter(only_audio=True,file_extension="mp4").first()
    
    print(video_stream)
    video_stream.download(output_path="music", filename=f"{video_title}___{random_string}.mp4")

    # Imprime el nombre del video descargado
    print(f"Descargando: {video_title}")