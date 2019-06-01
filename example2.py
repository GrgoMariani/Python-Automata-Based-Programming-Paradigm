from automatabpp import *


def print_w_timeout(text: str):
    import time
    print("\r {}".format(text), end="")
    time.sleep(0.6)


BEHAVIOUR.load_behaviour_from_graph("hbfs/harderfaster.graphml", "HARDER/FASTER")


@EXECUTION.state
def HARDER(**_):
    print_w_timeout("Work it harder")


@EXECUTION.state
def FASTER(**_):
    print_w_timeout("Do it faster")


BEHAVIOUR.load_behaviour_from_graph("hbfs/betterstronger.graphml", "BETTER/STRONGER")


@EXECUTION.state
def BETTER(**_):
    print_w_timeout("make it better")


@EXECUTION.state
def STRONGER(**_):
    print_w_timeout("makes us stronger")


# ...............................................................................
# ---------- DEFINITIONS COMPLETE - RUNNING THE PROGRAM -------------------------
# ...............................................................................
OPERATION.start_fsm()
OPERATION.run_fsm()
