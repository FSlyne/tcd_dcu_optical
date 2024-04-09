import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')

chunk=[
('193425', '193475', 1),
('193475', '193525', 2),
('193525', '193575', 1)
]

roadm3.make_channel_chunk_mux(chunk)
roadm3.make_channel_chunk_demux(chunk)