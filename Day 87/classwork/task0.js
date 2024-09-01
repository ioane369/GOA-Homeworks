//  Create an interval, and in the passed function, create a new Date object each time. When the current minute equals 35, the interval should be cleared.

const timer = setInterval(function(){
    let date = new Date();

    console.log(date.getSeconds());
    if (date.getMinutes() === 34){
        clearInterval(timer);
    }
}, 60000);