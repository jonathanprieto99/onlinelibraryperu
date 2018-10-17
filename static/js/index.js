$(function(){

    var data ;
    $.getJSON( "/libros", function( datos ) {
        data = datos;
         $.each(data, function(index, libro) {

        $(".images").append("<img width='40px' height='40px' src='/imagen/"+libro.ID+"'/>");
    });
    });
    var currentlibro;
  
    var popupOptions = {
        width: 660,
        height: 540,
        contentTemplate: function() {
            var result = $(_.template($("#property-details").html(), currentlibro));
            var button = result.find("#favorites")
                .dxButton(buttonOptions)
                .dxButton("instance");
            setButtonText(button, currentlibro.Favorite);
            return result;
        },
        showTitle: true,
        visible: false,
        dragEnabled: false,
        closeOnOutsideClick: true
    };
  
    var buttonOptions = {
        icon: "favorites",
        width: 260,
        height: 44,
        onClick: function(e) {
            currentlibro.Favorite = !currentlibro.Favorite;
            setButtonText(e.component, currentlibro.Favorite);
            showToast(currentlibro.Favorite);
        }
    };
  
    var popoverOptions = {
        showEvent: "mouseenter",
        hideEvent: "mouseleave",
        width: 260,
        position: {
            offset: "0, 2",
            at: "bottom",
            my: "top",
            collision: "fit flip"
        }
    };
    
    function showToast(favoriteState) {
        var message = "This item has been "
          + (favoriteState ? "added to" : "removed from")
          + " the Favorites list!";
        DevExpress.ui.notify({
            message: message,
            width: 450
        }, favoriteState ? "success" : "error", 2000);
    }
  
    function setButtonText(button, isFav) {
        button.option("text", isFav
            ? "Remove from Favorites"
            : "Add to Favorites");
    }
  

});
