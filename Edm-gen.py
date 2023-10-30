Import the libraries
import librosa # for audio processing import magenta # for music generation import numpy as np # for numerical operations import random # for randomness

Define the subgenres and their descriptions and elements
subgenres = [“House”, “Electro House”, “Dub”, “Trap”, “Glitch-hop”, “Techno”, “Trance”] descriptions = [“A genre of EDM that originated in Chicago in the early 1980s. It is characterized by a 4/4 beat, a prominent bassline, and the use of electronic instruments such as synthesizers, drum machines, and samplers.”, “A subgenre of house music that emerged in the late 1990s and early 2000s. It combines elements of electro, techno, and big beat. It is known for its distorted and aggressive sound, heavy drops, and complex synth patterns.”, “A subgenre of reggae music that originated in Jamaica in the late 1960s. It is characterized by the remixing of existing recordings, often removing vocals and emphasizing drums and bass. It also uses effects such as reverb, delay, or echo to create a spacious and psychedelic sound.”, “A subgenre of hip hop music that originated in the Southern United States in the early 1990s. It is characterized by its use of 808 drum machines, fast hi-hats, heavy bass, and dark and ominous melodies. It also features vocals that often rap about drugs, violence, or money.”, “A subgenre of EDM that emerged in the late 1990s and early 2000s. It combines elements of hip hop, glitch, and IDM. It is known for its use of glitches, cuts, skips, and stutters to create rhythmic and melodic variations. It also uses samples from various sources such as funk, jazz, or soul.”, “A genre of EDM that originated in Detroit in the mid-1980s. It is characterized by a 4/4 beat, a minimalistic and futuristic sound, and the use of electronic instruments such as synthesizers, drum machines, and sequencers. It also draws influences from genres such as electro, funk, or industrial.”, “A genre of EDM that emerged in Germany in the early 1990s. It is characterized by a fast tempo (usually above 130 BPM), a repetitive and hypnotic sound, and a build-up and release structure. It also features elements such as synth leads, pads, plucks, or vocals.”] elements = [[“4/4 beat with a tempo of 120-130 BPM”, “Bassline that follows the kick drum pattern”, “Synthesizer chords, melodies,<br>or stabs”, “Vocal samples,<br>loops,<br>or hooks”, “Drum machines such as Roland TR-808<br>or TR-909”, “Effects such as reverb,<br>delay,<br>or compression”], [“Distorted and aggressive basslines”, “Heavy drops with build-ups and breakdowns”, “Complex synth patterns and leads”, “Electro or techno drum sounds”, “Effects such as distortion,<br>filter,<br>or modulation”], [“Remixing of existing reggae recordings”, “Emphasis on drums and bass”, “Removal or reduction of vocals”, “Effects such as reverb,<br>delay,<br>or echo”, “Dub sirens,<br>horns,<br>or melodicas”], [“808 drum machines with fast hi-hats<br>and kick drums”, “Heavy bass that often slides or glides”, “Dark and ominous melodies using synths<br>or pianos”, “Vocals that rap about drugs,<br>violence,<br>or money”, “Effects such as distortion,<br>chorus,<br>or flanger”], [“Glitches,<br>cuts,<br>skips,<br>and stutters to create rhythmic<br>and melodic variations”, “Samples from various sources such as funk,<br>jazz,<br>or soul”, “Hip hop drum sounds<br>and beats”, “Synth basses<br>or leads”, “Effects such as bitcrushing,<br>granular synthesis,<br>or time stretching”], [“4/4 beat with a tempo of 120-150 BPM”, “Minimalistic<br>and futuristic sound”, “Synthesizer chords,<br>melodies,<br>or pads”, “Drum machines such as Roland TR-808<br>or TR-909”, “Sequencers<br>or arpeggiators”], [“Fast tempo (usually above 130 BPM)”, “Repetitive<br>and hypnotic sound”, “Build-up<br>and release structure with breakdowns<br>and climaxes”, “Synth leads,<br>pads,<br>plucks,<br>or vocals”, “Effects such as reverb,<br>delay”]]

Define a function to generate a random subgenre
def random_subgenre():

Choose a random index from 0 to 6
index = random.randint(0, 6)

Return the subgenre and its description and elements at that index
return subgenres[index], descriptions[index], elements[index]

Define a function to generate a music track based on a subgenre and its elements
def generate_music(subgenre, elements):

Create an empty list to store the notes
notes = []

Create an empty list to store the drums
drums = []

Create an empty list to store the effects
effects = []

Loop through the elements of the subgenre
for element in elements: # If the element is about the beat, tempo, or drum machines if “beat” in element or “tempo” in element or “drum machines” in element: # Use the magenta library to generate a drum pattern based on the element drum_pattern = magenta.music.DrumTrackGenerator(element) # Append the drum pattern to the drums list drums.append(drum_pattern) # If the element is about the bassline, synth, or melodies if “bassline” in element or “synth” in element or “melodies” in element: # Use the magenta library to generate a melody based on the element melody = magenta.music.MelodyGenerator(element) # Append the melody to the notes list notes.append(melody) # If the element is about the vocals, samples, or loops if “vocals” in element or “samples” in element or “loops” in element: # Use the librosa library to load an audio file based on the element audio_file = librosa.load(element) # Append the audio file to the notes list notes.append(audio_file) # If the element is about the effects if “effects” in element: # Use the librosa library to apply an effect based on the element effect = librosa.effects.apply_effect(element) # Append the effect to the effects list effects.append(effect)

Use the magenta library to combine the notes, drums, and effects into a music track
music_track = magenta.music.MusicTrack(notes, drums, effects)

Return the music track
return music_track

Generate a random subgenre and its elements
subgenre, description, elements = random_subgenre()

Print the subgenre and its description
print(f"The subgenre is {subgenre}.“) print(f”{description}")

Generate a music track based on the subgenre and its elements
music_track = generate_music(subgenre, elements)

Save the music track as a Midi file with each individual element separated, and also as a full composed song and .wave file
 
