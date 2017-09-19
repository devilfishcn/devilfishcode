# -*- coding: utf-8 -*-
import sys
sys.path.append('./gen-py')
 
from name import SayName 
 
from thrift import Thrift 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
try:
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = SayName.Client(protocol)
  transport.open()
  msg = client.say("Hello!")
  print "server - " + msg
  transport.close()
except Thrift.TException, ex:
  print "%s" % (ex.message)