#include "Application.hpp"

class Application
{
private:
    void processEvents() {}
    void update() {}
    void render() {}
public:
    Application();
    ~Application();

    bool initialize();
    void run();
    void shutdown();
};
