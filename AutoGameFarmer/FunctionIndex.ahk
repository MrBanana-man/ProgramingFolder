/*Script Made By Me*/

/*Returns the character to the Adoption Center */
/*Change the Mouse last positions because it hits search bar and can be avoided*/
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

HpianoTask(){
    resetChar()
    Sleep(3000)
    SendInput "{a Down}"
    Sleep(400)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(2000)
    MouseMove(641, 629)
    Sleep(200)
    Click()
    Sleep(200)
    MouseMove(651, 620)
    Click()
    Sleep(200)
    SendInput "{2}"
}

HbathTask(){
    resetChar()
    Sleep(3000)
    SendInput "{a Down}"
    Sleep(400)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(2000)
    SendInput "{e}"
    Sleep(200)
    SendInput "{2}"
}

HdrinkTask(){
    resetChar()
    Sleep(3000)
    SendInput "{a Down}"
    Sleep(400)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(2000)
    MouseMove(1137, 387)
    Sleep(200)
    MouseMove(1130, 380)
    Click()
}

HeatTask(){
    resetChar()
    Sleep(3000)
    SendInput "{a Down}"
    Sleep(400)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(2000)
    MouseMove(1217, 385)
    Sleep(200)
    MouseMove(1220, 390)
    Click()
}

HsleepTask(){
    resetChar()
    Sleep(3000)
    SendInput "{a Down}"
    Sleep(400)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(2000)
    MouseMove(1197, 634)
    Sleep(200)
    MouseMove(1200, 640)
    Click()
}

/*Gets the character to school */
school(){
    pos0()
    Sleep(3000)
    SendInput "{w Down}"
    Sleep(1500)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{a Down}"
    Sleep(4000)
    SendInput "{a Up}"
}

/*Fixes the sick task */
sick() {
    pos0()
    Sleep(3000)
    SendInput "{w Down}"
    Sleep(400)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{d Down}"
    Sleep(4000)
    SendInput "{d Up}"
    Sleep(200)
    SendInput "{s Down}"
    Sleep(4000)
    SendInput "{s Up}"
    /*Walk to bed in hostpital */
    Sleep(2000)
    SendInput "{w Down}"
    Sleep(400)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{a Down}"
    Sleep(750)
    SendInput "{a Up}"
    Sleep(1000)
    SendInput "{w Down}"
    Sleep(3500)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{e}"
    Sleep(200)
    SendInput "{2}"
    
}

/*Gets the pizza party time */
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

/*Goes to the beach */
beach(){
    pos0()
    Sleep(3000)
    SendInput "{w Down}"
    Sleep(400)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{a Down}"
    Sleep(21000)
    SendInput "{a Up}"
    Sleep(200)
}

/*Goes to the salon */
salon(){ 
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
    SendInput "{w Down}"
    Sleep(5000)
    SendInput "{w Up}"
    Sleep(200)
}

camping() {
    pos0()
    Sleep(3000)
    SendInput "{w Down}"
    Sleep(1000)
    SendInput "{w Up}"
    Sleep(200)
    SendInput "{D Down}"
    Sleep(3000)
    SendInput "{D Up}"
    Sleep(200)
    SendInput "{s Down}"
    Sleep(4000)
    SendInput "{s Up}"
    Sleep(200)
    SendInput "{a Down}"
    Sleep(3000)
    SendInput "{a Up}"
    Sleep(200)
    SendInput "{s Down}"
    Sleep(13000)
    SendInput "{s Up}"
    Sleep(200)
    SendInput "{d Down}"
    Sleep(13000)
    SendInput "{d Up}"
    Sleep(200)
    SendInput "{s Down}"
    Sleep(12000)
    SendInput "{s Up}"
    Sleep(200)

}


/*REMEMBER TO ADD BIG TIME DELEY BETWEEN FUNCTIONS */
/*every function done */
/*NOW DO RESEARCH FOR HOW LONG THE TASKS ARE*/
F1::{
    camping()
}

F2::{
    resetChar()
}

F3::{
    MessageBox := MsgBox("Do you want to proceed to close the app?","Adopt Me Auto Farmer", "YesNo")
    if MessageBox = "Yes"
        ExitApp
}
