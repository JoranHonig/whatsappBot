from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

class BotLayer(YowInterfaceLayer):
  @ProtocolEntityCallback("message")
  def onMessage(self, entity):
    if True:
      # Send confirmation to othe whatsapp server that the message was read.
      entity.ack()
      entity.ack(True)

      if entity.getType() == 'text':
        messageString = entity.getBody() 
      else:
        messageString = "error"
      #Pass message to handler

  @ProtocolEntityCallback("receipt")
  def onReceipt(self, entity):
      #ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
      #self.toLower(ack)
      entity.ack()


