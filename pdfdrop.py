import os
import subprocess

import wx


class FileDropTarget(wx.FileDropTarget):
    def __init__(self, reference, *args, **kwargs):
        self.reference = reference
        super(FileDropTarget, self).__init__(*args, **kwargs)

    def OnDropFiles(self, x, y, filenames):
        self.reference.on_drop(filenames)


class PDFDropFrame(wx.Frame):
    def __init__(self, parent, title):
        super(PDFDropFrame, self).__init__(parent, title=title, size=(300, 300))

        dt = FileDropTarget(self)
        self.SetDropTarget(dt)

    def make_pdf(self, infiles, outfile):
        if not outfile.endswith('.pdf'):
            outfile += '.pdf'
        cmd = ['convert'] + sorted(infiles) + [outfile]
        print "writing " + outfile
        subprocess.call(cmd)

    def get_default_filename(self, filenames):
        first = sorted(filenames)[0]
        return os.path.basename(first).split('.')[0] + '.pdf'

    def on_drop(self, filenames):
        default_file = self.get_default_filename(filenames)
        dlg = wx.FileDialog(self, "Choose a Destination", os.getcwd(),
            default_file, '*.pdf', wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.make_pdf(filenames, dlg.GetPath())
        dlg.Destroy()


def main():
    app = wx.App(False)
    frame = PDFDropFrame(None, "PDFDrop")
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
