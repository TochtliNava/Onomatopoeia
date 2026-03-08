#include "Application.hpp"
#include <iostream>

int main() {

    Application* app = new Application();
    
    if (app->initialize()) {
        app->run();
    } else {
        std::cerr << "Failed to initialize the program." << std::endl;
    }

    app->shutdown();
    delete app;

    return 0;
}