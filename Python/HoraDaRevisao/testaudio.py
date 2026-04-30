import simpleaudio as sa

print("Iniciando o som...")
wave_obj = sa.WaveObject.from_wave_file("alarme.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
print("Som finalizado.")
