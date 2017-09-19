import socket
import sys
sys.path.append('./gen-py') 
from name import SayName
from name.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class SayHandler:  
     def say(self, msg):
        ret = "Received: " + msg    
        print ret    
        return ret

handler = SayHandler()
processor = SayName.Processor(handler)
transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory) 
server.serve()