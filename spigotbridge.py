import hexchat

__module_name__ = "Spigot Bridge"
__module_version__ = "0.1"
__module_description__ = "Changes how BridgeBabe's messages are displayed"

def chanmessage(word, word_eol, userdata):
	if hexchat.nickcmp(hexchat.strip(word[0]), "B") == 0 and word[1] == "(":
		w = word[1][1:]
		name = "." + w[:w.index(')')]
		message = w[w.index(')') + 2:]
		mode = ""
		if name[0] in "@+&~%":
			mode = name[0]
			name = name[1:]
		hexchat.emit_print(userdata['out'], name, message, mode)
		return hexchat.EAT_HEXCHAT
	return hexchat.EAT_NONE

hexchat.hook_print("Channel Message", chanmessage, userdata={'out':"Channel Message"})
hexchat.hook_print("Channel Msg Hilight", chanmessage, userdata={'out':"Channel Msg Hilight"})

