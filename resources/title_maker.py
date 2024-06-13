import pyfiglet

def create_ascii_art(text,font):
    ascii_art = pyfiglet.figlet_format(text, font, width=100)
    return ascii_art

if __name__ == "__main__":
    text = "" # Insert text here 
    font = "" # For list of all useable fonts: type "pyfiglet -l" in terminal
    print(create_ascii_art(text,font))
    
'''
                                     *
                                   **
                                   **
                                   **
                                   **           ****    
***  ****       ****       ****    **  ***     * ***  * 
 **** **** *   * ***  *   * ***  * ** * ***   *   ****  
  **   ****   *   ****   *   ****  ***   *** **    **   
  **    **   **    **   **         **     ** **    **   
  **    **   **    **   **         **     ** **    **   
  **    **   **    **   **         **     ** **    **   
  **    **   **    **   **         **     ** **    **   
  **    **   **    **   ***     *  **     **  ******
  ***   ***   ***** **   *******   **     **   ****
   ***   ***   ***   **   *****     **    **
                                          *
                                         *
                                        *
                                       *
'''