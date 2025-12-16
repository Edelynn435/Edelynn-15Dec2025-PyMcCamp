# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def tl():
    agent.turn(LEFT)
player.on_chat("tl", tl)

def tr(): 
    agent.turn(RIGHT)
player.on_chat("tr", tr)
