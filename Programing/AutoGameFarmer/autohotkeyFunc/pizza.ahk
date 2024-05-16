#Requires AutoHotkey v2.0

pos0() {
    SendInput "{b}"
    Sleep(200)
    MouseMove(900, 692)
    Sleep(200)
    MouseMove(896, 704)
    Click()
    Sleep(200)
    MouseMove(1131, 639)
    Sleep(200)
    MouseMove(1131, 649)
    Click()
    Sleep(3000)
    SendInput "{s Down}"
    Sleep(2000)
    SendInput "{s Up}"
    Sleep(200)
}

/*Returns Character to Home */
resetChar(){
    SendInput "{Esc}"
    Sleep(200)
    SendInput "r"
    MouseMove(852,478)
    Sleep(200)
    Click()
    MouseMove(852,480)
    Click()
    MouseMove(852,478)
    Sleep(200)
    
}

PIZZA() {
    pos0()
    Sleep(3000)
    SendInput "{w Down}"
    Sleep(15000)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{d Down}"
    Sleep(7000)
    SendInput "{d Up}"
    Sleep(200)
    SendInput "{s Down}"
    Sleep (3500)
    SendInput "{s Up}"
    Sleep(200)
    SendInput "{d Down}"
    Sleep(1500)
    SendInput "{d Up}"
    Sleep(200)
}

PIZZA()
ExitApp