from mcpi.minecraft import Minecraft
#mc = Minecraft.create("10.183.0.77", 4711)
air = 0
stone = 1
wood = 1
water = 8
obs = 49
glow = 89
glowred = 246
core = 247
wool = 35
#///////////////
mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.setBlocks(x+5, y+0, z+0, x+1, y+0, z+0, 42)
mc.setBlocks(x+5, y+1, z+0, x+4, y+1, z+0, 20)
mc.setBlocks(x+6, y+2, z+0, x+10, y+2, z+0, 20)
mc.setBlocks(x+11, y+2, z+0, x+11, y+2, z+0, 42)
mc.setBlocks(x+6, y+1, z+1, x+8, y+1, z+1, 35,11)
mc.setBlocks(x+6, y+1, z-1, x+8, y+1, z-1, 35,11)
mc.setBlocks(x+9, y+1, z+1, x+9, y+1, z+1, 42)
mc.setBlocks(x+9, y+1, z-1, x+9, y+1, z-1, 42)
mc.setBlocks(x+9, y+2, z+1, x+10, y+2, z+1, 35,11)
mc.setBlocks(x+9, y+2, z-1, x+10, y+2, z-1, 35,11)
mc.setBlocks(x+10, y+3, z+1, x+11, y+3, z+1, 35,11)
mc.setBlocks(x+10, y+3, z-1, x+11, y+3, z-1, 35,11)
mc.setBlocks(x+6, y-1, z+0, x+6, y-1, z+0, 42)
mc.setBlocks(x+6, y-1, z+1, x+7, y-1, z+1, 35,11)
mc.setBlocks(x+6, y-1, z-1, x+7, y-1, z-1, 35,11)
mc.setBlocks(x+8, y-2, z+1, x+10, y-2, z+1, 35,11)
mc.setBlocks(x+8, y-2, z-1, x+10, y-2, z-1, 35,11)
mc.setBlocks(x+6, y+0, z+1, x+6, y+0, z+1, 245)
mc.setBlocks(x+6, y+0, z-1, x+6, y+0, z-1, 245)
mc.setBlocks(x+7, y+0, z+1, x+7, y+0, z+1, 42)
mc.setBlocks(x+7, y+0, z-1, x+7, y+0, z-1, 42)
mc.setBlocks(x+9, y+0, z+1, x+9, y+0, z+1, 42)
mc.setBlocks(x+9, y+0, z-1, x+9, y+0, z-1, 42)
mc.setBlocks(x+8, y+0, z+2, x+10, y+0, z+2, 42)
mc.setBlocks(x+8, y+0, z-2, x+10, y+0, z-2, 42)
mc.setBlocks(x+11, y+0, z+3, x+13, y+0, z+3, 42)
mc.setBlocks(x+11, y+0, z-3, x+13, y+0, z-3, 42)
mc.setBlocks(x+14, y+0, z+4, x+15, y+0, z+4, 42)
mc.setBlocks(x+14, y+0, z-4, x+15, y+0, z-4, 42)
mc.setBlocks(x+16, y+0, z+5, x+17, y+0, z+5, 42)
mc.setBlocks(x+16, y+0, z-5, x+17, y+0, z-5, 42)
mc.setBlocks(x+9, y+0, z+0, x+9, y+0, z+0, 49)
mc.setBlocks(x+10, y+1, z+0, x+10, y+1, z+0, 35,1)