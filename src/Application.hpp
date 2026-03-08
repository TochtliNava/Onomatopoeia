#pragma once

struct SDL_WINDOW;

class Application {
public:
    Application();
    ~Application();

    bool initialize();
    void run();
    void shutdown();
    
private:
    void processEvents();
    void update();
    void render();

    // SDL_Window* _window;
    void* _glContext;
    bool _running;
    int _windowWidth;
    int _windowHeight;

    class Renderer* _renderer;
    class GUI* _gui;
};