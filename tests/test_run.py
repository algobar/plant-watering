from plantwatering.run import run

if __name__ == "__main__":
    run(
        "test",
        "EmailMessenger",
        interval=2,
        moisture_threshold=0,
        sender="barnharthomeserver",
        recipient="bob.ebarnhart@gmail.com",
    )
