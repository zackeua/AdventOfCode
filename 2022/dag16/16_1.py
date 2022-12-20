import sys

def main():

    with open(sys.argv[1], 'r') as f:
        with open(sys.argv[2], 'w') as f2:
            data = f.readlines()
            data = [row.replace('=', ' ') for row in data]
            data = [row.replace(';', '') for row in data]
            data = [row.replace(',', '') for row in data]
            data = [row.replace('\n', '') for row in data]
            node_list = []
            flow_rate = []
            node_edges = []
            node_connections = []
            for row in data:
                #print(row)
                split_row = row.split(' ')
                node = split_row[1]
                node_flow = split_row[5]
                next_possible_nodes = split_row[10:]
                node_edges.append(next_possible_nodes)
                node_list.append(node)
                flow_rate.append(node_flow)
                print(node)
                #print(node_flow)
                print(','.join(next_possible_nodes))
            for i, node in enumerate(node_list):
                node_connections.append(str(len(node_edges[i])+1))
                #while len(node_edges[i]) < max_length:

            f2.write(f'valves = {{{",".join(node_list)}}};\n')
            f2.write(f'flow_rate = [{",".join(flow_rate)}];\n')
            #f2.write(f'max_valve_connections = [{",".join(node_connections)}];\n')
            f2.write(
                f'valve_connections = [{{{"},{".join([",".join(row) for row in node_edges])}}}];\n')
            

if __name__ == '__main__':
    main()
