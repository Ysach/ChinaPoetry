// var myScroll = '';
// window.onload = function () {
//     document.querySelector('.container').addEventListener('touchmove', function (e) {
//         e.preventDefault();
//     });
//     /*区域滚动效果*/
//     /*条件：一个容器装着一个容器html结构*/
//     /*找到大容器*/
//     /*子容器大于父容器*/
//     myScroll = new IScroll(document.querySelector('.container'), {
//         scrollX: false,
//         scrollY: true,
//         mouseWheel: true,
//         probeType: 3
//     });
    // myScroll.on('scrollEnd', function () {
    //     // var height = this.y,
    //     //     bottomHeight = this.maxScrollY - height;
    //     // if (height < 60 && height >= 0) {
    //     //     console.log("drag.........")
    //     // }
    //     var scrollY = this.y;
    //     console.log("-----------end-", scrollY)
    // })
//     var isDrag = 0;
//     myScroll.on('scroll', function () {
//         var height = this.y;
//         var bottomHeight = this.maxScrollY - height;
//         if (bottomHeight > 60) {
//             isDrag = 1;
//         }
//     });
//     myScroll.on('scrollEnd', function () {
//         if (isDrag === 1) {
//             // console.log('==============');
//             searchPost();
//             isDrag = 0;
//             myScroll.refresh();
//         } else {
//             isDrag = 0;
//             myScroll.refresh();
//         }
//
//     })
// };

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = Zepto.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// var csrftoken = getCookie('csrftoken');
// var scrollOK = true;
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
//                 searchPost();
//             } else {
//                 scrollOK = true;
//             }
//         }
//     });
// });
// var searchPost = function () {
//         var pages = $("#poetry").find('li').length;
//         $.ajax(
//             {
//                 type: 'POST',
//                 url: document.location.href,
//                 data: {"pages": pages, 'csrfmiddlewaretoken': csrftoken},
//                 dataType: "html",
//                 beforeSend: function () {
//                     var page_end = $("#page-end");
//                     page_end.empty();
//                     page_end.append("<div class=\"loader circle\"></div>");
//                 },
//                 success: function (data) {
//                     if ($(data).find("div").length > 0) {
//                         $("#page-end").empty();
//                         $("#poetry").append(data);
//                         scrollOK = true;
//                         myScroll.refresh();
//                     } else {
//                         var page_end = $("#page-end");
//                         page_end.empty();
//                         page_end.addClass('list');
//                         page_end.append("<div class=\"page-end\">\n" +
//                             "            <h3>我是有底线的!</h3>\n" +
//                             "        </div>");
//                         scrollOK = true;
//                         myScroll.refresh();
//                     }
//                 }
//             }
//         )
//     };