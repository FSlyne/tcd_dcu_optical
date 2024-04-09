import json

from tcdona2.lumentum2 import *

roadm3=Lumentum('10.10.10.33')

roadm3.wss_delete_connection(1,'all')
roadm3.wss_delete_connection(2,'all')
