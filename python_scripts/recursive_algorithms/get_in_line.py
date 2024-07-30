
def get_in_line(person):
    if person - 1 == 0:
        return 1
    else:
        person = person - 1
        return get_in_line(person) + 1

answer = get_in_line(7)

print(answer)