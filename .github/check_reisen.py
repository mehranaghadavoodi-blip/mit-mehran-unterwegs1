import json,sys
fehler=[]
try:
    d=json.load(open('reisen.json',encoding='utf-8'))
except Exception as e:
    print('reisen.json ist kein gültiges JSON:',e);sys.exit(1)
if not isinstance(d,list):fehler.append('reisen.json muss eine Liste sein')
else:
    for i,e in enumerate(d):
        n=f'Eintrag {i+1} ({e.get("cc","?")})'
        if not isinstance(e.get('cc'),str):fehler.append(n+': "cc" (Ländercode) fehlt')
        for t in e.get('trips',[]):
            if not t.get('t'):fehler.append(n+': Reise ohne Titel "t"')
            if t.get('u') and not str(t['u']).startswith('http'):fehler.append(n+': Link "u" muss mit http beginnen')
        for p in e.get('p',[]):
            if len(p)<3 or not isinstance(p[1],(int,float)) or not isinstance(p[2],(int,float)):fehler.append(n+': Ort '+str(p[:1])+' braucht [Name, Breite, Länge]')
            elif not(-90<=p[1]<=90 and -180<=p[2]<=180):fehler.append(n+': Koordinaten von '+str(p[0])+' außerhalb des Bereichs')
if 'DEINE-DOMAIN' in open('index.html',encoding='utf-8').read():print('Hinweis: In index.html steht noch DEINE-DOMAIN.de – echte Adresse eintragen.')
if fehler:
    print('\n'.join('FEHLER: '+f for f in fehler));sys.exit(1)
print('reisen.json ist in Ordnung.')
