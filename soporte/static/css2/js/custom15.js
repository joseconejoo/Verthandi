$(document).ready(function() {
  // Bootstrap collapse
  $('[data-toggle="collapse"]').on({
    'click': function () {
      var $this = $(this),
          target = $this.data('target') || null;

      if ($(target).size() > 0) {
        $this.toggleClass('target-open', !$(target).hasClass('in'));
      }
    },
  });

  // Tooltip & popovers
  $('[data-toggle="tooltip"]').tooltip();
  $('[data-toggle="popover"]').popover();

  // Dropdowns on hover on desktop
  var navbarToggle = '.navbar-toggle'; // name of navbar toggle, BS3 = '.navbar-toggle', BS4 = '.navbar-toggler'
  $('.dropdown, .dropup').each(function() {
    var dropdown = $(this),
      dropdownToggle = $('[data-toggle="dropdown"]', dropdown),
      dropdownHoverAll = dropdownToggle.data('dropdown-hover-all') || false;

    // Mouseover
    dropdown.hover(function(){
      var notMobileMenu = $(navbarToggle).size() > 0 && $(navbarToggle).css('display') === 'none';
      if( ! $(this).closest('.dropdown').hasClass('open')) {
        return;
      }
      if ((dropdownHoverAll == true || (dropdownHoverAll == false && notMobileMenu))) {
        dropdownToggle.trigger('click');
      }
    })
  });

  // Background image via data tag
  $('[data-block-bg-img]').each(function() {
    // @todo - invoke backstretch plugin if multiple images
    var $this = $(this),
      bgImg = $this.data('block-bg-img');

      $this.css('backgroundImage','url('+ bgImg + ')').addClass('block-bg-img');
  });

  // jQuery counterUp
  if(jQuery().counterUp) {
    $('[data-counter-up]').counterUp({
      delay: 20,
    });
  }

  //Scroll Top link
  $(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
      $('.scrolltop').fadeIn();
    } else {
      $('.scrolltop').fadeOut();
    }
  });

  $('.scrolltop').click(function(){
    $("html, body").animate({
      scrollTop: 0
    }, 600);
    return false;
  });








  // OwlCarousel
  $('[data-toggle="owlcarousel"], [data-toggle="owl-carousel"]').each(function() {
    var $this = $(this),
      owlCarouselSettings = $this.data('owlcarousel-settings') || {};

    $this.owlCarousel(owlCarouselSettings);
  });

  //initialise Stellar.js
  $(window).stellar({
    responsive: true,
    
  });

});











function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}



(function($) {

  // Menu filer
  $("#menu-flters li a").click(function() {
    $("#menu-flters li a").removeClass('active');
    $(this).addClass('active');

    var selectedFilter = $(this).data("filter");
    //  $("#menu-wrapper").fadeTo(100, 0);

    $(".menu-restaurant").fadeOut();

    setTimeout(function() {
      $(selectedFilter).slideDown();
      //$("#menu-wrapper").fadeTo(300, 1);
    }, 300);
  });

  // Add smooth scrolling to all links in navbar + footer link
  $(".sidenav a").on('click', function(event) {
    var hash = this.hash;
    if (hash) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function() {
        window.location.hash = hash;
      });
    }

  });

  $(".sidenav a").on('click', function() {
		closeNav();
	});

})(jQuery);










$('#myModal1').on('show.bs.modal', function (e) {
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });
       var xadd = $(e.relatedTarget).data('id');
       var valks = $(e.relatedTarget).data('href');

       //document.getElementById("pr1").innerHTML = x12[3];
       //var xsd = document.getElementById("Fbs1").acat;
       var oForm = document.forms["amxj"];
       oForm.action=valks;


       //var xsd = document.getElementById("Fbs1").acat;
       //alert(oForm.action);

       //alert(JSON.stringify(valks, null, 4));
       //accesKey o className puede significar cualquier clase de html
       //xasd=$('#abrirpop2').val(this.id);
       //alert(JSON.stringify(xasd, null, 4));
       //document.getElementById("pr1").innerHTML = xadd;
       //document.getElementById("pr1").innerHTML = "xaddT";

       //window.print("hola")

});
$('#myModal2').on('show.bs.modal', function (e) {
       $(this).find('.modal-content').css({
              width:'auto', //probably not needed
              height:'auto', //probably not needed 
              'max-height':'10%'

       });
       var xadd = $(e.relatedTarget).data('id');
       var valks = $(e.relatedTarget).data('href');

       var oForm = document.forms["amxj2"];
       oForm.action=valks;




});


/*

$('.container-modal .title').each(function (idx, item) {
    var winnerId = "winner-" + idx;
     this.id = winnerId;
     $(this).click(function(){
       var btn = $("#winner-" + idx);
       var span = $(".close");
       var popId = $('#win-'+ idx);
       btn.click(function() {
          $(popId).addClass('on');
          $('body').addClass('lorem');
        }); 
        span.click(function() {
           $(popId).removeClass('on');
           $('body').removeClass('lorem');
         });
       
        
     
     });
 });
  
document.getElementById('id').scrollIntoView();



  
*/




/* opciones de soporte */

$("#id_tipo_sop").change(function () {
  var url = $("#ProblemForm").attr("dataP-url");
  var tipo_sopId = $(this).val();  

  if (tipo_sopId) {
    $.ajax({
      url: url,
      data: {
        'tipo_sop': tipo_sopId
      },
      success: function (data) {
        $("#id_descrip1").html(data);
      }
    });

  }

  else if (!tipo_sopId) {
    data2 = '"<option value="">---------</option>"';
    $("#id_descrip1").html(data2);

  }
});

