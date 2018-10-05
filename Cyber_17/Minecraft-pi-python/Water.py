from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint


def init():
	mc = Minecraft.create("192.168.3.2", 4711)
	x,y,z = mc.player.getPos()
	return mc
	
def main():
	mc = init()
	mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+100, y+34, z+100, x-127, y-62, z-100, 9)
	mc.setBlocks(x+100, y+33, z+100, x-127, y+62, z-100, 0)
	for loop in range (200):
		mc.setBlock(x+randint(-100, 100),y+33,z+randint(-100, 100),8)
		mc.setBlock(x+randint(-100, 100),y+34,z+randint(-100, 100),8)
main()

