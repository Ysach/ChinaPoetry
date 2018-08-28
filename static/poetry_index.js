/***
var myScroll = '';

window.onload = function () {
    document.querySelector('.container').addEventListener('touchmove', function (e) {

        e.preventDefault();

    });
    myScroll = new IScroll(document.querySelector('.container'), {
        scrollX: false,
        scrollY: true,
        mouseWheel: true,
        probeType: 3
    });
    var isDrag = 0;
    myScroll.on('scroll', function () {
        var height = this.y;
        var bottomHeight = this.maxScrollY - height;
        if (bottomHeight > 60) {
            isDrag = 1;
        }
    });
    myScroll.on('scrollEnd', function () {
        if (isDrag === 1) {
            // console.log('==============');
            poetryPost();
            isDrag = 0;
            myScroll.refresh();
        } else {
            isDrag = 0;
            myScroll.refresh();
        }

    })
};
***/

// $(function () {
//     $(window).scroll(function () {
//         var scrollTop = 0;
//         if (typeof window.pageYOffset !== 'undefined') {
//             scrollTop = window.pageYOffset;
//         }
//         else if (typeof document.compatMode !== 'undefined' && document.compatMode !== 'BackCompat') {
//             scrollTop = document.documentElement.scrollTop;
//         }
//         else if (typeof document.body !== 'undefined') {
//             scrollTop = document.body.scrollTop;
//         }
//         var scrollHeight = $(document).height();
//         var windowHeight = $(this).height();
//         if (scrollOK) {
//             scrollOK = false;
//             if (scrollTop + windowHeight >= scrollHeight) {
//                 poetryPost();
//             } else {
//                 scrollOK = true;
//             }
//         }
//     });
// });
