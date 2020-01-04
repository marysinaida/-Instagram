$(function(){
    $('body').contents().eq(0).each(function(){
        if(this.nodeName.toString()=='#text' && this.data.trim().charCodeAt(0)==8203){
            $(this).remove();
        }
    });
});

