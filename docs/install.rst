Installation using pip
======================

System-wide
-----------

::

    sudo pip install ppu

User mode
---------

::

    pip install --user ppu

Virtual envs
------------

::

    pip install ppu

Installation from sources
=========================

To install the library from sources system-wide run run the following
command:

::

    sudo python setup.py install

If you don't want to install it system-wide you can install it in your
home directory; run run the following command:

::

    python setup.py install --user

Option '--user' installs scripts into $HOME/.local/bin;
add the directory to your $PATH or move the script to a directory in your
$PATH.
