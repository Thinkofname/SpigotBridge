import hexchat

__module_name__ = "Spigot Bridge"
__module_version__ = "0.1"
__module_description__ = "Changes how BridgeBabe's messages are displayed"

def chanmessage(word, word_eol, userdata):
	nick = word[0]
	message = word[1]
	if hexchat.nickcmp(hexchat.strip(nick), "B") == 0 and message.startswith("("):
		
		name = "." + message[1:message.index(')')]
		message = message[message.index(')') + 2:]
		mode = name[1] if name[1] in "@+&~%" else ""
		name = name if mode == "" else "." + name[2:]

		hexchat.emit_print(userdata, name, message, mode)
		return hexchat.EAT_HEXCHAT
	return hexchat.EAT_NONE

hexchat.hook_print("Channel Message", chanmessage, "Channel Message")
hexchat.hook_print("Channel Msg Hilight", chanmessage, "Channel Msg Hilight")
