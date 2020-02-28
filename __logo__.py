# -*- coding: utf8 -*-
# coding-utf8
import time,sys,random

def sprint(s):
        for c in s +'\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.1  / 100)
        
banner = """
  \x1b[91m+------=[\x1b[00m Saydog framework tool \x1b[00mversion 1.2   \x1b[91m]=------\x1b[91m+
  \x1b[91m+------=[\x1b[00m Software exploit, Bruteforce Attack \x1b[91m]=------\x1b[91m+
  \x1b[91m+------=[\x1b[00m Malware collection, Others tools    \x1b[91m]=------\x1b[91m+
"""

git_logo = """\x1b[36m
                    ,cxOKXNNXKOxl,.                 
               .:d0NNNNNNNNNNNNNNNN0xc'             
            ;dKNNNNNNNNNNNNNNNNNNNNNNNNXx:.         
         .dXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNx,       
       .kNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNO'     
      oNNNNNNklokXNNNNNNNNNNNNNNNNNNXOdldNNNNNNx.   
    .0NNNNNNK     .:xxoc:;;;;:cldkc.     ONNNNNNK'  
   .KNNNNNNNO                            dNNNNNNNX, 
  .KNNNNNNNNX.                           0NNNNNNNNX.
  dNNNNNNNNX,                            .0NNNNNNNNO
  NNNNNNNNN'                              .KNNNNNNNN
  NNNNNNNNk                                oNNNNNNNN
  NNNNNNNNx                                lNNNNNNNN
  NNNNNNNN0                                xNNNNNNNN
  NNNNNNNNN;                              .XNNNNNNNN
  KNNNNNNNNX'                            .0NNNNNNNNX
  ;NNNNNNNNNXo.                         cXNNNNNNNNNl
   oNNNNkokXNNNOc'.                .'ckXNNNNNNNNNNk 
    dNNNKl'.:KNNNNNXKl          :0XNNNNNNNNNNNNNNk  
     :XNNNX;.'kKNNNNO            xNNNNNNNNNNNNNNl   
      .kNNNNc  ..,,..            :NNNNNNNNNNNNO.    
        'kNNNKo:,'',.            :NNNNNNNNNNO;      
          .l0NNNNNNNd            :NNNNNNNKo.        
             .ckXNNNd            :NNNNOl'           
                 :OX;            .K0l.
               
                   \x1b[00m\033[41m SAYDOG OFFICIAL \033[00m
             From nothing to be something
            Still connected and keep exploit
\x1b[91m -----------------------------------------------------
\x1b[91m |\x1b[00m Github   \x1b[33m * \x1b[36mhttps://github.com/saydog\x1b[00m             \x1b[91m|
\x1b[91m |\x1b[00m Youtube  \x1b[33m * \x1b[36mhttps://youtube.com/saydog-official\x1b[00m   \x1b[91m|
\x1b[91m |\x1b[00m Instagram\x1b[33m * \x1b[36mhttps://instagram.com/saydog.official\x1b[00m \x1b[91m|
\x1b[91m -----------------------------------------------------"""

logo1 = """\x1b[36m
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMM......WK.....lM:.dW..KX.....:Mc.....KW......MMMMM
   MMMMM. XM .MX .Md lM. dM. NW  Mk .Ml dM. NM. WO .MMMMM
   MMMMM. XN .MK .k: cM. cM. XN  Mk .Mc oM. XM. oXXkMMMMM
   MMMMWd. lKkM0  l. :MXOc.  0K  Mk .M. lW. KW  o. .MMMMM
   MMMMMlxx. :MX .Md lMkcON  NW  Mk .Ml dM. NM. MK .MMMMM
   MMMMM. dO .MX .Md lM: c0. NW  . .lMl :O. NM. 0x .MMMMM
   MMMMMo::::cWX:cWk:xMd:::::XX::xXMMMd:::::XWc::::oMMMMM
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMMMMMMMMMMM  \x1b[33mSAYDOG FRAMEWORK\x1b[36m  MMMMMMMMMMMMMMMMMM
   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

logo2 = """\x1b[91m
         ...                         ..   
     .x888888hx    :   ..          dF               
    d88888888888hxx   @L          '88bu.             
   8" ... `"*8888%`  9888i   .dL  '*88888bu        uL.
   !  "   ` .xnxx.    `Y888k:*888.   ^"*8888N   .ue888Nc.
 X'    .H8888888%:    888E  888I  beWE "888L d88E`"888E
 X 'hn8888888*"   >   888E  888I  888E  888E 888E  888E
 X: `*88888%`     !   888E  888I  888E  888E 888E  888E
 '8h.. ``     ..x8>   888E  888I  888E  888F 888E  888E
  `88888888888888f   x888N><888' .888N..888  888& .888E
   '%8888888888*"     "88"  888   `"888*""   *888" 888&  
      ^"****""`             88F      ""       `"   "888E
                    \x1b[33mCopyright©saydog2020\x1b[91m     .dWi   `88E
                         ./"                 4888~  J8% 
                        ~`                    ^"===*"`
"""

logo3 = """\x1b[36m
        .MMM"bgd `YMM'   `MM'`7MMMMMYb.     .g8MMMbgd  
       ,MI    "Y   VMA   ,V    MM    `Yb. .dP'     `M  
       `MMb.        VMA ,V     MM     `Mb dM'       `  
         `YMMNq.     VMMP      MM      MM MM           
       .     `MM      MM       MM     ,MP MM.    `7MMF'
       Mb     dM      MM       MM    ,dP' `Mb.     MM  
       P"Ybmmd"     .JMML.   .JMMmmmdP'     `"bmmmdPY 
                 \x1b[33mF  R  A  M  E  W  O  R  K\x1b[00m
"""
def gitlogo():
        sprint(git_logo)
        
def randomlogo():
        listlogo = [logo1,logo2,logo3]
        logo=(random.choice(listlogo))
        sprint(logo)