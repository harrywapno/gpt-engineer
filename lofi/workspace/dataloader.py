import os
import glob
import pretty_midi

class DataLoader:
    def __init__(self):
        pass
    
    def load_midi_files(self):
        """
        Load midi files from the database and convert them into a format that can be used for training the AI model.
        """
        midi_data = []
        midi_files = glob.glob(os.path.join("midi_database", "*.mid"))
        for file in midi_files:
            midi = pretty_midi.PrettyMIDI(file)
            midi_data.append(midi)
        return midi_data
