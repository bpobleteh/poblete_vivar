function iniciarMap(){
    var coord = {lat:-33.511581, lng:-70.752578};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map:map
    })
}