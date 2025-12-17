# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def chop(ht):
    for count in range(ht):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)
    agent.teleport_to_player()

player.on_chat("chop", chop)

# chopping stone
def mine(length):
    for count in range(25):
        agent.move(FORWARD,1)
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
player.on_chat("destroy", mine)