def line(people):
    the_line = "The line is currently:"
    if len(people) == 0:
        print("The line is currently empty.")
    else:
        for index, person in enumerate(people):
            the_line += f" {index +1}. {person}"
        print(the_line)
        
        
def take_a_number(people, name):
    people.append(name)
    print(f"Welcome, {name}. You are number {len(people)} in line.")

def now_serving(people):
    if len(people) == 0:
        print("There is nobody waiting to be served!")
    else:
        person = people[0]
        del people[0]
        print(f"Currently serving {person}.")
    pass