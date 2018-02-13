"""
obspy.io.rg16 - receiver gather v1.6 read support for ObsPy
===========================================================

Functions to read waveform data from Receiver Gather 1.6-1 format.
This format is used for continuous data by
`Farfield Nodal <fairfieldnodal.com>`_
`Zland product line <http://fairfieldnodal.com/equipment/zland>`_.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)

Inspired by a similar project by a `similar script
<https://github.com/iceseismic/Fairfield-Receiver-Gather`_.


.. note::
    1. Some useful diagrams, provided by Faifield technical support, for
    understanding Base Scan intervals, data format, and sensor type numbers
    can be found `here <https://imgur.com/a/4aneG>`_.

    2. Because there is not a standard deployment orientation, channel codes
    contained in the file format are 2, 3, and 4. See the above link for the
    orientation in respect to instrument orientation.

Reading
-------
The rg16 format can be read using two methods:

1. Using the standard :func:`~obspy.core.stream.read` function. Optionally,
   the format parameter can be specified as "rg16" in order to avoid spending
   time checking if the file is one of the other formats.

2. Using the :mod:`obspy.io.rg16` specific function
   :func:`obspy.io.rg16.read_rg16` function.

Noteworthy parameters of the read_rg16 (which can be passed as kwargs in
read):

1. The parameter "merge" will merge many traces belonging to the same channel
   into a single trace. This is much more efficient than the
   :func: `obspy.core.Steam.merge` when there are many (thousands) of traces
   because the function can make some assumptions about data continuity and
   type. If you are reading a rg16 file that is several GB in size and that
   contains many traces it may be beneficial to use this parameter.

2. The parameters "starttime" and "endtime" can be used to only load slices of
   the file at a time, avoiding the need to store the whole file in memory at
   one time.

3. Setting the parameter "standard_orientation" to True indicates the file
   either contains 1C instruments or that the nodes were deployed with the
   gold contact terminals facing north. It will then map the components to
   Z, N, and E (if 3C) as well as correct the polarity for the Z component.

>>> import obspy
>>> from obspy.io.rg16.core import read_rg16
>>> from obspy.core.util import get_example_file
>>> filename = get_example_file('three_chans_six_traces.fcnt')
>>> # these are all equivalent:
>>> st = obspy.read(filename)
>>> st = obspy.read(filename, format='rg16')
>>> st = read_rg16(filename)

If the file was very large using the merge parameter may speed up downstream
processing.

>>> st = obspy.read(filename, merge=True)

If the instruments were single component, or if the gold contact terminals
were deployed facing north, setting standard_orientation to True will result
in a stream with seed compliant channel codes with components Z, N, E.

>>> st = obspy.read(filename, standard_orientation=True)

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA
