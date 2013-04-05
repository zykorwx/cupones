import sys
from twisted.python import log
from twisted.internet import reactor
from autobahn.websocket import connectWS
from autobahn.wamp import WampClientFactory, WampClientProtocol

class PubSubClient1(WampClientProtocol):
 
   def onSessionOpen(self):
      self.subscribe("http://clicktotal.com.mx/notifica#", self.onSimpleEvent)
      self.sendSimpleEvent()
 
   def onSimpleEvent(self, topicUri, event):
      print "Event", topicUri, event
 
   def sendSimpleEvent(self):
      self.publish("http://clicktotal.com.mx/notifica#", "Hello!")
      reactor.callLater(2, self.sendSimpleEvent)
 
 
if __name__ == '__main__':
 
   log.startLogging(sys.stdout)
   debug = len(sys.argv) > 1 and sys.argv[1] == 'debug'
 
   factory = WampClientFactory("ws://zykorwx.no-ip.org:9000", debugWamp = debug)
   factory.protocol = PubSubClient1
 
   connectWS(factory)
 
   reactor.run()