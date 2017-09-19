# -*- coding: utf-8 -*-
import sys
sys.path.append('./gen-py')
 
from add import AddFunction 
 
from thrift import Thrift 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
try:
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = AddFunction.Client(protocol)
  transport.open()
  msg = client.add(1,2)
  print '从server返回的结果为：',msg
  transport.close()
except Thrift.TException, ex:
  print "%s" % (ex.message)