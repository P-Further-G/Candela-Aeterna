MovSpeed = 8;
RotSpeed = 0.18;
CamPoz = [0,0,0];
CamRot = [0,0,0];
Width = 1280;
Height = 620;
Aspect = Width/float(Height);
Title = "Equilibrium";
Fov = 60;
Fps = 120.0;
Level = 0;
Start = False;

class WindowOptions:
    SampleBuffer = 1;
    Samples = 4;
    DepthSize = 24;
    DoubleBuffer = True;
    Vsync = False;
    Resizable = True;