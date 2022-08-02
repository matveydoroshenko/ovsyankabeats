def create_users_txt(list_of_users):
    lines = []
    for index, user in enumerate(list_of_users):
        user = list(user)
        user.insert(0, f"{index + 1}. ")
        element = (' '.join(map(str, user)))
        lines.append(element)
    with open("data/users.txt", "w") as file:
        for line in lines:
            file.write(line + '\n')