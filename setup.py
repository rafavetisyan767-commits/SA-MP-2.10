import os, shutil

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def prepend(path, content):
    if os.path.exists(path):
        with open(path, 'r') as f:
            original = f.read()
        if content.strip() in original:
            return
        with open(path, 'w') as f:
            f.write(content + original)

# 1. Добавляем #pragma once в BitStream.h если его нет
prepend("app/src/main/cpp/samp/vendor/RakNet/BitStream.h",
    "#pragma once\n")

# 2. RakClient.h только если нет
rc_path = "app/src/main/cpp/samp/vendor/RakNet/RakClient.h"
if not os.path.exists(rc_path):
    write(rc_path, """
#pragma once
#include "BitStream.h"
namespace RakNet {
    class RakClient {
    public:
        RakClient(){}
        ~RakClient(){}
        bool Connect(const char* host,unsigned short port,unsigned short cp,unsigned int d,int t){return false;}
        void Disconnect(unsigned int d){}
        bool IsConnected() const {return false;}
        bool Send(const BitStream* bs,int p,int r,char o){return false;}
        bool Send(const char* d,int l,int p,int r,char o){return false;}
    };
}
""")

# 3. PlayerTabList наследуется от Widget
write("app/src/main/cpp/samp/gui/samp_widgets/playerTabList.h", """
#pragma once
#include "../widget.h"

class PlayerTabList : public Widget {
private:
    bool m_visible = false;
public:
    PlayerTabList() {}
    ~PlayerTabList() {}
    void render() {}
    void toggle() { m_visible = !m_visible; }
    void show() { m_visible = true; }
    void hide() { m_visible = false; }
    bool visible() const { return m_visible; }
    bool isVisible() const { return m_visible; }
    void setVisible(bool v) { m_visible = v; }
};
""")

# 4. INVALID_SOCKET в Network.h
prepend("app/src/main/cpp/samp/voice_new/Network.h",
    "#ifndef INVALID_SOCKET\n#define INVALID_SOCKET (-1)\n#endif\n")

# 5. RGBA.h fix
rgba = "app/src/main/cpp/samp/game/rgba.h"
RGBA = "app/src/main/cpp/samp/game/RGBA.h"
if os.path.exists(rgba) and not os.path.exists(RGBA):
    shutil.copy(rgba, RGBA)

print("All files created!")
