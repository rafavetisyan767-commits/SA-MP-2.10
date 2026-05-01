import os, shutil

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def prepend(path, content):
    if os.path.exists(path):
        with open(path, 'r') as f:
            original = f.read()
        with open(path, 'w') as f:
            f.write(content + original)

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

bs_path = "app/src/main/cpp/samp/vendor/RakNet/BitStream.h"
if not os.path.exists(bs_path):
    write(bs_path, """
#pragma once
#include <cstdint>
#include <cstring>
namespace RakNet {
    class BitStream {
    public:
        BitStream(){}
        BitStream(unsigned char* data,unsigned int len,bool copy){}
        ~BitStream(){}
        void Reset(){}
        void Write(bool v){}
        void Write(unsigned char v){}
        void Write(int v){}
        void Write(unsigned int v){}
        void Write(float v){}
        void Write(const char* v,int len){}
        bool Read(bool &v){v=false;return false;}
        bool Read(unsigned char &v){v=0;return false;}
        bool Read(int &v){v=0;return false;}
        bool Read(unsigned int &v){v=0;return false;}
        bool Read(float &v){v=0.0f;return false;}
        unsigned int GetNumberOfBitsUsed() const {return 0;}
        unsigned int GetNumberOfBytesUsed() const {return 0;}
        unsigned char* GetData() const {return nullptr;}
        void SetWriteOffset(unsigned int o){}
        void SetReadOffset(unsigned int o){}
        unsigned int GetReadOffset() const {return 0;}
        unsigned int GetWriteOffset() const {return 0;}
    };
}
""")

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

prepend("app/src/main/cpp/samp/voice_new/Network.h",
    "#ifndef INVALID_SOCKET\n#define INVALID_SOCKET (-1)\n#endif\n")

rgba = "app/src/main/cpp/samp/game/rgba.h"
RGBA = "app/src/main/cpp/samp/game/RGBA.h"
if os.path.exists(rgba) and not os.path.exists(RGBA):
    shutil.copy(rgba, RGBA)

print("All files created!")
