import sublime
import sublime_plugin


class HexToAsciiCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        hexdig = '0123456789abcdefABCDEF '
        v = self.view
        reglist = list(v.sel())
        for j in range(0, len(reglist)):
            hx = v.substr(v.sel()[j])
            hx = hx.strip('{} .,')
            hx = hx.replace(' ', '')
            hx = hx.replace(',', '')
            hx = hx.replace('0x', '')
            hx = hx.replace('\n', '')
            astr = ''
            if (len(hx) % 2 != 0):
                sublime.status_message("Perhaps we lost key \"%s\" in the end of line?" % hx[len(hx) - 1])
            for i in range(0, len(hx)-1, 2):
                if not(hx[i] in hexdig) or not(hx[i+1] in hexdig):
                    sublime.error_message("\"%s\" isn't a part of hexadecimal number!" % hx[i:i+2])
                    break
                st = hx[i]+hx[i+1]
                astr = astr + chr(int(st, 16))
                v.replace(edit, v.sel()[j], astr)
