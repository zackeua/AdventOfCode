import sys


class Singleton:  # Singleton decorator

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self):
        if self.instance is None:
            self.instance = self.cls()
        return self.instance


class Signal:

    def __init__(self, signal):
        self.signal = signal

    def __not__(self):
        return Signal(~self.signal)

    def __lt__(self, other):
        return self.signal < other.signal

    def __eq__(self, other):
        return self.signal == other.signal

    def __hash__(self):
        return hash(self.signal)


class Module:

    def __init__(self, name):
        self.name = name
        self.inputs = []

    def send_signal(self):
        pass

    def __lt__(self, other):
        return self.name < other.name and self.node_type < other.node_type

    def __eq__(self, other):
        return self.name == other.name and self.node_type == other.node_type

    def __hash__(self):
        return hash(self.name)*len(self.name) + hash(self.node_type)


class FlipFlop(Module):

    def __init__(self, name):
        super().__init__(name)

    def send_signal(self):
        assert len(self.inputs) == 1
        signal = self.inputs[0]
        if signal.value == 0:
            if self.memory == 0:
                self.memory = 1
                return Signal(0)
            else:
                return Signal(1)
        else:
            return None


class Conjunction(Module):

    def __init__(self, name):
        super().__init__(name)
        self.input_memory = [0 for _ in self.inputs]

    def send_signal(self):
        if all(self.input_memory):
            return Signal(0)
        else:
            return Signal(1)


@Singleton
class Broadcast(Module):

    def __init__(self):
        super().__init__('broadcaster')

    def send_signal(self):
        if self.inputs[0].value == 0:
            return Signal(0)
        else:
            return Signal(1)


@Singleton
class Button(Module):

    def __init__(self):
        super().__init__('button')

    def send_signal(self):
        return Signal(0)


def create_module(name_name):
    node_type = name_name[0]
    name = name_name

    if node_type == '%':
        return FlipFlop(name[1:])
    elif node_type == '&':
        return Conjunction(name[1:])
    elif name == 'broadcaster':
        return get_broadcaster()
    elif name == 'button':
        return get_button()
    else:
        raise ValueError('Unknown node type: {}'.format(node_type))


def get_button():
    return Button()


def get_broadcaster():
    return Broadcast()


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        nodes = {}
        outgoing_connections = {}
        for line in data:
            node_name, outgoing = line.split(' -> ')
            name = node_name
            if node_name[0] == '%' or node_name[0] == '&':
                name = node_name[1:]
            node = create_module(node_name)
            nodes[name] = node
        node = get_button()
        nodes['button'] = node
        node = get_broadcaster()
        assert id(node) == id(nodes['broadcaster'])  # Singleton test
        node = get_button()
        assert id(node) == id(nodes['button'])  # Singleton test

        for line in data:
            node_name, outgoing = line.split(' -> ')
            if outgoing:
                outgoing = outgoing.split(', ')
                for out in outgoing:
                    nodes[node_name].inputs.append(nodes[out])

        print(data)
        print(nodes)


if __name__ == '__main__':
    main()
