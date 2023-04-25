from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
model = pickle.load(open('churn3.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template('base.html')
    
@app.route('/assesment')
def prediction():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def admin():
    a= request.form["gender"]
    if (a == 'f'):
        a=0
    if (a == 'm'):
        a=1
    b= request.form["senior-citizen"]
    if (b == 'n'):
        b=0
    if (b == 'y'):
        b=1
    c= request.form["partner"]
    if (c == 'n'):
        c=0
    if (c == 'y'):
        c=1
    d= request.form["dependents"]
    if (d == 'n'):
        d=0
    if (d == 'y'):
        d=1
    e= request.form["tenure"]
    f= request.form["phoneService"]
    if (f == 'n'):
        f=0
    if (f == 'y'):
        f=1
    g= request.form["multipleLines"]
    if (g == 'n'):
        g=0
    if (g == 'nps'):
        g=1
    if (g == 'y'):
        g=2
    h= request.form["internetService"]
    if (h == 'dsl'):
        h=0
    if (h == 'fo'):
        h=1
    if (h == 'n'):
        h=2
    i= request.form["onlineSecurity"]
    if (i == 'n'):
        i=0
    if (i == 'nis'):
        i=1
    if (i == 'y'):
        i=2
    j= request.form["onlineBackup"]
    if (j == 'n'):
        j=0
    if (j == 'nis'):
        j=1
    if (j == 'y'):
        j=2
    k= request.form["deviceProtection"]
    if (k == 'n'):
        k=0
    if (k == 'nis'):
        k=1
    if (k == 'y'):
        k=2
    l= request.form["techSuport"]
    if (l == 'n'):
        l=0
    if (l == 'nis'):
        l=1
    if (l == 'y'):
        l=2
    m= request.form["StreamingTV"]
    if (m == 'n'):
        m=0
    if (m == 'nis'):
        m=1
    if (m == 'y'):
        m=2
    n= request.form["streamingMovies"]
    if (n == 'n'):
        n=0
    if (n == 'nis'):
        n=1
    if (n == 'y'):
        n=2
    o= request.form["contract"]
    if (o == 'mtm'):
        o=0
    if (o == 'oyr'):
        o=1
    if (o == 'tyrs'):
        o=2
    p= request.form["paymentMethod"]
    if (p == 'ec'):
        p=2
    if (p == 'mail'):
        p=3
    if (p == 'bt'):
        p=0
    if (p == 'cc'):
        p=1
    q= request.form["paperlessBilling"]
    if (q == 'n'):
        q=0
    if (q == 'y'):
        q=1
    r= request.form["MonthlyCharges"]
    s= request.form["TotalCharges"]

    t=[[int(a),int(b),int(c),int(d),int(e),int(f),  int(g),int(h),int(i),int(j),int(k),int(l),int(m),int(n),int(o),int(p),int(q), int(r), int(s)]]
    x = model.predict(t)
    if (x[0] == 0):
        y ="No"
        return render_template("predno.html",z = y)

        
    if (x[0] == 1):
        y ="Yes"
        return render_template("predyes.html",z = y)

if __name__== '__main__':
    app.run(debug = True)
