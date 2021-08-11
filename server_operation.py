"""
Perform operations on servers
"""
def allocate_on_server(server_list, number_users, user_server_map, max_users):
    """ Function to allocate users on a server

    Params:
        server_list: List informing servers with their respective allocated
        user numbers.
        number_users: Integer informing the number of users to be entered.
        user_server_map: List informing mapping on quantity increment and its
        respective server which user was entered.
        max_users: Integer stating maximum number of users per server.

    Returns:
        list ->
            server_list: List informing servers with their respective
            allocated user numbers.
            user_server_map: List informing mapping on quantity increment and
            its respective server which user was entered.
    """
    server_values = sorted(set(server_list), reverse=True)
    if max_users in server_values:
        server_values.remove(max_users)

    index_server_values = 0
    user_server_map_temp = []
    while number_users > 0:
        # Allocate users to existing server spaces
        while index_server_values < len(server_values):
            for i, server in enumerate(server_list):
                if server_values[index_server_values] == server:
                    number_users_position = 0
                    while server_list[i] < max_users and number_users > 0:
                        number_users -= 1
                        number_users_position += 1
                        server_list[i] = server_list[i] + 1
                    user_server_map_temp.append([number_users_position, i])
                    if number_users <= 0:
                        break
            index_server_values += 1

        # Allocate users to new servers
        number_users_position = 0
        if number_users < max_users:
            server_list.append(number_users)
            number_users_position = number_users
        else:
            server_list.append(max_users)
            number_users_position = max_users
        i = len(server_list) - 1
        user_server_map_temp.append([number_users_position, i])
        number_users -= max_users

    if user_server_map_temp:
        user_server_map.append(user_server_map_temp)
    return [server_list, user_server_map]


def deallocate_server(server_list, user_input, user_server_map):
    """ Function that deallocates users from servers

    Params:
        server_list: List informing servers with their respective allocated
        user numbers.
        user_input: Integer informing the number of users to be removed.
        user_server_map: List informing mapping on quantity increment and its
        respective server which user was entered.
    Returns:
        list ->
            server_list: List informing servers with their respective
            allocated user numbers.
            user_server_map: List informing mapping on quantity increment and
            its respective server which user was entered.
    """
    if user_input:
        for element in user_server_map[0]:
            for i in range(len(server_list)):
                if element[1] == i:
                    server_list[i] -= element[0]
        del user_server_map[0]
    return [server_list, user_server_map]
