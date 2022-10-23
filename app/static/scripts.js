function myFunc() {
  return xValues + yValues
}


console.log(xValues);
console.log();
new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(0,0,255,1.0)",
      borderColor: "rgba(0,0,255,0.1)",
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      yAxes:[{
        scaleLabel: {
        display: true,
          fontColor: "black",
          fontSize: 25,
        labelString: 'Velocity (inches/second)'
      },
      ticks: {min: 0, max:Math.max(...yValues)*1.1}
    }],
     xAxes: [{
     scaleLabel: {
     display: true,
       fontColor: "black",
       fontSize: 25,
     labelString: 'Time (seconds)'
     },
      ticks: {min: 0, max:1000}
     }],
     
    },
    title: {
      display: true,
      fontColor: "black",
      fontSize: 35,
      text: "Velocity of Breath Chart"
    }
  }
});