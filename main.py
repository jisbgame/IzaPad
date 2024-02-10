from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QAction, QFileDialog, QFontDialog, QColorDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QColor
import sys

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.text.setFont(QFont('Arial', 13))
        self.setCentralWidget(self.text)
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Arquivo')
        editMenu = menubar.addMenu('Editar')
        fontMenu = menubar.addMenu('Fonte')
        helpMenu = menubar.addMenu('Ajuda')

        openFile = QAction(QIcon('foto.png'), 'Abrir', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.open_text)
        fileMenu.addAction(openFile)

        saveFile = QAction(QIcon('save.png'), 'Salvar', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.triggered.connect(self.save_text)
        fileMenu.addAction(saveFile)

        saveAsFile = QAction(QIcon('saveas.png'), 'Salvar Como', self)
        saveAsFile.setShortcut('Ctrl+Shift+S')
        saveAsFile.triggered.connect(self.saveas_text)
        fileMenu.addAction(saveAsFile)

        exitAction = QAction(QIcon('exit.png'), 'Sair', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        cutAction = QAction(QIcon('cut.png'), 'Recortar', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.triggered.connect(self.text.cut)
        editMenu.addAction(cutAction)

        copyAction = QAction(QIcon('copy.png'), 'Copiar', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.text.copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction(QIcon('paste.png'), 'Colar', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.text.paste)
        editMenu.addAction(pasteAction)

        undoAction = QAction(QIcon('undo.png'), 'Desfazer', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.text.undo)
        editMenu.addAction(undoAction)

        redoAction = QAction(QIcon('redo.png'), 'Refazer', self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.text.redo)
        editMenu.addAction(redoAction)

        fontAction = QAction(QIcon('font.png'), 'Mudar Fonte', self)
        fontAction.setShortcut('Ctrl+T')
        fontAction.triggered.connect(self.font_dialog)
        fontMenu.addAction(fontAction)

        # Adicionando a opção de mudar a cor da fonte
        colorAction = QAction(QIcon('color.png'), 'Cor da Fonte', self)
        colorAction.setShortcut('Ctrl+Shift+C')
        colorAction.triggered.connect(self.color_dialog)
        fontMenu.addAction(colorAction)

        # Adicionando a opção "Sobre"
        aboutAction = QAction(QIcon('sobre.png'), 'Sobre', self)
        aboutAction.triggered.connect(self.about_dialog)
        helpMenu.addAction(aboutAction)

        self.setGeometry(500, 300, 800, 500)
        self.setWindowTitle('IzaPad')
        self.show()

    def open_text(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.text.setText(data)

    def save_text(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                data = self.text.toPlainText()
                file.write(data)

    def saveas_text(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                data = self.text.toPlainText()
                file.write(data)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)

    # Adicionando a função de mudar a cor da fonte
    def color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text.setTextColor(color)

    def about_dialog(self):
        QMessageBox.about(self, "Sobre o IzaPad",
                          "Nome do Programa: IzaPad\n"
                          "Versão: 1.0\n"
                          "Autor: Israel Batista\n"
                          "Código Fonte: https://github.com/seu_nome/notepad")

def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
