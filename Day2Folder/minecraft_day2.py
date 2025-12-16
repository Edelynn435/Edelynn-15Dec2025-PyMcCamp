# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
# agent move forward
def forward(count): 
    agent.move(FORWARD, count)
player.on_chat("fw", forward)

# agent move back
def back(count):
    agent.move(BACK, count)
player.on_chat("bk", back)

# agent move up
def up(count):
    agent.move(UP, count)
player.on_chat("up", up)

# agent move down
def down(count):
    agent.move(DOWN, count)
player.on_chat("dn", down)

# obby 1
def MoveSteps():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 2)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("move", MoveSteps)

# chop
def chop():
    for i in range(6):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)
    agent.teleport_to_player()

player.on_chat("chop", chop)