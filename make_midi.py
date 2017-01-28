"""This is a bunch of simple midi stuff.

Usage
-----
$ python make_midi.py my_sweet_file.mid
"""
import argparse
import pretty_midi


def rando_midi(filename):
    """Create a midi file.

    Parameters
    ----------
    filename : str
        Filepath for writing a midi file out.

    Returns
    -------
    None
    """
    # Create a PrettyMIDI object
    cello_c_chord = pretty_midi.PrettyMIDI()

    # Create an Instrument instance for a cello instrument
    cello_program = pretty_midi.instrument_name_to_program('Cello')
    cello = pretty_midi.Instrument(program=cello_program)
    # Iterate over note names, which will be converted to note number later
    for note_name in ['C5', 'E5', 'G5']:
        note_number = pretty_midi.note_name_to_number(note_name)

        cello.notes.append(pretty_midi.Note(velocity=100, pitch=note_number,
                                            start=0., end=.5))

    for note_name in ['C5', 'E5', 'G5']:
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.Note(velocity=100, pitch=note_number,
                                start=1., end=.5)
        cello.notes.append(note)

    # Add the cello instrument to the PrettyMIDI object
    cello_c_chord.instruments.append(cello)
    # Write out the MIDI data
    cello_c_chord.write(filename)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename", type=str,
        help="Filename for the output MIDI")

    args = parser.parse_args()
    rando_midi(args.filename)
