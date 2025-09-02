# List of musical notes
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
#Created keys of musical notes

# Dictionary of chord step patterns
chords = {
    "major": [4, 7],
    "minor": [3, 7],
    "augmented fifth": [4, 8],
    "minor fifth": [4, 6],
    "major sixth": [4, 7, 9],
    "minor sixth": [3, 7, 9],
    "dominant seventh": [4, 7, 10],
    "minor seventh": [3, 7, 10],
    "major seventh": [4, 7, 11],
    "diminished seventh": [3, 6, 10]
}

#Createed dictionary for chord steps

def get_chord(key, chord_type):
    if key not in notes:
        return f"Invalid key: {key}"
    if chord_type not in chords:
        return f"Invalid chord type: {chord_type}"

    # find root index
    root_index = notes.index(key)

    # build chord
    chord_steps = chords[chord_type]
    chord_notes = [key]  # include root
    for step in chord_steps:
        chord_notes.append(notes[(root_index + step) % 12])
    
    return chord_notes

# --- Main Program ---
if __name__ == "__main__":
    key = input("Enter the key (e.g., C, D#, F#): ").strip()
    chord_type = input("Enter the chord type (e.g., major, minor seventh): ").strip().lower()

    result = get_chord(key, chord_type)
    print("Chord notes:", result)

#Now the muscial notes are clearly identified


