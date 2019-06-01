import xml.etree.ElementTree as ET
from automatabpp.machines.machines import Machines
from automatabpp.commandqueue.commandqueue import CommandQueue


def read_graphml(graphml_path: str, machine_name: str):
    read_graphml.ns = {"ns0": "http://graphml.graphdrawing.org/xmlns", "ns2": "http://www.yworks.com/xml/graphml"}
    read_graphml.desc_key = "d5"

    class GraphNode:

        def __init__(self, _node):
            self.id = _node.attrib["id"]
            self.name = ""
            self.transitions_after = ""
            result = _node.find("ns0:data/ns2:ShapeNode/ns2:NodeLabel", read_graphml.ns)
            if result is not None:
                self.name = result.text
            result = _node.find("ns0:data[@key='{}']".format(read_graphml.desc_key), read_graphml.ns)
            if result is not None and result.text is not None:
                self.transitions_after = result.text.rstrip().lstrip()

    class GraphEdge:

        def __init__(self, _edge):
            self.id = _edge.attrib["id"]
            self.name = ""
            result = _edge.findall("ns0:data/ns2:PolyLineEdge/ns2:EdgeLabel", read_graphml.ns) + \
                     _edge.findall("ns0:data/ns2:BezierEdge/ns2:EdgeLabel", read_graphml.ns) + \
                     _edge.findall("ns0:data/ns2:ArcEdge/ns2:EdgeLabel", read_graphml.ns) + \
                     _edge.findall("ns0:data/ns2:SplineEdge/ns2:EdgeLabel", read_graphml.ns) + \
                     _edge.findall("ns0:data/ns2:QuadCurveEdge/ns2:EdgeLabel", read_graphml.ns) + \
                     _edge.findall("ns0:data/ns2:GenericEdge/ns2:EdgeLabel", read_graphml.ns)
            if len(result) > 0:
                self.name = result[0].text
            self.source, self.target = _edge.attrib["source"], _edge.attrib["target"]

    root = ET.parse(graphml_path).getroot()
    read_graphml.desc_key = root.find("ns0:key[@attr.name='description']", read_graphml.ns).attrib["id"]
    edges = [GraphEdge(edge) for edge in root.findall("ns0:graph/ns0:edge", read_graphml.ns)]
    nodes = [GraphNode(node) for node in root.findall("ns0:graph/ns0:node", read_graphml.ns)]
    node_map = dict()
    new_machine = Machines().AddNewMachine(machine_name)
    for node in nodes:
        node_map[node.id] = node.name
        for transition in node.transitions_after.split(CommandQueue.SEPARATOR):
            new_machine.GetStateWithName(node.name).AddCommandToCallAfterExecution(transition)
    for edge in edges:
        for transition_name in edge.name.split():
            new_machine.AddTransition(node_map[edge.source], transition_name, node_map[edge.target])
