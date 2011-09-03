$(document).ready(function(){
    var a = new Array();
    a[0] = "Digite seu nome completo";
    a[1] = "Digite seu cpf";
    a[2] = "Informe seu email";
    
    $('input').focus(function(event){
       var valor = $(this).attr("value");
       for(i=0; i <= a.length; i++){
            if(valor == a[i])
            {
                $(this).attr('value', '');
                break;
            }
       }
    });
})
