/**
 * Created by eduhg on 10/24/16.
 */
$(document).ready(function () {
    console.log('Dashboard JS File Loaded');

    $('#slide-out>li').on('click', 'a', function (e) {
        console.log('nimefinywa');
    });

    $("#search_name").prop('disabled', true);

    $(".use-address").click(function() {
        var $row = $(this).closest("tr");    // Find the row
        var id = $row.find(".id").text(); // Find the text

        var full_name = $row.find(".full_name").text(); // Find the text
        var reported_date = $row.find(".reported_date").text(); // Find the text

        $('#add_close_id').val(id)
        $('#add_close_name').val(full_name)
    });

    $("#search_input").keyup(function(){
        var search_id = $('#search_input').val();
        console.log('searching id => '+ search_id)

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
                    $('#search_name').val(first_name + " " + other_names)
                } else {
                    $('#search_name').val("")
                }
            },
            error: function(data) {
                console.log(data);
                $('#search_name').val("")
            }
        });

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
                    $('#result').html(data);
                } else {
                    $( "#result" ).html(data);
                }
            },
            error: function(data) {
                console.log(data);
            }
        });

    });

    $("#search_with_username").keyup(function(){
        var username = $('#search_with_username').val();

        console.log('searching => ' + username)

        $.ajax({
            url: "/dashboard/search_system_users",
            method: "GET",
            dataType: 'html',
            data: {
                username: username
            },
            success: function(data) {
                if(data.length > 0){
                    $('#users_tbl_body').html(data);
                } else {
                    $( "#users_tbl_body" ).html(data);
                }
            },
            error: function(data) {
                console.log(data);
            }
        });

    });


    $('.display_notes').click(function () {
        var search_id = this.id;

        $.ajax({
            url: "/my_search_results",
            method: "GET",
            dataType: 'html',
            data: {
                search_id: search_id
            },
            success: function(data) {
                console.log(data);

                if(data.length > 0){
                    $('#search_result').html(data);
                } else {
                    $( "#search_result" ).html(data);
                }
            },
            error: function(data) {
                console.log(data);
            }
        });

        return false;
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

    $("#reported_search_id").keyup(function(){
        var search_id = $('#reported_search_id').val();

        $.ajax({
            url: "/dashboard/reported_cases_search",
            method: "GET",
            dataType: 'html',
            data: {
                search_id: search_id
            },
            success: function(data) {
                console.log(data);

                if(data.length > 0){
                    $('#tbl_body').html(data);
                } else {
                    $('#tbl_body').html(data);
                }
            },
            error: function(data) {
                console.log(data);
            }
        });

    });


    /*************************************************************************
     * Closed Cases Pi Chart
    *************************************************************************/

    $.ajax({
        url: "/dashboard/closed_cases_chart",
        method: "GET",
        success: function(data) {
            console.log(data);
            var player = [];
            var score = [];

            for(var i in data) {
                player.push(data[i].complaint);
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

    /*************************************************************************
     * Reported Cases Pi Chart
    *************************************************************************/

    $.ajax({
        url: "/dashboard/reported_cases_chart",
        method: "GET",
        success: function(data) {
            console.log(data);
            var player = [];
            var score = [];

            for(var i in data) {
                player.push(data[i].complaint);
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

            var ctx = $("#newCasesPie");

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

    /*************************************************************************
     * Total Reported Cases Chart
    *************************************************************************/

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


    /*************************************************************************
     * Summary of Cases Chart
    *************************************************************************/

    $.ajax({
        url: "/dashboard/reported_cases_chart",
        method: "GET",
        success: function(data) {
            console.log(data);
            var player = [];
            var score = [];

            for(var i in data) {
                player.push(data[i].complaint);
                score.push(data[i].total_count);
            }

            var bg_colors = randomColor({luminosity: 'dark', count: player.length});
            console.log(bg_colors)

            var chartdata = {
                labels: player,
                datasets : [
                    {
                        label: 'Summary of Cases',
                        backgroundColor: bg_colors,
                        borderColor: bg_colors,
                        hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
                        hoverBorderColor: 'rgba(200, 200, 200, 1)',
                        data: score
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

});


