(function($){

  calendario = function() {
    $("#id_fecha_publicacion").datepicker({ dateFormat: 'yy-mm-dd', changeMonth: true, changeYear: true });
    $("#id_fecha_termino").datepicker({ dateFormat: 'yy-mm-dd', changeMonth: true, changeYear: true  });
  };




  mensajes = function(){
	$(" #id_fecha_publicacion").on( "click", function( event ) {
  	$('#mensaje_field').text(' <p class="important message">Introduzca la fecha en que desea que se publique automaticamente la promocion. Este campo se puede dejar vacio.</p>' )});

  $(" #id_fecha_termino").on( "click", function( event ) {
    $('#mensaje_field').text('<p class="important message">Introduzca la fecha en que desea que termine la promocion. La promocion desaparecera el dia indicado a  las 11:59 pm' +
                             'Este campo se puede dejar vacio. </p>')});

  $(" #id_num_limite").on( "click", function( event ) {
    $('#mensaje_field').html('Introduzca el numero limite de cupones que desea dar. Este campo se puede dejar vacio. <cite>Puede combinar el numero de cupones con la fecha de publicacion y fecha limite </cite>')});

  $(" #id_estado").on( "click", function( event ) {
    $('#mensaje_field').text('Elija si su promocion se publica o no. Si elije publicar cuando la promocion ya llego a su fecha final o al limite de sus cupones, forzara a su publicacion, o igual si ya no desea que se muestre la promocion tambien lo puede forzar.')});

  $(" #id_descripcion").on( "click", function( event ) {
    $('#mensaje_field').text('Escriba una breve descripcion sobre la promocion')});


};    



})(jQuery);

