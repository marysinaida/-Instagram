// $( document ).ready(function() {
//     var abc = document.body.innerHTML;
//     var a = String(abc).replace(/\u200B/g,'');
//     document.body.innerHTML = a;
// });

$(function(){
    $('body').contents().eq(0).each(function(){
        if(this.nodeName.toString()=='#text' && this.data.trim().charCodeAt(0)==8203){
            $(this).remove();
        }
    });
});