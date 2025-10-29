from template_package.template_module import Greeter


def main() -> None:
    greeter = Greeter("Paco")
    print(greeter.greet())


if __name__ == "__main__":
    main()
