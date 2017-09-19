# -*- coding: utf-8 -*-
import socket
import sys
sys.path.append('./gen-py') 
from add import AddFunction
from add.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import logging
class addHandler:  
     def add(self, a,b):
        ret = a + b
        print 'server的计算机过程结果为：',ret    
        return str(ret)
logging.basicConfig(level=logging.INFO)
handler = addHandler()
processor = AddFunction.Processor(handler)
transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory) 
server.serve()