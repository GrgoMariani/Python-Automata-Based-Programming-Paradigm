# FSM

I won't cover too much how the code is written but rather how to use it.

Once we `import automatabpp` into our python script we can use the following 4 classes.

| [OPERATION](#operation) | [BEHAVIOUR](#behaviour) | [EXECUTION](#execution) | [INTERFACE](#interface) | [COMPARISONS](#comparisons) |
| --- | --- | --- | --- | --- |


### OPERATION

Operation is a class that only executes the global operations on the FSMs.
```python
OPERATION.start()       # Starts the FSMs by sending the '_start_' command to all the machines

.OPERATIONstop()        # Stops all the FSMs by sending the '_stop_' command to all the machines,
                            # reseting them to the default '_START_' state and emptying the machine commands stack.

.rOPERATIONeset()       # Stops and starts the FSMs

.ruOPERATIONn()         # Runs all the commands in the CommandQueue until the queue is empty.

.runOPERATION(cmd)      # Runs only the cmd on all machines now without running the rest of the queue.
```

### BEHAVIOUR
Behaviour class is used to load the machine behaviour from the graph.
```python
BEHAVIOUR.set_default_graph_directory(path)             # sets the default graph directory path

BEHAVIOUR.load_behaviour_from_graph(path, machine_name) # loads the machine from path and stores it as machine_name
```

### EXECUTION
Execution class consists only of an operator on our function that defines what function should be called once the state has been reached.
```python
EXECUTION.state(func)       # usually used as a decorator over the function we wish to be called on state execution
```

### INTERFACE
Interface is an interface to the automatabpp we can use. Consists of only a decorator we can use on a function.
```python
INTERFACE.run_command_if_lambda_on_result_true(lambda_function, command)
# When the function decorated with this function is called, the command will be run if the lambda on result is True
```

### COMPARISONS
A helper class with lots of comparison `lambda` type functions. Can only return `True` or `False` .
```python
COMPARISONS.less_than(num)
COMPARISONS.between(num1, num2)
COMPARISONS.more_than(num)
COMPARISONS.equal(num)
COMPARISONS.not_equal(num)
COMPARISONS.contains(string)
COMPARISONS.one_of(items)
COMPARISONS.none_of(items)
COMPARISONS.always_true()
COMPARISONS.on_result_true()
COMPARISONS.on_result_false()
```

| [Back to Main][prev] | ----- | [Tutorial][next] |
| --- | --- | --- |

[prev]: ../README.md "Main"
[next]: tutorial.md "Tutorial"
