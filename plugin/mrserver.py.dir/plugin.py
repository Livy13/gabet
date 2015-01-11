# PYTHON!
# -*- coding: iso-8859-1 -*-

# Copyright 2014 Team TLS
# All rights reserved.
#
# Contact: maxlxl(at)abwesend.de

# Variablen
__plugin_name__ = "mrserver"
__plugin_version__ = "0.0.10"
__plugin_mainclass__ = "MRServer"
try:
    mrdebug = True
    mrchata = "[MRServerPy] "
    mrchatmarker = "#####[MRServerPy]#####"
    mrversionbukkit = "Craftbukkit 1.7.9-R0.2-#3086"
    mrerror = False
    endlinewindows = "\n\r"
    endlinelinux = "\n"

    # Importe
    import time,os,sys
    from java.io import File
    from java.lang import Class
    import org.bukkit as bukkit
#    from org.bukkit.plugin import TimedRegisteredListener
    
    class MRServer(PythonPlugin):
        def __init__(self):
            if mrdebug == True:
                print "[MRServerPy] Plugin-Initialisierung geladen."
#            try:
#                mrlog = open("log.txt", "a", -1)
#                print type(mrlog)
#            except IOError:
#                print mrchata + "!!!!!ERROR!!!!!: #1 Log-Datei zum speichern konnte nicht geoeffnet werden."
#            except Exception:
#                print mrchata + "!!!!!ERROR!!!!!: #2 Unbekannter Log-Datei Fehler."
            
        def onEnable(self): #onDisable befindet sich weiter unten als gewoehnlich
            print mrchata + "MRServer-Python - Version:", __plugin_version__, "enabled."
#            print mrchata + "No Update found. [automatic updates are not usable yet...]"
            print mrchata + "Programmed for", mrversionbukkit
#            print mrchata + "LOG: [" + time.strftime("%d.%m.%y %H:%M:%S", time.localtime()) + "] Plugin enabled."
            self.mrWriteLog("Plugin enabled.")

        def mrWriteLog(self, message):
            message = "[" + time.strftime("%d.%m.%y %H:%M:%S", time.localtime()) + "] " + message + endlinelinux
            try:
                f = open(File(self.dataFolder, "log.txt").getCanonicalPath(), "a") # a = writing_add, r = read, w = writing, r+ = writing and reading
            except Exception:
                print mrchata + "FEHLER: #7 Zugriff auf Logdatei fehlgeschlagen."
                if mrdebug == True:
                    print mrchata + "DEBUG: Dateipfad: " + File(self.dataFolder, "log.txt").getCanonicalPath()
                    print sys.exc_info()[0]
            if mrdebug == True:
                print mrchata + "LOG: " + message
            try:
                f.write(message)
            except Exception:
                print mrchata + "FEHLER: #8 Konnte keine Daten in Logdatei schreiben."
                if mrdebug == True:
                    print mrchata + "DEBUG: Dateipfad: " + File(self.dataFolder, "log.txt").getCanonicalPath()
                    print sys.exc_info()[0]
            try:
                f.close
            except Exception:
                print mrchata + "FEHLER: #9 Konnte Logdatei nich schliessen. Aenderungen werden eventuell nicht gespeichert."
                if mrdebug == True:
                    print mrchata + "DEBUG: Dateipfad: " + File(self.dataFolder, "log.txt").getCanonicalPath()
                    print sys.exc_info()[0]
            
        def onDisable(self):
            print mrchata + "MRServer-Python - Version:", __plugin_version__, "disabled."
            self.mrWriteLog("Plugin disabled.")
            
        def onCommand(self, sender, command, label, args): # label ist der eingegebene command! # commands nur von spielern
#            tmp = "self: ", self, " | sender: ", sender, " | command: ", command, " | label: ", label, " | args: ", args
#            print tmp
#            return True
            if mrdebug == True:
                tmp = "self: " + str(self) + " | sender: " + str(sender) + " | command: " + str(command) + " | label: " + str(label) + " | args: " + str(args)
#                tmp = str(tmp)
                self.mrWriteLog(tmp)
            if label == "mrsdebuga":
                msgconsole = mrchata + "DEBUG: A called."
                msgplayer = mrchata + "Hello dev. You have called the debug-script A. Done."
                self.mrWriteLog("DEBUG: A called.")
                print msgconsole
                if mrdebug == True:
                    print mrchata + "DEBUG: sender:", sender
                    print mrchata + "DEBUG: command:", command
                    print mrchata + "DEBUG: label:", label
                    print mrchata + "DEBUG: args:", args
                sender.sendMessage(msgplayer)
                return True
                
            elif label == "mrsdebugb":
                msgconsole = mrchata + "DEBUG: B called."
                msgplayer = mrchata + "Hello dev. You have called the debug-script B. Done."
                print msgconsole
                if mrdebug == True:
                    print mrchata + "DEBUG: sender:", sender
                    print mrchata + "DEBUG: command:", command
                    print mrchata + "DEBUG: label:", label
                    print mrchata + "DEBUG: args:", args
                sender.sendMessage(msgplayer)
                return True
                
            elif label == "mrsdebugc":
                msgconsole = mrchata + "DEBUG: C called."
                msgplayer = mrchata + "Hello dev. You have called the debug-script C. Done."
                print msgconsole
                if mrdebug == True:
                    print mrchata + "DEBUG: sender:", sender
                    print mrchata + "DEBUG: command:", command
                    print mrchata + "DEBUG: label:", label
                    print mrchata + "DEBUG: args:", args
                sender.sendMessage(msgplayer)
                return True
                
            elif label == "mrscmdblock" and args[0] == "help":
                msgplayer = mrchata + "Dieser command ist nur fuer Kommandobloecke! Folgend eine kleine Liste:"
                msgplayerb = "Aktuell keine Kommandos vorhanden."
                if mrdebug == True:
                    print mrchata + "DEBUG: sender:", sender
                    print mrchata + "DEBUG: command:", command
                    print mrchata + "DEBUG: label:", label
                    print mrchata + "DEBUG: args:", args
                sender.sendMessage(msgplayer)
                sender.sendMessage(msgplayerb)
                return True
#            elif label == "a" and args[0] == "password":
#                msgconsolea = mrchata + "Someone have found the secret function... but it is secret."
#                msgconsoleb = mrchata + "But please do not tell anybody of this :D - thx."
#                msgplayer = mrchata + "Congratulations. You have found a secret. Tell maxlxl."
#                print msgconsolea
#                print msgconsoleb
#                if mrdebug == True:
#                    print mrchata + "DEBUG: sender:", sender
#                    print mrchata + "DEBUG: command:", command
#                    print mrchata + "DEBUG: label:", label
#                    print mrchata + "DEBUG: args:", args
#                sender.sendMessage(msgplayer)
#                return True
            else:
                return False
    
 #   class MRListenerOpenEnderchest()
            
    if (mrdebug == True):
        print mrchata + "DEBUG: mrsp run 1"

except Exception:
    mrerror = True
    print "#######################################################################"
    print "!!!!!!!!!!##########!!!!!!!!!!FATAL ERROR!!!!!!!!!!##########!!!!!!!!!!"
    print "#######################################################################"
    print "ERROR IN PLUGIN MRServerPy!"
    print "Type: UNKNOWN"
    print "Please report to max_rutkowski(at)gmx.de"
    print "-----------------------------------------------------------------------"
    print "mrdebug-Info:"
    raise
finally:
    if mrerror == True:
        print "#######################################################################"
        print "!!!!!!!!!!##########!!!!!!!!!!FATAL ERROR!!!!!!!!!!##########!!!!!!!!!!"
        print "#######################################################################"


# END
