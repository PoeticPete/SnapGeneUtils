SnapGene Utils
===============

SnapGene Utils is a Python library to parse Snapgene ``*.dna`` files into dictionaries or Biopython SeqRecords:

.. code:: python

  from snapgene_utils import snapgene_file_to_dict, snapgene_file_to_seqrecord

  file_path = './snap_gene_file.dna'
  dictionary = snapgene_file_to_dict(filepath)
  seqrecord = snapgene_file_to_seqrecord(filepath)

Installation
------------

Install with PIP:

.. code:: bash

    pip install snapgene_utils

Test with Pytest:

.. code:: bash

    pytest --cov=snapgene_utils tests/

Development
------------
.. code:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install -e .
    pip install -r requirements_dev.txt

    ## Run tests
    ./venv/bin/pytest tests/

    ## Distribute
    ## Make sure credentials are stored under ~/.pypirc
    git tag <version>
    git push origin --tags
    python -m build
    twine upload --repository pypi dist/*

Licence = MIT
-------------

SnapGene Utils is an open-source software originally written by `Isaac Luo <https://github.com/IsaacLuo>`_ at the Cai Lab. This fork is released under the MIT licence. Everyone is welcome to contribute!
