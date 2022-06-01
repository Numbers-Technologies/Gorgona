
function set_time(){
    var element = document.getElementById('current_time');
    var currentdate = new Date();
    
    element.textContent = ("0" + currentdate.getHours()).substr(-2) + ":" + ("0" + currentdate.getMinutes()).substr(-2);
    setInterval(set_time, 1000);
}
