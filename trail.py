import mcpi.minecraft as minecraft
import time

server_address = "158.69.221.37"
my_player_name = "bob"

# Open a connection to the minecraft server
mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

# Repeat every 0.2 seconds...
while True:

    events = mc.events.pollBlockHits()
    for e in events:
        print "e.Hit.__code__", e.Hit.__code__
        print "e.Hit.__doc__", e.Hit.__doc__
        print "e.Hit.__globals__", e.Hit.__globals__
        print "e.Hit.__repr__", e.Hit.__repr__
        print "e.Hit.__str__", e.Hit.__str__
        #['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']

        #print "e.HIT", e.HIT, type(e.HIT)
        #print "e.Hit", e.Hit(), type(e.Hit)
        #print "e.entityId", e.entityId, type(e.entityId)
        #print "e.face", e.face, type(e.face)
        #print "e.pos", e.pos, type(e.pos)
        #print "e.type", e.type, type(e.type)


    time.sleep(0.2)