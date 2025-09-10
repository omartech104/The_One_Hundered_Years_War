import shutil
import pyfiglet

def print_title_screen():
    columns = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format("The One Hundred Years' War", font="roman", width=columns)
    print(banner.center(columns))


longsword = """            //
()========>>=========================--
            \\\\"""

battle_axe=r"""  ,  /\  .  
 //`-||-'\\ 
(| -=||=- |)
 \\,-||-.// 
  `  ||  '  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()"""

# For the lack of ascii art compund_bow and short_bow are going to have the same image

short_bow=r"""   (
    \
     )
##-------->     
     )
    /
   ("""

warhammer=r"""             +-+
=============| |
            `:_;'"""
dagger=r""")xxxxx[;;;;;;;;;>"""

rapier=r"""       |
       /~\
Oxxxxx|  (|=========================-
 \____/\_/
       |"""

halbred=r"""  ,  /\
 //`-||
(| -=||
 \\,-||
  `  ||  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()"""

crossbow=r"""                .-.                        
               /  \\   
          .---/-+--||   
          |  K=====++-> 
          '---\-+--||  
               \  //  
                `-' """
mace = r"""       <__>
        __
        __
        __
        __
      .___`.
      |<<>>|
       `__."""


