import xchat

__module_name__ = "Spigot Bridge"
__module_version__ = "0.1"
__module_description__ = "Changes how BridgeBabe's messages are displayed"

def chanmessage(word, word_eol, userdata):
	nick = word[0]
	message = word[1]
	if (xchat.nickcmp(xchat.strip(nick), "B") == 0 or xchat.nickcmp(xchat.strip(nick), "BridgeBabe") == 0) and message.startswith("("):		
		name = "." + message[1:message.index(')')]
		message = message[message.index(')') + 2:]
		mode = name[1] if name[1] in "@+&~%" else ""

		xchat.emit_print(userdata, name, message, mode)
		return xchat.EAT_ALL
	return xchat.EAT_NONE

xchat.hook_print("Channel Message", chanmessage, "Channel Message")
xchat.hook_print("Channel Msg Hilight", chanmessage, "Channel Msg Hilight")
xchat.hook_print("Channel Action", chanmessage, "Channel Action")
xchat.hook_print("Channel Action Hilight", chanmessage, "Channel Action Hilight")
