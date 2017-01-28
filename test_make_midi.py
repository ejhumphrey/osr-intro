import pytest
import os

import make_midi


def test_rando_midi_writes_output(tmpdir):
    fout = os.path.join(str(tmpdir), "test_rando_midi_out-1.mid")
    assert not os.path.exists(fout)
    make_midi.rando_midi(fout)
    assert os.path.exists(fout)


def test_rando_midi_not_empty(tmpdir):
    fout = os.path.join(str(tmpdir), "test_rando_midi_out-2.mid")
    assert not os.path.exists(fout)
    make_midi.rando_midi(fout)
    assert open(fout).read()
