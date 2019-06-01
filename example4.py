from automatabpp import *
import math, time


class LED:
    BEHAVIOUR.load_behaviour_from_graph("embedded/led_light.graphml", "Embedded LED Light machine")

    @EXECUTION.state
    def LED_ON(**_):
        print("Turning LED on")

    @EXECUTION.state
    def LED_OFF(**_):
        print("Turning LED off")


class FAN:
    BEHAVIOUR.load_behaviour_from_graph("embedded/fan.graphml", "Embedded Fan machine")

    @EXECUTION.state
    def FAN_ON(**_):
        print("Turning fan on")

    @EXECUTION.state
    def FAN_OFF(**_):
        print("Turning fan off")


class HEATER:
    BEHAVIOUR.load_behaviour_from_graph("embedded/heater.graphml", "Embedded Heater machine")

    @EXECUTION.state
    def HEATER_ON(**_):
        print("Turning heater on")

    @EXECUTION.state
    def HEATER_OFF(**_):
        print("Turning heater off")


BEHAVIOUR.load_behaviour_from_graph("embedded/led_light_model.graphml", "Model for LED light behaviour")
BEHAVIOUR.load_behaviour_from_graph("embedded/heater_model.graphml", "Model for heater behaviour")
BEHAVIOUR.load_behaviour_from_graph("embedded/fan_model.graphml", "Model for fan behaviour")


@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.less_than(3.2), "battery_critically_low")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.between(3.2, 3.5), "battery_low")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.between(3.501, 4.2), "battery_normal")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.more_than(4.2), "battery_full")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.less_than(3.5), "battery_nearly_empty")
def simulate_battery_voltage_reading(num):
    return (math.sin(num)+1)*2.5


@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.less_than(-5), "temp_critically_low")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.between(-5, 0), "temp_low")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.between(1, 50), "temp_normal")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.between(51, 62), "temp_high")
@INTERFACE.run_command_if_lambda_on_result_true(COMPARISONS.more_than(62), "temp_critically_high")
def simulate_temperature_reading(num):
    return (math.sin(2*pow(num, 2))+1)*50-20


# ...............................................................................
# ---------- DEFINITIONS COMPLETE - RUNNING THE PROGRAM -------------------------
# ...............................................................................
OPERATION.start_fsm()


for i in range(100):
    volt = round(simulate_battery_voltage_reading(i), 2)
    temp = round(simulate_temperature_reading(i), 2)
    print("\t\t|\t{}V\t|\t{}°C".format(volt, temp))
    OPERATION.run_fsm()
    time.sleep(2)
