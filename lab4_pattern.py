class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")


def main():
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Hello, Singleton!")
    logger2.log("Same instance")

    # Proof that both variables reference the same instance
    print(logger1 is logger2)


if __name__ == "__main__":
    main()
