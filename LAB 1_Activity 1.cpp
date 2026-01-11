#include <iostream>
using namespace std;

class Logger {
private:
    Logger() {}

    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;

public:
    static Logger& getInstance() {
        static Logger instance;
        return instance;
    }

    void log(const string& message) {
        cout << "Log: " << message << endl;
    }
};

int main() {
    Logger& logger1 = Logger::getInstance();
    Logger& logger2 = Logger::getInstance();

    logger1.log("Hello, Singleton!");
    logger2.log("Same instance");

    return 0;
}
