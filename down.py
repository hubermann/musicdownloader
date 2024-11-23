import yt_dlp

# URL de la playlist de YouTube
# playlist_url = "https://music.youtube.com/playlist?list=RDCLAK5uy_nX21_ZSVbClYkXhcLsVUEbABHn3ZqgCvs"

playlist_url = "https://music.youtube.com/playlist?list=PLvH0FyPdm2j33aFu1ryt-it-AK0PE427o"
# Configuración de yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',  # Descargar la mejor calidad de audio disponible
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Convertir a MP3
        'preferredquality': '320',  # Calidad máxima (320 kbps)
    }],
    'outtmpl': 'music/%(title)s.%(ext)s',  # Ruta de salida
    'ignoreerrors': True,  # Ignorar errores en videos individuales
}

# Descargar la playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
