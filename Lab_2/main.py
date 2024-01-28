from pizza import Terminal


def main():
    terminal = Terminal()
    order = terminal.create_order()
    terminal.checkout(order)


if __name__ == "__main__":
    main()
