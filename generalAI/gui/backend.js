//var c = require('./example');

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
  runPythonScript('./../classifier.py', [output_light, output_co2, output_temp]);
  document.getElementById("result").innerHTML = "result";

  output_light.innerHTML = this.value;
  var result = read_json();
} 

slider_co2.oninput = function() {
    output_co2.innerHTML = this.value;
    runPythonScript('./../classifier.py', [output_light, output_co2, output_temp]);
    var result = read_json();
    document.getElementById("result").innerHTML = result;
  }

slider_temp.oninput = function() {
    output_temp.innerHTML = this.value;
    runPythonScript('./../classifier.py', [output_light, output_co2, output_temp]);
    var result = read_json();
    document.getElementById("result").innerHTML = result;
} 

// Run a Python script and return output
function runPythonScript(scriptPath, args) {

  // Use child_process.spawn method from 
  // child_process module and assign it to variable
  const pyProg = spawn('python', [scriptPath].concat(args));

  // Collect data from script and print to console
  let data = '';
  pyProg.stdout.on('data', (stdout) => {
    data += stdout.toString();
  });

  // Print errors to console, if any
  pyProg.stderr.on('data', (stderr) => {
    console.log(`stderr: ${stderr}`);
  });

  // When script is finished, print collected data
  pyProg.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    console.log(data);
  });
}

function read_json(){
  return require("./result.json")["data"];
}