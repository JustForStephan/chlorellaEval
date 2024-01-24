// for the light slidecontainer
var slider_light = document.getElementById("myRange_light");
var output_light = document.getElementById("actualval_light");
output_light.innerHTML = slider_light.value; // Display the default slider value

// for the co2 slidecontainer
var slider_co2 = document.getElementById("myRange_co2");
var output_co2 = document.getElementById("actualval_co2");
output_co2.innerHTML = slider_co2.value; // Display the default slider value

// for the temperature slidecontainer
var slider_temp = document.getElementById("myRange_temp");
var output_temp = document.getElementById("actualval_temp");
output_temp.innerHTML = slider_temp.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider_light.oninput = function() {
  output_light.innerHTML = this.value;
} 
slider_co2.oninput = function() {
    output_co2.innerHTML = this.value;
  } 
slider_temp.oninput = function() {
    output_temp.innerHTML = this.value;
} 
