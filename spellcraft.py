from mcpi import minecraft
import time

"""
Project spells, based on direction player is facing, close is default and is 1 block away, medium is 10 blocks away, far is 30 blocks away or something. Have player hit ground while facing that direction to trigger.

See if we can poll arrow hits.
https://bukkit.org/threads/player-shoot-arrow-event.104774/
https://hub.spigotmc.org/javadocs/bukkit/
https://bukkit.org/threads/tutorial-player-interact-events.231864/

PROBLEM
- Keeps doing it over and over, needs to remove arrow as soon as it finds coordinates.

"""

server_address = "158.69.221.37"
my_player_name = "bob"

mc = minecraft.Minecraft.create(name=my_player_name)

my_id = mc.getPlayerEntityId(my_player_name)
def shield(pos):
    mc.postToChat("Shield activated!")
    x = pos.x-1
    y = pos.y-1
    z = pos.z-1

    x2 = x + 2
    y2 = y + 3
    z2 = z + 2

    bedrock_block_id = 7
    mc.setBlocks(x, y, z, x2, y2, z2, bedrock_block_id)

    air_block_id = 0
    mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

    time.sleep(4)

    bedrock_block_id = 20
    mc.setBlocks(x, y, z, x2, y2, z2, bedrock_block_id)

    air_block_id = 0
    mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

def imonfire(pos):
    mc.postToChat("Pouring water over you!")

    water_block_id = 8
    mc.setBlock(pos.x, pos.y+3, pos.z, water_block_id)

    time.sleep(3)

    air_block_id = 0
    mc.setBlock(pos.x, pos.y+3, pos.z, air_block_id)

def nuke(victim_pos):
    #TNT
    mc.setBlock(victim_pos.x+2, victim_pos.y, victim_pos.z-2, 46)
    mc.setBlock(victim_pos.x-2, victim_pos.y, victim_pos.z+2, 46)
    mc.setBlock(victim_pos.x+2, victim_pos.y, victim_pos.z+2, 46)
    mc.setBlock(victim_pos.x-2, victim_pos.y, victim_pos.z-2, 46)

    #Redstone
    mc.setBlock(victim_pos.x+2, victim_pos.y-1, victim_pos.z-2, 152)
    mc.setBlock(victim_pos.x-2, victim_pos.y-1, victim_pos.z+2, 152)
    mc.setBlock(victim_pos.x+2, victim_pos.y-1, victim_pos.z+2, 152)
    mc.setBlock(victim_pos.x-2, victim_pos.y-1, victim_pos.z-2, 152)

def lava_swim(victim_pos):
    x = victim_pos.x-1
    y = victim_pos.y-1
    z = victim_pos.z-1

    x2 = x + 2
    y2 = y
    z2 = z + 2

    lava_block_id = 10
    mc.setBlocks(x, y, z, x2, y2, z2, lava_block_id)

def tnt_trap(pos):
    mc.setBlock(pos.x, pos.y-1, pos.z, 46)
    mc.setBlock(pos.x, pos.y-2, pos.z, 152) #Redstone

def fall_trap(pos):
    mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x-1, pos.y, pos.z-1, 12)
    mc.setBlocks(pos.x+1, pos.y+1, pos.z+1, pos.x-1, pos.y+1, pos.z-1, 55) #redstone
    mc.setBlock(pos.x, pos.y+1, pos.z, 70)
    mc.setBlocks(pos.x+1, pos.y-1, pos.z+1, pos.x-1, pos.y-1, pos.z-1, 46)
    mc.setBlocks(pos.x+1, pos.y-2, pos.z+1, pos.x-1, pos.y-30, pos.z-1, 0)

def clear(pos):
    mc.setBlocks(pos.x+2, pos.y+2, pos.z+2, pos.x-2, pos.y-2, pos.z-2, 0)

active_spell = "tnt_trap"

while True:

    for blockhit in mc.events.pollProjectileHits():
        print "AAAAAY1", blockhit
        #AAAAAY1 BlockEvent(BlockEvent.HIT, -23, -4, 46, 1, 773)
        #Worked, but only on hitting entity, not block

        if blockhit.entityId == my_id:
            pos = blockhit.pos
            #clear(pos)

            mc.player.setPos(pos.x, pos.y, pos.z)
            print "sb1"


    for blockhit in mc.events.pollBlockHits():
        if blockhit.entityId == my_id:
            pos = blockhit.pos
            clear(pos)
            print "sb1"

    for chatpost in mc.events.pollChatPosts():

        if chatpost.entityId == my_id:

            if chatpost.message.lower() == "s/clear":
                mc.postToChat("Activated Clear spell shortcut")
                active_spell = "clear"
            if chatpost.message.lower() == "s/tnt":
                mc.postToChat("Activated TNT Trap spell shortcut")
                active_spell = "tnt_trap"
            if chatpost.message.lower() == "s/fall":
                mc.postToChat("Activated Fall Trap spell shortcut")
                active_spell = "fall_trap"


            if chatpost.message.lower() == "shield":
                pos = mc.player.getPos()
                shield(pos)

            elif chatpost.message.lower() == "imonfire":
                pos = mc.player.getPos()
                imonfire(pos)

            elif "nuke" in chatpost.message.lower():
                who = chatpost.message.lower().split(' ')
                if len(who) > 1:
                    who = who[1]
                    mc.postToChat("Nuking "+who+"!")
                    mc_victim = minecraft.Minecraft.create(address=server_address, name=who)
                    victim_pos = mc_victim.player.getPos()
                    nuke(victim_pos)


            elif "lavaswim" in chatpost.message.lower():
                who = chatpost.message.lower().split(' ')
                if len(who) > 1:
                    who = who[1]
                    mc.postToChat("Created swimming pool of lava for " +who+"!")
                    mc_victim = minecraft.Minecraft.create(address=server_address, name=who)
                    victim_pos = mc_victim.player.getPos()
                    lava_swim(victim_pos)

    time.sleep(.1)