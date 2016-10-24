/**
 * Created by eduhg on 10/13/16.
 */

$(document).ready(function () {
    console.log('First JS File Loaded');

    $('select').material_select();

    $('.modal-trigger').leanModal();

    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });

    $('.button-collapse').sideNav({
        menuWidth: 300, // Default is 240
        closeOnClick: false // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });
    $('.collapsible').collapsible();

});


