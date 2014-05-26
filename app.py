from flask import Flask, render_template
from serial import Serial

app = Flask(__name__)
porta = '/dev/ttyACM0'


@app.route('/cores')
@app.route('/cores/<cor>')
def home(cor=None):
    cores = (
        ('verde', '1'),
        ('amarelo', '2'),
        ('vermelho', '3'),
        ('desliga', '0')
    )
    if cor:
        s = Serial(porta, 9600)
        if cor == cores[0][0]:
            c = cores[0][1]
        elif cor == cores[1][0]:
            c = cores[1][1]
        elif cor == cores[2][0]:
            c = cores[2][1]
        elif cor == cores[3][0]:
            c = cores[3][1]
        else:
            c = cores[3][1]
        s.write(c)
        s.close()
    return render_template('index.html')


@app.route('/liga')
@app.route('/liga/<estado>')
def liga(estado=None):
    if estado in ('0', '4'):
        s = Serial(porta, 9600)
        s.write(str(estado))
        s.close()
    return render_template('liga.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
