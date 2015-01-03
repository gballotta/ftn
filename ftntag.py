class FtnBaseTag(object):
    def __init__(self, initialclasses=[]):
        self.classes = []
        if len(initialclasses) != 0:
            self.classes.extend(initialclasses)
        self.propBuffer = {}

    def _parse(self, stringa):
        if stringa is not None:
            strip1 = stringa.split('\r\n')
            for i in strip1:
                strip2 = i.split(' = ')
                if len(strip2) == 2:
                    chiave = strip2[0]
                    valori = strip2[1].split(',')
                    self.propBuffer[chiave] = valori

    def _getclasses(self):
        if 'ftnclass' in self.propBuffer:
            for i in self.propBuffer['ftnclass']:
                self.classes.append(i)

    def _updatepropbuffer(self):
        if len(self.classes) > 0:
            self.propBuffer['ftnclass'] = self.classes

    def _renderpropbuffer(self):
        outputstring = ''
        for i in self.propBuffer.keys():
            outputstring += i + ' = '
            for j in self.propBuffer[i]:
                outputstring += j + ','
            outputstring = outputstring[:-1]
            outputstring += "\r\n"
        return outputstring


    def getfromnode(self, node):
        pass

    def getpropbuffer(self):
        return self.propBuffer

    def hasclass(self, classe):
        return classe in self.classes

    def addclass(self, classe):
        if self.hasclass(classe) is False:
            self.classes.append(classe)
            self._updatepropbuffer()

    def removeclass(self, classe):
        if self.hasclass(classe) is True:
            self.classes.remove(classe)
            self._updatepropbuffer()