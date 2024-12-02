import os
import random
from video.create_video import create_video

audios_homero_path = "audios_homero"
gameplays_path = "resources/videos"
transcript_paths = "transcripts_homero"
homero_foto_path = "resources/images/homero"

def create_video_homero():
    audios_homero = os.listdir(audios_homero_path)
    transcripts_homero = os.listdir(transcript_paths)
    gameplays = os.listdir(gameplays_path)
    
    for audio in audios_homero:
        for transcript in transcripts_homero:
            if audio.split(".wav")[0] == transcript.split(".json")[0] + "_RVC_1":
                gameplay_path = random.choice(gameplays)
                homero_foto = random.choice(os.listdir(homero_foto_path))
                
                absolute_gameplay_path = gameplays_path + "/" + gameplay_path
                absolute_audio_path = audios_homero_path + "/" + audio
                absolute_transcript_path = transcript_paths + "/" + transcript
                absolute_foto_path = homero_foto_path + "/" + homero_foto
                
                name_of_video = audio.split(".wav")[0]
                
                create_video(absolute_gameplay_path,absolute_audio_path,absolute_transcript_path,absolute_foto_path,name_of_video)

    print(audios_homero)
    print(transcripts_homero)

if __name__ == "__main__":
    create_video_homero()
# create_video_homero()