(function($){

  calendario = function() {
    $("#id_fecha_publicacion").datepicker({ dateFormat: 'dd/mm/yy', changeMonth: true, changeYear: true, minDate: +0, maxDate: "+6M" });
    $("#id_fecha_termino").datepicker({ dateFormat: 'dd/mm/yy', changeMonth: true, changeYear: true, minDate: +0, maxDate: "+12M" });
  };




  mensajes = function(){
  $(" #id_fecha_publicacion").on( "click", function( event ) {
    $('#mensaje_field').html(' <p class="important message">Introduzca la fecha en que desea que se publique la promocion. '+
                              ' La promocion se publicara el dia indicado desde las  12:00 am. Este campo se puede dejar vacio.</p>' )});

  $(" #id_fecha_termino").on( "click", function( event ) {
    $('#mensaje_field').html('<p class="important message">Introduzca la fecha en que desea que termine la promocion. La promocion desaparecera el dia indicado a  las 11:59 pm.' +
                             ' Este campo se puede dejar vacio. </p>')});

  $(" #id_num_limite").on( "click", function( event ) {
    $('#mensaje_field').html('<p class="important message">Introduzca el numero limite de cupones que desea dar. Cuando se llegue al limite de cupones ' +
                             'establecido ya no se podran generar cupones para esta promocion. Este campo se puede dejar vacio. </p>')});

  $(" #id_estado").on( "click", function( event ) {
    $('#mensaje_field').html('<p class="important message">Elija si su promocion se publica o no. Si elije "Publicar" se llevaran acabo las anteriores condiciones que haya establecido' +
                              ', si no introduce ninguna condicion y elije "Publicar"  la promocion se publicara. Si elije "No publicar" no se llevaran acabo las anteriores' +
                              ' condiciones que haya establecido, y su promocion no se mostrara por ningun motivo. </p>')});

  $(" #id_descripcion").on( "click", function( event ) {
    $('#mensaje_field').html('<p class="important message">Escriba una breve descripcion sobre la promocion. Este campo no se puede dejar vacio.</p>')});
  };    

  validaFecha = function(){
    var startDt=document.getElementById("id_fecha_publicacion").value;
    var endDt=document.getElementById("id_fecha_termino").value;
    if (startDt != "" && endDt != "")
    {
      if( (new Date(startDt).getTime() > new Date(endDt).getTime()))
      {
        $('#mensaje_field').html('<p class="warning message">La fecha de publicacion, debe ser menor a la fecha limite, por favor verifica tus datos.</p>')
        $('.large').attr('disabled','disabled');
      }
      else
      {
        $('.large').removeAttr('disabled');
      }
    }
    else
    {
      $('.large').removeAttr('disabled');
    }
  };


})(jQuery);

