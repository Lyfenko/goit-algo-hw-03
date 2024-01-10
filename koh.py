import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)


def get_user_input():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (ціле число більше 0): "))
            if order > 0:
                return order
            else:
                print("Будь ласка, введіть додатне число.")
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")


def main():
    order = get_user_input()

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)

    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    draw_koch_snowflake(snowflake_turtle, order, 300)

    window.exitonclick()


if __name__ == "__main__":
    main()
