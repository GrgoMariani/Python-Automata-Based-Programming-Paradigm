from automatabpp import *

email_to_test = ""


def test_email():
    for char in email_to_test:
        OPERATION.run_fsm(char)
    OPERATION.stop_fsm()


BEHAVIOUR.load_behaviour_from_graph("email/email.graphml", "E-Mail validation machine")


@EXECUTION.state
def GARBAGE(**_):
    print("{} IS NOT A VALID EMAIL".format(email_to_test))


@EXECUTION.state
def EMAIL(**_):
    print("{} IS A VALID EMAIL".format(email_to_test))


# ...............................................................................
# ---------- DEFINITIONS COMPLETE - RUNNING THE PROGRAM -------------------------
# ...............................................................................
OPERATION.start_fsm()

email_to_test = "a_valid@email.example"
test_email()

OPERATION.reset_fsm()

email_to_test = "an._invalid@email@example-"
test_email()
