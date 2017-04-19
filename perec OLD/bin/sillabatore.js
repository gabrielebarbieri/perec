
function spazio(frase) {
    
    frase = frase.split('  ').join(' ');
    frase = frase.split('   ').join(' ');
    frase = frase.split('    ').join(' ');
    frase = frase.split('     ').join(' ');
    frase = frase.split('      ').join(' ');
    frase = frase.split('       ').join(' ');
    frase = frase.split(' \'').join('\'');

    return frase;

}



function iato(frase)
{



replacement = '$1-$2';

var pattern = /([a])([aeoi])/g;
temp =frase.replace(pattern,replacement);

replacement = '$1$2$4';

var pattern = /([ ])([a])([-])([aeoi])/g;
temp = temp.replace(pattern,replacement);






replacement = '$1-$2';

var pattern = /([e])([aeo])/g;
temp =temp.replace(pattern,replacement);



var pattern = /([i])([aeoiu])/g;
replacement = '$1-$2';
//temp =temp.replace(pattern,replacement);

var pattern = /([i])([aeoiu])([ ])/g;
replacement = '$1-$2$3';
temp =temp.replace(pattern,replacement);


replacement = '$1-$2';

var pattern = /([o])([aeou])/g;
temp =temp.replace(pattern,replacement);



var pattern = /([bcdr])([u])([aeio])/g;
replacement = '$1$2-$3';
//temp =temp.replace(pattern,replacement);



replacement = '$1-$2';
var pattern = /([u])([aeo])$/g;
//temp =temp.replace(pattern,replacement);


replacement = '$1-$2$3';
var pattern = /([u])([aoe])([ ])/g;
//temp =temp.replace(pattern,replacement);





return temp;
}

function cinque(frase)
{
frase = frase.split('tm').join('t-m');
frase = frase.split('rf').join('r-f');
frase = frase.split('lp').join('l-p');
frase = frase.split('lz').join('l-z');
frase = frase.split('lv').join('l-v');
frase = frase.split('rv').join('r-v');
frase = frase.split('rd').join('r-d');
frase = frase.split('rl').join('r-l');
frase = frase.split('nz').join('n-z');
frase = frase.split('nc').join('n-c');
frase = frase.split('rc').join('r-c');
frase = frase.split('rs').join('r-s');
frase = frase.split('rn').join('r-n');
frase = frase.split('lm').join('l-m');
frase = frase.split('lt').join('l-t');
frase = frase.split('rm').join('r-m');
frase = frase.split('mb').join('m-b');
frase = frase.split('nf').join('n-f');
frase = frase.split('ms').join('m-s');
frase = frase.split('rc').join('r-c');
frase = frase.split('rg').join('r-g');
frase = frase.split('rt').join('r-t');
frase = frase.split('nd').join('n-d');
frase = frase.split('ns').join('n-s');
frase = frase.split('nt').join('n-t');
frase = frase.split('ng').join('n-g');
frase = frase.split('mp').join('m-p');
frase = frase.split('rp').join('r-p');   
frase = frase.split('pt').join('p-t');   
frase = frase.split('cn').join('c-n'); 
frase = frase.split('cq').join('c-q');    

frase = frase.split('bb').join('b-b');
frase = frase.split('cc').join('c-c');
frase = frase.split('dd').join('d-d');
frase = frase.split('ff').join('f-f');
frase = frase.split('gg').join('g-g');
frase = frase.split('ll').join('l-l');
frase = frase.split('mm').join('m-m');
frase = frase.split('nn').join('n-n');
frase = frase.split('pp').join('p-p');
frase = frase.split('qq').join('q-q');
frase = frase.split('rr').join('r-r');
frase = frase.split('ss').join('s-s');
frase = frase.split('tt').join('t-t');
frase = frase.split('vv').join('v-v');
frase = frase.split('zz').join('z-z');

return frase;
}



function sei_bis(frase)
{



var pattern = /([a-z])([lnmr])([bcdfglmnpqrstvz])([aeiou])/g

replacement = '$1$2-$3$4';

temp =frase.replace(pattern,replacement);

var pattern = /([s])([-])([ct])/g
replacement = '$1$3';
return temp.replace(pattern,replacement);

}

function sette(frase)
{
frase = frase.split('rst').join('r-st');
frase = frase.split('ntr').join('n-tr');
frase = frase.split('ltr').join('l-tr');
frase = frase.split('rtr').join('r-tr');
frase = frase.split('btr').join('b-tr');
return frase;
}







function uno(frase)
{
//abo ast

var pattern = /([aeiou])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g;

replacement = '$1-$2$3';

temp = frase.replace(pattern,replacement);

var pattern = /([aeiou])([bcdfghlmnpqrstvz])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g;

replacement = '$1-$2$3$4';

temp = temp.replace(pattern,replacement);



var pattern = /([aeiou])([bcdfghlmnpqrstvz])([bcdfghlmnpqrstvz])([lr])([aeiouèéàòùì])/g;

replacement = '$1-$2$3$4$5';

temp = temp.replace(pattern,replacement);

return temp;
}







function due(frase)
{

//cacodo
var pattern = /([bcdfghlmnpqrstvz])([aeiou])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g

replacement = '$1$2-$3$4';

temp =frase.replace(pattern,replacement);


//cacodo
var pattern = /([bcdfghlmnpqrstvz])([aeiou])([bcdfghlmnpqrstvz])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g

replacement = '$1$2-$3$4$5';

temp =temp.replace(pattern,replacement);



//cacodo
var pattern = /([bcdfghlmnpqrstvz])([aeiou])([bcdfghlmnpqrstvz])([bcdfghlmnpqrstvz])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g

replacement = '$1$2-$3$4$5$6';

temp =temp.replace(pattern,replacement);


//cacodo
var pattern = /([q])([u])([e])([a-z])([a-z])/g

replacement = '$1$2$3-$4$5';

temp =temp.replace(pattern,replacement);


// ...a-bo 
var pattern = /([aeiou])([bcdfghlmnpqrstvz])([aeiouèéàòùì])/g

replacement = '$1-$2$3';

return temp.replace(pattern,replacement);
}



function tre_bis(frase)
{

//medio-cre
var pattern = /([aeiou])([c])([lr])([aeiou])/g

replacement = '$1-$2$3$4';

return frase.replace(pattern,replacement);
}


function tre(frase)
{

//bra-- cri vre
var pattern = /([bcdfgptv])([lr])([aeiou])([a-zèéàòùì])([a-zèéàòùì])/g

replacement = '$1$2$3-$4$5';

return frase.replace(pattern,replacement);
}

function quattro(frase)
{

//stra spre
var pattern = /([s])([bcdfghlmnpqrstvz]+)([aeiou])([a-z])([a-zèéàòùì])/g

replacement = '$1$2$3-$4$5';
temp =frase.replace(pattern,replacement);

var pattern = /([i])([-])([e])/g

replacement = '$1$3';
return temp.replace(pattern,replacement);
}


function otto(frase)
{
//AU-guri pIO-lo

var pattern = /([iu])([aeo])([bcdfghlmnpqrstvz])/g

replacement = '$1$2-$3';

temp =frase.replace(pattern,replacement);

var pattern = /([aeo])([iu])([bcdfghlmnpqrstvz])/g

replacement = '$1$2-$3';
return temp.replace(pattern,replacement);

}


function nove(frase)
{
//pa-olo cia-o

var pattern = /([aeo])([aeoèéàòùì])/g

replacement = '$1-$2';




return frase.replace(pattern,replacement);

}


function dieci(frase)
{
//tritongo

var pattern = /([aeo])([iu])([aouieèéàòùì])/g

replacement = '$1-$2$3';

temp =frase.replace(pattern,replacement);

var pattern = /([aeoiu])([aouie])([iu])/g

replacement = '$1-$2$3';

return temp.replace(pattern,replacement);

}

function undici(frase)
{
//tritongo monosillabo

var pattern = /([ui])([-])([aeo])([iu])/g

replacement = '$1$3$4';

temp =frase.replace(pattern,replacement);

var pattern = /([ui])([aeo])([-])([iu])/g

replacement = '$1$2$4';
temp =frase.replace(pattern,replacement);



var pattern = /([ui])([-])([aeo])([-])([iu])/g

replacement = '$1$3-$5';
temp =frase.replace(pattern,replacement);




return temp

}

function  dodici(frase)
{
//ri - avere  prefisso  esperimental

var pattern = /([ ])([r])([i])([eauio])/g

replacement = '$1$2$3-$4';




return frase.replace(pattern,replacement);

}



function doit(pattern,replacement)
{
count_rules++;
if(count_rules<=limit_rules) 
temp =temp.replace(pattern,replacement);

//alert(count_rules+' '+limit_rules)

}



function tredici(frase)
{
/**************************************************************************
extra rulesssss
***************************************************************************/


limit_rules = 100;
//if(document.baseURI=='http://www.sillabare.it/divisione-in-sillabe/divisione-in-sillabe_TEST.php')   limit_rules = document.getElementById('limit_rules').value;



count_rules = 0;
temp = frase;

doit(/([c])([u])([-])([o])([i])([-])([oae])/g,'$1$2$4-$5$7'); // cuoio 1
doit(/([u])([i])([oae])/g,'$1-$2$3'); // buio 2
doit(/([g])([u])([-])([a])([i])/g,'$1$2$4$5'); // gauio 3
doit(/([ ])([i])([-])([o])([ ])/g,'$1$2$4$5'); // io 4
doit(/([-])([i])([-])([o])/g,'$1$2$4'); // -io 5
doit(/([aeiuo])([-])([z])([i])([-])([oae])/g,'$1$2$3$4$6'); // grazie 6
doit(/([g])([l])([i])([-])([oaeu])/g,'$1$2$3$5'); // me-glio 7
doit(/([a-z])([-])([bcdgprlmnptvz])([i])([-])([oae])/g,'$1$2$3$4$6'); // brac-ci-o 8
doit(/([d])([u])([e])([l])/g,'$1$2-$3$4'); // due-l-lo 9
doit(/([c])([i])([-])([a])/g,'$1$2$4'); // ri-sci-a 10
doit(/([bdflmprstvz])([u])([aeo])([^[a-z]{0,1})/g,'$1$2-$3$4'); // due 11
doit(/([bdflmprstvz])([u])([-])([aeo])([a-z])/g,'$1$2$4-$5'); // suadente 11bis
doit(/([bdflmprstvz])([u])([-])([aeo])([-])/g,'$1$2$4-'); // suadente 11tris

doit(/([n])([-])([g])([s])/g,'$1$3-$4'); //  tungsteno 12
doit(/([bs])([u])([-])([o])([a-z])/g,'$1$2$4-$5'); // buono 13
doit(/([bs])([u])([o])([-])([n])([-])([bcdfgstvz])/g,'$1$2$3$5-$7'); // buono 13

doit(/([s])([c])([u])([-])([o])/g,'$1$2$3$5'); // scu-o-la 14
doit(/([u])([i])([-])([aoe])/g,'$1-$2$4'); // bui-o 15
doit(/([s])([c])([i])([-])([aoeu])/g,'$1$2$3$5'); // li-sci-o 16
doit(/([s])([t])([r])([u])([-])([aoei])/g,'$1$2$3$4$6'); // mestru-o 17
doit(/([n])([-])([t])([u])([-])([a])/g,'$1$2$3$4$6'); // pron-tu-a-rio 18
doit(/([p])([a])([u])([-])([r])([o])/g,'$1$2-$3-$5$6'); // pauroso 19
doit(/([tsb])([u])([-])([oa])([i])/g,'$1$2$4$5'); // tuoi 20
doit(/([f])([e])([i])/g,'$1$2-$3'); // caffeina 21
//doit(/([t])([r])([o])([l])([-])([l])/g,'$1$2$3$4$6'); // troll 22
doit(/([t])([a])([s])([-])([m])([a])/g,'$1$2-$3$5$6'); // fantasma 23
doit(/([tsbg])([u])([oa])([-])([i])/g,'$1$2$3$5'); // tuoi 24
doit(/([v])([u])([-])([o])([i])/g,'$1$2$4$5'); // vuoi 25
doit(/([-])([d])([i])([a])/g,'$1$2$3-$4'); // lombordia 26
doit(/([aoeui])([g])([r])([oaiue])/g,'$1-$2$3$4'); // fotografia 27
doit(/([-])([f])([i])([a])/g,'$1$2$3-$4'); // fotografia 28
doit(/([s])([p])([i])([ao])/g,'$1$2$3-$4'); // spiare 29
doit(/([s])([p])([i])([e])([ ])/g,'$1$2$3-$4'); // spie 30
doit(/([v])([a])([-])([i])/g,'$1$2$4'); //  vai fai dai sai mai rai  31
doit(/([ ])([v])([i])([a])([-])([cdfglmnpqrstvzib])/g,'$1$2$3-$4-$6'); //  via 32
doit(/([m])([a])([-])([r])([i])([a])/g,'$1$2-$4$5-$6'); //  maria 33
doit(/([n])([i])([e])([-])([n])([t])/g,'$1$2$3$5-$6'); //  niente 34
doit(/([n])([i])([-])([g])([m])/g,'$1$2$4-$5'); //  enigma 35
doit(/([g])([h])([i])([a])([-])([n])([d])/g,'$1$2$3$4$6-$7'); //  ghianda 36
doit(/([a])([-])([i])([-])([r])([o])/g,'$1$3$4$5$6'); //  airone 37
doit(/([p])([o])([-])([n])([d])([e])/g,'$1$2$4-$5$6'); //  corrispondenza 38
doit(/([s])([c])([h])([i])([-])([aeou])/g,'$1$2$3$4$6'); //  schianto 39
doit(/([m])([i])([-])([e])([i])/g,'$1$2$3$4-$5'); //  miei 40
doit(/([t])([u])([i])([-])([t])([aeio])/g,'$1$2-$3-$5$6'); //  restituita 41
doit(/([c])([a])([u])([-])/g,'$1$2-$3-'); //  cause 42
doit(/([-])([r])([i])([e])/g,'-$2$3-$4'); //  canarie 43
doit(/([-])([c])([h])([i])([-])([o])/g,'-$2$3$5'); //  vecchio 44
doit(/([f])([i])([l])([-])([m])/g,'$1$2$3$5'); //  film 44
doit(/([l])([a])([u])([s])([t])/g,'$1$2-$3-$4$5'); //  balaustra 45
doit(/([ ])([a])([u])([s])([t])/g,'$1$2$3-$4$5'); //  australiano 46
doit(/([s])([t])([r])([i])([a])/g,'$1$2$3$4-$5'); //  austri-a-co 47 
doit(/([d])([r])([i])([aeou])/g,'$1$2$3-$4'); //  quadrielica 48
doit(/([a])([p])([-])([p])([ ])/g,'$1$2$4$5'); //  app 49
doit(/([s])([g])([u])([-])([a])/g,'$1$2$3$5'); //  sgualcire 50
doit(/([ ])([z])([i])([e])/g,'$1$2$3-$4'); //  zie 51
doit(/([q])([u])([-])([i])([e])/g,'$1$2$4$5'); //  quiete 52
doit(/([s])([t])([i])([-])([t])([u])([i])/g,'$1$2$3$4$5$6-$7'); //  resti tu-i scimelo 53
doit(/([m])([a])([-])([gc])([i])([aeou])/g,'$1$2$3$4$5-$6'); //  farma ci-a 54
doit(/([ ])([c])([u])([i])/g,'$1$2$3-$4'); //  cui
doit(/([i])([n])([-])([n])([i])([iou])/g,'$1$2$3$4$5-$6'); //  tintinnio
doit(/([r])([i])([-])([e])([-])([s])/g,'$1$2$4$5$6'); //  riesce
doit(/([t])([o])([-])([p])([i])([a])/g,'$1$2$3$4$5-$6'); //  utopia
doit(/([d])([u])([e])([-])([tl])/g,'$1$2$3$5'); //  duello
doit(/([b])([u])([-])([g])([i])([ae])/g,'$1$2$3$4$5-$6'); //  bugia
doit(/([p])([e])([-])([r])([i])([o])/g,'$1$2$3$4$5-$6'); //  periodo
doit(/([z])([-])([z])([i])([ae])/g,'$1$2$3$4-$5'); //  razzia
doit(/([m])([e])([-])([d])([i])([-])([aeo])/g,'$1$2$3$4$5$7'); //  mediano
doit(/([p])([i])([-])([oaei])/g,'$1$2$4'); //  pio
doit(/([i])([-])([s])([i])([aeou])/g,'$1$2$3$4-$5'); //  tunisia
doit(/([r])([e])([i])([n])/g,'$1$2-$3$4'); //  reintegro
doit(/([c])([a])([-])([u])([-])/g,'$1$2$4$5'); //  causa
doit(/([r])([i])([-])([u])([-])/g,'$1$2$4$5'); //  riunione
doit(/([s])([i])([-])([o])([-])([n])([ei])/g,'$1$2$4$5$6$7'); //  incisione
doit(/([a])([e])([-])([r])([e])([i])/g,'$1$2$3$4$5-$6');//aerei
doit(/([f])([i])([-])([s])([i])([-])([o])/g,'$1$2$3$4$5$7');//fisioterapia
doit(/([-])([v])([i])([oi])/g,'$1$2$3-$4');//rinvio


return temp;

/**************************************************************************
extra rulesssss
***************************************************************************/    
}


function sillaba_js(frase) {
    
    frase = frase.toLowerCase()
    frase=frase.split('-').join(''); 

    frase = cinque(frase); //doppie
    frase = tre_bis(frase);  //medio-cre
      
    frase = nove(frase);   //pa-olo cia-o
  
    frase = sei_bis(frase); // al-to pen-sa

    frase = due(frase); //ca-cao // bi-nocolo

    frase = sette(frase); //al-tro en-tro



    frase = uno(frase);   // a-tipico u-signolo

    frase = tre(frase);  //bra cri vre 

    frase = quattro(frase); // stra spre


    frase = iato(frase);

    frase = dieci(frase);    // trittongo
    frase = undici(frase);  //trittongo monosillabo (not necessay)
    frase = dodici(frase);  //ri - avere  prefisso  esperimental
    frase = tredici(frase);  // extra

    return frase;
}



// server
var express = require('express')
var app = express()

app.get('/:word', function (req, res) {
  res.send(sillaba_js(req.params.word))
})

app.listen(8000)

