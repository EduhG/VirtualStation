/**
 * Created by eduhg on 10/13/16.
 */

$('.button-collapse').sideNav({
    menuWidth: 300, // Default is 240
    closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
});
$('.collapsible').collapsible();


var config = {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            data: [65, 0, 80, 81, 56, 85, 40],
            fill: false
    }]
    },
    options: {
        legend: {
            display: false
        },
        tooltips: {
            callbacks: {
                label: function (tooltipItem) {
                    console.log(tooltipItem)
                    return tooltipItem.yLabel;
                }
            }
        }
    }
};

var ctx = document.getElementById("myChart").getContext("2d");
new Chart(ctx, config);


/*var ctx = document.getElementById("myChart");
/*var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "",
                fill: false,
                lineTension: 0.5,
                backgroundColor: "rgba(75,192,192,0.4)",
                borderColor: "rgba(75,192,192,1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(75,192,192,1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(75,192,192,1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 5,
                pointHitRadius: 10,
                data: [65, 59, 80, 81, 56, 55, 40],
                spanGaps: false,
            }
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        title: {
            display: false,
            text: 'Custom Chart Title'
        },
        legend: {
            display: false
        }
    }
});*/

var newCasesPie = document.getElementById("newCasesPie");
var myPieChart = new Chart(newCasesPie, {
    type: 'doughnut',
    data: {
        labels: [
        "Red",
        "Blue",
        "Yellow"
    ],
        datasets: [
            {
                data: [300, 50, 100],
                backgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56"
            ],
                hoverBackgroundColor: [
                "#FF6384",
                "#36A2EB",
                "#FFCE56"
            ]
        }]
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
        }],
            yAxes: [{
                gridLines: {
                    display: false
                }
        }]
        },
        title: {
            display: false,
            text: 'Custom Chart Title'
        },
        legend: {
            display: false
        }
    }
});
