---
title: "Como Colocar Um Site Hugo No Ar Apesar Do Título Do Post Ser Extremamente Grande"
date: 2021-08-10T14:34:14-03:00
author: Álvaro Junqueira

tags:
- hugo
- html
- css

thumb: //via.placeholder.com/1000x500

alt: computer
---

Mussum Ipsum, cacilds vidis litro abertis. Quem num gosta di mim que vai caçá sua turmis! Aenean aliquam molestie leo, vitae iaculis nisl. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo! A ordem dos tratores não altera o pão duris.Copo furadis é disculpa de bebadis, arcu quam euismod magna. Quem num gosta di mé, boa gentis num é. Cevadis im ampola pa arma uma pindureta. Não sou faixa preta cumpadi, sou preto inteiris, inteiris.

## Teste

Diuretics paradis num copo é motivis de denguis. Per aumento de cachacis, eu reclamis. Si num tem leite então bota uma pinga aí cumpadi! Quem manda na minha terra sou euzis!
Admodum accumsan disputationi eu sit. Vide electram sadipscing et per. Viva Forevis aptent taciti sociosqu ad litora torquent. Paisis, filhis, espiritis santis. Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Delegadis gente finis, bibendum egestas augue arcu ut est. Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus. Manduma pindureta quium dia nois paga.

![computer](https://cdn.dribbble.com/users/464226/screenshots/15944213/media/fa691691526776c99476dc53a2b3d486.png?compress=1&resize=800x600)

Pra lá , depois divoltis porris, paradis. Mé faiz elementum girarzis, nisi eros vermeio. Sapien in monti palavris qui num significa nadis i pareci latim. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. Sed non consequat odio. Mais vale um bebadis conhecidiss, que um alcoolatra anonimis. Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose. Leite de capivaris, leite de mula manquis sem cabeça. Mauris nec dolor in eros commodo tempor. Aenean aliquam molestie leo, vitae iaculis nisl. Casamentiss faiz malandris se pirulitá. Detraxit consequat et quo num tendi nada. In elementis mé pra quem é amistosis quis leo. Atirei o pau no gatis, per gatis num morreus.

```py
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html'), 200
    
@app.route('/about')
def about():
    return render_template('about.html'), 200
    
@app.route('/projects')
def projects():
    return render_template('projects.html'), 200

if __name__ == '__main__':
    app.run(debug=True)
```