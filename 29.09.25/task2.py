def describe_person(name, age=30):
    print(f"имя: {name}, возраст: {age}")
u_name=input("введите имя: ")
u_age=int(input("введите возраст: "))
describe_person(u_name, u_age)