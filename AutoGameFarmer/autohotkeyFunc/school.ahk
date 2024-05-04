#Requires AutoHotkey v2.0

pos0() {
    Send "{b}"
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
    Send "{s Down}"
    Sleep(2000)
    Send "{s Up}"
    Sleep(200)
}

/*Returns Character to Home */
resetChar(){
    Send "{Esc}"
    Sleep(200)
    Send "r"
    MouseMove(852,478)
    Sleep(200)
    Click()
    MouseMove(852,480)
    Click()
    MouseMove(852,478)
    Sleep(200)
    
}

school(){
    pos0()
    Sleep(3000)
    Send "{w Down}"
    Sleep(1500)
    Send "{w Up}"
    Sleep(200)
    Send "{a Down}"
    Sleep(4000)
    Send "{a Up}"
}

school()
ExitApp