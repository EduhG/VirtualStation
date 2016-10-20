/**
 * Created by eduhg on 10/13/16.
 */

$(document).ready(function () {
    $('select').material_select();

    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });

    $("#search_name").prop('disabled', true);

    $("#search_input").keyup(function(){
        var search_id = $('#search_input').val();
        console.log('searching id => '+ search_id)

        /*$.ajax({
            url: "/dashboard/search_reported_cases",
            method: "GET",
            dataType: 'json',
            data: {
                search_id: search_id
            },
            success: function(data) {
                console.log(data);

                if(data.length > 0){
                    var first_name = data[0]['first_name']
                    var other_names = data[0]['other_names']
                    $('#search_name').val(first_name + " " + other_names)
                } else {
                    $('#search_name').val("")
                }
            },
            error: function(data) {
                console.log(data);
                $('#search_name').val("")
            }
        });*/

        $.ajax({
            url: "/dashboard/search_notes",
            method: "GET",
            dataType: 'html',
            data: {
                search_id: search_id
            },
            success: function(data) {
                console.log(data);

                if(data.length > 0){
                    //$( "#result" ).load( data );
                    $('#result').html(data);
                } else {
                    $( "#result" ).load( data );
                }
            },
            error: function(data) {
                console.log(data);
            }
        });

    });

    $("#add_full_name").prop('disabled', true);

    $("#add_search_id").keyup(function(){
        var search_id = $('#add_search_id').val();
        console.log(search_id)

        $.ajax({
            url: "/dashboard/search_reported_cases",
            method: "GET",
            dataType: 'json',
            data: {
                search_id: search_id
            },
            success: function(data) {
                console.log(data);
                if(data.length > 0){
                    var first_name = data[0]['first_name']
                    var other_names = data[0]['other_names']
                    $('#add_full_name').val(first_name + " " + other_names)
                } else {
                    $('#add_full_name').val("")
                }

            },
            error: function(data) {
                console.log(data);
                $('#add_full_name').val("")
            }
        });
    });

    console.log("search_input => " + $('#search_input').val())
});

$('select').material_select();

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
});

$('.button-collapse').sideNav({
    menuWidth: 300, // Default is 240
    closeOnClick: false // Closes side-nav on <a> clicks, useful for Angular/Meteor
});
$('.collapsible').collapsible();

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


$.ajax({
    url: "/dashboard/reported_cases_chart",
    method: "GET",
    success: function(data) {
        console.log(data);
        var player = [];
        var score = [];

        for(var i in data) {
            player.push("Player " + data[i].complaint);
            score.push(data[i].total_count);
        }

        var bg_colors = randomColor({luminosity: 'dark', count: player.length});

        var chartdata = {
            labels: player,

            datasets : [
                {
                    label: 'Player Score',
                    backgroundColor: 'rgba(200, 200, 200, 0.75)',
                    borderColor: 'rgba(200, 200, 200, 0.75)',
                    data: score,
                    backgroundColor: bg_colors,
                    hoverBackgroundColor: bg_colors
                }
            ]
        };

        var ctx = $("#closedCasesPie");

        var doughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: chartdata,
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
    },
    error: function(data) {
        console.log(data);
    }
});

$.ajax({
    url: "/dashboard/reported_cases_chart",
    method: "GET",
    success: function(data) {
        console.log(data);
        var player = [];
        var score = [];

        for(var i in data) {
            player.push("Player " + data[i].complaint);
            score.push(data[i].total_count);
        }

        var bg_colors = randomColor({luminosity: 'dark', count: player.length});
        console.log(bg_colors)

        var chartdata = {
            labels: player,
            /*datasets : [
                {
                    label: 'Player Score',
                    backgroundColor: bg_colors,
                    borderColor: bg_colors,
                    hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
                    hoverBorderColor: 'rgba(200, 200, 200, 1)',
                    data: score
                }
            ]*/
            datasets: [
                {
                    type: 'bar',
                    label: 'Bar Chart',
                    data: score,
                    backgroundColor: bg_colors
                },
                {
                    type: 'line',
                    label: 'Line Chart',
                    data: score,
                    lineTension: 0.5,
                    borderColor: "rgba(75,192,192,1)"
                }
            ]
        };

        var ctx = $("#mycanvas1");

        var barGraph = new Chart(ctx, {
            type: 'bar',
            data: chartdata
        });
    },
    error: function(data) {
        console.log(data);
    }
});


$.ajax({
    url: "/dashboard/total_reported_cases_annually",
    method: "GET",
    success: function(data) {
        console.log('Annual Data => ' + data);
        var months = [];
        var total = [];

        for(var i in data) {
            months.push(data[i].calendar_month);
            total.push(data[i].month_count);
        }

        console.log('Annual Months => ' + months)
        console.log('Month Totals => ' + total)

        var config = {
            type: 'line',
            data: {
                labels: months,
                datasets: [{
                    label: "My First dataset",
                    data: total,
                    fill: true,
                    borderColor: "rgba(75,192,192,1)"
            }]
            },
            options: {
                scales: {
                    xAxes: [{
                        gridLines: {
                            display: false
                        }
                    }]
                },
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
    },
    error: function(data) {
        console.log(data);
    }
});



$("#search_input").click(function(){
    var search_id = $('#search_input').val();

    alert(search_id)
    console.log(search_id)
});

$(document).on('keyup', '#search_input', function() {
    alert('key up');
});



