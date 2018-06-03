jQuery(document).ready(function($) {
   'use strict';
   
   jQuery('.flexslider' ).flexslider({
                   animation: "slide",
                   navigation: true,
                   useCSS: true,
                   touch: true
             });
    
   jQuery('.aboutslider').flexslider({
      animation: 'slide',
      navigation: false
    });
    
    
                  /* venobox lightbox init */
                 jQuery('.venobox').venobox(); 
    
    // tooltips
         jQuery('[data-toggle~="tooltip"]').tooltip({
         container: 'body'
         });
    
    

    
    jQuery('#contactform').submit(function () {
                  
                  var action = $(this).attr('action');
                  
                  jQuery("#message").slideUp(750, function () {
                      jQuery('#message').hide();
                  
                      jQuery.post(action, {
                              name: $('#name').val(),
                              email: $('#email').val(),
                              phone: $('#phone').val(),
                              subject: $('#subject').val(),
                              comments: $('#comments').val()
                          },
                          function (data) {
                              document.getElementById('message').innerHTML = data;
                              $('#message').slideDown('slow');
                              if (data.match('success') != null) $('#contactform').slideUp('slow');
                  
                          }
                      );
                  
                  });
                  
                  return false;
                  
                  });
    
   });


jQuery(window).load(function() {
                  
                   var $container = $('#container');
                     $container.imagesLoaded( function(){
                       $container.isotope({
                         resizable: false,
                         layoutMode : 'fitRows',
                         itemSelector : '.project-item'
                       });
                     });
                  
                  
                     jQuery('#options a').click(function(){
                       var selector = $(this).attr('data-filter');
                       $container.isotope({ filter: selector });
                  
                       jQuery(this).parent().parent().find('.selected').removeClass('selected');
                       jQuery(this).addClass('selected');
                       return false;
                     });
                  
                   });



jQuery('html').niceScroll({
         cursorcolor: "#1A212C",
         zindex: '99999',
         cursorminheight: 60,
         scrollspeed: 50,
         cursorwidth: 9,
         autohidemode: true,
         background: "#aaa",
         cursorborder: 'none',
         cursoropacitymax: .7,
         cursorborderradius: 0,
         horizrailenabled: false
         });
         
         



         
