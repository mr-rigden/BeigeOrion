const colors = {
    blue: {
        fill: "#0000FF",
        stroke: "#0000B2",
    },
    green: {
        fill: "#00FF00",
        stroke: "#14660d",
    },
    yellow: {
        fill: "#FFFF00",
        stroke: "#B2B200",
    },
    orange: {
        fill: "#FF7F00",
        stroke: "#B25900",
    },
    red: {
        fill: "#FF0000",
        stroke: "#B20000",
    },
    gray: {
        fill: "#787878",
        stroke: "#404040",
    },
    black: {
        fill: "#202020",
        stroke: "#000000",
    },
};
var timeFormat = 'MM/DD/YYYY HH:mm';

function newDate(days) {
    return moment.unix(days).toDate();
}

function formatDate(weekOfYear) {
    return newDate(weekOfYear);
}

var xTime = subject_data.epoch_time.map(function(e) {
    e = newDate(e);
    return e;
});



var ctx = document.getElementById("botchart").getContext("2d");
Chart.defaults.global.elements.point.radius = 1;
const myChart = new Chart(ctx, {
    type: "line",
    data: {
        label: "# of Votes",
        labels: xTime,
        datasets: [{
            label: "No Timeline",
            position: "bottom",
            fill: true,
            backgroundColor: colors.black.fill,
            pointBackgroundColor: colors.black.stroke,
            borderColor: colors.black.stroke,
            pointHighlightStroke: colors.black.stroke,
            borderCapStyle: "butt",
            data: subject_data.no_timeline

        }, {
            label: "Protected",
            position: "bottom",
            fill: true,
            backgroundColor: colors.gray.fill,
            pointBackgroundColor: colors.gray.stroke,
            borderColor: colors.gray.stroke,
            pointHighlightStroke: colors.gray.stroke,
            borderCapStyle: "butt",
            data: subject_data.protected

        }, {
            label: "Very Poor",
            position: "bottom",
            fill: true,
            backgroundColor: colors.red.fill,
            pointBackgroundColor: colors.red.stroke,
            borderColor: colors.red.stroke,
            pointHighlightStroke: colors.red.stroke,
            borderCapStyle: "butt",
            data: subject_data.very_poor

        }, {
            label: "Poor",
            fill: true,
            backgroundColor: colors.orange.fill,
            pointBackgroundColor: colors.orange.stroke,
            borderColor: colors.orange.stroke,
            pointHighlightStroke: colors.orange.stroke,
            borderCapStyle: "butt",
            data: subject_data.poor,
        }, {
            label: "Neutral",
            fill: true,
            backgroundColor: colors.yellow.fill,
            pointBackgroundColor: colors.yellow.stroke,
            borderColor: colors.yellow.stroke,
            pointHighlightStroke: colors.yellow.stroke,
            borderCapStyle: "butt",
            data: subject_data.neutral,
        }, {
            label: "Good",
            fill: true,
            backgroundColor: colors.green.fill,
            pointBackgroundColor: colors.green.stroke,
            borderColor: colors.green.stroke,
            pointHighlightStroke: colors.green.stroke,
            data: subject_data.good,
        }, {
            label: "Very Good",
            fill: true,
            backgroundColor: colors.blue.fill,
            pointBackgroundColor: colors.blue.stroke,
            borderColor: colors.blue.stroke,
            pointHighlightStroke: colors.blue.stroke,
            data: subject_data.very_good,
        }]
    },
    options: {
        animation: {
            duration: 750,
        },
        legend: {
            position: "bottom",
            reverse: true
        },
        maintainAspectRatio: false,
        point: {
            radius: 10,
        },

        responsive: true,
        scales: {
            yAxes: [{

                stacked: true,
                scaleLabel: {
                    display: false,
                    fontSize: 16,
                    labelString: "Followers"
                }
            }],
            xAxes: [{
                type: "time",
                time: {
                    tooltipFormat: ' MMMM, Qo YYYY'
                },

            }],
        },
        title: {
            display: true,
            fontSize: 24,
            text: "Twitter Follower Quality"
        },
        tooltips: {
            enabled: true,
        }

    }
});