import os

from Bio import SeqIO

from snapgene_reader import snapgene_file_to_dict

TEST_DIR = os.path.join("tests", "test_samples")


def test_snapgene_file_to_seqrecord(tmpdir):
    TEST_FILE = os.path.join(TEST_DIR, "AcGFP1.dna")
    d = snapgene_file_to_dict(TEST_FILE)
    print(d)
