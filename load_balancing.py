"""
Program execution
"""
from server_operation import allocate_on_server, deallocate_server


def read_file(_file):
    """ Function that performs file reading.

    Params:
        _file: File that will be read.

    Retuns:
        List with the contents read from the file, if successful.
        None if there is an error reading the file.
    """
    try:
        with open(_file, 'r') as obj_file:
            content = obj_file.readlines()
    except FileNotFoundError:
        return None
    else:
        return content


def write_file(_file, list_output, cost):
    """ Function that performs writing to file.

    Params:
        _file: File where writing will be performed.
        list_output: List of servers allocated during program execution.
        cost: Total cost of operation.
    """
    with open(_file, 'w') as obj_file:
        for element in list_output:
            obj_file.write(f"{','.join(map(str, element))}\n")
        obj_file.write(f"{cost}\n")


def check_initial_conditions(list_content):
    """ Function that checks the initial conditions of input variables.

    Params:
        list_content: List with read file content.
    Returns:
        tuple ->
        final_condition_msg: Message informing verification result.
        return_variables: List with the desired variables, with an empty value
        in case of failure.
    """
    final_condition_msg = ''
    return_variables = []
    try:
        tick_task = int(list_content[0])
        user_max = int(list_content[1])
        list_users = [int(c) for c in list_content[2:]]
    except IndexError:
        final_condition_msg = 'ERRO: Argumentos insuficientes'
    else:
        if not 1 <= tick_task <= 10 or not 1 <= user_max <= 10:
            final_condition_msg = 'ERRO: Argumento(s) ttask ou/e umax '\
                                  'inválido(s)'
        elif len(set(list_users)) == 1 and list(set(list_users))[0] == 0:
            final_condition_msg = 'ERRRO: Todas as entradas de usuários tem '\
                              'valor igual a zero.'
        return_variables += [tick_task, user_max, list_users]
    return (final_condition_msg, return_variables)


def run_load_balancing(input_file, output_file):
    """ Function that runs the load balancing program.

    Params:
    input_file: Input file.
    output_file: Output file

    Returns:
        Message informing the result of the execution of the program.
    """
    content = read_file(input_file)
    if content is None:
        return 'ERRO: Arquivo não existe.'
    if not content:
        return 'Erro: Arquivo está vazio.'

    condition_message, variables = check_initial_conditions(content)
    if condition_message:
        return condition_message

    ttask = variables[0]
    umax = variables[1]
    users = variables[2]

    output = []  # saves all generated outputs
    output_tick = []  # Output of each tick
    running_users = []  # Constains running users
    user_server_map = []  # Mapping of each output

    total_cost = 0
    tick = 1
    while tick <= ttask:
        running_users.append(users[tick-1])
        output_tick, user_server_map = allocate_on_server(output_tick,
                                                          users[tick-1],
                                                          user_server_map,
                                                          umax)

        output_servers = [s for s in output_tick if s > 0]
        total_cost += len(output_servers)
        output.append(output_servers if output_servers else [0])
        tick += 1

    while tick <= len(users):
        running_users.append(users[tick-1])
        output_tick, user_server_map = deallocate_server(output_tick,
                                                         running_users.pop(0),
                                                         user_server_map)
        output_tick, user_server_map = allocate_on_server(output_tick,
                                                          users[tick-1],
                                                          user_server_map,
                                                          umax)

        output_servers = [s for s in output_tick if s > 0]
        total_cost += len(output_servers)
        output.append(output_servers if output_servers else [0])
        tick += 1

    while running_users:
        output_tick, user_server_map = deallocate_server(output_tick,
                                                         running_users.pop(0),
                                                         user_server_map)

        output_servers = [s for s in output_tick if s > 0]
        total_cost += len(output_servers)
        output.append(output_servers if output_servers else [0])


    write_file(output_file, output, total_cost)
    return 'Execução finalizada com sucesso.'

if __name__ == '__main__':
    INPUT_FILE = 'files/input.txt'
    OUTPUT_FILE = 'files/output.txt'
    RESULT = run_load_balancing(INPUT_FILE, OUTPUT_FILE)
    print(RESULT)
